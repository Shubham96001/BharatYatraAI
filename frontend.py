import os
import streamlit as st
from datetime import datetime

from langchain_core.messages import HumanMessage
from main import app
from image_utils import asset_src
from state_detail import render_state_detail

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
              "🐘 PostgreSQL", "🔍 Tavily Search", "✈️ AviationStack"]:
        st.markdown(f"<div class='sb-chip'>{t}</div>", unsafe_allow_html=True)

    st.markdown("<div class='sb-label'>🤖 Agent Pipeline</div>", unsafe_allow_html=True)
    for s in ["① Flight Agent — Routes & fares",
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
        ("Kashmir",     "Heaven on Earth",    "https://images.unsplash.com/photo-1597074866923-dc0589150458?w=400&q=75"),
        ("Rajasthan",   "Royal Desert",       "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=400&q=75"),
        ("Kerala",      "God's Own Country",  "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=400&q=75"),
        ("Goa",         "Beach Paradise",     "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=400&q=75"),
        ("Ladakh",      "Land of Passes",     "https://images.unsplash.com/photo-1626015365107-84e7e4e1f244?w=400&q=75"),
        ("Varanasi",    "Spiritual Capital",  "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=400&q=75"),
        ("Himachal",    "Mountain Magic",     "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=400&q=75"),
        ("Tamil Nadu",  "Temple Trail",       "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=400&q=75"),
        ("North East",  "Seven Sisters",      "https://images.unsplash.com/photo-1622308644420-2275cf5b8e21?w=400&q=75"),
        ("Andaman",     "Island Paradise",    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=400&q=75"),
        ("Gujarat",     "Land of Legends",    "https://images.unsplash.com/photo-1609948543911-7f9c5f937180?w=400&q=75"),
        ("Karnataka",   "Many Worlds",        "https://images.unsplash.com/photo-1600100397608-e4e0cfddee25?w=400&q=75"),
        ("Uttarakhand", "Land of the Gods",   "https://images.unsplash.com/photo-1606210122158-eeb10e0a3101?w=400&q=75"),
        ("Punjab",      "Five Rivers",        "https://images.unsplash.com/photo-1609947017136-9dab4b23bcb1?w=400&q=75"),
        ("Odisha",      "Soul of India",      "https://images.unsplash.com/photo-1590080875515-8a3a8dc5735e?w=400&q=75"),
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


# ══════════════════════════════════════════════════════════════════════════════
#  INPUT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""<div class="input-wrap">
    <div class="input-title">🗺️ Describe Your Indian Adventure</div>
    <div class="input-sub">Tell us where you want to go, how long, your budget, and what experiences you're looking for.</div>
</div>""", unsafe_allow_html=True)

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

# Quick-fill chips — 4 columns
st.markdown('<div class="qf-row">', unsafe_allow_html=True)
qcols = st.columns(4)
quick_fill = ""
for i, label in enumerate(QUICK):
    with qcols[i % 4]:
        if st.button(label, key=f"q_{label}"):
            quick_fill = label
st.markdown('</div>', unsafe_allow_html=True)

# Handle prefill from state_detail (persist in session state; do not pop)
if "quick_fill_input" in st.session_state and st.session_state.get("quick_fill_input"):
    initial_val = st.session_state.get("quick_fill_input")
else:
    initial_val = quick_fill

user_query = st.text_area(
    "Your trip details",
    value=initial_val,
    placeholder="e.g. Plan a 7-day Rajasthan heritage trip covering Jaipur, Jodhpur, "
                "Udaipur with palace stays under ₹1.5 lakhs including flights from Mumbai",
    height=110,
    label_visibility="collapsed",
)

# If requested, scroll/focus the planner textarea so the user sees the prefilled text.
if st.session_state.get("scroll_to_planner"):
    # Focus the first textarea on the page and scroll into view.
    st.markdown(
        "<script>const t=document.querySelector('textarea'); if(t){t.focus(); t.scrollIntoView({behavior:'smooth', block:'center'});} </script>",
        unsafe_allow_html=True,
    )
    # reset the flag
    st.session_state["scroll_to_planner"] = False

generate = st.button("🪷  Plan My Bharat Yatra", use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
#  AGENT PIPELINE  (functionality unchanged)
# ══════════════════════════════════════════════════════════════════════════════
AGENT_META = {
    "flight_agent":    ("✈️", "Flight Agent"),
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
            "flight_results": "", "hotel_results": "",
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
                "flight_results": "",
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
                    if node_name == "flight_agent":
                        text = state_update.get("flight_results", "")
                        collected["flight_results"] = text
                        st.markdown(text or "_No flight data returned._")

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

        # ── Save ──
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"travel_plan_{timestamp}.md"
        save_dir = os.path.join(os.path.dirname(__file__), "travel_plans")
        os.makedirs(save_dir, exist_ok=True)

        file_content = f"""# Bharat Yatra — Travel Plan
**Query:** {user_query}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**User ID:** {thread_id}

---

## ✈️ Flight Information
{collected['flight_results'] or 'N/A'}

---

## 🏨 Hotel Information
{collected['hotel_results'] or 'N/A'}

---

## 🗓️ Itinerary
{collected['itinerary'] or 'N/A'}

---

## 🧠 Final Travel Plan
{collected['final_response'] or 'N/A'}

---
*LLM Calls: {collected['llm_calls']}*
"""
        with open(os.path.join(save_dir, filename), "w", encoding="utf-8") as f:
            f.write(file_content)

        dl_col, info_col = st.columns([1, 3])
        with dl_col:
            st.download_button(
                "⬇️ Download Plan", data=file_content,
                file_name=filename, mime="text/markdown",
                use_container_width=True)
        with info_col:
            st.markdown(
                f"<div class='save-bar'>📁 Saved to "
                f"<code>travel_plans/{filename}</code></div>",
                unsafe_allow_html=True)