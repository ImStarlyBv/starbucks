# NutriBucks — Build Log (Advances)

Record of what was implemented against `BUILD-SPEC.md`, and the verification results.
Build completed 2026-06-06.

---

## Status: ✅ Complete & verified

All 7 planned phases done. The site builds, compiles, serves, and passes every check below.

| Phase | Deliverable | Status |
|---|---|---|
| 1 | Theme & tooling — `tailwind.config.js`, `package.json`, `src/assets/app.css` | ✅ |
| 2 | Data pipeline — `src/prepare_data.py` → `nutrition.min.json` + estimated deltas | ✅ |
| 3 | Templates — `base / home / category / drink / calculator / notfound / _macros` | ✅ |
| 4 | Calculator engine — `src/assets/calc.js` (additive model + search/filter) | ✅ |
| 5 | Generator — `src/build.py` + sitemap / robots / manifest / 404 | ✅ |
| 6 | Container — `Dockerfile`, `nginx.conf`, `docker-compose.yml`, `README.md` | ✅ |
| 7 | Build, compile Tailwind, verify | ✅ |

---

## What was built

### Data (real BASE, estimated deltas)
- Parsed `data/nutrition_full.json` → **391 drinks/foods**, each with real per-size macro
  profiles (calories, fat, sat fat, carbs, fiber, sugar, protein, sodium, cholesterol, caffeine).
- Categories: Hot 89 · Cold 157 · Frappuccino 45 · Food 31 · Bakery 45 · Snacks 24.
- Unique URL slugs (handles ®/™/accents); per-size defaults (milk + shots) read from data.
- Customization **deltas are estimated** (the source API never exposed them) and labelled as
  such in the UI. See `docs/DATA-MODEL.md`.

### Pages (all server-rendered, crawler-first)
- `/` — real `<h1>` "Starbucks Nutrition Calculator", hero search, 8 featured cards, category
  hub, SEO copy, on-page FAQ.
- `/{category}/` ×6 — filter/sort sidebar (progressive enhancement) over a fully rendered grid.
- `/drink/{slug}/` ×391 — full per-size nutrition **table baked into static HTML** + interactive
  calculator (size, milk, syrup pumps, extra shots, whipped cream, cold foam) + related drinks + FAQ.
- `/calculator/` — searchable drink picker + the same engine; deep-linkable via `?drink=slug`.
- `404.html`, `sitemap.xml` (399 URLs), `robots.txt`, `manifest.webmanifest`.

### Front end
- Tailwind compiled via CLI (no CDN), purged to **~27 KB**. Theme tokens ported verbatim from
  the design (`design/allthecode.md`).
- One vanilla ES module (`calc.js`, ~16 KB) — deferred, no framework.
- **Zero external images** — category-tinted SVG tiles + generated favicon/OG SVG.

---

## Verification results

| Check | Result |
|---|---|
| Generator run | 391 drinks + 6 categories + home + calculator + 404 |
| Tailwind compile | `dist/assets/app.css` = 27 KB (purged); all critical/arbitrary/JS-injected classes retained |
| JSON-LD validity | Parses on every page type — **0 errors**; no unrendered Jinja `{{ }}` |
| Internal links | **12,770 checked → 0 broken** (`scripts/check_links.py`) |
| Calculator math | default == real base; +Oatmilk +20 cal, +2 syrup +40, +shot +5 cal/+75 mg caffeine, +whip +80, size-scaling correct |
| Live HTTP serve | `/`, `/calculator/`, `/hot/`, `/drink/caffe-latte/`, `/data/...json`, `/assets/*`, `/404.html` → all **200** |

---

## SEO improvements over the original (from the teardown)

- Added a real keyword **`<h1>`** + clean H2/H3 outline (original had no H1).
- **On-page FAQ** with `FAQPage` schema (original exiled FAQs to another URL).
- Full JSON-LD graph: `Organization` + `WebSite` + `Person` (author) sitewide; per-page
  `WebPage`/`CollectionPage`, `BreadcrumbList`, `ItemList` (category), `MenuItem` +
  `NutritionInformation` (drink), `WebApplication` (calculator).
- Hub-and-spoke internal linking; self-referencing canonicals; OG/Twitter; consistent named author.

## Core Web Vitals measures (from the modern-web-guidance skill)

- Native `<details>` FAQ — crawlable, Find-in-page, works without JS.
- Font preconnect + `font-display: swap`; deferred ES module (no render-block JS).
- `content-visibility:auto` on long drink grids; `prefers-reduced-motion` honored.
- No image LCP/CLS risk (SVG tiles only).

---

## Known approximations (documented, not hidden)

- Customization deltas (milk/syrup/foam/shot) are **estimates** applied on top of real base
  nutrition, labelled "estimated" in the UI. Per `BUILD-SPEC.md §9`. Future enhancement:
  scrape per-drink deltas for exactness.

## Reference docs (written during/after the build)

- `docs/SITE-ARCHITECTURE.md` — pipeline & how pages are generated
- `docs/DATA-MODEL.md` — dataset shape + the estimated delta model
- `docs/SEO-IMPLEMENTATION.md` — schema, meta, CWV details
- `docs/DEPLOYMENT.md` — Docker / nginx / local build reference

---

## Source docs used at the start of the session (inputs)

The build was driven by these five files (paths relative to `nutribucks/`):

| File | What it gave us |
|---|---|
| `BUILD-SPEC.md` | The frozen build plan: goals, architecture, page list, SEO checklist, tech stack, build order, documented approximations. |
| `design/allthecode.md` | The 3 design mockups (Explore/home, Drink Calculator, Category listing) — source of the Material-3 green theme tokens, fonts, and component styling. |
| `docs/starbucks-calculator-ARCHITECTURE.md` | Reverse-engineering of the original tool: the additive `BASE + Σ DELTA` model and why deltas aren't directly downloadable. |
| `docs/starbucks-options-dataset.md` | Full catalog (455 entries, 6 categories) + 211 customization options across 26 categories + the 6 sizes. |
| `docs/starbucks-nutrition-calculator-ANALYSIS.md` | SEO teardown of the original page — the winning patterns to replicate and the weaknesses to fix (no H1, off-page FAQ, thin headings). |

Scraped data inputs consumed by the build: `data/nutrition_full.json`,
`data/products.json`, `data/customizations.json`.
