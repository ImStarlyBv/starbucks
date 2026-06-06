/* NutriBucks calculator engine + progressive enhancement.
 * Vanilla ES module, no dependencies. Deferred — never blocks render.
 *
 * The additive model mirrors the source's server logic (see
 * docs/starbucks-calculator-ARCHITECTURE.md): total = BASE[size] + Σ deltas.
 * BASE values are real; customization deltas are estimated (labelled in UI).
 */

const MACRO_KEYS = ["calories", "fat", "carbs", "sugar", "protein"];
const TABLE_FIELDS = [
  ["calories", "Calories", ""], ["fat", "Total Fat", "g"], ["sat_fat", "Sat. Fat", "g"],
  ["carbs", "Carbs", "g"], ["fiber", "Fiber", "g"], ["sugar", "Sugar", "g"],
  ["protein", "Protein", "g"], ["sodium", "Sodium", "mg"],
  ["cholesterol", "Cholesterol", "mg"], ["caffeine", "Caffeine", "mg"],
];
const PANEL = [
  ["calories", "Calories", "", 500], ["fat", "Total fat", "g", 30],
  ["sugar", "Sugar", "g", 60], ["caffeine", "Caffeine", "mg", 400],
];
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const sizeOz = (label) => { const m = String(label).match(/([\d.]+)\s*fl oz/); return m ? parseFloat(m[1]) : 16; };
const r1 = (n) => { const v = Math.round(n * 10) / 10; return Number.isInteger(v) ? v : v; };

/* ---- Core additive model ------------------------------------------------ */
function compute(drink, state, deltas) {
  const base = drink.base[state.size] || {};
  const out = { ...base };
  const factor = sizeOz(state.size) / 16; // volume scaling for milk/whip/foam
  const milkNew = deltas.milk[state.milk] || [0, 0, 0, 0, 0];
  const milkDef = deltas.milk[drink.default_milk] || [0, 0, 0, 0, 0];
  MACRO_KEYS.forEach((k, i) => { out[k] = (out[k] || 0) + (milkNew[i] - milkDef[i]) * factor; });

  const sp = deltas.syrup_pump;
  MACRO_KEYS.forEach((k, i) => { out[k] += sp[i] * (state.syrup || 0); });

  out.calories += deltas.shot.calories * (state.shot || 0);
  out.caffeine = (out.caffeine || 0) + deltas.shot.caffeine * (state.shot || 0);

  (state.addons || []).forEach((name) => {
    const a = deltas.addons[name];
    if (a) MACRO_KEYS.forEach((k, i) => { out[k] += a[i] * factor; });
  });

  for (const k in out) out[k] = Math.max(0, k === "calories" || k.endsWith("ium") || k === "cholesterol" || k === "caffeine" ? Math.round(out[k]) : r1(out[k]));
  return out;
}

/* ---- Wire a drink calculator inside `root` ------------------------------ */
function initDrinkCalc(root, drink, deltas) {
  const state = {
    size: drink.default_size,
    milk: drink.default_milk,
    syrup: 0, shot: 0, addons: new Set(),
  };
  const ACTIVE = ["border-2", "border-primary", "bg-primary-fixed-dim", "text-on-primary-fixed"];
  const IDLE = ["border", "border-outline-variant", "bg-surface-container-lowest"];
  const setActive = (btn, on) => {
    btn.classList.remove(...(on ? IDLE : ACTIVE));
    btn.classList.add(...(on ? ACTIVE : IDLE));
  };

  function render() {
    const n = compute(drink, { ...state, addons: [...state.addons] }, deltas);
    root.querySelectorAll("[data-out]").forEach((el) => {
      const k = el.getAttribute("data-out");
      if (n[k] !== undefined) el.textContent = n[k];
    });
    root.querySelectorAll("[data-bar]").forEach((el) => {
      const k = el.getAttribute("data-bar");
      const max = parseFloat(el.getAttribute("data-max")) || 100;
      el.style.width = Math.min(100, ((n[k] || 0) / max) * 100) + "%";
    });
  }

  root.querySelectorAll("[data-size]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.size = btn.getAttribute("data-size");
      root.querySelectorAll("[data-size]").forEach((b) => setActive(b, b === btn));
      const lbl = root.querySelector("[data-size-label]");
      if (lbl) lbl.textContent = state.size;
      render();
    });
  });
  root.querySelectorAll("[data-milk]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.milk = btn.getAttribute("data-milk");
      root.querySelectorAll("[data-milk]").forEach((b) => setActive(b, b === btn));
      render();
    });
  });
  root.querySelectorAll("[data-step]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.getAttribute("data-step");
      const dir = parseInt(btn.getAttribute("data-dir"), 10);
      state[key] = Math.max(0, (state[key] || 0) + dir);
      const out = root.querySelector(`[data-count="${key}"]`);
      if (out) out.textContent = state[key];
      render();
    });
  });
  root.querySelectorAll("[data-toggle]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const name = btn.getAttribute("data-toggle");
      const on = !state.addons.has(name);
      if (on) state.addons.add(name); else state.addons.delete(name);
      setActive(btn, on);
      render();
    });
  });
  render();
}

/* ---- Build the calculator panel markup (standalone calculator page) ----- */
function panelHTML(drink, milkChoices, rel = "") {
  const b = drink.base[drink.default_size];
  const sizeBtns = drink.is_food ? "" : `
    <section class="space-y-3">
      <div class="flex items-center justify-between">
        <h2 class="font-label-md text-label-md text-primary uppercase tracking-widest">Select size</h2>
        <span class="text-caption text-secondary" data-size-label>${esc(drink.default_size)}</span>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
        ${drink.sizes.map((s) => `<button type="button" data-size="${esc(s)}" class="p-3 rounded-xl ${s === drink.default_size ? "border-2 border-primary bg-primary-fixed-dim text-on-primary-fixed" : "border border-outline-variant bg-surface-container-lowest"} hover:border-primary transition-all flex flex-col items-center gap-1"><span class="material-symbols-outlined" aria-hidden="true">local_cafe</span><span class="font-label-md text-center leading-tight">${esc(s.split("(")[0])}</span></button>`).join("")}
      </div>
    </section>
    <section class="space-y-3">
      <h2 class="font-label-md text-label-md text-primary uppercase tracking-widest">Milk</h2>
      <div class="flex flex-wrap gap-2">
        ${milkChoices.map((m) => `<button type="button" data-milk="${esc(m)}" class="px-4 py-2 rounded-full font-label-md text-sm transition-all ${m === drink.default_milk ? "border-2 border-primary bg-primary-fixed-dim text-on-primary-fixed" : "border border-outline-variant bg-surface-container-lowest hover:border-primary"}">${esc(m.split("(")[0])}</button>`).join("")}
      </div>
    </section>
    <section class="space-y-3">
      <h2 class="font-label-md text-label-md text-primary uppercase tracking-widest">Customize</h2>
      ${["syrup", "shot"].map((k) => `<div class="flex items-center justify-between p-4 bg-surface-container rounded-xl"><div><p class="font-label-md text-on-surface">${k === "syrup" ? "Flavored syrup" : "Extra espresso shot"}</p><p class="text-caption text-secondary">${k === "syrup" ? "~20 kcal per pump (estimated)" : "+5 kcal, +75 mg caffeine each"}</p></div><div class="flex items-center gap-3"><button type="button" data-step="${k}" data-dir="-1" aria-label="Decrease" class="w-8 h-8 rounded-full border border-primary text-primary hover:bg-primary hover:text-white transition-colors">−</button><span class="font-headline-md w-6 text-center" data-count="${k}">0</span><button type="button" data-step="${k}" data-dir="1" aria-label="Increase" class="w-8 h-8 rounded-full border border-primary text-primary hover:bg-primary hover:text-white transition-colors">+</button></div></div>`).join("")}
      <div class="flex flex-wrap gap-2 pt-1">
        <button type="button" data-toggle="Whipped Cream" class="px-4 py-2 rounded-full border border-outline-variant bg-surface-container-lowest font-label-md text-sm hover:border-primary transition-all">+ Whipped cream</button>
        <button type="button" data-toggle="Cold Foam" class="px-4 py-2 rounded-full border border-outline-variant bg-surface-container-lowest font-label-md text-sm hover:border-primary transition-all">+ Cold foam</button>
      </div>
    </section>`;

  const panel = `
    <section class="bg-primary-container p-8 rounded-[2rem] text-on-primary-container shadow-xl">
      <h2 class="font-headline-md text-headline-md mb-6">Nutritional profile</h2>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
        ${PANEL.map(([k, label, unit, max]) => `<div class="space-y-1"><p class="text-caption opacity-80 uppercase font-semibold">${label}</p><p class="font-headline-md text-headline-md"><span data-out="${k}">${b[k]}</span>${unit}</p><div class="h-1 bg-on-primary-container/20 rounded-full overflow-hidden"><div class="h-full bg-primary-fixed rounded-full transition-all duration-500" data-bar="${k}" data-max="${max}" style="width:${Math.min(100, (b[k] / max) * 100)}%"></div></div></div>`).join("")}
      </div>
      <p class="text-caption opacity-80 mt-6">Estimated values · not affiliated with Starbucks.</p>
    </section>`;

  const table = `
    <section>
      <h2 class="font-headline-md text-headline-md text-primary mb-4">${esc(drink.name)} nutrition by size</h2>
      <div class="overflow-x-auto rounded-xl border border-outline-variant/50">
        <table class="w-full text-sm bg-white"><thead><tr class="bg-surface-container-high text-left"><th class="p-3 font-label-md text-primary">Nutrient</th>${drink.sizes.map((s) => `<th class="p-3 font-label-md text-primary whitespace-nowrap">${esc(s)}</th>`).join("")}</tr></thead>
        <tbody>${TABLE_FIELDS.map(([f, label, unit]) => `<tr class="border-t border-outline-variant/40"><th scope="row" class="p-3 text-left font-semibold text-on-surface-variant whitespace-nowrap">${label}</th>${drink.sizes.map((s) => `<td class="p-3 text-on-surface">${drink.base[s][f]}${unit}</td>`).join("")}</tr>`).join("")}</tbody></table>
      </div>
    </section>`;

  const hero = drink.image ? `<img src="${rel}${drink.image}" alt="${esc(drink.image_alt || drink.name)}" width="600" height="600" decoding="async" class="w-20 h-20 rounded-2xl object-cover shrink-0 shadow-sm">` : "";
  return `<div class="space-y-8">
    <header class="flex items-center gap-4">${hero}<div><span class="text-caption font-semibold uppercase tracking-wider text-secondary">${esc(drink.category)}</span>
      <h2 class="font-headline-lg text-headline-lg text-on-surface mt-1">${esc(drink.name)}</h2></div></header>
    ${sizeBtns}${panel}${table}
  </div>`;
}

/* ---- Home / global search (uses #search-index) -------------------------- */
function initSearch() {
  const form = document.querySelector("[data-home-search]");
  const idxEl = document.getElementById("search-index");
  if (!form || !idxEl) return;
  const input = form.querySelector("input[type=search]");
  const box = form.querySelector("[data-search-results]");
  let index = [];
  try { index = JSON.parse(idxEl.textContent); } catch { return; }
  const base = form.getAttribute("data-rel") || "";

  function run() {
    const q = input.value.trim().toLowerCase();
    if (q.length < 2) { box.classList.add("hidden"); box.innerHTML = ""; return; }
    const hits = index.filter((d) => d.n.toLowerCase().includes(q)).slice(0, 8);
    if (!hits.length) { box.innerHTML = `<p class="px-4 py-3 text-sm text-on-surface-variant">No matches for "${esc(q)}".</p>`; box.classList.remove("hidden"); return; }
    box.innerHTML = hits.map((d) => `<a href="${base}drink/${d.s}/" class="flex items-center justify-between gap-2 px-4 py-3 hover:bg-surface-container-low transition-colors"><span class="text-sm text-on-surface">${esc(d.n)}</span><span class="text-caption text-outline">${d.k} kcal</span></a>`).join("");
    box.classList.remove("hidden");
  }
  input.addEventListener("input", run);
  document.addEventListener("click", (e) => { if (!form.contains(e.target)) box.classList.add("hidden"); });
}

/* ---- Category page filter / sort --------------------------------------- */
function initCategoryFilter() {
  const scope = document.querySelector("[data-filter-scope]");
  if (!scope) return;
  const grid = scope.querySelector("[data-filter-grid]");
  const items = [...grid.children];
  const search = scope.querySelector("[data-filter-search]");
  const cal = scope.querySelector("[data-filter-cal]");
  const calOut = scope.querySelector("[data-cal-out]");
  const newOnly = scope.querySelector("[data-filter-new]");
  const sort = scope.querySelector("[data-filter-sort]");
  const count = scope.querySelector("[data-filter-count]");
  const empty = scope.querySelector("[data-filter-empty]");
  const meta = (el) => { const a = el.querySelector("a"); return { name: a.dataset.name || "", cal: +a.dataset.cal || 0, isNew: a.dataset.new === "1" }; };

  function apply() {
    const q = (search?.value || "").trim().toLowerCase();
    const maxCal = cal ? +cal.value : Infinity;
    if (calOut && cal) calOut.textContent = cal.value;
    let shown = 0;
    items.forEach((el) => {
      const m = meta(el);
      const ok = (!q || m.name.includes(q)) && m.cal <= maxCal && (!newOnly?.checked || m.isNew);
      el.style.display = ok ? "" : "none";
      if (ok) shown++;
    });
    if (sort && sort.value !== "name") {
      const dir = sort.value === "cal-asc" ? 1 : -1;
      [...items].sort((a, b) => (meta(a).cal - meta(b).cal) * dir).forEach((el) => grid.appendChild(el));
    } else {
      [...items].sort((a, b) => meta(a).name.localeCompare(meta(b).name)).forEach((el) => grid.appendChild(el));
    }
    if (count) count.textContent = `${shown} of ${items.length} shown`;
    if (empty) empty.classList.toggle("hidden", shown !== 0);
  }
  [search, cal, newOnly, sort].forEach((c) => c && c.addEventListener("input", apply));
  apply();
}

/* ---- Standalone calculator page ---------------------------------------- */
async function initCalculatorPage() {
  const wrap = document.querySelector("[data-calculator]");
  if (!wrap) return;
  const panel = wrap.querySelector("[data-calc-panel]");
  const list = wrap.querySelector("[data-picker-list]");
  const search = wrap.querySelector("[data-picker-search]");
  const rel = wrap.getAttribute("data-rel") || "";

  let data;
  try { data = await (await fetch(rel + "data/nutrition.min.json")).json(); }
  catch { return; } // links still work as a fallback

  function load(slug) {
    const drink = data.drinks[slug];
    if (!drink) return;
    panel.innerHTML = panelHTML(drink, data.milk_choices, wrap.getAttribute("data-rel") || "");
    initDrinkCalc(panel, drink, data.deltas);
    panel.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  list.querySelectorAll("a[data-slug]").forEach((a) => {
    a.addEventListener("click", (e) => { e.preventDefault(); load(a.getAttribute("data-slug")); });
  });
  // category chips
  const items = [...list.querySelectorAll("li")];
  wrap.querySelectorAll("[data-picker-cat]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const c = btn.getAttribute("data-picker-cat");
      wrap.querySelectorAll("[data-picker-cat]").forEach((b) => {
        const on = b === btn;
        b.classList.toggle("border-2", on); b.classList.toggle("border-primary", on);
        b.classList.toggle("bg-primary-fixed-dim", on); b.classList.toggle("text-on-primary-fixed", on);
        b.classList.toggle("border", !on); b.classList.toggle("border-outline-variant", !on); b.classList.toggle("bg-white", !on);
      });
      items.forEach((li) => { li.style.display = (c === "all" || li.dataset.cat === c) ? "" : "none"; });
    });
  });
  if (search) search.addEventListener("input", () => {
    const q = search.value.trim().toLowerCase();
    items.forEach((li) => { li.style.display = (!q || li.dataset.name.includes(q)) ? "" : "none"; });
  });

  // Deep link: ?drink=slug loads immediately
  const slug = new URLSearchParams(location.search).get("drink");
  if (slug && data.drinks[slug]) load(slug);
}

/* ---- Boot --------------------------------------------------------------- */
function boot() {
  // Drink page: self-contained payload (base + deltas + milk choices).
  const dd = document.getElementById("drink-data");
  if (dd) {
    try {
      const payload = JSON.parse(dd.textContent);
      initDrinkCalc(document, payload.drink, payload.deltas);
    } catch (e) { /* leave server-rendered defaults in place */ }
  }
  initSearch();
  initCategoryFilter();
  initCalculatorPage();
}

if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
else boot();
