import streamlit as st
import pandas as pd
from datetime import datetime
import streamlit_shadcn_ui as sd

# --- CONFIGURATION & RIGOR ---
st.set_page_config(
    page_title="Mark Lorenz | Digital Architect",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- THE ZENITH VISUAL ENGINE (Refined for Shadcn Harmony) ---
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Inter:wght@100..900&display=swap" rel="stylesheet">

<style>
    /* Base Reset & Core Typography */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        color: #F1F5F9;
    }

    /* THE DYNAMIC MESH */
    .stApp {
        background-color: #020617;
        background-image: 
            radial-gradient(at 0% 0%, hsla(222,47%,11%,1) 0, transparent 50%), 
            radial-gradient(at 50% 0%, hsla(190,90%,50%,0.1) 0, transparent 50%),
            radial-gradient(at 100% 0%, hsla(260,80%,60%,0.1) 0, transparent 50%);
        background-attachment: fixed;
    }

    /* Typography Overrides */
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
        letter-spacing: -0.04em !important;
    }

    /* GLASSMORHPISM 2.0 */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* ZENITH CARD DESIGN (Fallback for deep nesting) */
    .zenith-card {
        background: rgba(30, 41, 59, 0.3);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2.5rem;
        transition: all 0.4s ease;
    }
    .zenith-card:hover {
        transform: translateY(-5px);
        border-color: rgba(34, 211, 238, 0.3);
    }

    /* HERO TEXT */
    .hero-gradient {
        background: linear-gradient(to right, #22d3ee, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: clamp(2.5rem, 5vw, 4.5rem);
        font-weight: 900;
        line-height: 1.1;
    }

    /* CUSTOM COMPONENT: THE PILL CLOUD (Harmony with Shadcn Badges) */
    .pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 50px;
        background: rgba(34, 211, 238, 0.05);
        border: 1px solid rgba(34, 211, 238, 0.1);
        color: #22d3ee;
        font-size: 0.75rem;
        margin: 2px;
    }

    /* SCROLLBAR REFINEMENT */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.05); border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(34, 211, 238, 0.2); }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION DATA ---
NAV_ITEMS = {
    "The Zenith": "Home",
    "Solutions": "Services",
    "Masterpieces": "Portfolio",
    "The Journey": "Experience",
    "Collaborate": "Contact"
}

with st.sidebar:
    st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <img src='https://api.dicebear.com/7.x/avataaars/svg?seed=MarkLorenz&backgroundColor=020617' 
                 style='width: 120px; border-radius: 30px; border: 1px solid rgba(34, 211, 238, 0.2); padding: 5px;'>
        </div>
    """, unsafe_allow_html=True)
    
    st.title("Mark Lorenz")
    sd.badges(badge_list=[("Senior Technologist", "outline")])
    
    st.divider()
    selection = st.radio("Primary Selection", list(NAV_ITEMS.keys()), label_visibility="collapsed")
    current_page = NAV_ITEMS[selection]
    
    st.divider()
    st.download_button(
        label="📄 Export Credentials",
        data="MARK LORENZ | ZENITH CREDENTIALS",
        file_name="Mark_Lorenz_Zenith.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# --- PAGE: HOME (THE ZENITH) ---
if current_page == "Home":
    col_l, col_r = st.columns([1.6, 1])
    
    with col_l:
        st.markdown("<p style='color: #22d3ee; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase;'>Architecting Futures</p>", unsafe_allow_html=True)
        st.markdown('<h1 class="hero-gradient">Where Strategy <br>Meets Extraordinary <br>Engineering.</h1>', unsafe_allow_html=True)
        st.markdown("### I specialize in **Scale**, **Security**, and **High-Frequency Visuals**.")
        
        st.write("")
        sd.card(title="Value Proposition", content="Every solution I engineer is built on a foundation of zero-error logic and distinctive brand identity. I deliver products that operate at the edge of possibility.", description="Executive Tier Partnership")
        
        st.write("")
        if st.button("Initiate Collaboration ➝"):
            st.toast("Ready to elevate your vision.")
            st.balloons()
            
    with col_r:
        st.markdown("<div style='margin-top: 2rem;'>", unsafe_allow_html=True)
        sd.metric_card(title="Solutions Shipped", value="15+", content="Industry Grade", mode="standard")
        st.write("")
        sd.metric_card(title="Alpha Delivered", value="100%", content="Client Satisfaction", mode="standard")
        st.write("")
        sd.metric_card(title="Reliability", value="99.9%", content="System Uptime", mode="standard")
        st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE: SERVICES (SOLUTIONS) ---
elif current_page == "Services":
    st.markdown("<h1 style='text-align: center;'>Strategic Solutions</h1>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    services = [
        {"icon": "💻", "title": "Web Ops", "desc": "High-resiliancy systems using Next.js & Spring Boot."},
        {"icon": "🎨", "title": "Brand Tier", "desc": "Award-worthy visual identities and UI systems."},
        {"icon": "🛡️", "title": "Consulting", "desc": "Infrastructure auditing and security hardening."}
    ]
    
    for i, col in enumerate([c1, c2, c3]):
        with col:
            s = services[i]
            st.markdown(f"""
                <div class="zenith-card">
                    <h1 style='font-size: 3rem; margin: 0;'>{s['icon']}</h1>
                    <h3 style='margin-top: 1rem;'>{s['title']}</h3>
                    <p style='color: #94A3B8;'>{s['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.write("")
            sd.badges(badge_list=[("Enterprise Ready", "secondary")])

# --- PAGE: PORTFOLIO (MASTERPIECES) ---
elif current_page == "Portfolio":
    st.title("Featured Masterpieces")
    
    # Using Shadcn tabs for nested perfection
    tab_selection = sd.tabs(tabs=["Full Systems", "Visual Designs"], key="portfolio_tabs")
    
    if tab_selection == "Full Systems":
        st.write("")
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            sd.card(title="TradeMate CRM", content="The industry standard for tradesperson revenue management.", description="Java | Spring Boot | React")
            st.button("Explore Case Study", key="tm_s")
        with c_p2:
            sd.card(title="HIMO Ecosystem", content="A suite of AI-driven tools for high-frequency freelancer success.", description="Python | OpenAI | Streamlit")
            st.button("Explore Case Study", key="himo_s")
            
    elif tab_selection == "Visual Designs":
        st.write("")
        st.info("🎨 High-resolution visual assets and 3D motion design portfolios are available upon inquiry.")
        sd.badges(badge_list=[("Design Portfolio Enabled", "outline")])

# --- PAGE: EXPERIENCE (THE JOURNEY) ---
elif current_page == "Experience":
    st.header("Professional Trajectory")
    
    col_l, col_r = st.columns([1.5, 1])
    
    with col_l:
        st.markdown("""
            <div style='border-left: 2px solid rgba(255,255,255,0.05); padding-left: 2rem; margin-left: 1rem;'>
                <div style='margin-bottom: 2.5rem;'>
                    <h4 style='color: #22d3ee; margin:0;'>Head of Creative Services</h4>
                    <p style='color: #94A3B8; font-size: 0.8rem;'>Wildcats Esports | 2025</p>
                    <p>Led brand direction for major championships, achieving 30% faster production cycles.</p>
                </div>
                <div style='margin-bottom: 2.5rem;'>
                    <h4 style='color: #22d3ee; margin:0;'>Full Stack Developer</h4>
                    <p style='color: #94A3B8; font-size: 0.8rem;'>Graham & Doddsville | 2025</p>
                    <p>Optimized core database infrastructures for high-frequency data operations.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_r:
        st.markdown("<div class='zenith-card' style='padding: 1.5rem;'>", unsafe_allow_html=True)
        st.subheader("Credentials")
        sd.badges(badge_list=[("ISC2 Cybersecurity", "default")])
        st.write("")
        sd.badges(badge_list=[("GA Data Analytics", "default")])
        st.write("")
        sd.badges(badge_list=[("AWS Cloud Arch", "secondary")])
        st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE: CONTACT (COLLABORATE) ---
elif current_page == "Contact":
    st.title("Secure a Partnership")
    
    c_form, c_info = st.columns([1.5, 1])
    
    with c_form:
        with st.form("contact_protocol"):
            name = st.text_input("Entity Name")
            email = st.text_input("Communication Channel (Email)")
            details = st.text_area("Scope & Objectives")
            if st.form_submit_button("Initiate Protocol ➝"):
                if name and email and details:
                    st.success("Connection confirmed. Peer review in progress.")
                    st.balloons()
                else:
                    st.error("Incomplete packet. Please fill all fields.")
    
    with c_info:
        st.markdown("<div class='zenith-card' style='padding: 2rem;'>", unsafe_allow_html=True)
        st.markdown("### Intel")
        st.write("📍 **Base:** Cebu City, PH")
        st.write("🕒 **Availability:** Q1 2026")
        st.write("📡 **Socials:** [LinkedIn](#) | [GitHub](#)")
        st.markdown("</div>", unsafe_allow_html=True)

# --- SIGN OFF ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569; font-size: 0.8rem;'>© 2026 MARK LORENZ | ZENITH SHADCN EDITION | NO DATA CENTERS WERE HARMED</p>", unsafe_allow_html=True)
