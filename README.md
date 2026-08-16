# Bharat Yatra AI

Bharat Yatra AI is an AI-powered India travel planner built with Streamlit and LangGraph. It helps users compare routes, understand bus/train/flight timing from source to destination, and generate a polished trip plan with destination imagery.

## Project Overview

This project combines:

- Streamlit frontend for the user experience
- LangGraph workflow for multi-agent orchestration
- Groq LLM integration for planning and summarization
- Tavily search for transport, hotel, and route research
- Destination metadata with curated image lookup
- Optional PostgreSQL checkpointer for persistence

The app is designed around a four-step agent pipeline:

1. One Transit Agent
2. Hotel Agent
3. Itinerary Agent
4. Final Response Agent

The system accepts a travel request such as a source city, destination, duration, budget, or route, and returns a practical plan that explains bus, train, and flight timing options from source to destination.

## Tech Stack

- Python
- Streamlit
- LangGraph
- LangChain
- Groq
- Tavily
- ReportLab (for PDF export)
- PostgreSQL (optional)

## Project Structure

- `main.py` – LangGraph agent workflow and application logic
- `frontend.py` – Streamlit UI, route intelligence, and PDF export
- `state_detail.py` – state-specific detail screen logic
- `states_data.py` – state and destination metadata with images
- `image_utils.py` – asset handling for images
- `style.css` – custom styling for the UI
- `tools/tavily_tool.py` – search-based transport and hotel research
- `travel_plans/` – generated travel plans saved as PDF files
- `.env` – local environment variables for API keys

## Prerequisites

Make sure you have:

- Python 3.10+
- A virtual environment or project venv
- Access to the following services:
  - Groq API key
  - Tavily API key
- Optional: PostgreSQL for persistent conversation checkpoints

## Setup Instructions

### 1. Open a terminal in the project folder

```bash
cd d:\BharatYatraAI\BharatYatraAI
```

### 2. Activate the virtual environment

On Windows PowerShell:

```powershell
.\langgraph_env\Scripts\Activate.ps1
```

### 3. Install dependencies

If required packages are not installed yet, run:

```powershell
pip install streamlit langgraph langchain-core langchain-groq tavily-python python-dotenv psycopg requests reportlab
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
DATABASE_URL=postgresql://username:password@host:port/database
```

Notes:

- `GROQ_API_KEY` is required by the LLM agent.
- `TAVILY_API_KEY` is required for transport, hotel, and route research.
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
   - "From Delhi to Jaipur by train and flight options for 3 days"
   - "Mumbai to Kerala with bus and train timings under ₹10,000"
   - "Bengaluru to Goa route and travel timing comparison"
3. Click the planning button.
4. The app runs the agents and generates a complete travel itinerary with transport timing guidance.
5. The final output is downloaded as a PDF plan with the matching destination image in the `travel_plans/` folder.

## Output Files

Generated travel plans are saved in:

```text
travel_plans/
```

Each PDF includes:

- Transport timing guidance for buses, trains, and flights
- Hotel suggestions
- Itinerary
- Final response
- Destination image
- Timestamp and user query

## Notes

- The app uses live APIs, so service availability depends on your API keys and network access.
- Some features gracefully fall back when services are unavailable.
- If PostgreSQL is not configured, the app still works using an in-memory checkpointer.
- The transport agent focuses on route timing and mode comparison instead of flight-only data.

## Common Troubleshooting

### Streamlit not found

```powershell
pip install streamlit
```

### Missing environment variables

Confirm your `.env` file exists in the project root and contains valid keys.

### No transport or hotel data returned

Check:

- your API keys are valid
- your internet connection is active
- the API service is responding

### PDF export issue

```powershell
pip install reportlab
```

## License

This project is for local development and travel-planning experimentation.
