import streamlit as st

def show():
    # ── Hero ──────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style='text-align:center; padding: 3rem 0 2rem; position:relative;'>
        <div style='font-family: Bebas Neue, sans-serif; font-size: clamp(3rem,8vw,6rem);
             line-height:1; letter-spacing:0.05em;
             background: linear-gradient(135deg, #00E5FF 0%, #FF2D78 55%, #FFB800 100%);
             -webkit-background-clip:text; -webkit-text-fill-color:transparent;
             filter: drop-shadow(0 0 40px rgba(0,229,255,0.3));'>
            RUN AI COACH
        </div>
        <div style='font-family:JetBrains Mono,monospace; font-size:0.9rem;
             color:var(--txt2); letter-spacing:0.3em; margin-top:0.5rem;
             text-transform:uppercase;'>
            AI-POWERED ELITE RUNNING FORM ANALYZER
        </div>
        <div style='font-size:0.8rem; color:var(--txt3); margin-top:0.4rem;
             font-family:JetBrains Mono,monospace;'>
            YOLOv8 Pose Estimation · Real-time Biomechanics · Personal AI Coach
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats bar ─────────────────────────────────────────────────────────────
    stats = [("14", "Biomechanical Metrics", "#00E5FF"),
             ("60fps", "Frame Analysis", "#FF2D78"),
             ("YOLOv8", "AI Detection", "#39FF14"),
             ("Pro DB", "Athlete Benchmarks", "#FFB800"),
             ("Claude", "AI Coach", "#A855F7")]

    cols = st.columns(5)
    for col, (val, lbl, color) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div style='text-align:center; background:var(--bg2);
                 border:1px solid var(--border); border-radius:12px; padding:1rem 0.5rem;
                 border-top: 2px solid {color};'>
                <div style='font-family:Bebas Neue; font-size:1.8rem; color:{color};
                     text-shadow: 0 0 20px {color}55;'>{val}</div>
                <div style='font-size:0.7rem; color:var(--txt3); font-family:JetBrains Mono;
                     margin-top:0.2rem; line-height:1.3;'>{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Feature cards ─────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    features = [
        ("🎯", "วิเคราะห์ท่าวิ่ง", "#00E5FF",
         "ตรวจจับ 17 จุดบนร่างกายแบบ Real-time ด้วย YOLOv8 คำนวณมุมข้อต่อ การก้าว และสมดุลลำตัวทุกเฟรม"),
        ("🏆", "เปรียบกับมือโปร", "#FF2D78",
         "เทียบกับฐานข้อมูลนักวิ่งระดับโลก ค้นหาจุดที่ต้องพัฒนาและวางแผนซ้อมอย่างมีเป้าหมาย"),
        ("💪", "โปรแกรมซ้อม AI", "#39FF14",
         "สร้างแผนฝึกซ้อมเฉพาะบุคคลตามจุดอ่อนที่ AI ตรวจพบ พร้อมวิดีโอแนะนำและตัวชี้วัดความก้าวหน้า"),
    ]
    for col, (icon, title, color, desc) in zip([col1, col2, col3], features):
        with col:
            st.markdown(f"""
            <div class='metric-card' style='height:220px; border-top:2px solid {color};'>
                <div style='font-size:2.5rem; margin-bottom:0.8rem;'>{icon}</div>
                <div style='font-family:Exo 2,sans-serif; font-size:1.1rem; font-weight:800;
                     color:{color}; margin-bottom:0.6rem;'>{title}</div>
                <div style='color:var(--txt2); font-size:0.9rem; line-height:1.6;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── How it works ──────────────────────────────────────────────────────────
    st.markdown("""
    <div style='font-family:Bebas Neue; font-size:1.8rem; color:var(--c1);
         letter-spacing:0.1em; margin-bottom:1rem;'>
        ⚡ วิธีการทำงาน
    </div>
    """, unsafe_allow_html=True)

    steps = [
        ("01", "📤", "อัปโหลดวิดีโอ",
         "รองรับ MP4, MOV, AVI, MKV ถ่ายจากด้านข้างระดับสะโพก ความยาว 5-60 วินาที", "#00E5FF"),
        ("02", "🤖", "AI ประมวลผล",
         "YOLOv8 ตรวจจับ 17 จุดร่างกายต่อเฟรม คำนวณ 14 ค่าชีวกลศาสตร์แบบ Real-time", "#FF2D78"),
        ("03", "📊", "รับรายงาน",
         "เห็นผลวิเคราะห์ละเอียด กราฟแต่ละเมทริก เทียบมาตรฐานมืออาชีพ และคะแนนรวม", "#39FF14"),
        ("04", "💬", "AI โค้ชแนะนำ",
         "คุยกับ AI Coach เพื่อรับคำแนะนำเฉพาะตัว แผนฝึกซ้อม และติดตามพัฒนาการ", "#FFB800"),
    ]

    cols = st.columns(4)
    for col, (num, icon, title, desc, color) in zip(cols, steps):
        with col:
            st.markdown(f"""
            <div style='text-align:center; padding:1rem 0.5rem;'>
                <div style='font-family:Bebas Neue; font-size:3rem; color:{color};
                     opacity:0.2; line-height:1; margin-bottom:-0.5rem;'>{num}</div>
                <div style='font-size:2rem; margin-bottom:0.5rem;'>{icon}</div>
                <div style='font-weight:800; color:var(--txt1); margin-bottom:0.4rem; font-size:0.95rem;'>{title}</div>
                <div style='color:var(--txt2); font-size:0.82rem; line-height:1.5;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Metrics grid ──────────────────────────────────────────────────────────
    st.markdown("""
    <div style='font-family:Bebas Neue; font-size:1.8rem; color:var(--c1);
         letter-spacing:0.1em; margin-bottom:1rem;'>
        📐 ตัวชี้วัดที่วิเคราะห์ (14 Metrics)
    </div>
    """, unsafe_allow_html=True)

    metrics = [
        ("🎯", "Head Lean", "มุมเอียงศีรษะ", "#00E5FF"),
        ("⚖️", "Shoulder Roll", "การหมุนไหล่", "#FF2D78"),
        ("🍑", "Pelvic Drop", "การตกของสะโพก", "#FFB800"),
        ("📐", "Torso Lean", "มุมเอียงลำตัว", "#39FF14"),
        ("🦵", "L/R Hip Angle", "มุมสะโพก", "#A855F7"),
        ("🦿", "L/R Knee Angle", "มุมเข่า", "#00E5FF"),
        ("💪", "L/R Arm Angle", "มุมแขน", "#FF2D78"),
        ("👣", "Step Length", "ระยะก้าว", "#FFB800"),
        ("📊", "Vert. Oscillation", "การแกว่งแนวตั้ง", "#39FF14"),
        ("🏃", "Foot Strike", "จังหวะการลงเท้า", "#A855F7"),
    ]

    cols = st.columns(5)
    for i, (icon, name, th, color) in enumerate(metrics):
        with cols[i % 5]:
            st.markdown(f"""
            <div style='background:var(--bg2); border:1px solid var(--border);
                 border-left:3px solid {color}; border-radius:8px;
                 padding:0.6rem 0.8rem; margin-bottom:0.5rem;'>
                <div style='font-size:1.2rem;'>{icon}</div>
                <div style='font-size:0.82rem; font-weight:700; color:var(--txt1);'>{name}</div>
                <div style='font-size:0.72rem; color:var(--txt3);'>{th}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ── CTA ───────────────────────────────────────────────────────────────────
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("🚀 เริ่มวิเคราะห์ท่าวิ่งเลย!", use_container_width=True):
            st.session_state.current_page = "upload"
            st.rerun()

    st.markdown("""
    <div style='text-align:center; margin-top:1rem; color:var(--txt3); font-size:0.8rem;
         font-family:JetBrains Mono;'>
        หรือดูตัวอย่างผลวิเคราะห์ด้านล่างก่อน ↓
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Demo preview box ──────────────────────────────────────────────────────
    st.markdown("""
    <div style='background:linear-gradient(135deg,rgba(0,229,255,0.05),rgba(255,45,120,0.05));
         border:1px solid var(--border); border-radius:16px; padding:1.5rem;'>
        <div style='font-family:Bebas Neue; font-size:1.2rem; color:var(--c4);
             margin-bottom:0.8rem;'>💡 ตัวอย่างผลวิเคราะห์จากนักวิ่งจริง</div>
        <div style='display:grid; grid-template-columns:repeat(4,1fr); gap:0.8rem;'>
    """, unsafe_allow_html=True)

    demo = [("68", "คะแนนรวม", "#FFB800"), ("7.2°", "Head Lean", "#00E5FF"),
            ("6.8°", "Pelvic Drop", "#FF2D78"), ("9.3°", "Torso Lean", "#39FF14")]
    cols = st.columns(4)
    for col, (val, lbl, color) in zip(cols, demo):
        with col:
            st.markdown(f"""
            <div style='text-align:center; background:var(--bg2); border-radius:10px; padding:0.8rem;'>
                <div style='font-family:Bebas Neue; font-size:2.2rem; color:{color};'>{val}</div>
                <div style='font-size:0.75rem; color:var(--txt3); font-family:JetBrains Mono;'>{lbl}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)
