<div align="center">

# Bharat Yatra AI
**An AI-powered India travel planner built with Streamlit and LangGraph.**

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

---

## 📖 Project Overview

Bharat Yatra AI helps users compare routes, understand bus/train/flight timings from source to destination, and generate a polished trip plan complete with destination imagery.

This project combines a responsive UI with a powerful multi-agent AI backend. It utilizes a **four-step agent pipeline**:
1. 🚌 **Transit Agent:** Evaluates and compares transportation modes.
2. 🏨 **Hotel Agent:** Researches accommodation options based on the query.
3. 🗺️ **Itinerary Agent:** Structures the day-by-day travel plan.
4. 📝 **Final Response Agent:** Compiles the data into a polished, final output.

The system accepts natural language travel requests (e.g., source city, destination, duration, budget, or route) and returns a practical plan that explains bus, train, and flight timing options, ultimately exporting a formatted PDF.

### ✨ Core Capabilities
- **Streamlit frontend** for an intuitive user experience.
- **LangGraph workflow** for advanced multi-agent orchestration.
- **Groq LLM integration** for rapid planning and summarization.
- **Tavily search** for live transport, hotel, and route research.
- **Destination metadata** with curated image lookup capabilities.
- **Optional PostgreSQL checkpointer** for conversational memory and persistence.

---

## 🛠️ Tech Stack
*   **Language:** Python
*   **UI Framework:** Streamlit
*   **AI/Orchestration:** LangGraph, LangChain, Groq LLM
*   **Search Engine:** Tavily
*   **PDF Generation:** ReportLab
*   **Database:** PostgreSQL (optional for persistent state)

---

## 📂 Project Structure

```text
📦 BharatYatraAI
 ┣ 📂 tools/
 ┃ ┗ 📜 tavily_tool.py    # Search-based transport and hotel research
 ┣ 📂 travel_plans/       # Generated travel plans saved as PDF files
 ┣ 📂 assets/             # Destination images and static assets[cite: 3]
 ┣ 📂 utils/              # Utility functions and helpers[cite: 3]
 ┣ 📜 main.py             # LangGraph agent workflow and core logic
 ┣ 📜 frontend.py         # Streamlit UI, route intelligence, and PDF export
 ┣ 📜 state_detail.py     # State-specific detail screen logic
 ┣ 📜 states_data.py      # State and destination metadata with images
 ┣ 📜 image_utils.py      # Asset handling for images
 ┣ 📜 style.css           # Custom styling for the UI
 ┣ 📜 requirements.txt    # Python dependencies list[cite: 3]
 ┣ 📜 LICENSE             # MIT License[cite: 3]
 ┗ 📜 .env                # Local environment variables for API keys

```
## 🚀 Setup Instructions

### Prerequisites

Make sure you have:

* **Python 3.10+**
* A virtual environment (recommended)
* Access to the following services:
* [Groq API key](https://console.groq.com/)
* [Tavily API key](https://tavily.com/)


* *Optional:* PostgreSQL server for persistent conversation checkpoints.

### 1️⃣ Installation

Open a terminal in your project folder (e.g., `cd d:\BharatYatraAI\BharatYatraAI`) and activate your virtual environment:

**On Windows PowerShell:**

```powershell
.\langgraph_env\Scripts\Activate.ps1

```

**Install dependencies:**
Run the following command to install the required packages (or use `pip install -r requirements.txt` if available):

```bash
pip install streamlit langgraph langchain-core langchain-groq tavily-python python-dotenv psycopg requests reportlab

```

### 2️⃣ Environment Variables (`.env`)

Create a file named `.env` in the project root with the following variables:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
DATABASE_URL=postgresql://username:password@host:port/database

```

* **Note:** `GROQ_API_KEY` and `TAVILY_API_KEY` are strictly required.
* **Note:** `DATABASE_URL` is optional. If it is not set, the app gracefully falls back to using an in-memory storage checkpointer.

---

## 💻 Run the Application

You can launch Bharat Yatra AI in two ways depending on your needs:

**Option 1: Launch the Streamlit Web App (Recommended)**
This starts the full web-based user interface.

```bash
streamlit run frontend.py

```

**Option 2: Run the CLI Logic**
This runs the core travel planner logic in a terminal prompt-based flow without the GUI.

```bash
python main.py

```

---

## 🧭 How to Use

1. Open the Streamlit app in your web browser.
2. Enter your trip request in natural language. Examples:
* *"From Delhi to Jaipur by train and flight options for 3 days"*
* *"Mumbai to Kerala with bus and train timings under ₹10,000"*
* *"Bengaluru to Goa route and travel timing comparison"*


3. Click the planning button.
4. The application orchestrates the agents and generates a complete travel itinerary with transport timing guidance.
5. The final output is available for download as a PDF plan (including a matching destination image) saved in the `travel_plans/` folder.

### 📄 Output Files

Generated travel plans are automatically saved in the `travel_plans/` directory. Each exported PDF includes:

* Transport timing guidance for buses, trains, and flights
* Hotel suggestions
* Structured Day-by-day Itinerary
* Final response summary
* Destination image
* Timestamp and original user query

---

## ⚠️ Notes & Limitations

* **Live APIs:** The app uses live internet APIs; service availability and data accuracy depend on your API keys and network access.
* **Graceful Degradation:** Some features will gracefully fall back when certain services or keys are unavailable.
* **Transport Logic:** The transport agent focuses specifically on route timing and mode comparison (bus/train) instead of relying solely on flight-only data.

---

## 🔧 Common Troubleshooting

**Streamlit not found:**

```bash
pip install streamlit

```

**Missing environment variables:**
Confirm your `.env` file exists in the exact project root and contains valid, active API keys.

**No transport or hotel data returned:**
Check that:

* Your API keys have remaining credits/are valid.
* Your internet connection is active.
* The external API services (Groq/Tavily) are currently responding.

**PDF export issue (ModuleNotFoundError):**

```bash
pip install reportlab

```

---

## 📜 License

This project is licensed under the MIT License and is intended for local development and travel-planning experimentation.

```

```
