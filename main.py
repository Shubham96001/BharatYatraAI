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
import time
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# LLM is optional at startup; the app must still work when the user has not
# configured API keys yet.
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
) if GROQ_API_KEY else None

# State
class TravelState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    user_query: str
    transport_results: str
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
    if llm is None:
        print("GROQ_API_KEY missing; returning fallback response without LLM call.")
        return AIMessage(content=fallback)

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

# One Transit Agent
# Helps users compare buses, trains, and flights for the source-to-destination route.
def transport_agent(state: TravelState):
    query = state["user_query"]
    transit_query = (
        f"Find practical bus, train, and flight timings, routes, and travel duration "
        f"for the trip described below. Include departure, arrival, recommended mode, "
        f"and transfer guidance: {query}"
    )
    transport_text = _run_tool(
        tavily_search,
        transit_query,
        "Transport search is temporarily unavailable. Suggest likely bus, train, and flight options based on the route in the request.",
    )

    return {
        "transport_results": transport_text,
        "messages": [AIMessage(content="One Transit Agent completed")],
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

    Transport Results:
    {state['transport_results']}

    Hotel Results:
    {state['hotel_results']}
    """

    response = _run_llm([
        SystemMessage(content=(
            "You are the itinerary agent for Bharat Yatra. Create a practical "
            "day-by-day plan using only the supplied trip request and research. "
            "Include a clear source-to-destination travel section covering buses, trains, "
            "and flights where relevant, and mark uncertain timing details clearly."
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

    Transport Options:
    {state['transport_results']}

    Hotels:
    {state['hotel_results']}

    Itinerary:
    {state['itinerary']}
    """

    response = _run_llm([
        SystemMessage(content=(
            "You are the final travel response agent. Return a polished, honest "
            "trip plan with sections for overview, transport, hotels, itinerary, "
            "budget notes, and practical tips. Highlight bus, train, and flight timing "
            "options from source to destination, preserve useful research details, avoid "
            "claiming unavailable data is confirmed, and answer the user's original "
            "request directly."
        )),
        HumanMessage(content=final_prompt),
    ], "The final AI response is temporarily unavailable. Review the flight, hotel, and itinerary sections above.")

    return {
        "messages": [response],
        "final_response": _text(response.content),
        "llm_calls": state.get("llm_calls", 0) + 1
    }


graph = StateGraph(TravelState)

graph.add_node("transport_agent", transport_agent)
graph.add_node("hotel_agent", hotel_agent)
graph.add_node("itinerary_agent", itinerary_agent)
graph.add_node("final_agent", final_agent)

graph.add_edge(START, "transport_agent")
graph.add_edge("transport_agent", "hotel_agent")
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
            "transport_results": "",
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