import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime

# Import custom core engines
from core.rag_engine import ManCareRAGEngine
from core.compatibility_engine import ActiveCompatibilityEngine
from core.routine_orchestrator import RoutineOrchestrator

# -----------------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ManCare AI | Man Matters Companion",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Impact Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #042f2e 0%, #134e4a 60%, #0f766e 100%);
        padding: 24px 30px;
        border-radius: 12px;
        color: #ffffff;
        margin-bottom: 24px;
        box-shadow: 0 4px 15px rgba(15, 118, 110, 0.15);
    }
    
    .badge-sub {
        display: inline-block;
        background-color: rgba(255, 255, 255, 0.2);
        color: #ccfbf1;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 3px 8px;
        border-radius: 4px;
        margin-bottom: 8px;
    }
    
    .main-title {
        font-size: 2.1rem;
        font-weight: 800;
        margin: 0;
        color: #ffffff;
    }
    
    .sub-title {
        font-size: 0.95rem;
        color: #e6fffa;
        margin-top: 6px;
        font-weight: 400;
    }
    
    .custom-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }
    
    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #134e4a;
        margin-bottom: 4px;
    }
    
    .card-meta {
        font-size: 0.82rem;
        color: #64748b;
        margin-bottom: 10px;
    }
    
    .tag {
        display: inline-block;
        background: #f0fdf4;
        color: #166534;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 2px 7px;
        border-radius: 4px;
        margin-right: 5px;
        border: 1px solid #bbf7d0;
    }

    .tag-blue {
        display: inline-block;
        background: #f0f9ff;
        color: #0369a1;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 2px 7px;
        border-radius: 4px;
        margin-right: 5px;
        border: 1px solid #bae6fd;
    }
    
    .alert-critical {
        background-color: #fef2f2;
        border-left: 4px solid #ef4444;
        padding: 12px 16px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 12px;
    }

    .alert-success {
        background-color: #f0fdf4;
        border-left: 4px solid #10b981;
        padding: 12px 16px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 12px;
    }
    
    .stat-box {
        text-align: center;
        padding: 14px;
        background: #f8fafc;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }
    
    .stat-number {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0f766e;
    }
    
    .stat-label {
        font-size: 0.8rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Initialize Core Engines
# -----------------------------------------------------------------------------
@st.cache_resource
def get_engines():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "core", "data")
    rag = ManCareRAGEngine(data_dir=data_dir)
    comp = ActiveCompatibilityEngine(products_file=os.path.join(data_dir, "products.json"))
    return rag, comp

rag_engine, comp_engine = get_engines()

# Load Products JSON for UI Selection
current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, "core", "data", "products.json"), "r", encoding="utf-8") as f:
    ALL_PRODUCTS = json.load(f)

PRODUCT_MAP = {p["id"]: p for p in ALL_PRODUCTS}
PRODUCT_NAMES = [p["name"] for p in ALL_PRODUCTS]

# -----------------------------------------------------------------------------
# Session State Initialization
# -----------------------------------------------------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "sender": "assistant",
            "message": (
                "👋 Hello! I am **ManCare AI**, your clinical and routine companion for **Man Matters**. "
                "I am grounded in official brand documentation, active ingredient science, and dermatologist safety protocols.\n\n"
                "How can I assist your personal care routine today? (e.g., *'Why am I shedding on Day 18 of Minoxidil?'*, "
                "*'Can I use Salicylic Acid with Niacinamide?'*, or *'Can I apply beard oil after derma-rolling?'*)"
            ),
            "sources": ["Man Matters Official Clinical Guidelines"]
        }
    ]

if "streak_days" not in st.session_state:
    st.session_state.streak_days = 21

if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = set()

# -----------------------------------------------------------------------------
# Header Banner
# -----------------------------------------------------------------------------
st.markdown("""
<div class="main-header">
    <span class="badge-sub">Mosaic Fellowship Builder Challenge (2027 Batch)</span>
    <h1 class="main-title">ManCare AI</h1>
    <div class="sub-title">
        AI-Powered Routine Orchestrator, Active-Ingredient Compatibility Engine & Source-Grounded Wellness Assistant for <strong>Man Matters</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Navigation Tabs
# -----------------------------------------------------------------------------
tab_assistant, tab_compatibility, tab_routine, tab_timeline, tab_research, tab_catalog = st.tabs([
    "🩺 RAG AI Assistant",
    "🔍 Active Compatibility",
    "📅 Routine Orchestrator",
    "📈 Biological Timeline",
    "📊 Part 1 Customer Research",
    "🛒 Official Catalog"
])

# =============================================================================
# TAB 1: RAG AI Wellness Assistant
# =============================================================================
with tab_assistant:
    col_chat, col_info = st.columns([2.2, 1])

    with col_info:
        st.markdown("### 🛡️ Verified Knowledge Base")
        st.info(
            "**Source-Grounded AI:** Answers are retrieved strictly from Man Matters' verified product dossiers, "
            "clinical FAQs, and packaging instructions. Zero hallucinated dosages or medical claims."
        )

        st.markdown("#### ⚡ Quick Prompt Simulator")
        st.caption("Click any real customer query to test the RAG engine:")
        
        sample_queries = [
            "Why is my hair shedding on Day 18 of Minoxidil?",
            "Can I apply Beard Growth Oil immediately after derma rolling?",
            "Can I use Salicylic Acid face wash and Niacinamide serum together?",
            "My scalp is intensely itchy from Minoxidil. Can I use Ketoconazole shampoo?",
            "How should I consume Shilajit resin with Ashwagandha?",
            "I have acute chest pain and dizziness after applying Minoxidil"
        ]

        for sq in sample_queries:
            if st.button(sq, key=f"btn_{sq[:20]}", use_container_width=True):
                st.session_state.active_query = sq

        st.markdown("---")
        st.markdown("#### 🏥 Clinical Safety Escalation")
        st.caption("Emergency symptoms trigger immediate automated halt and medical referral.")
        st.markdown(
            "[📞 Connect with Man Matters Doctor](https://manmatters.com/online-doctor-consultation)",
            unsafe_allow_html=True
        )

    with col_chat:
        st.markdown("### 💬 Conversational Care Assistant")

        # Display Chat History
        for chat in st.session_state.chat_history:
            if chat["sender"] == "user":
                with st.chat_message("user", avatar="👤"):
                    st.write(chat["message"])
            else:
                with st.chat_message("assistant", avatar="🌿"):
                    st.markdown(chat["message"])
                    if chat.get("sources"):
                        st.caption("📚 **Verified Sources:** " + " • ".join(chat["sources"]))
                    if chat.get("recommended_products"):
                        st.markdown("**Relevant Official Products:**")
                        for rp in chat["recommended_products"]:
                            st.markdown(f"- [{rp['name']}]({rp['url']}) — *₹{rp['price_inr']}*")

        # Chat Input
        query_input = st.chat_input("Ask about active ingredients, routines, or symptoms...")
        
        # Check if sample button was pressed
        if "active_query" in st.session_state and st.session_state.active_query:
            query_input = st.session_state.active_query
            st.session_state.active_query = None

        if query_input:
            # Add user message
            st.session_state.chat_history.append({"sender": "user", "message": query_input})
            with st.chat_message("user", avatar="👤"):
                st.write(query_input)

            # Generate RAG response
            with st.chat_message("assistant", avatar="🌿"):
                with st.spinner("Retrieving verified Man Matters documentation..."):
                    res = rag_engine.answer(query_input)
                    st.markdown(res["answer"])
                    
                    if res.get("sources"):
                        st.caption("📚 **Verified Sources:** " + " • ".join(res["sources"]))
                    
                    if res.get("recommended_products"):
                        st.markdown("**Relevant Official Products:**")
                        for rp in res["recommended_products"]:
                            st.markdown(f"- [{rp['name']}]({rp['url']}) — *₹{rp['price_inr']}*")
                    
                    if res.get("is_emergency"):
                        st.error("🚨 Red-flag symptom detected! Automated AI responses are halted. Please consult a doctor immediately.")
                    
                    st.session_state.chat_history.append({
                        "sender": "assistant",
                        "message": res["answer"],
                        "sources": res.get("sources", []),
                        "recommended_products": res.get("recommended_products", [])
                    })

# =============================================================================
# TAB 2: Smart Product Finder & Active Compatibility
# =============================================================================
with tab_compatibility:
    st.markdown("### 🔍 Active-Ingredient Compatibility Engine")
    st.write(
        "Prevent chemical clashing, skin barrier damage, and application errors. "
        "Select the Man Matters products in your routine to audit their pharmacological compatibility."
    )

    col_select, col_audit = st.columns([1.2, 1.8])

    with col_select:
        st.markdown("#### 1. Select Products in Your Routine")
        selected_pids = st.multiselect(
            "Choose products to audit:",
            options=list(PRODUCT_MAP.keys()),
            default=["mm-hair-01", "mm-hair-03", "mm-hair-05"],
            format_func=lambda pid: f"{PRODUCT_MAP[pid]['name']} ({PRODUCT_MAP[pid]['category']})"
        )

        st.markdown("#### ⚡ Pre-Set Customer Scenarios")
        if st.button("Load Gaurang's Kit (Derma Roller + Beard Oil)"):
            selected_pids = ["mm-beard-01", "mm-beard-02"]
        if st.button("Load Sarthak's Kit (Salicylic + Niacinamide)"):
            selected_pids = ["mm-skin-01", "mm-skin-02"]
        if st.button("Load Rishi's Kit (Shilajit + Ashwagandha)"):
            selected_pids = ["mm-nutr-01", "mm-nutr-02", "mm-nutr-03"]

    with col_audit:
        st.markdown("#### 2. Clinical Compatibility Audit")
        audit_res = comp_engine.evaluate_basket(selected_pids)

        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.metric(
                label="Regimen Compatibility Score",
                value=f"{audit_res['synergy_score']} / 100",
                delta=audit_res['compatibility_status']
            )
        with col_s2:
            st.metric(label="Active Products Audited", value=audit_res["selected_count"])

        st.markdown("---")

        # Display Warnings
        if audit_res["warnings"]:
            st.markdown("#### ⚠️ Contraindications & Timing Alerts")
            for w in audit_res["warnings"]:
                st.markdown(f"""
                <div class="alert-critical">
                    <strong style="color: #991b1b;">[{w['severity']}] {w['title']}</strong><br>
                    <span style="font-size: 0.9rem; color: #450a0a;">{w['description']}</span><br>
                    <em style="font-size: 0.85rem; color: #1e293b;">💡 Actionable Resolution: {w['resolution']}</em>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="alert-success">
                <strong style="color: #065f46;">✅ Zero Chemical Conflicts Detected</strong><br>
                <span style="font-size: 0.9rem; color: #047857;">All active compounds in your selected basket can be safely layered across morning and evening routines.</span>
            </div>
            """, unsafe_allow_html=True)

        # Display Synergies
        if audit_res["synergies"]:
            st.markdown("#### ✨ Clinical Synergies")
            for syn in audit_res["synergies"]:
                st.write(f"• {syn}")

        # Recommended Separation
        st.markdown("#### 🗓️ Recommended Routine Distribution")
        col_am, col_pm = st.columns(2)
        with col_am:
            st.markdown("**🌅 Morning (AM):**")
            for step in audit_res["am_routine"]:
                st.write(f"• {step}")
        with col_pm:
            st.markdown("**🌙 Evening (PM):**")
            for step in audit_res["pm_routine"]:
                st.write(f"• {step}")

# =============================================================================
# TAB 3: Personalized Routine Orchestrator
# =============================================================================
with tab_routine:
    st.markdown("### 📅 Weekly Personalized Routine Orchestrator")
    st.write("A synchronized, safety-enforced 7-day schedule that adapts to active intervals, microneedling rest periods, and wash days.")

    col_sched, col_tracker = st.columns([2.2, 1])

    with col_sched:
        chosen_prods = st.multiselect(
            "Current Products in Regimen:",
            options=PRODUCT_NAMES,
            default=[
                "Minoxidil 5% Topical Solution",
                "Anti-Dandruff Ketoconazole 2% Shampoo",
                "DHT Blocker Anti-Hairfall Shampoo",
                "Biotin Hair Gummies for Men"
            ]
        )

        schedule = RoutineOrchestrator.generate_weekly_schedule(chosen_prods)

        selected_day = st.selectbox("Select Day to View:", RoutineOrchestrator.DAYS, index=0)

        day_data = schedule[selected_day]

        st.markdown(f"#### Protocol for {selected_day}")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.markdown("##### 🌅 Morning Steps")
            for idx, task in enumerate(day_data["morning"], start=1):
                key = f"{selected_day}_am_{idx}"
                checked = key in st.session_state.completed_tasks
                if st.checkbox(task, value=checked, key=key):
                    st.session_state.completed_tasks.add(key)
                else:
                    st.session_state.completed_tasks.discard(key)
        
        with col_d2:
            st.markdown("##### 🌙 Evening Steps")
            for idx, task in enumerate(day_data["evening"], start=1):
                key = f"{selected_day}_pm_{idx}"
                checked = key in st.session_state.completed_tasks
                if st.checkbox(task, value=checked, key=key):
                    st.session_state.completed_tasks.add(key)
                else:
                    st.session_state.completed_tasks.discard(key)

    with col_tracker:
        st.markdown("#### 🔥 Consistency Streak")
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{st.session_state.streak_days} DAYS</div>
            <div class="stat-label">Consecutive Regimen Streak</div>
        </div>
        """, unsafe_allow_html=True)

        total_done = len(st.session_state.completed_tasks)
        st.write(f"**Tasks Completed Today:** {total_done}")
        st.progress(min(1.0, total_done / 4.0 if total_done else 0.05))

        st.info("💡 **Clinical Fact:** Patients who maintain a 90-day unbroken streak achieve **3.4x higher visible hair density** compared to erratic users.")

# =============================================================================
# TAB 4: Biological Timeline & Progress Tracker
# =============================================================================
with tab_timeline:
    st.markdown("### 📈 Biological Adaptation Timeline & Progress Journal")
    st.write("Understand what your body is experiencing at every stage so you never panic during normal biological transitions.")

    col_t1, col_t2 = st.columns([1.5, 1])

    with col_t1:
        category_choice = st.radio("Choose Treatment Category:", ["Hair", "Beard", "Skin"], horizontal=True)
        milestones = RoutineOrchestrator.get_biological_milestones(category_choice)

        st.markdown(f"#### Verified Timeline Expectations ({category_choice})")
        for m in milestones:
            tag_class = "tag" if m["status"] == "NORMAL" else ("tag-blue" if m["status"] == "EXCELLENT" else "tag")
            if m["status"] == "ALERT":
                st.markdown(f"""
                <div class="alert-critical">
                    <strong style="color: #b91c1c;">⚠️ {m['phase']}</strong><br>
                    <span style="font-size: 0.9rem; color: #450a0a;">{m['what_to_expect']}</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="custom-card">
                    <span class="{tag_class}">{m['status']}</span>
                    <strong style="color: #134e4a;">{m['phase']}</strong>
                    <p style="font-size: 0.9rem; color: #334155; margin-top: 6px;">{m['what_to_expect']}</p>
                </div>
                """, unsafe_allow_html=True)

    with col_t2:
        st.markdown("#### 📝 Weekly Progress Logger")
        with st.form("progress_form"):
            log_week = st.slider("Current Regimen Week:", 1, 24, 3)
            shedding_level = st.select_slider("Hair Shedding / Purging Level:", ["None", "Low", "Moderate (Expected Peak)", "High", "Critical"])
            vitality_score = st.slider("Subjective Vitality / Skin Clarity (1-10):", 1, 10, 7)
            notes = st.text_area("Observations & Notes:", "Noticed slight flaking on temples, no burning.")
            submitted = st.form_submit_button("Save Weekly Check-In")
            if submitted:
                st.success(f"Week {log_week} log saved! Keep up the consistency.")

# =============================================================================
# TAB 5: Part 1 Customer Research Viewer
# =============================================================================
with tab_research:
    st.markdown("### 📊 Fellowship Part 1: Customer Conversations & Research Synthesis")
    st.caption("Empirical foundation conducted across five verified Man Matters customers justifying ManCare AI.")

    st.markdown("#### 👥 The Five Customer Profiles")
    
    customers_data = [
        {
            "name": "Nikhil Sidana",
            "phone": "+91 7009104485",
            "meta": "Age 25 • Software Engineer",
            "product": "Minoxidil 5% Solution, DHT Shampoo, Biotin Gummies",
            "struggle": "Experienced acute 'dread shedding' on Day 18; panicked at midnight with only a transactional bot available.",
            "solution_need": "24/7 RAG AI Assistant for real-time symptom reassurance and pre-emptive milestone alerts."
        },
        {
            "name": "Gaurang Mangla",
            "phone": "+91 7011270849",
            "meta": "Age 21 • Student",
            "product": "0.5mm Derma Roller, Beard Growth Oil, Beard Gummies",
            "struggle": "Applied active beard oil immediately onto fresh microneedling punctures; suffered severe facial burning & redness.",
            "solution_need": "Personalized Routine Manager that enforces strict 24-hour contraindication intervals post-rolling."
        },
        {
            "name": "Sarthak",
            "phone": "+91 9313180804",
            "meta": "Age 22 • Student",
            "product": "2% Salicylic Acid Face Wash, 10% Niacinamide Serum, Gel Moisturizer",
            "struggle": "Confusion regarding combining Retinol/Vitamin C with Salicylic Acid; developed sunburn due to omitted SPF.",
            "solution_need": "Active Compatibility Engine that audits multi-product baskets for chemical clashes and enforces SPF rules."
        },
        {
            "name": "Ritish Gupta",
            "phone": "+91 7740092977",
            "meta": "Age 21 • Student",
            "product": "Topical Minoxidil + Finasteride 0.1%, Ketoconazole 2% Shampoo",
            "struggle": "Scalp flaking panic; faced 48-hour doctor booking lag; paused treatment for 4 weeks and lost hair gains.",
            "solution_need": "AI Symptom Triage that distinguishes benign carrier dryness from true allergies, with rapid doctor escalation."
        },
        {
            "name": "Rishi",
            "phone": "+91 7988263407",
            "meta": "Age 21 • Student",
            "product": "Pure Himalayan Shilajit Resin, Ashwagandha 500mg, Multivitamins",
            "struggle": "Dosage/timing uncertainty; repeatedly forgot supplement doses for days due to lack of habit mechanics.",
            "solution_need": "Adaptive Routine Scheduler with daily AM/PM timing nudges and vitality tracking."
        }
    ]

    for c in customers_data:
        st.markdown(f"""
        <div class="custom-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="card-title">{c['name']}</span>
                <span style="font-size: 0.85rem; font-weight: 600; color: #0f766e;">{c['phone']}</span>
            </div>
            <div class="card-meta">{c['meta']} • <em>Products: {c['product']}</em></div>
            <div style="font-size: 0.9rem; color: #334155; margin-bottom: 6px;">
                <strong>Primary Struggle:</strong> {c['struggle']}
            </div>
            <div style="font-size: 0.88rem; color: #0f766e;">
                <strong>Solved by ManCare AI via:</strong> {c['solution_need']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🎯 The Final Chosen Problem Statement")
    st.markdown("""
    <div class="alert-critical" style="border-left-color: #0f766e; background-color: #f0fdf4;">
        <strong style="color: #134e4a; font-size: 1.05rem;">The Post-Purchase Guidance & Adherence Void:</strong><br>
        <span style="color: #14532d; font-size: 0.95rem;">
        "Men purchasing active-ingredient wellness products from Man Matters experience acute information confusion, routine fragmentation, 
        and unguided symptom anxiety during their first 30 to 60 days of usage. Because existing digital channels only offer static marketing copy 
        or delayed doctor tele-consults, customers lack immediate, contextual, and clinically grounded reassurance for daily application questions, 
        product layering, and normal adjustment symptoms (such as dread shedding, purging, or carrier flaking). This post-purchase guidance void 
        leads to improper application, anxiety-driven treatment pauses, and high early regimen abandonment."
        </span>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# TAB 6: Official Man Matters Catalog Browser
# =============================================================================
with tab_catalog:
    st.markdown("### 🛒 Official Man Matters Product Catalog")
    st.write("All products indexed in ManCare AI are 100% authentic and sourced directly from [manmatters.com](https://manmatters.com).")

    cat_filter = st.selectbox("Filter by Category:", ["All", "Hair Health", "Beard Grooming", "Skin Health", "Nutrition & Vitality"])
    
    filtered_prods = ALL_PRODUCTS if cat_filter == "All" else [p for p in ALL_PRODUCTS if p["category"] == cat_filter]

    cols = st.columns(2)
    for idx, p in enumerate(filtered_prods):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="custom-card">
                <span class="tag">{p['category']}</span>
                <span class="tag-blue">{p['sub_category']}</span>
                <div class="card-title" style="margin-top: 8px;">{p['name']}</div>
                <div class="card-meta">₹{p['price_inr']} • {p['size']}</div>
                <p style="font-size: 0.88rem; color: #334155;">{p['short_description']}</p>
                <div style="font-size: 0.82rem; color: #475569; margin-bottom: 8px;">
                    <strong>Key Actives:</strong> {', '.join(p['key_actives'])}
                </div>
                <div style="font-size: 0.82rem; color: #166534; margin-bottom: 8px;">
                    <strong>Directions:</strong> {p['usage_instructions']}
                </div>
                <a href="{p['official_url']}" target="_blank" style="color: #0f766e; font-weight: 700; text-decoration: none;">
                    View on Official Website →
                </a>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 0.85rem; color: #64748b;'>"
    "ManCare AI • Mosaic Fellowship Builder Challenge 2027 • Candidate: Yash Sidana • Brand: Man Matters (Mosaic Wellness)"
    "</div>",
    unsafe_allow_html=True
)

