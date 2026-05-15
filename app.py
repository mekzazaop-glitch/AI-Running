import streamlit as st
import os

st.set_page_config(
    page_title="RunAI Coach",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "RunAI Coach v3.0 — AI-Powered Running Form Analyzer"}
)

# ── CSS ────────────────────────────────────────────────────────────────────────
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100..900;1,100..900&family=JetBrains+Mono:wght@300;400;700&family=Bebas+Neue&display=swap');

    :root {
        --bg0: #02060F;
        --bg1: #060D1C;
        --bg2: #0A1628;
        --bg3: #0E1E38;
        --bg4: #122444;
        --c1: #00E5FF;
        --c2: #FF2D78;
        --c3: #39FF14;
        --c4: #FFB800;
        --c5: #A855F7;
        --txt1: #EEF4FF;
        --txt2: #7A9DC0;
        --txt3: #3A5A80;
        --border: #1A3050;
        --glow1: rgba(0,229,255,0.25);
        --glow2: rgba(255,45,120,0.25);
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    html, body, .stApp {
        background: var(--bg0) !important;
        color: var(--txt1) !important;
        font-family: 'Exo 2', sans-serif !important;
    }

    /* ── scrollbar ── */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: var(--bg1); }
    ::-webkit-scrollbar-thumb { background: var(--c1); border-radius: 2px; }

    /* ── hide streamlit chrome ── */
    #MainMenu, footer, header, [data-testid="stToolbar"],
    .viewerBadge_container__1QSob { display: none !important; }

    /* ── sidebar ── */
    [data-testid="stSidebar"] {
        background: var(--bg1) !important;
        border-right: 1px solid var(--border) !important;
        padding-top: 0 !important;
    }
    [data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }
    [data-testid="stSidebar"] * { color: var(--txt1) !important; }

    /* ── buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, var(--c1) 0%, #0099CC 100%) !important;
        color: #000 !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Exo 2', sans-serif !important;
        font-weight: 800 !important;
        font-size: 0.9rem !important;
        padding: 0.65rem 1.4rem !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
        transition: all 0.25s ease !important;
        cursor: pointer !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 30px var(--glow1) !important;
        filter: brightness(1.1) !important;
    }
    .stButton > button:active { transform: translateY(0) !important; }

    /* nav buttons */
    .nav-btn > button {
        background: transparent !important;
        color: var(--txt2) !important;
        border: 1px solid var(--border) !important;
        font-size: 0.85rem !important;
        padding: 0.5rem 0.8rem !important;
        text-align: left !important;
        width: 100% !important;
        justify-content: flex-start !important;
    }
    .nav-btn > button:hover {
        background: rgba(0,229,255,0.08) !important;
        border-color: var(--c1) !important;
        color: var(--c1) !important;
        transform: none !important;
        box-shadow: none !important;
    }
    .nav-btn-active > button {
        background: rgba(0,229,255,0.12) !important;
        border-color: var(--c1) !important;
        color: var(--c1) !important;
    }

    /* ── tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        background: var(--bg2) !important;
        border-radius: 10px !important;
        gap: 4px !important;
        padding: 5px !important;
        border: 1px solid var(--border) !important;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        color: var(--txt2) !important;
        font-family: 'Exo 2', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 7px !important;
        padding: 0.4rem 1rem !important;
    }
    .stTabs [aria-selected="true"] {
        background: var(--c1) !important;
        color: #000 !important;
    }

    /* ── progress ── */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--c1), var(--c2)) !important;
        border-radius: 99px !important;
    }
    .stProgress > div > div {
        background: var(--bg3) !important;
        border-radius: 99px !important;
    }

    /* ── file uploader ── */
    [data-testid="stFileUploader"] {
        background: var(--bg2) !important;
        border: 2px dashed var(--border) !important;
        border-radius: 16px !important;
        transition: border-color 0.3s !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--c1) !important;
    }

    /* ── metric card ── */
    .metric-card {
        background: var(--bg2);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 1.2rem;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, var(--c1), var(--c2));
    }
    .metric-card:hover {
        border-color: rgba(0,229,255,0.5);
        box-shadow: 0 0 30px var(--glow1), inset 0 0 30px rgba(0,229,255,0.03);
        transform: translateY(-3px);
    }

    /* ── alerts ── */
    .alert-good {
        background: rgba(57,255,20,0.08);
        border-left: 3px solid var(--c3);
        border-radius: 0 8px 8px 0;
        padding: 0.8rem 1rem;
        margin: 0.4rem 0;
        color: var(--c3);
    }
    .alert-warn {
        background: rgba(255,184,0,0.08);
        border-left: 3px solid var(--c4);
        border-radius: 0 8px 8px 0;
        padding: 0.8rem 1rem;
        margin: 0.4rem 0;
        color: var(--c4);
    }
    .alert-bad {
        background: rgba(255,45,120,0.08);
        border-left: 3px solid var(--c2);
        border-radius: 0 8px 8px 0;
        padding: 0.8rem 1rem;
        margin: 0.4rem 0;
        color: var(--c2);
    }
    .alert-info {
        background: rgba(0,229,255,0.06);
        border-left: 3px solid var(--c1);
        border-radius: 0 8px 8px 0;
        padding: 0.8rem 1rem;
        margin: 0.4rem 0;
        color: var(--c1);
    }

    /* ── selectbox ── */
    .stSelectbox > div > div {
        background: var(--bg3) !important;
        border-color: var(--border) !important;
        color: var(--txt1) !important;
    }

    /* ── expander ── */
    .streamlit-expanderHeader {
        background: var(--bg2) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--txt1) !important;
        font-family: 'Exo 2', sans-serif !important;
        font-weight: 600 !important;
    }
    .streamlit-expanderContent {
        background: var(--bg2) !important;
        border: 1px solid var(--border) !important;
        border-top: none !important;
    }

    /* ── divider ── */
    hr { border-color: var(--border) !important; }

    /* ── mono font ── */
    .mono { font-family: 'JetBrains Mono', monospace !important; }

    /* ── grid bg pattern ── */
    .grid-bg {
        position: fixed; inset: 0; z-index: -1; pointer-events: none;
        background-image:
            linear-gradient(rgba(0,229,255,0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,229,255,0.03) 1px, transparent 1px);
        background-size: 40px 40px;
    }

    /* ── scan line ── */
    @keyframes scan {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100vh); }
    }
    .scan-line {
        position: fixed; left: 0; right: 0; height: 2px;
        background: linear-gradient(transparent, rgba(0,229,255,0.15), transparent);
        z-index: 9999; pointer-events: none;
        animation: scan 6s linear infinite;
    }

    /* ── glow text ── */
    .glow { text-shadow: 0 0 20px currentColor; }

    /* ── badge ── */
    .badge {
        display: inline-block;
        padding: 0.15rem 0.6rem;
        border-radius: 99px;
        font-size: 0.75rem;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
    }
    .badge-good { background: rgba(57,255,20,0.15); color: var(--c3); border: 1px solid var(--c3); }
    .badge-warn { background: rgba(255,184,0,0.15); color: var(--c4); border: 1px solid var(--c4); }
    .badge-bad  { background: rgba(255,45,120,0.15); color: var(--c2); border: 1px solid var(--c2); }
    </style>
    <div class="grid-bg"></div>
    <div class="scan-line"></div>
    """, unsafe_allow_html=True)

load_css()

# ── Session State Init ─────────────────────────────────────────────────────────
for k, v in {
    "current_page": "home",
    "uploaded_video": None,
    "analysis_results": None,
    "video_path": None,
    "video_bytes": None,
    "chat_history": [],
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 1.5rem 1rem 1rem; border-bottom: 1px solid var(--border); margin-bottom: 1rem;'>
        <div style='font-family: Bebas Neue, sans-serif; font-size: 2.2rem; line-height: 1;
             background: linear-gradient(135deg, #00E5FF, #FF2D78);
             -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            RUN AI
        </div>
        <div style='font-family: JetBrains Mono, monospace; color: var(--txt3);
             font-size: 0.7rem; letter-spacing: 0.2em; margin-top: 2px;'>
            ELITE COACH v3.0
        </div>
    </div>
    """, unsafe_allow_html=True)

    pages = [
        ("🏠", "หน้าหลัก", "home"),
        ("📤", "อัปโหลดวิดีโอ", "upload"),
        ("🤖", "วิเคราะห์ท่าวิ่ง", "analyze"),
        ("📊", "รายงานละเอียด", "report"),
        ("🏆", "เปรียบเทียบมือโปร", "compare"),
        ("💪", "แผนฝึก AI", "training"),
        ("💬", "AI โค้ช Chat", "chat"),
        ("📚", "คู่มือการใช้งาน", "guide"),
    ]

    for icon, label, pid in pages:
        is_active = st.session_state.current_page == pid
        css_class = "nav-btn-active" if is_active else "nav-btn"
        st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
        if st.button(f"{icon}  {label}", key=f"nav_{pid}", use_container_width=True):
            st.session_state.current_page = pid
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Status
    if st.session_state.uploaded_video:
        vname = st.session_state.uploaded_video[:22] + "…" if len(st.session_state.uploaded_video) > 25 else st.session_state.uploaded_video
        st.markdown(f"""
        <div style='background: rgba(57,255,20,0.08); border: 1px solid var(--c3);
             border-radius: 10px; padding: 0.8rem; margin-bottom: 0.5rem;'>
            <div style='color: var(--c3); font-size: 0.75rem; font-weight: 700; margin-bottom: 0.3rem;'>
                ✅ VIDEO READY
            </div>
            <div style='color: var(--txt2); font-size: 0.8rem; font-family: JetBrains Mono;
                 overflow: hidden; text-overflow: ellipsis; white-space: nowrap;'>
                {vname}
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.session_state.analysis_results:
            score = st.session_state.analysis_results.get("overall_score", 0)
            col = "#39FF14" if score >= 80 else "#FFB800" if score >= 60 else "#FF2D78"
            st.markdown(f"""
            <div style='background: rgba(0,229,255,0.06); border: 1px solid var(--border);
                 border-radius: 10px; padding: 0.8rem; text-align: center;'>
                <div style='font-family: Bebas Neue; font-size: 2rem; color: {col};'>{score}</div>
                <div style='color: var(--txt3); font-size: 0.7rem; font-family: JetBrains Mono;'>OVERALL SCORE</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background: rgba(255,45,120,0.06); border: 1px solid rgba(255,45,120,0.4);
             border-radius: 10px; padding: 0.8rem; text-align: center;'>
            <div style='color: var(--c2); font-size: 0.8rem;'>⚠️ ยังไม่มีวิดีโอ</div>
            <div style='color: var(--txt3); font-size: 0.75rem; margin-top: 0.2rem;'>อัปโหลดเพื่อเริ่มต้น</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style='margin-top: 1.5rem; color: var(--txt3); font-size: 0.7rem;
         font-family: JetBrains Mono; text-align: center; padding-top: 1rem;
         border-top: 1px solid var(--border);'>
        Powered by YOLOv8 + Claude AI<br>
        <span style='color: var(--txt3); opacity: 0.5;'>© 2025 RunAI Coach</span>
    </div>
    """, unsafe_allow_html=True)

# ── Page Router ───────────────────────────────────────────────────────────────
page = st.session_state.current_page

import sys
sys.path.insert(0, os.path.dirname(__file__))

if page == "home":
    from pages import home; home.show()
elif page == "upload":
    from pages import upload; upload.show()
elif page == "analyze":
    from pages import analyze; analyze.show()
elif page == "report":
    from pages import report; report.show()
elif page == "compare":
    from pages import compare; compare.show()
elif page == "training":
    from pages import training; training.show()
elif page == "chat":
    from pages import chat; chat.show()
elif page == "guide":
    from pages import guide; guide.show()
