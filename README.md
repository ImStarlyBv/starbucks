# NutriBucks — Starbucks Nutrition Calculator

A fast, SEO-first **static** Starbucks nutrition & calorie calculator. Every page is
pre-rendered HTML (great for crawlers and Core Web Vitals); the calculator runs entirely
client-side from an embedded dataset. Ships in a single nginx container.

- **391** drinks & foods across 6 categories, each with a full per-size nutrition table
- Real base nutrition (calories, fat, carbs, sugar, protein, sodium, caffeine…) baked into the HTML
- Live calculator: size · milk · syrup pumps · extra shots · whipped cream · cold foam
- On-page FAQ with `FAQPage` schema, plus `WebSite`/`Organization`/`BreadcrumbList`/`ItemList`/`MenuItem` JSON-LD
- No external imagery, no JS framework — category-tinted SVG tiles, one small ES module

## Architecture

```
data/*.json ─► src/prepare_data.py ─► clean dataset + estimated delta table
                       │
                  src/build.py (Jinja2) ─► dist/  (home, 6 categories, ~391 drinks,
                       │                            calculator, 404, sitemap, robots, manifest)
                  Tailwind CLI ───────────► dist/assets/app.css  (purged + minified)
                  src/assets/calc.js ─────► dist/assets/calc.js  (calculator engine + search/filter)
```

The nutrition model is **additive** (mirrors the source's server logic):
`total = BASE[drink][size] + Σ customization deltas`. Base numbers are real/scraped;
customization deltas were never exposed by the source API, so they are **documented
estimates** applied on top and labelled "estimated" throughout the UI
(see `BUILD-SPEC.md` §9 and `docs/starbucks-calculator-ARCHITECTURE.md`).

## Run with Docker (recommended)

One service, **one exposed port**:

```bash
docker compose up --build
# open http://localhost:8080
```

Set the canonical/sitemap domain for a real deploy:

```bash
NUTRIBUCKS_SITE_URL=https://yourdomain.com docker compose up --build
```

## Build locally (without Docker)

Requires Python 3 (+ `jinja2`) and Node 18+.

```bash
npm install                       # Tailwind CLI + plugins
pip install jinja2
npm run build                     # python src/build.py  → then compiles Tailwind
npm run serve                     # serve dist/ at http://localhost:8080
```

Individual steps:

```bash
npm run render        # python src/build.py   (HTML + sitemap/robots/manifest + data json)
npm run css           # compile + minify Tailwind into dist/assets/app.css
npm run css:watch     # rebuild CSS on change
```

> **Build order matters:** `build.py` runs first to render `dist/`, then Tailwind purges
> against the real output. `npm run build` already does this in the right order.

## Project layout

```
src/
  prepare_data.py     transforms scraped JSON → dataset + estimated deltas
  build.py            static site generator (Jinja2)
  templates/          base, home, category, drink, calculator, notfound, _macros
  assets/app.css      Tailwind entry + custom components (glass-card, disclosure, …)
  assets/calc.js      vanilla calculator engine + progressive search/filter
tailwind.config.js    design tokens (Material-3 green theme)
data/                 scraped inputs (nutrition_full, products, customizations)
dist/                 build output (served by nginx)
Dockerfile            multi-stage: node+python build → nginx static
nginx.conf            clean URLs, custom 404, gzip, cache + security headers
docker-compose.yml    single service, single port (8080→80)
```

## SEO notes

- Single keyword `<h1>` per page + clean H2/H3 outline (fixes the original's missing H1)
- Self-referencing canonical, OpenGraph/Twitter, `robots: index,follow`
- On-page FAQ uses native `<details>` — crawlable, Find-in-page friendly, works without JS
- `font-display:swap` + preconnect; deferred ES module; lazy/SVG visuals → green CWV targets
- "Not affiliated with Starbucks · estimated values" disclaimer on every page

## Disclaimer

NutriBucks is an independent reference tool and is **not affiliated with, endorsed by, or
sponsored by Starbucks Corporation**. Nutrition values are estimates for informational use
only and are not medical or dietary advice.
