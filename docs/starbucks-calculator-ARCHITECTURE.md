# Starbucks Calorie Calculator — How the Calculation Actually Works

**Investigated:** 2026-06-02. Plugin v2.2.1 (`wp-content/plugins/starbucks-calorie-calculator/`).
**Bottom line up front:** There is **no calorie formula in the browser**. All nutrition math runs **server-side in the WordPress plugin's PHP**, which is never sent to the client. The page can't be "copied" by lifting a JS formula — there isn't one. What *is* replicable is the **architecture, the data, and the additive calorie model** described below.

---

## 1. Architecture (client ↔ server)

The front-end is a jQuery widget. It holds **zero nutrition numbers**. Every value the user sees comes back from an AJAX round-trip to `wp-admin/admin-ajax.php`. The flow:

```
User picks category  → AJAX get_product_names → list of drinks
User picks a drink   → AJAX get_sizes          → sizes + each size's default ("included") customizations
User picks size      → AJAX get_customization  → full option lists (milks, syrups, foams, …) [loaded once]
User changes anything→ AJAX calculate          → { totalCalories, html } ← SERVER computes here
```

The browser's only job is to assemble a selection object and render the HTML the server returns. The `totalCalories` number is produced entirely by the server.

---

## 2. The AJAX endpoints (the real API)

All are `POST` to `https://…/wp-admin/admin-ajax.php`, each guarded by its own WP nonce (from the page's inline `ajax_object`) and requiring the session cookie + a same-site `Referer`.

| `action` | Params | Returns |
|---|---|---|
| `get_product_names` | `topCategory` (slug), `filterData` (JSON or null), nonce | `[{name, is_new}]` — group headers + indented variants |
| `get_sizes` | `product_name`, nonce | `{success, sizes:[{size, included_customizations}]}` |
| `get_customization` | nonce only | `{success, customizations:{ Milk:[…], Syrups:[…], … }}` |
| `calculate` | `formData` (serialized form: product, size, customizations JSON), nonce | `{ totalCalories, html, orderDetails }` |
| `save_community_drink` / `get_community_drinks` / `vote_community_drink` / `get_single_drink` / `search_similar_drinks` / `check_drink_exists` / `increment_share_count` | various | community "save & share a drink" feature |

**Category slugs:** `hot, cold, frappe, foodmeal, bakery, snack`.

**`get_sizes` example** (`Caffè Americano`) — note it returns each size's *default* included customizations, not calories:
```json
{"success":true,"sizes":[
  {"size":"Short(8 fl oz)","included_customizations":{"Espresso Roast":"Signature Espresso Roast","Espresso & Shot Options":{"Espresso Shot":"1"}}},
  {"size":"Tall(12 fl oz)","included_customizations":{"Espresso Roast":"Signature Espresso Roast","Espresso & Shot Options":{"Espresso Shot":"2"}}},
  {"size":"Grande(16 fl oz)","included_customizations":{…"Espresso Shot":"3"}}, …
]}
```

---

## 3. The calorie model (what the server is doing)

From the response shapes and the client code, the server uses a **stored-base + additive-delta** model — *not* a clever formula:

```
total_calories(drink, size, selections)
  = BASE[drink][size]                         # pre-stored per drink, per size
  + Σ DELTA[customization_option][size]        # each add-on contributes calories, often size-scaled
  − defaults that were removed                 # "No Milk", "Light", "Sugar-Free", etc. subtract
```

Evidence for this model:
- **Per-size base values:** sizes are discrete (Short→Trenta) and each carries its own `included_customizations`, so each (drink × size) has its own stored nutrition row.
- **Customizations are line items:** the client diffs `preloaded` (size defaults) vs `customized` (user changes) and sends only the *changes* to `calculate`. The server adds/removes each line's calories. (Client code literally builds `de.preloaded` and `de.customized` objects and deletes unchanged keys before sending.)
- **Modifier intensities:** every option has `Extra / Regular / Light / No` variants (e.g. "Extra Apple Juice", "Light Peach Juice Blend", "No Apple Juice") — these are *separate stored values*, confirming a lookup table, not arithmetic scaling.
- **Size-specific add-ons:** the changelog repeatedly mentions "size-specific calculations for all milk types," "size-based nutrition logic," "splash calories upgraded with adjustable intensity" — i.e. `DELTA` is keyed by `[option][size]`, not a single number.
- The `calculate` response returns pre-rendered **HTML** (the itemized nutrition breakdown) plus the summed `totalCalories`, so the server owns both the math and the presentation.

**There is no proprietary equation to reverse — it's a big nutrition lookup table summed line by line.** Replicating it = obtaining the tables, not deriving a formula.

---

## 4. What you need to replicate the page

To rebuild a functional clone you need **three data tables** + the same UI flow:

1. **Drink catalog** — ✅ already scraped → `starbucks-options-dataset.md` (455 entries, 6 categories).
2. **Customization options** — ✅ already scraped (211 options across 12 categories).
3. **The number tables (NOT yet captured):**
   - `BASE[drink][size]` — calories of each drink at each size (the size defaults).
   - `DELTA[option][size]` — calories each customization adds/removes at each size.

Table #3 is only obtainable by driving the `calculate` endpoint once per combination and recording the returned `totalCalories` (i.e. measuring the black box). It is **not** downloadable as a file — the server never exposes its tables directly. My probes to `calculate` returned `"Nutritional information not available"` because the endpoint expects the *exact* serialized dynamic-form payload (the full `formData` the live form builds, including hidden fields and the precise `customizations` object shape), which needs to be reconstructed field-for-field from a real browser session (easiest via a headless browser / DevTools "copy as cURL" of a live request).

### Two honest paths forward
- **(A) Measure the black box:** Use a headless browser (Playwright) to load the tool, select each drink+size with no customizations → record `totalCalories` = `BASE`. Then toggle one customization at a time → the difference = that option's `DELTA`. This rebuilds tables #3 empirically. ~hundreds–thousands of requests; fully automatable.
- **(B) Use authoritative source data:** Starbucks publishes official nutrition for menu items; pairing the scraped catalog with official per-item nutrition gives you the same tables without hammering their endpoint, and is cleaner for your own SEO page.

---

## 5. Replication checklist (page parity)

- [ ] Category tabs (Hot / Cold / Frappe / Food/Meal / Bakery / Snacks & Sweets)
- [ ] Drink dropdown grouped by family (group header → variants), `🆕` flags
- [ ] Size selector with icons (Short → Trenta), per-size default customizations
- [ ] Customization panel: Milk, Espresso Roast, Syrups, Cold Foams, Juice, Scoop, Refresher Base, Toppings, Sauces, Drizzle, Tea, Powders — each with Extra/Regular/Light/No intensities
- [ ] Live total with `BASE + Σ DELTA` (client-side this time, so no server round-trips)
- [ ] Filters: calorie range + size + milk/foam/syrup/sauce/topping
- [ ] Save/share custom drink (link + community list) — optional
- [ ] Itemized nutrition breakdown HTML under the total
- [ ] SEO shell from `starbucks-nutrition-calculator-ANALYSIS.md` (Article schema, freshness, internal links) — and fix that page's weaknesses (real H1, on-page FAQ schema)

---
*Companion files: `starbucks-options-dataset.md` (catalog + options), `starbucks-nutrition-calculator-ANALYSIS.md` (SEO teardown), raw: `_products.json`, `_customizations.json`, `_bundle.js`.*
