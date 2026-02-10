import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURATION & RIGOR ---
st.set_page_config(
    page_title="Revenue-Driven Engineering | Agency",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ZINC DARK DESIGN SYSTEM (Custom HTML/CSS) ---
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>
    /* ZINC DARK CORE */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #09090b !important;
        color: #e4e4e7 !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: -0.02em;
    }

    [data-testid="stHeader"] {
        background: rgba(9, 9, 11, 0.8) !important;
        backdrop-filter: blur(10px);
    }

    /* TYPOGRAPHY: TRACKING-TIGHT */
    h1, h2, h3, h4 {
        font-weight: 800 !important;
        letter-spacing: -0.05em !important;
        color: #ffffff !important;
        margin-bottom: 1rem !important;
    }

    /* DASHBOARD SIDEBAR (STICKY) */
    [data-testid="stSidebar"] {
        background-color: #09090b !important;
        border-right: 1px solid #27272a !important;
        width: 300px !important;
    }

    .sidebar-content {
        padding: 2rem 1rem;
    }

    /* CUSTOM COMPONENT: SHADCN CARD */
    .zinc-card {
        background-color: #18181b;
        border: 1px solid #27272a;
        border-radius: 8px;
        padding: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .zinc-card:hover {
        border-color: #3f3f46;
        box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.02), 0 10px 30px rgba(0, 0, 0, 0.5);
        transform: translateY(-2px);
    }

    /* CUSTOM COMPONENT: PILL BADGE */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        background-color: rgba(63, 63, 70, 0.3);
        color: #a1a1aa;
        border: 1px solid #27272a;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .badge-primary {
        background-color: rgba(255, 255, 255, 0.1);
        color: #ffffff;
        border-color: rgba(255, 255, 255, 0.2);
    }

    /* GRID SYSTEM */
    .portfolio-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }

    .portfolio-item {
        position: relative;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #27272a;
        aspect-ratio: 16/10;
        background-color: #18181b;
    }

    .portfolio-item img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.7;
        transition: opacity 0.3s ease;
    }

    .portfolio-item:hover img {
        opacity: 0.4;
    }

    .portfolio-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 1.5rem;
        background: linear-gradient(transparent, rgba(9, 9, 11, 0.9));
        transform: translateY(10px);
        opacity: 0;
        transition: all 0.3s ease;
    }

    .portfolio-item:hover .portfolio-overlay {
        transform: translateY(0);
        opacity: 1;
    }

    /* BUTTONS */
    .stButton>button {
        background-color: #ffffff !important;
        color: #09090b !important;
        border-radius: 6px !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.2rem !important;
        width: 100%;
        transition: opacity 0.2s ease !important;
    }

    .stButton>button:hover {
        opacity: 0.9 !important;
    }

    /* HIDE STREAMLIT BRANDING */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: REVENUE-DRIVEN NAVIGATION ---
with st.sidebar:
    st.markdown(f"""
        <div style='margin-bottom: 2.5rem; margin-top: 1rem;'>
            <img src='https://images.unsplash.com/photo-1635332396251-850fd091b22e?q=80&w=200&auto=format&fit=crop' 
                 style='width: 100%; border-radius: 12px; border: 1px solid #27272a;'>
        </div>
        <div style='margin-bottom: 2rem;'>
            <h3 style='margin-bottom: 0.2rem !important;'>Mark Lorenz</h3>
            <p style='color: #a1a1aa; font-size: 0.85rem;'>Revenue-Driven Engineering</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 0.7rem; color: #52525b; text-transform: uppercase; font-weight: 700; margin-bottom: 1rem;'>Operations</p>", unsafe_allow_html=True)
    
    menu = ["Revenue Engine", "Solutions Stack", "Masterpieces", "Growth Strategy", "Inquiry Portal"]
    selection = st.radio("Nav", menu, label_visibility="collapsed")
    
    st.markdown("<div style='position: fixed; bottom: 2rem; width: 260px;'>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<p style='color: #52525b; font-size: 0.75rem;'>Status: Operational (Q1 2026)</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION: REVENUE ENGINE (HERO) ---
if selection == "Revenue Engine":
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("<div style='margin-top: 5vh;'>", unsafe_allow_html=True)
        st.markdown("<p style='color: #a1a1aa; font-weight: 500;'>Transforming code into capital.</p>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 4.5rem; line-height: 1;'>I Build High-Performance Web Apps.</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.25rem; color: #a1a1aa; margin-top: 1.5rem;'>Software isn't an expense—it's a leverage points. I engineer systems that solve expensive problems and drive measurable revenue growth.</p>", unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        btn_col1, btn_col2 = st.columns([1, 1.5])
        with btn_col1:
            if st.button("Start Growth Project"):
                st.toast("Initialization complete.")
        
    with col2:
        st.markdown("<div style='margin-top: 10vh; padding: 2rem; background: radial-gradient(circle at center, rgba(255,255,255,0.03) 0%, transparent 70%);'>", unsafe_allow_html=True)
        st.markdown("""
            <div class="zinc-card">
                <div>
                    <p style='color: #a1a1aa; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em;'>Direct ROI</p>
                    <h2>+42%</h2>
                    <p style='color: #a1a1aa;'>Average efficiency gain for client operations in 2025.</p>
                </div>
                <div style='margin-top: 1.5rem;'>
                    <span class="badge badge-primary">Spring Boot</span>
                    <span class="badge">React</span>
                    <span class="badge">Next.js</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- SECTION: SOLUTIONS STACK ---
elif selection == "Solutions Stack":
    st.markdown("<h1 style='margin-bottom: 0.5rem !important;'>Solutions Stack</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a1a1aa; margin-bottom: 3rem;'>Industrial-grade infrastructure for modern businesses.</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    solution_data = [
        {
            "title": "Enterprise Web Apps",
            "desc": "Full-stack architectures designed for scale, security, and high-concurrency user traffic.",
            "stack": ["Spring Boot", "Next.js", "PostgreSQL"]
        },
        {
            "title": "Visual Engineering",
            "desc": "High-fidelity UI systems that command premium pricing and establish market authority.",
            "stack": ["React", "Framer", "Zinc Design"]
        },
        {
            "title": "Systems Security",
            "desc": "Rigorous infrastructure auditing and hardening for high-stakes financial and data operations.",
            "stack": ["ISC2 Standard", "AWS", "NIST"]
        }
    ]
    
    for i, col in enumerate([c1, c2, c3]):
        with col:
            s = solution_data[i]
            stack_html = "".join([f'<span class="badge">{item}</span>' for item in s['stack']])
            st.markdown(f"""
                <div class="zinc-card">
                    <div>
                        <h3 style='margin-bottom: 1rem !important;'>{s['title']}</h3>
                        <p style='color: #a1a1aa; font-size: 0.9rem; line-height: 1.6;'>{s['desc']}</p>
                    </div>
                    <div style='margin-top: 2rem;'>
                        {stack_html}
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- SECTION: MASTERPIECES (PORTFOLIO GRID) ---
elif selection == "Masterpieces":
    st.markdown("<h1>Active Masterpieces</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a1a1aa;'>Recent commercial-grade deployments and high-stakes projects.</p>", unsafe_allow_html=True)
    
    # 3x3 MASONRY GRID SIMULATION
    st.markdown('<div class="portfolio-grid">', unsafe_allow_html=True)
    
    projects = [
        {"title": "TradeMate CRM", "type": "FinTech", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=TradeMate+CRM"},
        {"title": "HIMO AI", "type": "Automation", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=HIMO+AI"},
        {"title": "Zenith Engine", "type": "UI/UX", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=Zenith+Engine"},
        {"title": "Wildcats Esports", "type": "Branding", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=Wildcats+Esports"},
        {"title": "Doddsville Web", "type": "Operations", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=Doddsville"},
        {"title": "Cyber Audit", "type": "Security", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=Cyber+Audit"},
        {"title": "Proprietary X", "type": "R&D", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=Proprietary+X"},
        {"title": "The Nexus", "type": "E-Commerce", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=The+Nexus"},
        {"title": "Alpha Protocol", "type": "Infrastucture", "img": "https://placehold.co/600x400/18181b/e4e4e7?text=Alpha+Protocol"},
    ]
    
    # Render with multi-column to simulate grid
    cols = st.columns(3)
    for i in range(9):
        with cols[i % 3]:
            p = projects[i]
            st.markdown(f"""
                <div class="portfolio-item">
                    <img src="{p['img']}">
                    <div class="portfolio-overlay">
                        <p style='color: #ffffff; font-weight: 700; margin-bottom: 0.2rem;'>{p['title']}</p>
                        <p style='color: #a1a1aa; font-size: 0.75rem; margin-bottom: 0;'>{p['type']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.write("")
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION: GROWTH STRATEGY ---
elif selection == "Growth Strategy":
    st.markdown("<h1>Growth Strategy</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="zinc-card" style='margin-bottom: 2rem;'>
            <h3 style='color: #ffffff;'>The Execution Protocol</h3>
            <p style='color: #a1a1aa;'>My process is built on speed, transparency, and relentless focus on end-user value. We define the KPI, architect the solution, and deploy with zero downtime.</p>
        </div>
    """, unsafe_allow_html=True)
    
    levels = st.columns(3)
    phases = [
        {"n": "01", "t": "Discovery", "d": "Identify fiscal leaks and technical debt."},
        {"n": "02", "t": "Engineering", "d": "Build the custom solution with rigor."},
        {"n": "03", "t": "Deployment", "d": "Scale and monitor for maximum ROI."}
    ]
    
    for i, col in enumerate(levels):
        with col:
            p = phases[i]
            st.markdown(f"""
                <div class="zinc-card" style='border-top: 2px solid #3f3f46;'>
                    <h1 style='color: #3f3f46; font-size: 3rem;'>{p['n']}</h1>
                    <h3>{p['t']}</h3>
                    <p style='color: #a1a1aa; font-size: 0.85rem;'>{p['d']}</p>
                </div>
            """, unsafe_allow_html=True)

# --- SECTION: INQUIRY PORTAL ---
elif selection == "Inquiry Portal":
    st.markdown("<h1>Inquiry Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a1a1aa; margin-bottom: 2rem;'>Secure a high-performance partner for your next operation.</p>", unsafe_allow_html=True)
    
    with st.form("agency_inquiry"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Entity Name", placeholder="Company or Individual")
        with c2:
            email = st.text_input("Communication Channel", placeholder="email@address.com")
        
        scope = st.selectbox("Operation Scope", ["Web Platform Development", "Visual Identity Systems", "Security Audit", "Fractional CTO Services"])
        objective = st.text_area("Strategic Objectives", placeholder="What are your primary KPIs?")
        
        if st.form_submit_button("Initiate Protocol"):
            if name and email and objective:
                st.success("Transmission Received. Analyzing requirements.")
            else:
                st.warning("Encryption Error: All fields required.")

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; border-top: 1px solid #27272a; padding-top: 2rem;'>
        <p style='color: #52525b; font-size: 0.8rem;'>© 2026 MARK LORENZ | REVENUE-DRIVEN ENGINEERING</p>
    </div>
""", unsafe_allow_html=True)
