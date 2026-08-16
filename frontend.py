import os
import io
import textwrap
import requests
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

from langchain_core.messages import HumanMessage
from main import app
from image_utils import asset_src
from state_detail import render_state_detail
from states_data import INDIA_STATES

st.set_page_config(
    page_title="Bharat Yatra AI — India Trip Planner",
    page_icon="🪷",
    layout="wide",
)

# ══════════════════════════════════════════════════════════════════════════════
#  CSS — Light, warm, culturally-rich Indian travel theme
# ══════════════════════════════════════════════════════════════════════════════
# Load stylesheet
style_path = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(style_path):
    with open(style_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-icon">🪷</div>
        <div class="sb-name">Bharat Yatra AI</div>
        <div class="sb-sub">India Trip Intelligence</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    thread_id = st.text_input(
        "👤 User ID", value="shubham_user",
        help="Session ID — keeps your travel history across queries")

    st.markdown("<div class='sb-label'>🛠️ Powered By</div>", unsafe_allow_html=True)
    for t in ["🔗 LangGraph", "🧠 Groq · LLaMA 3.3 70B",
              "🐘 PostgreSQL", "🔍 Tavily Search"]:
        st.markdown(f"<div class='sb-chip'>{t}</div>", unsafe_allow_html=True)

    st.markdown("<div class='sb-label'>🤖 Agent Pipeline</div>", unsafe_allow_html=True)
    for s in ["① One Transit Agent — Bus, train & flight timings",
              "② Hotel Agent — Stays & ratings",
              "③ Itinerary Agent — Day plans",
              "④ Final Agent — Complete plan"]:
        st.markdown(f"<div class='sb-chip'>{s}</div>", unsafe_allow_html=True)

    st.markdown("<div class='sb-label'>🇮🇳 Coverage</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="sb-stats">
        <div class="sb-stat"><div class="sb-stat-v">28</div><div class="sb-stat-l">States</div></div>
        <div class="sb-stat"><div class="sb-stat-v">8</div><div class="sb-stat-l">UTs</div></div>
        <div class="sb-stat"><div class="sb-stat-v">6</div><div class="sb-stat-l">Neighbours</div></div>
    </div>
    """, unsafe_allow_html=True)


# Check for active selection in URL query parameters
selected_state = st.query_params.get("state")
selected_country = st.query_params.get("country")

if selected_state:
    render_state_detail(selected_state, is_country=False)
elif selected_country:
    render_state_detail(selected_country, is_country=True)
else:
    # ══════════════════════════════════════════════════════════════════════════════
    #  HERO
    # ══════════════════════════════════════════════════════════════════════════════
    st.markdown(f"""
    <div class="hero-container">
        <div class="hero-text">
            <div class="hero-pill">✦ AI-Powered · 4 Agents · India-First</div>
            <h1><em>Bharat Yatra</em> AI</h1>
            <p>From Kashmir's snow-crowned peaks to Kerala's emerald backwaters,
               from Rajasthan's golden sands to the living temples of Tamil Nadu —
               let four AI agents craft your dream Indian journey.</p>
        </div>
        <div class="hero-gallery">
            <div class="stack-card stack-card-1">
                <img src="{asset_src('Kashmir_1.jpg')}" alt="Kashmir Shikara"/>
            </div>
            <div class="stack-card stack-card-2">
                <img src="{asset_src('tajMahalAgra.jpg')}" alt="Taj Mahal Agra"/>
            </div>
            <div class="stack-card stack-card-3">
                <img src="{asset_src('Kerala_1.jpg')}" alt="Kerala Backwaters"/>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="tricolor"></div>', unsafe_allow_html=True)


    # ══════════════════════════════════════════════════════════════════════════════
    #  DESTINATIONS — Indian States / Regions
    # ══════════════════════════════════════════════════════════════════════════════
    st.markdown("""<div class='sec-head'>
        <div class='sec-dot'></div>
        <span>Explore India</span>
    </div>""", unsafe_allow_html=True)

    DESTINATIONS = [
        ("Kashmir",     "Heaven on Earth",    "Kashmir_1.jpg"),
        ("Rajasthan",   "Royal Desert",       "Rajasthan_1.jpg"),
        ("Kerala",      "God's Own Country",  "Kerala_1.jpg"),
        ("Goa",         "Beach Paradise",     "Goa_1.jpg"),
        ("Ladakh",      "Land of Passes",     "Ladakh_1.jpg"),
        ("Varanasi",    "Spiritual Capital",  "Varanasi_1.jpg"),
        ("Himachal",    "Mountain Magic",     "Himachal_1.jpg"),
        ("Tamil Nadu",  "Temple Trail",       "Tamil Nadu_1.jpg"),
        ("North East",  "Seven Sisters",      "North-East_1.jpg"),
        ("Andaman",     "Island Paradise",    "Andaman_1.jpg"),
        ("Gujarat",     "Land of Legends",    "Gujarat_1.jpg"),
        ("Karnataka",   "Many Worlds",        "Karnataka_1.jpg"),
        ("Uttarakhand", "Land of the Gods",   "Uttarakhand_1.jpg"),
        ("Punjab",      "Five Rivers",        "Punjab_1.jpg"),
        ("Odisha",      "Soul of India",      "Odisha_1.jpg")
    ]

    html = '<div class="dest-grid">'
    for name, tag, img in DESTINATIONS:
        html += f'''<a href="?state={name}" target="_self" class="card-link">
            <div class="dest-card">
                <img src="{asset_src(img, name)}" alt="{name}"/>
                <div class="d-info"><div class="d-name">{name}</div><div class="d-tag">{tag}</div></div>
            </div>
        </a>'''
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


    # ══════════════════════════════════════════════════════════════════════════════
    #  NEIGHBOURING COUNTRIES
    # ══════════════════════════════════════════════════════════════════════════════
    st.markdown("""<div class='sec-head'>
        <div class='sec-dot'></div>
        <span>Neighbouring Countries</span>
    </div>""", unsafe_allow_html=True)

    NEIGHBOURS = [
        ("🇳🇵", "Nepal",      "Himalayan trails"),
        ("🇱🇰", "Sri Lanka",  "Island heritage"),
        ("🇧🇹", "Bhutan",     "Last Shangri-La"),
        ("🇲🇻", "Maldives",   "Tropical bliss"),
        ("🇲🇲", "Myanmar",    "Golden pagodas"),
        ("🇧🇩", "Bangladesh", "River deltas"),
    ]

    nb_html = '<div class="nb-grid">'
    for flag, name, sub in NEIGHBOURS:
        nb_html += f'''<a href="?country={name}" target="_self" class="card-link">
            <div class="nb-card">
                <div class="nb-flag">{flag}</div>
                <div class="nb-name">{name}</div>
                <div class="nb-sub">{sub}</div>
            </div>
        </a>'''
    nb_html += '</div>'
    st.markdown(nb_html, unsafe_allow_html=True)


    # ══════════════════════════════════════════════════════════════════════════════
    #  EXPERIENCES
    # ══════════════════════════════════════════════════════════════════════════════
    st.markdown("""<div class='sec-head'>
        <div class='sec-dot'></div>
        <span>Travel Experiences</span>
    </div>""", unsafe_allow_html=True)

    EXPERIENCES = [
        ("🛕", "Heritage & Temples"),
        ("🏖️", "Beaches"),
        ("🏔️", "Mountains & Treks"),
        ("🏜️", "Desert Safari"),
        ("🐅", "Wildlife"),
        ("🙏", "Spiritual Journeys"),
        ("🪂", "Adventure Sports"),
        ("🛶", "Backwaters & Lakes"),
        ("🍛", "Culinary Trails"),
        ("🏰", "Royal Palaces"),
        ("🌿", "Ayurveda & Wellness"),
        ("📸", "Photography Tours"),
    ]

    exp_html = '<div class="exp-strip">'
    for icon, name in EXPERIENCES:
        exp_html += f'<div class="exp-pill"><span class="ep-icon">{icon}</span> {name}</div>'
    exp_html += '</div>'
    st.markdown(exp_html, unsafe_allow_html=True)

    st.markdown('<div class="tricolor"></div>', unsafe_allow_html=True)


def _resolve_destination_image(user_query: str):
    query = user_query.lower()
    for name, data in INDIA_STATES.items():
        if name.lower() in query or data.get("full_name", "").lower() in query:
            images = data.get("images", [])
            if images:
                return name, images[0]
    return None, None


def create_travel_plan_pdf(user_query: str, collected: dict, thread_id: str):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.utils import ImageReader
        from reportlab.pdfgen import canvas
    except ImportError as exc:
        raise RuntimeError("reportlab is required for PDF export. Install it with: pip install reportlab") from exc

    destination_name, image_url = _resolve_destination_image(user_query)
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    pdf.setTitle("Bharat Yatra Travel Plan")
    pdf.setAuthor("Bharat Yatra AI")
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, height - 50, "Bharat Yatra — Travel Plan")

    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 75, f"Query: {user_query[:120]}{'...' if len(user_query) > 120 else ''}")
    pdf.drawString(50, height - 90, f"Destination: {destination_name or 'Not identified'}")
    pdf.drawString(50, height - 105, f"User ID: {thread_id}")

    if image_url:
        try:
            response = requests.get(image_url, timeout=15)
            response.raise_for_status()
            pdf.drawImage(ImageReader(io.BytesIO(response.content)), 420, height - 255, width=120, height=90, preserveAspectRatio=True)
        except Exception:
            pass

    sections = [
        ("Transport", collected.get("transport_results") or "N/A"),
        ("Hotels", collected.get("hotel_results") or "N/A"),
        ("Itinerary", collected.get("itinerary") or "N/A"),
        ("Final Travel Plan", collected.get("final_response") or "N/A"),
    ]

    y = height - 160
    for title, content in sections:
        if y < 120:
            pdf.showPage()
            y = height - 60

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, title)
        y -= 18
        pdf.setFont("Helvetica", 9)
        lines = textwrap.wrap(content.replace("\r", ""), width=100)
        for line in lines[:18]:
            pdf.drawString(60, y, line[:100])
            y -= 12
        y -= 18

    pdf.save()
    return buffer.getvalue()


# ══════════════════════════════════════════════════════════════════════════════
#  INPUT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """<div class="input-wrap">
    <div class="input-title">🗺️ Describe Your Indian Adventure</div>
    <div class="input-sub">Tell us where you want to go, how long, your budget, and what experiences you're looking for.</div>
</div>""",
    unsafe_allow_html=True,
)

# Custom CSS to invert Quick-Fill button colors
st.markdown(
    """
<style>
/* Style quick-fill buttons with inverse color scheme */
div[data-testid="column"] button {
    background-color: #1E293B !important;
    color: #FFFFFF !important;
    border: 1px solid #475569 !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease-in-out !important;
}

div[data-testid="column"] button:hover {
    background-color: #0F172A !important;
    color: #38BDF8 !important;
    border-color: #38BDF8 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

QUICK = [
    "7-day Rajasthan royal tour under ₹1.5L",
    "Kerala backwaters + Munnar 5 days",
    "Ladakh bike trip 10 days",
    "Varanasi & Rishikesh spiritual retreat",
    "Goa beach holiday 4 days budget",
    "Kashmir to Leh road trip",
    "North East India 12-day explorer",
    "Weekend trek near Delhi",
]

# Initialize session state for prefilled text if not set
if "quick_fill_input" not in st.session_state:
    st.session_state["quick_fill_input"] = ""


# Callback function to handle button click directly in session state
def set_quick_fill(text):
    st.session_state["quick_fill_input"] = text


# Quick-fill chips — 4 columns
st.markdown('<div class="qf-row">', unsafe_allow_html=True)
qcols = st.columns(4)
for i, label in enumerate(QUICK):
    with qcols[i % 4]:
        st.button(
            label,
            key=f"q_{label}",
            on_click=set_quick_fill,
            args=(label,),
            use_container_width=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

with st.form("travel_form", clear_on_submit=False):
    user_query = st.text_area(
        "Your trip details",
        value=st.session_state.get("quick_fill_input", ""),
        placeholder="e.g. Plan a 7-day Rajasthan heritage trip covering Jaipur, Jodhpur...",
        height=110,
        label_visibility="collapsed",
    )

    generate = st.form_submit_button(
        "🪷  Plan My Bharat Yatra", use_container_width=True
    )

# Execute JavaScript using components.html for smooth scrolling/focusing
if st.session_state.get("scroll_to_planner"):
    components.html(
        """
        <script>
            const textarea = window.parent.document.querySelector('textarea');
            if (textarea) {
                textarea.focus();
                textarea.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        </script>
        """,
        height=0,
    )
    st.session_state["scroll_to_planner"] = False

# ══════════════════════════════════════════════════════════════════════════════
#  AGENT PIPELINE  (functionality unchanged)
# ══════════════════════════════════════════════════════════════════════════════
AGENT_META = {
    "transport_agent": ("🚆", "One Transit Agent"),
    "hotel_agent":     ("🏨", "Hotel Agent"),
    "itinerary_agent": ("🗓️", "Itinerary Agent"),
    "final_agent":     ("🧠", "Final Agent"),
}

if generate:
    if not user_query.strip():
        st.warning("Please describe your trip first.")
    else:
        config = {"configurable": {"thread_id": thread_id}}
        collected = {
            "transport_results": "", "hotel_results": "",
            "itinerary": "", "final_response": "", "llm_calls": 0,
        }

        st.markdown("---")
        st.markdown("""<div class='sec-head'>
            <div class='sec-dot'></div>
            <span>🤖 Agent Pipeline — Live</span>
        </div>""", unsafe_allow_html=True)

        for chunk in app.stream(
            {
                "messages": [HumanMessage(content=user_query)],
                "user_query": user_query,
                "transport_results": "",
                "hotel_results": "",
                "itinerary": "",
                "final_response": "",
                "llm_calls": 0,
            },
            config=config,
            stream_mode="updates",
        ):
            for node_name, state_update in chunk.items():
                icon, label = AGENT_META.get(node_name, ("🔧", node_name))

                with st.status(f"{icon}  {label}", state="complete", expanded=True):
                    if node_name == "transport_agent":
                        text = state_update.get("transport_results", "")
                        collected["transport_results"] = text
                        st.markdown(text or "_No transport data returned._")

                    elif node_name == "hotel_agent":
                        text = state_update.get("hotel_results", "")
                        collected["hotel_results"] = text
                        st.markdown(text or "_No hotel data returned._")

                    elif node_name == "itinerary_agent":
                        text = state_update.get("itinerary", "")
                        collected["itinerary"] = text
                        st.markdown(text or "_No itinerary generated._")

                    elif node_name == "final_agent":
                        msgs = state_update.get("messages", [])
                        text = msgs[-1].content if msgs else ""
                        collected["final_response"] = text
                        st.markdown(text or "_No final response._")

                    collected["llm_calls"] = state_update.get(
                        "llm_calls", collected["llm_calls"])

        # ── Metrics ──
        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-box">
                <div class="metric-val">4</div>
                <div class="metric-lbl">Agents Run</div>
            </div>
            <div class="metric-box">
                <div class="metric-val">{collected['llm_calls']}</div>
                <div class="metric-lbl">LLM Calls</div>
            </div>
            <div class="metric-box">
                <div class="metric-val">✅</div>
                <div class="metric-lbl">Status</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Final plan ──
        if collected["final_response"]:
            st.markdown("""<div class='sec-head'>
                <div class='sec-dot'></div>
                <span>🧠 Your Travel Plan</span>
            </div>""", unsafe_allow_html=True)
            st.markdown(
                f"<div class='final-card'>{collected['final_response']}</div>",
                unsafe_allow_html=True)

        # ── Save PDF plan with destination image ──
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"travel_plan_{timestamp}.pdf"
        save_dir = os.path.join(os.path.dirname(__file__), "travel_plans")
        os.makedirs(save_dir, exist_ok=True)

        try:
            pdf_bytes = create_travel_plan_pdf(user_query, collected, thread_id)
            pdf_path = os.path.join(save_dir, filename)
            with open(pdf_path, "wb") as f:
                f.write(pdf_bytes)
            download_data = pdf_bytes
            download_mime = "application/pdf"
            save_message = f"<div class='save-bar'>📁 Saved to <code>travel_plans/{filename}</code></div>"
        except Exception as exc:
            st.warning(f"PDF export failed: {exc}")
            file_content = f"# Bharat Yatra — Travel Plan\n**Query:** {user_query}\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n**User ID:** {thread_id}\n\n---\n\n## 🚆 Transport\n{collected['transport_results'] or 'N/A'}\n\n---\n\n## 🏨 Hotel Information\n{collected['hotel_results'] or 'N/A'}\n\n---\n\n## 🗓️ Itinerary\n{collected['itinerary'] or 'N/A'}\n\n---\n\n## 🧠 Final Travel Plan\n{collected['final_response'] or 'N/A'}\n"
            download_data = file_content.encode("utf-8")
            download_mime = "text/plain"
            save_message = "<div class='save-bar'>⚠️ PDF export unavailable; saved a text fallback.</div>"

        dl_col, info_col = st.columns([1, 3])
        with dl_col:
            st.download_button(
                "⬇️ Download Plan", data=download_data,
                file_name=filename, mime=download_mime,
                use_container_width=True)
        with info_col:
            st.markdown(save_message, unsafe_allow_html=True)