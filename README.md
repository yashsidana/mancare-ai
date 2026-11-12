# ManCare AI 🌿
### AI-Powered Personalized Men's Care, Active Compatibility & Routine Companion
**Prepared for:** Mosaic Fellowship Builder Challenge (2027 Batch)  
**Selected Brand:** **Man Matters** (Mosaic Wellness)  
**Candidate:** **Yash Sidana**  
**Repository:** [https://github.com/yashsidana/mancare-ai](https://github.com/yashsidana/mancare-ai)  
**Live Application Target:** Streamlit Cloud / Hugging Face Spaces / Local Web

---

## 📌 Executive Summary & Challenge Connection

ManCare AI is an end-to-end, AI-powered digital wellness companion engineered specifically for **Man Matters**, India's leading digital-first men's health and wellness platform. 

In active-ingredient personal care (Minoxidil 5%, Topical Finasteride, Redensyl, Salicylic Acid 2%, Himalayan Shilajit, Ketoconazole 2%), treatment efficacy requires **90 to 180 days of continuous daily compliance**. However, customers experience acute drop-offs during the first 30–45 days due to:
1. **Dread Shedding & Purging Panic:** Misinterpreting normal biological adaptation phases as treatment failure.
2. **Active Ingredient Clashing:** Accidental chemical burns or barrier damage (e.g., applying beard oil onto freshly derma-rolled skin, or skipping sunscreen with Salicylic Acid).
3. **The Post-Purchase Guidance Void:** Transactional delivery bots cannot answer clinical questions, while tele-doctor appointments take 24–48 hours to schedule.

ManCare AI bridges this void by providing **24/7 source-grounded conversational intelligence, chemical compatibility auditing, and synchronized routine orchestration**.

---

## 🚀 Key Features

```
                                  [ MANCARE AI ARCHITECTURE ]
                                               │
             ┌─────────────────────────────────┼─────────────────────────────────┐
             ▼                                 ▼                                 ▼
   [ 🩺 RAG AI Assistant ]        [ 🔍 Compatibility Engine ]       [ 📅 Routine Orchestrator ]
  • Semantic Vector Retrieval    • Multi-Product Basket Audit       • 7-Day Synchronized Schedule
  • Verified Official Citations  • Chemical Clashing Detection      • Safety Interval Enforcement
  • Doctor Escalation Gateway    • AM / PM Safe Separation          • Daily Adherence Streaks
```

### 1. 🩺 RAG-Based AI Wellness Assistant
* **Zero Hallucination Guarantee:** Uses Retrieval-Augmented Generation (RAG) strictly indexed over verified Man Matters product catalogues, official FAQs, and clinical dossiers.
* **Contextual & Empathetic:** Answering situational questions (*"I washed my hair with Ketoconazole shampoo, can I apply Minoxidil now?"* or *"Why am I shedding on Day 18?"*).
* **Clinical Citations:** Every response provides direct source references to official Man Matters documentation and product pages.
* **Deterministic Medical Guardrails:** Emergency symptoms (chest pain, tachycardia, severe allergic swelling) automatically trigger an automated response halt and present immediate doctor escalation pathways.

### 2. 🔍 Active-Ingredient Compatibility Engine
* **Basket Audit:** Select any combination of Man Matters products to audit pharmacological compatibility.
* **Contraindication Detection:** Catches severe errors—such as using physical microneedling (0.5mm Derma Roller) and active oils simultaneously, or using BHAs without photoprotection (SPF 50).
* **Synergy Scoring:** Rates the scientific synergy of the user's regimen (0–100%) and generates safe AM vs. PM application steps.

### 3. 📅 Personalized Routine Orchestrator & Streak Tracker
* **Safety-Aware Scheduling:** Enforces critical rest days (e.g. microneedling on Wednesday/Sunday nights with zero chemical serums for 24 hours).
* **Interactive Checklist:** Daily morning and evening task checkboxes to build sustained habit compliance.
* **Gamified Adherence:** Tracks consecutive streak days to drive 90-day retention.

### 4. 📈 Biological Adaptation Timeline & Progress Journal
* **Pre-Emptive Milestone Education:** Visualizes expected physiological timelines (Days 1-14 Activation, Days 15-30 Dread Shedding Alert, Month 2-3 Stabilization, Month 4-6 Transformation).
* **Weekly Check-In Logger:** Allows users to track shedding levels, skin clarity, and subjective vitality scores over 24 weeks.

### 5. 📊 In-App Fellowship Part 1 Research Viewer
* Complete embedded record of the 5 customer interviews (**Nikhil Sidana**, **Gaurang Mangla**, **Sarthak**, **Ritish Gupta**, **Rishi**), their verbatim feedback, cross-cutting patterns, root causes, and the formal problem statement.

### 6. 🛒 Official Man Matters Catalog Browser
* Direct catalog browser linking to authentic product PDPs on `manmatters.com` with MRP, active ingredients, and directions.

---

## 👥 Customer Validation & Research Mapping (Part 1)

Every feature in ManCare AI was derived directly from five customer interviews:

| Customer Profile | Domain | Verified Pain Point | Solved by ManCare AI |
|---|---|---|---|
| **Nikhil Sidana** (25, Software Eng.)<br>`+91 7009104485` | Hair Regrowth (Minoxidil 5%) | Day 18 dread shedding panic; paused treatment in terror. | **RAG Assistant:** Explains telogen shedding biology with 24/7 reassurance. |
| **Gaurang Mangla** (21, Student)<br>`+91 7011270849` | Beard Grooming (Derma Roller) | Applied beard oil directly onto open needle punctures; severe redness. | **Routine Orchestrator:** Enforces 24-hour rest protocol post-rolling. |
| **Sarthak** (22, Student)<br>`+91 9313180804` | Active Skincare (Salicylic Acid) | Actives clashing confusion; sunburn patches from missing SPF. | **Compatibility Engine:** Audits multi-actives and mandates Mineral SPF 50. |
| **Ritish Gupta** (21, Student)<br>`+91 7740092977` | Clinical Hair (Finasteride) | Scalp flaking panic; 48h doctor delay caused 4-week dropout. | **AI Triage Guardrails:** Real-time symptom triage + doctor escalation. |
| **Rishi** (21, Student)<br>`+91 7988263407` | Ayurvedic Nutrition (Shilajit) | Dosing/timing ambiguity; forgot doses for days. | **Adaptive Scheduler:** Delivers AM/PM timing nudges and vitality logging. |

---

## 📂 Project Structure

```
mancare-ai/
│
├── app.py                         # Main Streamlit Web Application
├── requirements.txt               # Production Python Dependencies
├── README.md                      # Comprehensive Project Documentation
│
├── .streamlit/
│   └── config.toml                # Man Matters Brand Theme & Styling Config
│
├── core/
│   ├── __init__.py
│   ├── rag_engine.py              # Semantic Retrieval & Grounded Q&A Engine
│   ├── compatibility_engine.py    # Active Compatibility & Chemical Clashing Logic
│   ├── routine_orchestrator.py    # 7-Day Schedule Generator & Timeline Logic
│   │
│   └── data/
│       ├── products.json          # Authentic Man Matters Product Catalog (Hair, Beard, Skin, Nutrition)
│       ├── faqs.json              # Verified Official Clinical FAQs & Usage Protocols
│       └── clinical_dossiers.json # Deep Pharmacological Profiles of Key Actives
│
└── docs/
    ├── PART_1_CUSTOMER_CONVERSATIONS_AND_PROBLEM_STATEMENT.md # Part 1 Submission
    └── PART_1_SUBMISSION_MAN_MATTERS.html                     # Word/PDF-Ready Submission
```

---

## 🛠️ Local Setup & Quickstart

### Prerequisites
* Python 3.10 or 3.11 installed.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yashsidana/mancare-ai.git
   cd mancare-ai
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the web application:
   ```bash
   streamlit run app.py
   ```
   The application will automatically open in your default browser at `http://localhost:8501`.

---

## 🌐 1-Click Free Cloud Deployment

### Deploying to Streamlit Community Cloud (Free & Instant):
1. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub (`yashsidana`).
2. Click **New app**.
3. Select this repository: `yashsidana/mancare-ai`.
4. Branch: `main` | Main file path: `app.py`.
5. Click **Deploy!** Your app will be live with a permanent URL like `https://mancare-ai.streamlit.app`.

### Deploying to Hugging Face Spaces:
1. Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces).
2. Space SDK: **Streamlit**.
3. Connect your GitHub repository `yashsidana/mancare-ai` or push code to the Space remote.

---

## 📜 Authentic Brand Alignment Notice
All product names, active concentrations, pricing in INR, usage instructions, and official links in this application are strictly sourced from and attributed to **Man Matters** ([https://manmatters.com](https://manmatters.com)), a brand owned by Mosaic Wellness Pvt. Ltd. This prototype was constructed independently for the **Mosaic Fellowship Builder Challenge (2027 Batch)**.

---
**Candidate:** Yash Sidana  
**Contact:** [GitHub Profile](https://github.com/yashsidana)
