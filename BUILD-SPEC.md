# NutriBucks — Build Specification

A fast, SEO-first Starbucks nutrition calculator. Static-rendered HTML for crawlers + a client-side calculator powered by real scraped nutrition data. Docker-ready.

> **Status:** spec frozen before build. Design source: `design/allthecode.md` (3 mockups: Explore/home, Drink Calculator, Category listing). Data sources: `../starbucks-options-dataset.md`, `../starbucks-base-calories.md`, and the scraped JSON (`../_products.json`, `../_customizations.json`, `../_nutrition_full.json`).

---

## 1. Goals & non-negotiables

1. **Crawler-first:** every meaningful piece of content (drink names, categories, calories, macros, descriptions, FAQ) ships in the **static HTML** — not injected by JS. A bot with JS disabled sees the full nutrition tables and all drink data.
2. **Working calculator:** drink + size + customizations → live calories & macros, computed **client-side** (no backend round-trip), using a pre-built nutrition dataset embedded as JSON.
3. **Docker-ready:** `docker build` → `docker run` serves the finished site (nginx, static). One command to deploy.
4. **SEO power:** fixes the weaknesses found in the original (`../starbucks-nutrition-calculator-ANALYSIS.md`): real single `<h1>`, clean heading outline, on-page FAQ with `FAQPage` schema, `WebApplication` + `BreadcrumbList` + `ItemList` schema, internal-link hub-and-spoke, fast LCP.
5. **Faithful to the NutriBucks design** (Material-3 green theme, Plus Jakarta Sans + Source Sans 3).

---

## 2. Architecture

**Static Site Generation (SSG) via a Python build script — no runtime backend.**

```
build.py  ── reads ──►  scraped JSON (nutrition + options)
   │
   ├─ renders ─► dist/index.html                 (Explore / home)
   ├─ renders ─► dist/<category>/index.html       (6 category listing pages)
   ├─ renders ─► dist/drink/<slug>/index.html     (≈391 per-drink calculator pages)
   ├─ renders ─► dist/calculator/index.html       (standalone full calculator)
   ├─ writes  ─► dist/data/nutrition.min.json      (calculator dataset)
   ├─ copies  ─► dist/assets/{calc.js, app.css, ...}
   ├─ writes  ─► dist/sitemap.xml, robots.txt, manifest.webmanifest
   └─ writes  ─► dist/404.html
```

Why SSG (not Next/Astro): zero JS framework weight, every page is plain pre-rendered HTML (ideal for crawlers + LCP), trivially Dockerized behind nginx, no Node runtime in production. The build step can run in CI or locally.

**Tailwind:** compile to a static `app.css` via the Tailwind CLI in the Docker build stage (NOT the Play CDN — the CDN ships a large JS runtime and causes FOUC, both bad for SEO/perf). The exact theme tokens from the design's `tailwind.config` are ported into `tailwind.config.js`.

---

## 3. Data model (the calculator engine)

Confirmed by reverse-engineering the source's `calculate` endpoint (see `../starbucks-calculator-ARCHITECTURE.md`). It is an **additive lookup model**, not a formula:

```
nutrition(drink, size, selections) =
    BASE[drink][size]                       # full profile: cal, fat, sat, carbs, sugar, protein, caffeine, sodium…
  + Σ DELTA[option][size]                   # each added customization's contribution
  − defaults removed (e.g. "No Milk")       # subtract a default the user turned off
```

- `BASE[drink][size]` — harvested for all ~391 drinks × every offered size (full macro profile). Source of truth.
- `DELTA[option][size]` — per-customization contribution, measured by toggling each option on a neutral base and diffing the full profile (size-specific). Stored once; reused across drinks (documented approximation, labelled "estimated").
- Sizes: Short(8) · Tall(12) · Grande(16) · Venti hot(20) · Venti cold(24) · Trenta(30). Not every drink offers every size — only render offered ones.
- All numbers carry the **"estimated / not affiliated with Starbucks"** disclaimer, matching the source.

`nutrition.min.json` shape:
```json
{
  "sizes": ["Short(8 fl oz)", "Tall(12 fl oz)", ...],
  "drinks": {
    "caffe-latte": {
      "name": "Caffè Latte", "category": "hot", "desc": "...",
      "base": { "Grande(16 fl oz)": {"calories":190,"fat":7,"sugar":18,"protein":13,"caffeine":150, ...}, ... },
      "defaults": { "Grande(16 fl oz)": {"milk":"2% Milk","shots":2} }
    }, ...
  },
  "deltas": { "milk": { "Oatmilk": {"Grande(16 fl oz)": {"calories":90,...}}, ... }, "syrups": {...}, ... }
}
```

---

## 4. Pages & content (all server-rendered HTML)

### 4.1 Home / Explore (`/`)
- `<h1>` **"Starbucks Nutrition Calculator"** (real keyword H1 — fixes the original's missing H1).
- Hero with search (progressive enhancement: filters the static grid client-side; works as a link list without JS).
- Category chips → link to category pages.
- Featured drink grid (cards rendered from data, each links to its drink page) — real calories in HTML.
- SEO body copy + **on-page FAQ** (accordion that is open/readable without JS) with `FAQPage` schema.
- Internal links to all 6 categories + calculator (hub-and-spoke).

### 4.2 Category listing (`/<category>/`)  ×6
- `<h1>` = category name (e.g. "Hot Coffees").
- Filter sidebar (roast / caffeine / dietary) — progressive enhancement over a fully-rendered list.
- Bento grid of every drink in the category, each card shows real Grande calories + macros and links to the drink page.
- `ItemList` + `BreadcrumbList` schema. Intro copy for the category.

### 4.3 Drink calculator page (`/drink/<slug>/`) ×~391
- `<h1>` = drink name. Description.
- **Full static nutrition table** for every size (crawlable) — this is the SEO meat: each drink page targets "{drink} calories / nutrition".
- Interactive calculator (size buttons, milk, syrups, foams, etc.) that updates the live nutrition panel from the embedded dataset.
- Default selection pre-rendered so numbers are visible before JS runs.
- `BreadcrumbList` + `WebApplication`/`NutritionInformation`-style schema, related-drink internal links.

### 4.4 Standalone calculator (`/calculator/`)
- Full drink picker (searchable) + the same calculator engine. Canonical "calculator" landing page.

---

## 5. SEO checklist (applied to every page)
- Unique `<title>` + meta description (templated per page).
- Single `<h1>`, logical `<h2>/<h3>` outline.
- Canonical URL, OpenGraph + Twitter card, `robots: index,follow`.
- JSON-LD: `WebSite` + `Organization` (sitewide), plus per-page `WebPage`/`Article`, `BreadcrumbList`, `ItemList` (category), `FAQPage` (home), `SoftwareApplication`/`WebApplication` (calculator). Named author for E-E-A-T.
- `sitemap.xml` (all pages), `robots.txt`, `manifest.webmanifest` (PWA-ish, matches original's app angle).
- Performance: compiled CSS, no render-blocking JS, `font-display:swap`, preconnect to fonts, lazy `loading="lazy"` images, calculator JS deferred. Target green Core Web Vitals.
- Disclaimers + "not affiliated with Starbucks; estimated values" on every page.

---

## 6. Tech stack
- **Build:** Python 3 (stdlib + Jinja2 for templates).
- **Styles:** Tailwind CSS (compiled via CLI), theme ported from design.
- **Client JS:** vanilla ES module `calc.js` (calculator engine + search/filter progressive enhancement). No framework.
- **Serve:** nginx (alpine) serving `dist/`.
- **Container:** multi-stage Dockerfile (stage 1: node→tailwind + python→build; stage 2: nginx static). `docker-compose.yml` for local run.

---

## 7. Repo layout
```
nutribucks/
  BUILD-SPEC.md            ← this file
  design/allthecode.md     ← original design mockups (reference)
  data/                    ← generated dataset (build input copies)
  src/
    templates/             ← Jinja2: base.html, home.html, category.html, drink.html, calculator.html
    assets/calc.js
    assets/app.css         ← Tailwind entry (@tailwind …) + custom (.glass-card, etc.)
    build.py               ← the generator
    prepare_data.py        ← transforms scraped JSON → nutrition.min.json
  tailwind.config.js
  package.json             ← tailwind build script
  Dockerfile
  docker-compose.yml
  nginx.conf
  dist/                    ← build output (served)
  README.md                ← how to build / run / deploy
```

---

## 8. Build order (execution plan)
1. ⏳ **Data:** finish full-nutrition scrape (`_nutrition_full.json`), then `prepare_data.py` → `nutrition.min.json` + delta table.
2. **Theme:** `tailwind.config.js` + `app.css` from design tokens.
3. **Templates:** `base.html` (head/schema/nav/footer) → home → category → drink → calculator.
4. **Engine:** `calc.js` (additive model, size/milk/syrup/foam controls, live panel, search/filter).
5. **Generator:** `build.py` renders all pages + sitemap/robots/manifest.
6. **Container:** Dockerfile (multi-stage) + nginx.conf + compose; `README.md`.
7. **Verify:** build, run container, spot-check rendered HTML has data without JS, calculator math matches source for sample drinks, Lighthouse pass.

---

## 9. Open approximations (documented, not hidden)
- **Customization deltas** are measured on a neutral base and applied uniformly; real per-drink interactions (e.g. removing a default milk) are approximated. Labelled "estimated," consistent with the source site's own disclaimer. A future enhancement can store per-drink deltas if exactness is required.
- Images in the design are AI-generated placeholders; production will use category icons / a neutral cup image (no scraped third-party imagery).
