import json
import os
from typing import List, Dict, Any

class ActiveCompatibilityEngine:
    """
    Evaluates multi-product active ingredient regimens for Man Matters customers.
    Detects chemical contraindications, sequence errors, and recommends safe AM/PM distribution.
    """

    def __init__(self, products_file: str = None):
        if products_file is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            products_file = os.path.join(current_dir, "data", "products.json")
        
        self.products_file = products_file
        self.products: Dict[str, Dict[str, Any]] = {}
        self.load_products()

    def load_products(self):
        if os.path.exists(self.products_file):
            with open(self.products_file, "r", encoding="utf-8") as f:
                prods = json.load(f)
                for p in prods:
                    self.products[p["id"]] = p

    def evaluate_basket(self, product_ids: List[str]) -> Dict[str, Any]:
        """Audits a basket of products for compatibility, clashes, and optimal routine placement."""
        selected = [self.products[pid] for pid in product_ids if pid in self.products]
        if not selected:
            return {
                "compatibility_status": "EMPTY",
                "synergy_score": 0,
                "warnings": [],
                "synergies": [],
                "am_routine": [],
                "pm_routine": []
            }

        warnings = []
        synergies = []
        am_routine = []
        pm_routine = []
        base_score = 85

        # Check Derma Roller + Beard Oil
        has_roller = any("derma" in p["id"] for p in selected)
        has_beard_oil = any("beard-02" in p["id"] or "beard oil" in p["name"].lower() for p in selected)

        if has_roller and has_beard_oil:
            warnings.append({
                "severity": "CRITICAL",
                "title": "Severe Timing Conflict: Derma Roller & Beard Growth Oil",
                "description": (
                    "NEVER apply Beard Growth Oil immediately after micro-needling. "
                    "Open micro-punctures absorb active carrier oils aggressively, causing severe erythema, "
                    "burning, and follicular pustules. Wait 24 HOURS before applying beard oil."
                ),
                "resolution": "Roll on Wednesday/Sunday night; apply only gentle hydration. Resume Beard Oil on Thursday/Monday."
            })
            base_score -= 15
        elif has_roller:
            synergies.append("Derma Roller activates collagen channels. Ensure 70% isopropyl alcohol sanitization.")

        # Check Salicylic Acid + Sunscreen
        has_salicylic = any("salicylic" in p["name"].lower() for p in selected)
        has_sunscreen = any("sunscreen" in p["name"].lower() for p in selected)

        if has_salicylic:
            if not has_sunscreen:
                warnings.append({
                    "severity": "HIGH",
                    "title": "Missing Sunscreen Protection with Salicylic Acid",
                    "description": (
                        "Salicylic Acid (BHA) chemically exfoliates dead surface cells, reducing UV tolerance by up to 50%. "
                        "Without daily SPF 50, you risk severe sun tanning, hyperpigmentation, and blotches."
                    ),
                    "resolution": "Add Man Matters Mineral Matte Sunscreen SPF 50 PA++++ to your morning regimen."
                })
                base_score -= 10
            else:
                synergies.append("Excellent protection: Mineral Sunscreen SPF 50 shields skin post-Salicylic Acid exfoliation.")
                base_score += 5

        # Check Salicylic Acid + Niacinamide
        has_niacinamide = any("niacinamide" in p["name"].lower() for p in selected)
        if has_salicylic and has_niacinamide:
            synergies.append(
                "Synergistic Acne Control: Salicylic Acid clears deep pore sebum while Niacinamide calms redness and repairs barrier."
            )
            base_score += 10

        # Check Minoxidil + Ketoconazole Shampoo
        has_minox = any("minoxidil" in p["name"].lower() for p in selected)
        has_keto = any("ketoconazole" in p["name"].lower() for p in selected)

        if has_minox and has_keto:
            synergies.append(
                "Clinically Proven Hair Protocol: Ketoconazole clears Malassezia yeast and DHT on scalp, maximizing Minoxidil absorption."
            )
            warnings.append({
                "severity": "MODERATE",
                "title": "Application Sequence Notice",
                "description": "Never apply topical Minoxidil on damp hair after washing with Ketoconazole shampoo. Allow scalp to dry 100% first.",
                "resolution": "Wash with Ketoconazole 2x/week, wait 20 minutes for bone-dry scalp, then apply 1ml Minoxidil at night."
            })
            base_score += 5

        # Check Shilajit + Ashwagandha
        has_shilajit = any("shilajit" in p["name"].lower() for p in selected)
        has_ashwa = any("ashwagandha" in p["name"].lower() for p in selected)

        if has_shilajit and has_ashwa:
            synergies.append(
                "Classic Ayurvedic Synergy: Shilajit promotes daytime cellular ATP stamina, while Ashwagandha reduces nocturnal cortisol and promotes restorative sleep."
            )
            base_score += 10

        # Build Routine Distribution
        for p in selected:
            cat = p["category"]
            name = p["name"]

            if cat == "Skin Health":
                if "face wash" in name.lower():
                    am_routine.append(f"Step 1: Cleanse with {name} (60s lather)")
                    pm_routine.append(f"Step 1: Cleanse with {name}")
                elif "serum" in name.lower():
                    am_routine.append(f"Step 2: Apply 3 drops of {name}")
                    pm_routine.append(f"Step 2: Apply 3 drops of {name}")
                elif "moisturizer" in name.lower():
                    am_routine.append(f"Step 3: Hydrate with {name}")
                    pm_routine.append(f"Step 3: Hydrate with {name}")
                elif "sunscreen" in name.lower():
                    am_routine.append(f"Step 4: Shield with {name} (2 fingers amount)")
            elif cat == "Hair Health":
                if "shampoo" in name.lower():
                    am_routine.append(f"Shower: Wash hair with {name} (3x weekly)")
                elif "gummies" in name.lower():
                    am_routine.append(f"Oral: Chew 1 {name} post breakfast")
                elif "solution" in name.lower() or "serum" in name.lower():
                    pm_routine.append(f"Targeted Treatment: Apply 1ml {name} to dry scalp before bed")
            elif cat == "Beard Grooming":
                if "roller" in name.lower():
                    pm_routine.append(f"Weekly Physical Tool: {name} (Wed/Sun Night ONLY, 4-8 passes)")
                elif "oil" in name.lower():
                    pm_routine.append(f"Nightly Nourishment: Apply 3-5 drops of {name} (Skip on Derma Rolling nights)")
            elif cat == "Nutrition & Vitality":
                if "shilajit" in name.lower():
                    am_routine.append(f"Morning Vitality: Dissolve pea-sized {name} in warm water/milk")
                elif "multivitamin" in name.lower():
                    am_routine.append(f"Breakfast: Take 1 tablet of {name}")
                elif "ashwagandha" in name.lower():
                    pm_routine.append(f"Bedtime Recovery: Take 1 tablet of {name} with water")

        final_score = max(50, min(100, base_score))
        status = "EXCELLENT" if final_score >= 85 else ("GOOD" if final_score >= 70 else "NEEDS_ADJUSTMENT")

        return {
            "compatibility_status": status,
            "synergy_score": final_score,
            "warnings": warnings,
            "synergies": synergies,
            "am_routine": am_routine,
            "pm_routine": pm_routine,
            "selected_count": len(selected)
        }

