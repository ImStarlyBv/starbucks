# Site Architecture (the built site)

How NutriBucks is generated and served. (For the *original* site's reverse-engineering, see
`starbucks-calculator-ARCHITECTURE.md`.)

## Overview

Static Site Generation — no runtime backend. A Python script renders every page to plain HTML;
nginx serves the folder. The calculator runs client-side from an embedded dataset.

```
data/*.json
   │  (real per-size macros, product groups, option lists)
   ▼
src/prepare_data.py   build_dataset()  ─► drinks{slug:…}, by_category, estimated DELTAS
   │                  minimal_for_client() ─► dist/data/nutrition.min.json
   ▼
src/build.py (Jinja2) ─► dist/
   ├─ index.html                         (home / explore)
   ├─ {category}/index.html        ×6    (category listings)
   ├─ drink/{slug}/index.html      ×391  (per-drink calculator + static table)
   ├─ calculator/index.html              (standalone calculator)
   ├─ 404.html
   ├─ sitemap.xml · robots.txt · manifest.webmanifest
   └─ assets/{favicon.svg, og-default.svg}, data/nutrition.min.json, assets/calc.js (copied)

Tailwind CLI  ─► dist/assets/app.css   (purges against rendered dist/ + templates + calc.js)
```

## Components

| File | Role |
|---|---|
| `src/prepare_data.py` | Cleans scraped JSON → dataset; defines the estimated delta table; writes `nutrition.min.json`. |
| `src/build.py` | Jinja2 renderer. Owns site config (`SITE`, `NUTRIBUCKS_SITE_URL`), FAQ generators, featured selection, per-page meta, sitemap/robots/manifest, SVG assets. |
| `src/templates/base.html` | `<head>` (meta, OG/Twitter, fonts, sitewide JSON-LD), header nav, footer hub, mobile nav, skip link. Blocks: `schema`, `content`, `body_scripts`. |
| `src/templates/_macros.html` | `cat_icon`, `tile` (SVG visual), `drink_card`, `breadcrumbs`, `faq_block`. |
| `src/templates/{home,category,drink,calculator,notfound}.html` | Page templates extending `base`. |
| `src/assets/calc.js` | Calculator engine + home search + category filter + standalone picker. |
| `src/assets/app.css` | Tailwind entry + custom components (`glass-card`, `disclosure`, `cv-auto`, fallbacks). |

## Path handling (portability)

`build.py` injects a `rel` prefix per page depth (`""`, `"../"`, `"../../"`) so all internal
links are **relative** — the site works at a domain root or a sub-path. The `404.html` is the
one exception: it uses absolute `/` paths because it is served from arbitrary URLs.

Canonical / OG / sitemap URLs are **absolute**, built from `NUTRIBUCKS_SITE_URL`
(default `https://www.nutribucks.app`; override via env or the compose build arg).

## Calculator data flow

- **Drink page:** self-contained. `build.py` embeds a `<script id="drink-data">` JSON payload
  (that drink's base + the deltas + milk choices). `calc.js` hydrates in place — no fetch.
- **Standalone calculator:** `calc.js` fetches `data/nutrition.min.json` (all drinks + deltas)
  once, then renders any selected drink's panel on demand. The picker links also work without
  JS (they point at each drink's own page).

## Build order (important)

`build.py` runs **before** Tailwind, because Tailwind purges against the rendered HTML in
`dist/`. `npm run build` and the Dockerfile both enforce this order. Running Tailwind first
would strip classes that only appear in generated pages.

## Why SSG (vs Next/Astro)

Zero framework weight, every page is pre-rendered HTML (ideal for crawlers + LCP), trivially
Dockerized behind nginx, no Node runtime in production. See `DEPLOYMENT.md`.
