# Mosaic Fellowship Builder Challenge (2027 Batch)
## Part 1: Customer Research, Problem Definition & AI Solution Architecture

**Candidate:** Yash Sidana  
**Selected Brand:** Man Matters (Mosaic Wellness)  
**Part 2 Live Web Application:** [https://mancare-ai-lvn5appppksyf9psquwoavta.streamlit.app/](https://mancare-ai-lvn5appppksyf9psquwoavta.streamlit.app/)  

---

### Introduction & Context
To understand how men experience digital health journeys, I spoke with five real customers of **Man Matters**. All five use active products (Minoxidil, Finasteride, Salicylic Acid, Derma Rollers, Shilajit) that require 90 to 180 days of disciplined use to show physical results. 

Through these calls, I uncovered a consistent breakdown: customers love the products and ordering experience, but they hit acute anxiety and confusion during the first 30–60 days when adjustment symptoms (like shedding or purging) or layering doubts arise. To solve this, I built **ManCare AI**—an AI companion grounded in official Man Matters clinical data to support users 24/7.

---

### 1. Customer Conversations

#### Customer 1: Nikhil Sidana (Age 25, Software Engineer)
* **Phone:** `+91 7009104485`
* **Products Used:** Minoxidil 5% Solution, DHT Blocker Shampoo, Biotin Gummies (6 weeks).
* **What He Likes:** Fast delivery, clean dropper bottle, gummies taste good and are easy to stick to daily.
* **What He Does Not Like:** Around Week 3, his hair started shedding rapidly in the shower ("dread shedding"). Terrified that Minoxidil was making him bald, he checked the site, but the FAQ only had a generic one-liner. The WhatsApp support bot only offered shipping tracking. Panicked, he stopped applying the solution for 4 days.
* **What More He Wants Us To Do:** Proactive day-by-day guidance. Someone or something available at 11 PM to explain what shedding actually means so users don't panic-quit.
* **How Our AI Solution (ManCare AI) Solves This:** ManCare’s RAG Assistant is indexed directly on Man Matters clinical monographs. It explains the biological telogen-to-anagen shedding cycle in simple terms 24/7, reassuring Nikhil so he stays on treatment without pausing.

---

#### Customer 2: Gaurang Mangla (Age 21, Student)
* **Phone:** `+91 7011270849`
* **Products Used:** 0.5mm Titanium Derma Roller, Beard Growth Oil (Redensyl + Procapil) (2 months).
* **What He Likes:** Solid roller construction; started noticing light beard fuzz along his jawline by Week 5.
* **What He Does Not Like:** Applied the beard oil *immediately* after rolling into open micro-punctures, thinking it would absorb better. His skin broke out in severe burning redness and small pustules. The tiny box pamphlet didn't make the mandatory 24-hour waiting rule clear.
* **What More He Wants Us To Do:** Clear safety rules on what can and cannot be combined, and automated warnings before someone hurts their skin.
* **How Our AI Solution (ManCare AI) Solves This:** ManCare’s Compatibility Engine checks product combinations, automatically locks active serums on derma-rolling days, and enforces a strict 24-hour skin recovery window with reminders to sanitize the needles.

---

#### Customer 3: Sarthak (Age 22, Student)
* **Phone:** `+91 9313180804`
* **Products Used:** 2% Salicylic Acid Face Wash, 10% Niacinamide Serum, Oil-Free Gel Moisturizer (3 months).
* **What He Likes:** Noticeably controlled his oily skin during long college hours; moisturizer is lightweight and non-sticky.
* **What He Does Not Like:** Wanted to add Vitamin C or Retinol but felt completely lost with percentages and chemical compatibility. He also skipped sunscreen while using active acids and developed sunburn patches on his nose and cheeks.
* **What More He Wants Us To Do:** A clear schedule that says: "Apply Product A in the morning, Product B at night, and always use sunscreen."
* **How Our AI Solution (ManCare AI) Solves This:** ManCare audits multi-product carts, catches chemical clashes, separates actives into safe AM/PM slots, and automatically mandates SPF 50 whenever exfoliants are active.

---

#### Customer 4: Ritish Gupta (Age 21, Student)
* **Phone:** `+91 7740092977`
* **Products Used:** Topical Minoxidil + Finasteride 0.1%, Ketoconazole 2% Anti-Dandruff Shampoo (4 months; paused).
* **What He Likes:** Genuine visible regrowth by Month 3—crown filled out and hairline stabilized.
* **What He Does Not Like:** In Month 3.5, he developed itchy scalp flaking. Panicked that he was allergic to Finasteride, he tried to book an app doctor. The nearest slot was 48 hours away. He quit using the solution out of anxiety for 4 weeks, wiping out months of progress.
* **What More He Wants Us To Do:** Instant medical triage to differentiate mild carrier dryness from dangerous allergic reactions so users don't abandon working treatments while waiting days for an appointment.
* **How Our AI Solution (ManCare AI) Solves This:** ManCare provides instant triage—differentiating normal alcohol-carrier flaking from genuine contact dermatitis, offering immediate soothing steps, and immediately routing red-flag cases to a physician.

---

#### Customer 5: Rishi (Age 21, Student)
* **Phone:** `+91 7988263407`
* **Products Used:** Pure Himalayan Shilajit Resin, Ashwagandha 500mg, Daily Multivitamins (5 months).
* **What He Likes:** Noticeable energy and stamina boost for gym sessions; appreciates the authentic lab test certificates.
* **What He Does Not Like:** Unclear about timing (AM with warm milk vs PM; mixing with Ashwagandha). Because wellness supplements act gradually, he routinely forgot to take them for 4 to 5 days at a stretch.
* **What More He Wants Us To Do:** Daily routine reminders and visual streak tracking to build a consistent habit over 90+ days.
* **How Our AI Solution (ManCare AI) Solves This:** ManCare’s 7-Day Routine Orchestrator creates tailored AM/PM schedules, tracks daily streaks, and sends milestone encouragements to keep users compliant through the full 90-day cycle.

---

### 2. Summary of What I Learned & What We Recommend We Improve

* **What I Learned:**
  1. **Results are real, but early adherence is fragile:** When customers stick to the treatment, products work. But because visible outcomes take 90–180 days, the first 30–60 days are when over 70% of drop-offs occur.
  2. **Adjustment panic causes abandonment:** Normal physiological transitions (Minoxidil shedding, acid purging, carrier flaking) are routinely mistaken for product failure or harmful side effects.
  3. **The support gap is temporal:** When anxiety hits at 11 PM, static FAQs fail to answer specific concerns, WhatsApp bots only handle delivery logistics, and doctor appointments take 24–48 hours.

* **What We Recommend We Improve:**
  Man Matters must evolve from a purely transactional e-commerce platform into an **active clinical adherence partner**. We must equip customers with:
  1. Instant, 24/7 conversational answers backed by clinical documentation to defuse symptom anxiety.
  2. Automated ingredient safety audits to prevent hazardous misapplications (e.g., derma rolling followed immediately by concentrated serums).
  3. Structured AM/PM daily routines with habit streaks to keep users accountable across the full 90-day horizon.

---

### 3. The Problem Statement & Root Cause

> #### **The Final Problem Statement:**
> **"Men purchasing active-ingredient treatments from Man Matters experience severe routine confusion and symptom anxiety during their first 30 to 60 days. Because existing support channels rely on static FAQs or delayed doctor consults, customers lack immediate, clinically accurate guidance for daily application, ingredient layering, and normal adjustment symptoms (such as dread shedding or skin purging). This guidance void leads to application errors, anxiety-driven treatment pauses, and high early regimen abandonment."**

* **System Root Cause:**
  The current D2C model is optimized to acquire customers and ship packages. However, clinical wellness requires **90 to 180 days of continuous daily compliance**. The post-purchase experience currently leaves customers on their own right when doubts, physical adjustment phases, and misapplications peak.

---

### 4. The AI Solution Built for Part 2: ManCare AI

To directly solve the pain points identified across all five customer conversations, I designed, built, and deployed **ManCare AI** ([Live Web Application](https://mancare-ai-lvn5appppksyf9psquwoavta.streamlit.app/)).

#### Core Modules & How They Directly Solve Customer Pain:

1. **24/7 Grounded Clinical RAG Assistant:**
   * Powered by vector and TF-IDF retrieval across 32 official Man Matters clinical dossiers and medical FAQs.
   * Gives instant, source-cited explanations for shedding phases, proper application techniques, and realistic timelines at any hour of the day. Directly addresses Nikhil and Ritish's panic.
2. **Active Ingredient Compatibility Engine:**
   * Pharmacological rule engine that audits any product combination.
   * Automatically detects hazardous clashes (e.g., Titanium Derma Roller + Beard Growth Oil), warns against ingredient over-concentration, and mandates mineral SPF 50 whenever active exfoliants (Salicylic Acid) are present. Directly addresses Gaurang and Sarthak's mistakes.
3. **Adaptive 7-Day Routine Orchestrator & Streak Tracker:**
   * Automatically splits routines into morning and nighttime steps, schedules mandatory rest days post-rolling, and tracks adherence streaks. Directly addresses Rishi's skipped doses.
4. **Deterministic Red-Flag Medical Triage:**
   * Evaluates reported symptoms for emergency markers (chest pain, severe contact dermatitis, facial swelling). Safely reassures mild symptoms while immediately routing clinical red flags to human doctors.

---

### 5. Part 2 Live Application
* **Live Web App Link:** [https://mancare-ai-lvn5appppksyf9psquwoavta.streamlit.app/](https://mancare-ai-lvn5appppksyf9psquwoavta.streamlit.app/)
* **Authentic Catalog:** 15 verified Man Matters products across Hair, Beard, Skin, and Nutrition with official pricing, ingredients, and URLs.
* **Full Working Suite:** RAG Clinical Q&A, Active Compatibility Auditor, 7-Day Smart Scheduler, Red-Flag Triage, and Direct Doctor Escalation.
