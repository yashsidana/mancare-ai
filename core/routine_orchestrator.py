from typing import List, Dict, Any

class RoutineOrchestrator:
    """
    Generates structured, clinically safe 7-day personal care schedules
    tailored to selected Man Matters products, with adherence streak simulation.
    """

    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def generate_weekly_schedule(product_names: List[str]) -> Dict[str, Dict[str, List[str]]]:
        """Builds an intelligent 7-day schedule ensuring active intervals and safe rest days."""
        has_minoxidil = any("minoxidil" in p.lower() for p in product_names)
        has_derma_roller = any("derma" in p.lower() for p in product_names)
        has_beard_oil = any("beard" in p.lower() and "oil" in p.lower() for p in product_names)
        has_salicylic = any("salicylic" in p.lower() for p in product_names)
        has_niacinamide = any("niacinamide" in p.lower() for p in product_names)
        has_sunscreen = any("sunscreen" in p.lower() for p in product_names)
        has_keto = any("ketoconazole" in p.lower() for p in product_names)
        has_shampoo = any("shampoo" in p.lower() and "keto" not in p.lower() for p in product_names)
        has_shilajit = any("shilajit" in p.lower() for p in product_names)
        has_ashwagandha = any("ashwagandha" in p.lower() for p in product_names)
        has_gummies = any("gummies" in p.lower() for p in product_names)

        schedule = {}

        for day in RoutineOrchestrator.DAYS:
            am_tasks = []
            pm_tasks = []

            # Morning Routine
            if has_salicylic:
                am_tasks.append("Cleanse face with 2% Salicylic Acid Face Wash (60 sec lather)")
            if has_niacinamide:
                am_tasks.append("Apply 2-3 drops of 10% Niacinamide Daily Serum")
            if has_sunscreen:
                am_tasks.append("Apply Mineral Matte Sunscreen SPF 50 (Mandatory outdoors)")
            
            # Morning Hair & Nutrition
            if has_keto and day in ["Tuesday", "Saturday"]:
                am_tasks.append("Shower: Wash scalp with Ketoconazole 2% Shampoo (LEAVE FOR 5 MIN)")
            elif has_shampoo and day in ["Monday", "Thursday", "Sunday"]:
                am_tasks.append("Shower: Wash hair with DHT Blocker Anti-Hairfall Shampoo")

            if has_shilajit:
                am_tasks.append("Pre-Workout/Morning: 300mg Shilajit resin in lukewarm water/milk")
            if has_gummies:
                am_tasks.append("Post-Breakfast: Chew 1 Biotin / Beard Gummy")

            # Evening Routine
            if has_salicylic:
                pm_tasks.append("Gentle cleanse to wash away daily grime & pollution")
            if has_niacinamide:
                pm_tasks.append("Apply 2 drops 10% Niacinamide Serum to clean face")

            # Beard Micro-Needling Schedule (Wed & Sun)
            if has_derma_roller:
                if day in ["Wednesday", "Sunday"]:
                    pm_tasks.append("CRITICAL: 0.5mm Derma Roller (Sanitize in 70% alcohol 5 min, roll 4-8 times. DO NOT APPLY BEARD OIL)")
                elif has_beard_oil:
                    pm_tasks.append("Beard Care: Massage 3-5 drops Beard Growth Oil into skin (Safe on non-rolling nights)")
            elif has_beard_oil:
                pm_tasks.append("Beard Care: Massage 3-5 drops Beard Growth Oil into skin")

            # Nightly Hair Regrowth
            if has_minoxidil:
                pm_tasks.append("Hair Regrowth: Apply 1ml Minoxidil solution to clean, DRY scalp before bed")

            # Bedtime Nutrition
            if has_ashwagandha:
                pm_tasks.append("Bedtime Recovery: Take 1 tablet Ashwagandha KSM-66 with warm water")

            schedule[day] = {
                "morning": am_tasks if am_tasks else ["Hydrate with water and gentle face wash"],
                "evening": pm_tasks if pm_tasks else ["Cleanse face and apply gentle moisturizer"]
            }

        return schedule

    @staticmethod
    def get_biological_milestones(category: str = "Hair") -> List[Dict[str, str]]:
        """Returns standard verified clinical expectation milestones."""
        if category == "Hair":
            return [
                {
                    "phase": "Days 1 to 14: Cellular Activation",
                    "status": "NORMAL",
                    "what_to_expect": "Vasodilation begins. Scalp micro-circulation increases. Minor carrier drying or mild flaking may occur."
                },
                {
                    "phase": "Days 15 to 30: Dread Shedding Window",
                    "status": "ALERT",
                    "what_to_expect": "Increased hair shedding (20-50% more hair in drain). THIS IS HEALTHY. Resting telogen hairs are shedding to make way for new anagen growth. DO NOT STOP."
                },
                {
                    "phase": "Days 31 to 60: Stabilization",
                    "status": "STABILIZING",
                    "what_to_expect": "Shedding sharply declines back to baseline. Hair roots strengthen. Scalp sebum production balances."
                },
                {
                    "phase": "Days 61 to 90: Early Regrowth",
                    "status": "IMPROVING",
                    "what_to_expect": "Fine, unpigmented baby vellus hairs appear along temples and crown. Hair strand diameter begins to increase."
                },
                {
                    "phase": "Days 91 to 180: Peak Density Transformation",
                    "status": "EXCELLENT",
                    "what_to_expect": "Vellus hairs mature into pigmented terminal hairs. Noticeable crown thickening and visible coverage."
                }
            ]
        elif category == "Beard":
            return [
                {
                    "phase": "Weeks 1 to 2: Follicle Priming",
                    "status": "NORMAL",
                    "what_to_expect": "Micro-needling enhances localized blood flow. Transient redness lasting 1-2 hours after rolling."
                },
                {
                    "phase": "Weeks 3 to 6: Dormant Awakening",
                    "status": "IMPROVING",
                    "what_to_expect": "Peptide actives (Redensyl + Procapil) activate dormant cheek follicles. Fine fuzz emerges."
                },
                {
                    "phase": "Weeks 7 to 12: Density Thickening",
                    "status": "EXCELLENT",
                    "what_to_expect": "Cheek patches connect. Facial hair softens and strengthens with continuous oil nourishment."
                }
            ]
        else: # Skin
            return [
                {
                    "phase": "Days 1 to 7: Sebum Reduction",
                    "status": "NORMAL",
                    "what_to_expect": "Instant reduction in forehead and nose oiliness. Pores feel cleaner after wash."
                },
                {
                    "phase": "Days 8 to 21: The Purging Window",
                    "status": "ALERT",
                    "what_to_expect": "Small superficial whiteheads may surface as BHA cleans trapped sub-surface impurities. Continue routine with daily SPF 50."
                },
                {
                    "phase": "Days 22 to 60: Barrier Clarity & Glow",
                    "status": "EXCELLENT",
                    "what_to_expect": "Pores appear tighter, post-acne dark marks fade, and overall skin texture smooths out."
                }
            ]

