"""
build.py — static site generator for NutriBucks.

Renders crawler-first HTML for every page (home, 6 categories, ~391 drinks,
standalone calculator, 404) plus sitemap.xml, robots.txt and manifest.webmanifest
into dist/. Tailwind compiles dist/assets/app.css separately (see package.json).

Run:  python src/build.py
Env:  NUTRIBUCKS_SITE_URL  (canonical/OG/sitemap base; default https://www.nutribucks.app)
"""

from __future__ import annotations

import datetime as _dt
import json
import os
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from prepare_data import build_dataset, minimal_for_client, MACRO_FIELDS, DELTAS, MILK_CHOICES

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
TEMPLATES = SRC / "templates"

SITE = {
    "name": "NutriBucks",
    "url": os.environ.get("NUTRIBUCKS_SITE_URL", "https://nutribucks.shop").rstrip("/"),
    "author": "Olivia Bennett",
}
BUILD_DATE = _dt.date.today().isoformat()
YEAR = _dt.date.today().year

FEATURED_NAMES = [
    "Caffè Latte", "Caramel Macchiato", "Cappuccino", "Caffè Americano",
    "Iced Caffè Latte", "Iced Caramel Macchiato", "Matcha Latte", "Pumpkin Spice Latte",
]

FEATURES = [
    {"icon": "database", "title": "Every size, real numbers",
     "text": "Calories and macros for Short through Trenta, compiled per drink."},
    {"icon": "tune", "title": "All your customizations",
     "text": "Swap milk, add syrup pumps, extra shots, whipped cream or cold foam."},
    {"icon": "bolt", "title": "Instant, client-side",
     "text": "Totals update live in your browser — no waiting, no sign-up."},
    {"icon": "verified", "title": "Independent & free",
     "text": "Not affiliated with Starbucks. Always free, no ads on the data."},
]


# ---------------------------------------------------------------------------
# FAQ generators (data-driven so each page is unique)
# ---------------------------------------------------------------------------
def home_faqs(drink_count):
    return [
        {"q": "Is the NutriBucks Starbucks nutrition calculator free?",
         "a": "Yes. NutriBucks is a free, independent tool covering "
              f"{drink_count} Starbucks drinks and foods. There's no sign-up and the "
              "nutrition data is open to browse."},
        {"q": "How accurate are the calorie and macro numbers?",
         "a": "Base nutrition for each drink and size is compiled from published Starbucks "
              "figures. Customization effects (milk swaps, extra syrup, cold foam) are "
              "estimated and added on top, so totals are a close guide rather than an exact label."},
        {"q": "Can I calculate calories for a customized drink?",
         "a": "Yes. Open any drink, choose your size, switch the milk, add or remove syrup "
              "pumps, add espresso shots or top with cold foam, and the calories, sugar, "
              "protein and caffeine update instantly."},
        {"q": "Does NutriBucks show caffeine and sugar, not just calories?",
         "a": "Every drink lists calories, total fat, saturated fat, carbs, fiber, sugar, "
              "protein, sodium, cholesterol and caffeine for each size."},
        {"q": "Is NutriBucks affiliated with Starbucks?",
         "a": "No. NutriBucks is an independent reference tool and is not affiliated with, "
              "endorsed by, or sponsored by Starbucks Corporation. Always check official "
              "Starbucks nutrition for allergen and medical decisions."},
    ]


def calculator_faqs():
    return [
        {"q": "How does the Starbucks calorie calculator work?",
         "a": "It starts from the real base nutrition for your drink and size, then adds the "
              "estimated calories and macros of each customization you choose — milk, syrup "
              "pumps, espresso shots, whipped cream and cold foam."},
        {"q": "Why are customization values labelled 'estimated'?",
         "a": "Starbucks doesn't publish a public figure for every single add-on at every "
              "size, so add-on contributions are reasonable estimates applied on top of the "
              "verified base nutrition."},
        {"q": "Can I share or save a calculated drink?",
         "a": "Each drink has its own URL, and the calculator accepts a ?drink=slug link so "
              "you can jump straight to a drink. Bookmark the page to keep your favorite."},
        {"q": "Does the calculator work on mobile?",
         "a": "Yes — it's a fast, responsive web app that runs entirely in your browser, so "
              "it works on phones, tablets and desktop without installing anything."},
    ]


def drink_faqs(d):
    b = d["base"][d["default_size"]]
    size = d["default_size"]
    faqs = [{
        "q": f"How many calories are in a {size} {d['name']}?",
        "a": (f"A {size} {d['name']} has about {b['calories']} calories, with {b['fat']}g fat, "
              f"{b['carbs']}g carbs, {b['sugar']}g sugar and {b['protein']}g protein (estimated)."),
    }]
    if d["is_food"]:
        faqs.append({"q": f"How much protein is in {d['name']}?",
                     "a": f"{d['name']} provides about {b['protein']}g of protein and {b['sugar']}g of sugar per serving."})
        faqs.append({"q": f"Is {d['name']} a good Starbucks snack option?",
                     "a": (f"At roughly {b['calories']} calories it can fit many plans. Check the "
                           "full nutrition table above and pair it with a lower-calorie drink to balance your order.")})
    else:
        caf = b.get("caffeine", 0)
        if caf:
            faqs.append({"q": f"How much caffeine is in a {d['name']}?",
                         "a": f"A {size} {d['name']} has about {caf}mg of caffeine. Larger sizes and extra espresso shots add more."})
        else:
            faqs.append({"q": f"Does {d['name']} contain caffeine?",
                         "a": f"A {d['name']} has little to no caffeine in its standard recipe."})
        faqs.append({"q": f"What's the lowest-calorie way to order a {d['name']}?",
                     "a": ("Pick a smaller size, switch to nonfat or almond milk, cut the syrup "
                           "pumps and skip whipped cream. Use the calculator above to see the exact savings.")})
    return faqs


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------
def rel_for(out_path: Path) -> str:
    """Relative prefix from a rendered file back to dist root."""
    depth = len(out_path.relative_to(DIST).parts) - 1  # minus the filename
    return "../" * depth


def write(env, template, out_rel: str, ctx: dict):
    out_path = DIST / out_rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Pages may force an absolute rel (e.g. 404 served from arbitrary URLs).
    ctx = {**ctx, "rel": ctx.get("rel") or rel_for(out_path)}
    out_path.write_text(env.get_template(template).render(**ctx), encoding="utf-8")
    return out_path


def page(title, description, path, og_type="website"):
    """Build the per-page meta object. `path` is the public URL path (with trailing /)."""
    canonical = f"{SITE['url']}{path}"
    return {"title": title, "description": description, "canonical": canonical, "og_type": og_type}


# ---------------------------------------------------------------------------
# Static asset generators (SVG -> no external imagery, tiny + crisp)
# ---------------------------------------------------------------------------
FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#006241"/>
<path d="M20 18h22a4 4 0 0 1 4 4 12 12 0 0 1-12 12h-2v6a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V18z" fill="none" stroke="#a2f3c8" stroke-width="3" stroke-linejoin="round"/>
<path d="M44 22h3a5 5 0 0 1 0 10h-3" fill="none" stroke="#a2f3c8" stroke-width="3"/>
</svg>"""

OG_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#006241"/>
<g opacity="0.12" fill="#ffffff"><circle cx="100" cy="100" r="3"/><circle cx="200" cy="160" r="3"/><circle cx="300" cy="80" r="3"/></g>
<text x="80" y="300" font-family="Plus Jakarta Sans, sans-serif" font-size="84" font-weight="800" fill="#ffffff">NutriBucks</text>
<text x="80" y="380" font-family="Source Sans 3, sans-serif" font-size="40" fill="#a2f3c8">Starbucks Nutrition Calculator</text>
<text x="80" y="440" font-family="Source Sans 3, sans-serif" font-size="28" fill="#d2e7e0">Calories, macros &amp; caffeine for every drink and size</text>
</svg>"""


def emit_assets(dataset):
    assets = DIST / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC / "assets" / "calc.js", assets / "calc.js")
    (assets / "favicon.svg").write_text(FAVICON_SVG, encoding="utf-8")
    (assets / "og-default.svg").write_text(OG_SVG, encoding="utf-8")
    # client dataset for the standalone calculator
    (DIST / "data").mkdir(parents=True, exist_ok=True)
    (DIST / "data" / "nutrition.min.json").write_text(
        json.dumps(minimal_for_client(dataset), ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def emit_meta_files(urls):
    # robots.txt
    (DIST / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n", encoding="utf-8")
    # sitemap.xml
    items = "\n".join(
        f"  <url><loc>{SITE['url']}{p}</loc><lastmod>{BUILD_DATE}</lastmod>"
        f"<changefreq>{cf}</changefreq><priority>{pr}</priority></url>"
        for p, cf, pr in urls)
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{items}\n</urlset>\n", encoding="utf-8")
    # manifest
    manifest = {
        "name": "NutriBucks — Starbucks Nutrition Calculator",
        "short_name": "NutriBucks",
        "description": "Calories, macros and caffeine for every Starbucks drink and food.",
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "background_color": "#e6fff6",
        "theme_color": "#006241",
        "icons": [
            {"src": "/assets/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any maskable"}
        ],
    }
    (DIST / "manifest.webmanifest").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    dataset = build_dataset()
    drinks = dataset["drinks"]
    by_cat = dataset["by_category"]
    categories = dataset["categories"]
    cat_counts = {c["slug"]: len(by_cat[c["slug"]]) for c in categories.values()}
    drink_count = len(drinks)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True, lstrip_blocks=True,
    )

    common = {
        "site": SITE, "build_date": BUILD_DATE, "year": YEAR,
        "categories": categories, "cat_counts": cat_counts, "drink_count": drink_count,
    }

    # featured slugs (by name, fallback to first hot/cold)
    name_to_slug = {d["name"]: s for s, d in drinks.items()}
    featured_slugs = [name_to_slug[n] for n in FEATURED_NAMES if n in name_to_slug]
    for s in by_cat["hot"] + by_cat["cold"]:
        if len(featured_slugs) >= 8:
            break
        if s not in featured_slugs:
            featured_slugs.append(s)
    featured = [drinks[s] for s in featured_slugs[:8]]

    search_index = [
        {"n": d["name"], "s": d["slug"], "c": d["category"], "k": d["base"][d["default_size"]]["calories"]}
        for d in drinks.values()
    ]

    sitemap_urls = [("/", "weekly", "1.0"), ("/calculator/", "weekly", "0.9")]

    # ---- Home ----
    write(env, "home.html", "index.html", {
        **common, "nav": "home",
        "page": page("Starbucks Nutrition Calculator — Calories, Macros & Caffeine | NutriBucks",
                     "Free Starbucks nutrition calculator. Find calories, sugar, protein and "
                     "caffeine for every drink and size, then customize milk, syrups and add-ons.",
                     "/"),
        "featured": featured, "faqs": home_faqs(drink_count),
        "features": FEATURES, "search_index": search_index,
    })

    # ---- Categories ----
    for label, cat in categories.items():
        slug = cat["slug"]
        cat_drinks = [drinks[s] for s in by_cat[slug]]
        cal_max = max((d["base"][d["default_size"]]["calories"] for d in cat_drinks), default=500)
        cal_max = int((cal_max // 10 + 1) * 10)
        size_note = "Grande (16 fl oz) where available" if slug in ("hot", "cold", "frappuccino") else "the listed serving"
        title = f"{cat['title']} Nutrition — Calories & Macros | NutriBucks"
        desc = f"{cat['blurb']} {len(cat_drinks)} Starbucks {cat['title'].lower()} with full nutrition facts."
        write(env, "category.html", f"{slug}/index.html", {
            **common, "nav": slug, "cat": cat, "drinks": cat_drinks,
            "cal_max": cal_max, "size_note": size_note,
            "page": page(title, desc[:160], f"/{slug}/"),
        })
        sitemap_urls.append((f"/{slug}/", "weekly", "0.8"))

    # ---- Drinks ----
    for slug, d in drinks.items():
        related = [drinks[s] for s in by_cat[d["category"]] if s != slug]
        related.sort(key=lambda r: (r["group"] != d["group"], r["name"].lower()))
        related = related[:4]
        b = d["base"][d["default_size"]]
        title = f"{d['name']} Nutrition — {b['calories']} Calories ({d['default_size'].split('(')[0].strip()}) | NutriBucks"
        desc = d["desc"][:160]
        payload = {
            "drink": {k: d[k] for k in ("name", "category", "is_food", "sizes",
                                        "default_size", "default_milk", "default_shots", "base")},
            "deltas": DELTAS, "milk_choices": MILK_CHOICES,
        }
        write(env, "drink.html", f"drink/{slug}/index.html", {
            **common, "nav": d["category"], "d": d, "related": related,
            "macro_fields": MACRO_FIELDS, "milk_choices": MILK_CHOICES,
            "faqs": drink_faqs(d), "drink_payload": payload,
            "page": page(title, desc, f"/drink/{slug}/", og_type="article"),
        })
        sitemap_urls.append((f"/drink/{slug}/", "monthly", "0.7"))

    # ---- Standalone calculator ----
    all_drinks = sorted(drinks.values(), key=lambda d: d["name"].lower())
    write(env, "calculator.html", "calculator/index.html", {
        **common, "nav": "calculator", "all_drinks": all_drinks,
        "faqs": calculator_faqs(),
        "page": page("Starbucks Calorie Calculator — Customize Any Drink | NutriBucks",
                     "Build any Starbucks drink and see calories, sugar, protein and caffeine "
                     "update live. Choose size, milk, syrups, shots and cold foam.",
                     "/calculator/"),
    })

    # ---- 404 ----
    write(env, "notfound.html", "404.html", {
        **common, "nav": "", "featured": featured, "rel": "/",
        "page": page("Page not found — NutriBucks", "That page could not be found.", "/404.html"),
    })

    emit_assets(dataset)
    emit_meta_files(sitemap_urls)

    print(f"Built {drink_count} drinks + {len(categories)} categories + home + calculator + 404")
    print(f"Sitemap: {len(sitemap_urls)} URLs · site base: {SITE['url']}")


if __name__ == "__main__":
    main()
