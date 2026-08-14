import streamlit as st
from states_data import INDIA_STATES, NEIGHBOURS
from utils.prefill_utils import build_prefill_prompt
from image_utils import asset_src

def render_state_detail(name: str, is_country: bool = False):
    """
    Renders a premium showcase detail view of an Indian state or neighbouring country.
    """
    # Fetch data
    if is_country:
        data = NEIGHBOURS.get(name)
        title_prefix = f"{data.get('flag', '📍')} " if data else "📍 "
        title_text = name
    else:
        data = INDIA_STATES.get(name)
        title_prefix = "🇮🇳 "
        title_text = data.get("full_name", name) if data else name

    if not data:
        st.error(f"Destination '{name}' details not found.")
        if st.button("← Back to Explore", key="back_not_found"):
            st.query_params.clear()
            st.rerun()
        return


    # Back Navigation row
    back_col, prefill_col = st.columns([1, 1])
    with back_col:
        if st.button("← Back to Explore", key="back_btn_top", use_container_width=True):
            st.query_params.clear()
            st.rerun()

    # Pre-fill CTA setup (use normalized prompt builder)
    prefill_prompt = build_prefill_prompt(name, data, is_country=is_country)

    with prefill_col:
        if st.button("✨ Prefill Travel Planner", key="prefill_btn", use_container_width=True):
            st.session_state["quick_fill_input"] = prefill_prompt
            st.query_params.clear()
            # Set anchor to jump to input on next render
            st.session_state["scroll_to_planner"] = True
            st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

    # Main Detail Layout
    st.markdown(f"""
    <div class="detail-container">
        <div class="detail-header">
            <div class="detail-title">{title_prefix}{title_text}</div>
            <div class="detail-tagline">“ {data.get('tagline', '')} ”</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_info, col_visual = st.columns([5, 7])

    with col_info:
        # Stats Grid
        if is_country:
            st.markdown(f"""
            <div class="detail-grid" style="grid-template-columns: 1fr;">
                <div class="detail-stat">
                    <div class="detail-stat-lbl">🌅 Best Time to Visit</div>
                    <div class="detail-stat-val">{data.get('best_time', 'N/A')}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="detail-grid">
                <div class="detail-stat">
                    <div class="detail-stat-lbl">🏢 Capital</div>
                    <div class="detail-stat-val">{data.get('capital', 'N/A')}</div>
                </div>
                <div class="detail-stat">
                    <div class="detail-stat-lbl">🌅 Best Season</div>
                    <div class="detail-stat-val">{data.get('best_time', 'N/A')}</div>
                </div>
                <div class="detail-stat">
                    <div class="detail-stat-lbl">💰 Approx Budget</div>
                    <div class="detail-stat-val" style="font-size: 0.8rem;">{data.get('budget', 'N/A')}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div class='detail-section-title'>About the Destination</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='detail-desc'>{data.get('description', '')}</div>", unsafe_allow_html=True)

    with col_visual:
        st.markdown("<div class='detail-section-title'>Key Highlights & Experiences</div>", unsafe_allow_html=True)
        for highlight in data.get("highlights", []):
            st.markdown(f"""
            <div class="highlight-item">
                <span class="highlight-bullet">✦</span>
                <span>{highlight}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("<div class='detail-section-title'>Gallery</div>", unsafe_allow_html=True)
        
        # Display images from states_data
        if is_country:
            image_reference = data.get("image")
            if image_reference:
                st.html(f"""
                <div class="gallery-container single-gallery">
                    <div class="gallery-img-wrapper">
                        <img src="{asset_src(image_reference, name)}" alt="{name}"/>
                    </div>
                </div>
                """)
        else:
            images = data.get("images", [])
            if images:
                gallery_html = '<div class="gallery-container">'
                for image_index, image_reference in enumerate(images, start=1):
                    gallery_html += f"""
                    <div class="gallery-img-wrapper">
                        <img src="{asset_src(image_reference, name, image_index)}" alt="{name}"/>
                    </div>
                    """
                gallery_html += '</div>'
                st.html(gallery_html)
