# Data Model

How nutrition is represented and calculated.

## Inputs (`data/`)

| File | Contents |
|---|---|
| `nutrition_full.json` | **Source of truth.** `{ "<Drink Name>": { category, is_new, sizes:{<size>:{macros…}}, defaults:{<size>:{Milk, Espresso Roast, Espresso & Shot Options}} } }`. Macro values are strings like `"7 g"`, `"150 mg"`, `"190"`. |
| `products.json` | Category → ordered list of group headers (flush-left) and indented variants. Used to map each drink to its **group** (e.g. "Lattes"). |
| `customizations.json` | Option name lists per category (Milk, Syrups, Cold Foams…). **No nutrition values exist here or anywhere** — see the estimated-delta note below. |

## Cleaned dataset (`build_dataset()`)

Each drink becomes:

```jsonc
{
  "slug": "caffe-latte",
  "name": "Caffè Latte",
  "category": "hot",              // slug
  "category_label": "Hot Drinks",
  "group": "Lattes",
  "is_new": false,
  "is_food": false,               // true => no interactive customization, table only
  "desc": "A Grande Caffè Latte has roughly 190 calories, 18g sugar …",  // data-backed, unique
  "sizes": ["Short(8 fl oz)", "Tall(12 fl oz)", "Grande(16 fl oz)", "Venti(20 fl oz)"],
  "default_size": "Grande(16 fl oz)",
  "default_milk": "2% Milk",
  "default_shots": 2,
  "base": { "Grande(16 fl oz)": { "calories":190, "fat":7, "carbs":19, "sugar":18,
                                  "protein":13, "sat_fat":4.5, "fiber":0, "sodium":150,
                                  "cholesterol":25, "caffeine":150 }, … }
}
```

- Macro strings are parsed to numbers (`num()`); integers stay integers, else 1 decimal.
- Sizes are ordered by fl-oz ascending (beverages); food "piece" sizes keep source order.
- `default_size` = Grande if offered, else the first size.

`nutrition.min.json` (client) trims this to `{ milk_choices, deltas, drinks{…} }`.

## The calorie model — additive lookup

Mirrors the original server logic (`starbucks-calculator-ARCHITECTURE.md §3`):

```
total(drink, size, selections) = BASE[drink][size]            ← real, scraped
                               + Σ DELTA[option] (size-scaled where volumetric)
```

`BASE` already includes the drink's default recipe (default milk + shots), so with no changes
the calculator output **equals the published base** for that size.

### Estimated deltas (`src/prepare_data.py`)

⚠️ The source API never exposed per-option nutrition, so deltas are **documented estimates**,
labelled "estimated" everywhere in the UI (`BUILD-SPEC.md §9`).

| Group | Model | Example (Grande reference) |
|---|---|---|
| `milk` | `[cal, fat, carbs, sugar, protein]`, contribution per milk; swap effect = `(new − default) × size_factor` | Oatmilk `[120,5,16,7,3]`, 2% `[100,4,9,9,7]` |
| `addons` | volumetric, `× size_factor` | Whipped Cream `[80,7,6,5,1]`, Cold Foam `[55,3,5,5,1]` |
| `syrup_pump` | per-pump, fixed | `[20,0,5,5,0]` |
| `shot` | per-shot, fixed | `+5 cal`, `+75 mg` caffeine |

`size_factor = size_oz / 16`. Volumetric items (milk, whip, foam) scale with cup size; pumps
and shots are per-unit. `MILK_CHOICES` is the subset of milks offered as quick-swap chips.

### Engine (`calc.js → compute()`)

1. Start from `base[size]`.
2. Apply milk swap delta `(milk[new] − milk[default]) × factor`.
3. Add `syrup_pump × pumps`.
4. Add shots (`calories`, `caffeine`).
5. Add each active add-on `× factor`.
6. Clamp ≥ 0; round calories/mg to integers, grams to 1 decimal.

Verified: default == base; +Oatmilk +20 cal; +2 syrup +40; +shot +5 cal/+75 mg; +whip +80;
Short milk swap scales to half. (`BUILD-LOG.md`.)

## Adding / correcting data

- **New drink or fixed macros:** edit `data/nutrition_full.json`, rebuild. Slug auto-derives.
- **Tune a delta estimate:** edit `MILK_DELTAS` / `DELTAS` in `src/prepare_data.py`.
- **Exact per-drink deltas (future):** measure the source `calculate` endpoint per option and
  store per-drink deltas; the engine already supports a richer table.
