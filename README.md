# Bharat Yatra AI

Bharat Yatra AI is an AI-powered India travel planner built with Streamlit and LangGraph. It helps users discover destinations, generate flight and hotel ideas, and produce a structured travel itinerary using multiple agents.

## Project Overview

This project combines:

- Streamlit frontend for the user experience
- LangGraph workflow for multi-agent orchestration
- Groq LLM integration for planning and summarization
- Tavily search for hotel and travel research
- AviationStack integration for flight information
- Optional PostgreSQL checkpointer for persistence

The app is designed around a four-step agent pipeline:

1. Flight Agent
2. Hotel Agent
3. Itinerary Agent
4. Final Response Agent

The system accepts a travel request such as a trip destination, duration, budget, or route, and returns a polished travel plan.

## Tech Stack

- Python
- Streamlit
- LangGraph
- LangChain
- Groq
- Tavily
- AviationStack
- PostgreSQL (optional)

## Project Structure

- `main.py` – LangGraph agent workflow and application logic
- `frontend.py` – Streamlit UI and travel planner interface
- `state_detail.py` – state-specific detail screen logic
- `states_data.py` – state and destination metadata
- `image_utils.py` – asset handling for images
- `style.css` – custom styling for the UI
- `tools/flight_tool.py` – flight search integration
- `tools/tavily_tool.py` – hotel/web search integration
- `travel_plans/` – generated travel plans saved as Markdown files
- `.env` – local environment variables for API keys

## Prerequisites

Make sure you have:

- Python 3.10+
- A virtual environment or project venv
- Access to the following services:
  - Groq API key
  - Tavily API key
  - AviationStack API key
- Optional: PostgreSQL for persistent conversation checkpoints

## Setup Instructions

### 1. Open a terminal in the project folder

```bash
cd d:\agentic_project
```

### 2. Activate the virtual environment

On Windows PowerShell:

```powershell
.\langgraph_env\Scripts\Activate.ps1
```

### 3. Install dependencies

If required packages are not installed yet, run:

```powershell
pip install streamlit langgraph langchain-core langchain-groq tavily-python python-dotenv psycopg requests
```

If the project already has a requirements file in the future, you can instead use:

```powershell
pip install -r requirements.txt
```

### 4. Create a .env file

Create a file named `.env` in the project root with the following variables:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATION_API_KEY=your_aviationstack_api_key
DATABASE_URL=postgresql://username:password@host:port/database
```

Notes:

- `GROQ_API_KEY` is required by the LLM agent.
- `TAVILY_API_KEY` is required for hotel and research retrieval.
- `AVIATION_API_KEY` is required for flight data retrieval.
- `DATABASE_URL` is optional. If it is not set, the app uses in-memory storage.

## Run the Application

### Option 1: Launch the Streamlit app

```powershell
streamlit run frontend.py
```

This starts the full web-based UI.

### Option 2: Run the LangGraph logic directly in CLI mode

```powershell
python main.py
```

This runs the core travel planner logic in a terminal prompt-based flow.

## How to Use

1. Open the Streamlit app in your browser.
2. Enter your trip request, such as:
   - "7-day Rajasthan tour under ₹1.5L"
   - "Kerala backwaters and Munnar for 5 days"
   - "Ladakh bike trip 10 days"
3. Click the planning button.
4. The app runs the agents and generates a complete travel itinerary.
5. The final output can be downloaded as a Markdown file in the `travel_plans/` folder.

## Output Files

Generated travel plans are saved in:

```text
travel_plans/
```

Each file includes:

- Flights
- Hotels
- Itinerary
- Final response
- Timestamp and user query

## Notes

- The app uses live APIs, so service availability depends on your API keys and network access.
- Some features gracefully fall back when services are unavailable.
- If PostgreSQL is not configured, the app still works using an in-memory checkpointer.

## Common Troubleshooting

### Streamlit not found

```powershell
pip install streamlit
```

### Missing environment variables

Confirm your `.env` file exists in the project root and contains valid keys.

### No flight or hotel data returned

Check:

- your API keys are valid
- your internet connection is active
- the API service is responding

## License

This project is for local development and travel-planning experimentation.
