"""
prepare_data.py — transform the scraped Starbucks JSON into the clean dataset the
site is generated from (and the calculator runs on).

Inputs  (data/):
  - nutrition_full.json : real per-(drink x size) macro profiles  [SOURCE OF TRUTH]
  - products.json       : category -> ordered list of group headers + variants
  - customizations.json : option name lists (no nutrition values exist anywhere)

Output:
  - build_dataset()  -> the in-memory dataset used by build.py
  - main()           -> also writes dist/data/nutrition.min.json

The BASE numbers are REAL (scraped). Customization DELTAS were never exposed by the
source endpoint (see docs/starbucks-calculator-ARCHITECTURE.md §4), so we ship a small
*estimated* delta table. Every estimated number is labelled "estimated" in the UI,
consistent with the source site's own disclaimer and BUILD-SPEC.md §9.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# ---------------------------------------------------------------------------
# Category metadata: data label -> (slug, display title, icon, short blurb)
# ---------------------------------------------------------------------------
CATEGORIES = {
    "Hot": {
        "slug": "hot",
        "title": "Hot Drinks",
        "icon": "coffee",
        "blurb": "Lattes, brewed coffees, espresso, hot chocolates and teas — with full "
                 "calorie and macro breakdowns for every cup size.",
    },
    "Cold": {
        "slug": "cold",
        "title": "Cold Drinks",
        "icon": "ac_unit",
        "blurb": "Iced lattes, cold brews, shaken espresso, Refreshers and iced teas. "
                 "See calories, sugar and caffeine before you order.",
    },
    "Frappe": {
        "slug": "frappuccino",
        "title": "Frappuccino®",
        "icon": "icecream",
        "blurb": "Blended Frappuccino® coffee and crème drinks. Calorie and sugar "
                 "counts for Tall, Grande and Venti, plus your customizations.",
    },
    "Food/Meal": {
        "slug": "food",
        "title": "Food & Meals",
        "icon": "lunch_dining",
        "blurb": "Egg bites, sandwiches, wraps and protein boxes — calories, protein and "
                 "macros for every item.",
    },
    "Bakery": {
        "slug": "bakery",
        "title": "Bakery",
        "icon": "bakery_dining",
        "blurb": "Croissants, muffins, loaves, cake pops and cookies, with calories and "
                 "sugar per piece.",
    },
    "Snacks & Sweets": {
        "slug": "snacks",
        "title": "Snacks & Sweets",
        "icon": "cookie",
        "blurb": "Bars, chips, chocolates and grab-and-go snacks with full nutrition facts.",
    },
}

CATEGORY_ORDER = ["Hot", "Cold", "Frappuccino", "Food/Meal", "Bakery", "Snacks & Sweets"]

# Macro fields surfaced to the front end (numeric). 'unit' drives display.
MACRO_FIELDS = [
    ("calories", "Calories", ""),
    ("fat", "Total Fat", "g"),
    ("sat_fat", "Sat. Fat", "g"),
    ("carbs", "Carbs", "g"),
    ("fiber", "Fiber", "g"),
    ("sugar", "Sugar", "g"),
    ("protein", "Protein", "g"),
    ("sodium", "Sodium", "mg"),
    ("cholesterol", "Cholesterol", "mg"),
    ("caffeine", "Caffeine", "mg"),
]

# ---------------------------------------------------------------------------
# Estimated customization deltas (Grande reference; volume items scale by oz/16
# inside calc.js). NOT scraped — documented approximations. See module docstring.
# ---------------------------------------------------------------------------
MILK_DELTAS = {
    # name: [calories, fat, carbs, sugar, protein]  (Grande, 16 fl oz reference)
    "No Milk": [0, 0, 0, 0, 0],
    "Nonfat Milk": [70, 0, 10, 10, 7],
    "Skimmed Milk": [70, 0, 10, 10, 7],
    "Semi-Skimmed Milk": [90, 3, 9, 9, 7],
    "2% Milk": [100, 4, 9, 9, 7],
    "Whole Milk": [150, 8, 9, 9, 7],
    "Oatmilk": [120, 5, 16, 7, 3],
    "Almond Milk": [60, 3, 3, 2, 2],
    "Coconut Milk": [70, 4, 8, 6, 1],
    "Soy": [110, 4, 9, 7, 6],
    "Breve (Half and Half)": [315, 28, 10, 9, 7],
    "Heavy Cream": [410, 44, 3, 3, 3],
    "Vanilla Sweet Cream": [190, 16, 11, 11, 2],
    "Nondairy Vanilla Sweet Cream": [170, 12, 13, 11, 1],
    "Protein-boosted Milk": [130, 4, 9, 8, 13],
}

# Milks offered as quick-swap chips in the calculator (subset, common ones first).
MILK_CHOICES = [
    "No Milk", "Nonfat Milk", "2% Milk", "Whole Milk",
    "Oatmilk", "Almond Milk", "Soy", "Coconut Milk", "Breve (Half and Half)",
]

DELTAS = {
    # per-volume items: scaled by size in calc.js (factor = size_oz / 16)
    "milk": MILK_DELTAS,
    "scalable": ["milk", "whip", "foam"],
    "addons": {
        # name: [calories, fat, carbs, sugar, protein]  (Grande reference)
        "Whipped Cream": [80, 7, 6, 5, 1],
        "Cold Foam": [55, 3, 5, 5, 1],
    },
    # per-unit items (count driven, not size scaled)
    "syrup_pump": [20, 0, 5, 5, 0],        # one pump flavored syrup
    "syrup_pump_sf": [5, 0, 1, 0, 0],      # sugar-free pump
    "sauce_pump": [30, 1, 6, 6, 0],        # mocha/caramel sauce pump
    "shot": {"calories": 5, "caffeine": 75},  # one extra espresso shot
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def slugify(name: str) -> str:
    """URL-safe slug; strips ®/™, accents and punctuation."""
    s = name.strip()
    s = s.replace("®", "").replace("™", "").replace("℠", "")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    s = re.sub(r"-{2,}", "-", s)
    return s or "drink"


def num(value) -> float:
    """Parse '7 g', '150 mg', '190', 0 -> float. Returns 0.0 if not parseable."""
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    m = re.search(r"-?\d+(\.\d+)?", str(value))
    return float(m.group()) if m else 0.0


def as_int_or_float(x: float):
    return int(x) if float(x).is_integer() else round(x, 1)


def size_oz(size_label: str) -> float | None:
    """Extract fl-oz from a size label, else None (food piece sizes)."""
    m = re.search(r"([\d.]+)\s*fl oz", size_label)
    return float(m.group(1)) if m else None


def is_beverage_size(size_label: str) -> bool:
    return "fl oz" in size_label


def order_sizes(sizes: dict) -> list[str]:
    """Beverage sizes ascending by fl oz; non-beverage kept in source order."""
    labels = list(sizes.keys())
    bev = [s for s in labels if is_beverage_size(s)]
    other = [s for s in labels if not is_beverage_size(s)]
    bev.sort(key=lambda s: size_oz(s) or 0)
    return bev + other


# ---------------------------------------------------------------------------
# products.json -> map each variant drink name to its group header
# ---------------------------------------------------------------------------
def build_group_map(products: dict) -> dict[str, str]:
    group_of: dict[str, str] = {}
    for _cat, entries in products.items():
        current_group = ""
        for e in entries:
            raw = e.get("name", "")
            name = raw.strip()
            if not name:
                continue
            if raw.startswith("  "):  # indented => a variant under current group
                group_of[name] = current_group
            else:                      # flush-left => a group header
                current_group = name
    return group_of


def make_description(name: str, group: str, cat_label: str, grande: dict | None,
                     is_food: bool) -> str:
    """Unique, data-backed one-liner (uses real numbers to avoid thin/dupe copy)."""
    g = (group or cat_label).rstrip("s")
    if grande:
        cal = as_int_or_float(grande.get("calories", 0))
        sugar = as_int_or_float(grande.get("sugar", 0))
        protein = as_int_or_float(grande.get("protein", 0))
        if is_food:
            return (f"{name} from Starbucks has about {cal} calories with {protein}g protein "
                    f"and {sugar}g sugar. See the full nutrition facts below.")
        return (f"A Grande {name} has roughly {cal} calories, {sugar}g sugar and {protein}g "
                f"protein. Calculate calories and macros for every size and customization.")
    return (f"{name} — Starbucks {g.lower()} nutrition facts. See calories, sugar, protein "
            f"and caffeine for every size.")


# ---------------------------------------------------------------------------
# Main dataset builder
# ---------------------------------------------------------------------------
def build_dataset() -> dict:
    nutrition = json.loads((DATA_DIR / "nutrition_full.json").read_text(encoding="utf-8"))
    products = json.loads((DATA_DIR / "products.json").read_text(encoding="utf-8"))
    group_of = build_group_map(products)

    drinks: dict[str, dict] = {}
    by_category: dict[str, list[str]] = {c["slug"]: [] for c in CATEGORIES.values()}
    slug_seen: dict[str, int] = {}

    for name, rec in nutrition.items():
        cat_label = rec.get("category", "Hot")
        cat = CATEGORIES.get(cat_label)
        if not cat:
            continue
        raw_sizes = rec.get("sizes", {})
        if not raw_sizes:
            continue

        ordered = order_sizes(raw_sizes)
        is_food = not any(is_beverage_size(s) for s in ordered)

        # normalize macro values to numbers, keep only offered sizes
        base = {}
        for s in ordered:
            row = raw_sizes[s]
            base[s] = {field: as_int_or_float(num(row.get(field)))
                       for field, _label, _unit in MACRO_FIELDS}

        # pick a default size: Grande for beverages else the first offered size
        default_size = next((s for s in ordered if s.startswith("Grande")), ordered[0])
        grande = base.get(default_size)

        # default milk + shots from scraped per-size defaults (if any)
        defaults = rec.get("defaults", {}) or {}
        dsize_defaults = defaults.get(default_size, {}) if isinstance(defaults, dict) else {}
        default_milk = dsize_defaults.get("Milk", "2% Milk")
        if default_milk not in MILK_DELTAS:
            default_milk = "2% Milk"
        shot_opts = dsize_defaults.get("Espresso & Shot Options", {}) or {}
        try:
            default_shots = int(num(shot_opts.get("Espresso Shot", 0)))
        except Exception:
            default_shots = 0

        # unique slug
        slug = slugify(name)
        if slug in slug_seen:
            slug_seen[slug] += 1
            slug = f"{slug}-{slug_seen[slug]}"
        else:
            slug_seen[slug] = 1

        group = group_of.get(name, "")
        drinks[slug] = {
            "slug": slug,
            "name": name,
            "category": cat["slug"],
            "category_label": cat["title"],
            "group": group,
            "is_new": bool(rec.get("is_new")),
            "is_food": is_food,
            "desc": make_description(name, group, cat["title"], grande, is_food),
            "sizes": ordered,
            "default_size": default_size,
            "default_milk": default_milk,
            "default_shots": default_shots,
            "base": base,
        }
        by_category[cat["slug"]].append(slug)

    # sort drinks within each category alphabetically by name
    for slug_list in by_category.values():
        slug_list.sort(key=lambda s: drinks[s]["name"].lower())

    return {
        "drinks": drinks,
        "by_category": by_category,
        "categories": CATEGORIES,
        "macro_fields": MACRO_FIELDS,
        "milk_choices": MILK_CHOICES,
        "deltas": DELTAS,
    }


def minimal_for_client(dataset: dict) -> dict:
    """Trim the dataset to what calc.js needs (drives the standalone calculator)."""
    drinks = {}
    for slug, d in dataset["drinks"].items():
        drinks[slug] = {
            "name": d["name"],
            "category": d["category"],
            "is_food": d["is_food"],
            "sizes": d["sizes"],
            "default_size": d["default_size"],
            "default_milk": d["default_milk"],
            "default_shots": d["default_shots"],
            "base": d["base"],
        }
    return {
        "milk_choices": dataset["milk_choices"],
        "deltas": dataset["deltas"],
        "drinks": drinks,
    }


def main():
    dataset = build_dataset()
    out_dir = ROOT / "dist" / "data"
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = minimal_for_client(dataset)
    (out_dir / "nutrition.min.json").write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"nutrition.min.json: {len(payload['drinks'])} drinks written")


if __name__ == "__main__":
    main()
