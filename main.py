import os
from typing import TypedDict, Annotated
import operator

import psycopg
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import (
    AnyMessage,
    HumanMessage,
    AIMessage,
    SystemMessage,
)

from langchain_groq import ChatGroq

from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights, search_flights_structured
import time
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# State
class TravelState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    user_query: str
    flight_results: str
    hotel_results: str
    itinerary: str
    final_response: str
    llm_calls: int


def _text(value) -> str:
    """Convert tool and model output into prompt-safe text."""
    if value is None:
        return "No information returned."
    if isinstance(value, str):
        return value.strip() or "No information returned."
    return str(value)


def _run_tool(tool, query: str, unavailable_message: str) -> str:
    start = time.time()
    try:
        result = tool(query)
        dur = time.time() - start
        print(f"Tool {tool.__name__} took {dur:.2f}s")
        return _text(result)
    except Exception as exc:
        dur = time.time() - start
        print(f"{tool.__name__} failed after {dur:.2f}s: {exc}")
        return unavailable_message


def _run_llm(messages: list[AnyMessage], fallback: str) -> AIMessage:
    start = time.time()
    try:
        response = llm.invoke(messages)
        dur = time.time() - start
        print(f"LLM call took {dur:.2f}s")
        return AIMessage(content=_text(response.content))
    except Exception as exc:
        dur = time.time() - start
        print(f"LLM call failed after {dur:.2f}s: {exc}")
        return AIMessage(content=fallback)

# Flight Agent
def flight_agent(state: TravelState):
    query = state["user_query"]
    # Use structured flight search so downstream agents can make semantic decisions.
    try:
        structured = search_flights_structured(query)
    except Exception as exc:
        print(f"structured flight search failed: {exc}")
        structured = []

    # Create a textual summary for display and for compatibility with existing agents
    if structured:
        summary_lines = []
        for it in structured:
            summary_lines.append(
                f"Airline: {it.get('airline_name')} Departure: {it.get('departure_airport')} Arrival: {it.get('arrival_airport')} Status: {it.get('status')}"
            )
        flight_text = "\n".join(summary_lines)
    else:
        flight_text = "Flight search is temporarily unavailable. Plan airport transfers manually."

    return {
        "flight_results": flight_text,
        "flight_structured": structured,
        "messages": [AIMessage(content="Flight agent completed")],
        "llm_calls": state.get("llm_calls", 0),
    }

# Hotel Agent
def hotel_agent(state: TravelState):
    query = f"Best hotels for {state['user_query']}"
    hotel_results = _run_tool(
        tavily_search,
        query,
        "Hotel search is temporarily unavailable. Include hotel selection guidance instead.",
    )

    return {
        "hotel_results": hotel_results,
        "messages": [AIMessage(content="Hotel agent completed")],
        "llm_calls": state.get("llm_calls", 0),
    }

# Itinerary Agent
def itinerary_agent(state: TravelState):

    prompt = f"""
    Create a travel itinerary.
    User Query:
    {state['user_query']}

    Flight Results:
    {state['flight_results']}

    Hotel Results:
    {state['hotel_results']}
    """

    response = _run_llm([
        SystemMessage(content=(
            "You are the itinerary agent for Bharat Yatra. Create a practical "
            "day-by-day plan using only the supplied trip request and research. "
            "Mark uncertain details clearly and do not invent live prices."
        )),
        HumanMessage(content=prompt),
    ], "Itinerary generation is temporarily unavailable. Use the research above to plan each day manually.")

    return {
        "itinerary": _text(response.content),
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }

# Final Response Agent
def final_agent(state: TravelState):

    final_prompt = f"""
    Generate final travel response.

    Flights:
    {state['flight_results']}

    Hotels:
    {state['hotel_results']}

    Itinerary:
    {state['itinerary']}
    """

    response = _run_llm([
        SystemMessage(content=(
            "You are the final travel response agent. Return a polished, honest "
            "trip plan with sections for overview, flights, hotels, itinerary, "
            "budget notes, and practical tips. Preserve useful research details, "
            "avoid claiming unavailable data is confirmed, and answer the user's "
            "original request directly."
        )),
        HumanMessage(content=final_prompt),
    ], "The final AI response is temporarily unavailable. Review the flight, hotel, and itinerary sections above.")

    return {
        "messages": [response],
        "final_response": _text(response.content),
        "llm_calls": state.get("llm_calls", 0) + 1
    }


graph = StateGraph(TravelState)

graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", hotel_agent)
graph.add_node("itinerary_agent", itinerary_agent)
graph.add_node("final_agent", final_agent)

graph.add_edge(START, "flight_agent")
graph.add_edge("flight_agent", "hotel_agent")
graph.add_edge("hotel_agent", "itinerary_agent")
graph.add_edge("itinerary_agent", "final_agent")
graph.add_edge("final_agent", END)


# Use PostgreSQL persistence when configured and available; otherwise the app
# remains usable with an in-memory checkpointer.
_conn = None
if DATABASE_URL:
    try:
        _conn = psycopg.connect(DATABASE_URL, autocommit=True)
        checkpointer = PostgresSaver(_conn)
        checkpointer.setup()
    except Exception as exc:
        print(f"PostgreSQL checkpointer unavailable: {exc}")
        checkpointer = MemorySaver()
else:
    checkpointer = MemorySaver()

app = graph.compile(checkpointer=checkpointer)

if __name__ == "__main__":
    config = {
        "configurable": {
            "thread_id": "user_shubham"
        }
    }

    user_input = input("Enter travel request: ")

    result = app.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ],
            "user_query": user_input,
            "flight_results": "",
            "hotel_results": "",
            "itinerary": "",
            "final_response": "",
            "llm_calls": 0
        },
        config=config
    )

    print("\nFINAL RESPONSE:\n")

    for msg in result["messages"]:
        print(msg.content)