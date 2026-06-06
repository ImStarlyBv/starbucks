import urllib.request, urllib.parse, sys, http.cookiejar, json, re, time
sys.stdout.reconfigure(encoding='utf-8')

cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', 'Mozilla/5.0 Chrome/120'),
                 ('Referer', 'https://starbucks-calorie-calculator.com/starbucks-nutrition-calculator/'),
                 ('X-Requested-With', 'XMLHttpRequest')]
URL = 'https://starbucks-calorie-calculator.com/wp-admin/admin-ajax.php'
NS, NC = '4ab28d42dc', '1307f6bb62'

def post(d, tries=3):
    for i in range(tries):
        try:
            return op.open(urllib.request.Request(URL, data=urllib.parse.urlencode(d).encode()), timeout=30).read().decode('utf-8', 'ignore')
        except Exception as e:
            if i == tries - 1:
                return json.dumps({'error': str(e)})
            time.sleep(1.5)

def norm(k):
    return re.sub(r'\s+', '-', k.replace('&', 'and')).lower()

def preload(inc):
    pre = {}
    if not isinstance(inc, dict):
        return pre
    for k, v in inc.items():
        nk = norm(k)
        if isinstance(v, dict):
            pre[nk] = dict(v)
        else:
            pre.setdefault(nk, {})[v] = 1
    return pre

FIELDS = {
    'Calories': 'calories', 'Calories from fat': 'cal_from_fat', 'Total Fat': 'fat',
    'Saturated Fat': 'sat_fat', 'Trans Fat': 'trans_fat', 'Cholesterol': 'cholesterol',
    'Sodium': 'sodium', 'Total Carbohydrates': 'carbs', 'Dietary Fiber': 'fiber',
    'Sugars': 'sugar', 'Protein': 'protein', 'Caffeine': 'caffeine',
}

def parse_nutrition(html):
    out = {}
    for row in re.findall(r'<tr>(.*?)</tr>', html, re.S):
        cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.S)]
        if len(cells) >= 2 and cells[0] in FIELDS:
            out[FIELDS[cells[0]]] = cells[1]
    return out

op.open('https://starbucks-calorie-calculator.com/starbucks-nutrition-calculator/', timeout=30).read()
import html as H
prod = json.load(open('_products.json', encoding='utf-8'))
results = {}
total = sum(1 for rows in prod.values() for r in rows if H.unescape(r['name']).startswith(' '))
done = 0
for cat, rows in prod.items():
    for r in rows:
        raw = H.unescape(r['name'])
        if not raw.startswith(' '):
            continue
        name = raw.strip()
        try:
            sz = json.loads(post({'action': 'get_sizes', 'product_name': name, '_wpnonce': NS}))
            sizes = sz.get('sizes', []) if isinstance(sz, dict) else []
        except Exception:
            sizes = []
        entry = {'category': cat, 'is_new': bool(r.get('is_new')), 'sizes': {}, 'defaults': {}}
        for s in sizes:
            label = s['size']
            inc = s.get('included_customizations', {})
            if not isinstance(inc, dict):
                inc = {}
            entry['defaults'][label] = inc
            de = {'preloaded': preload(inc), 'customized': {}}
            cr = post({'action': 'calculate', 'formData[product_name]': name, 'formData[size]': label,
                       'formData[customizations]': json.dumps(de, ensure_ascii=False), '_wpnonce': NC})
            try:
                j = json.loads(cr)
                nut = parse_nutrition(j.get('html', ''))
                nut['total'] = j.get('totalCalories')
                entry['sizes'][label] = nut
            except Exception:
                entry['sizes'][label] = None
            time.sleep(0.12)
        results[name] = entry
        done += 1
        if done % 20 == 0:
            print(f'{done}/{total}', flush=True)
            json.dump(results, open('_nutrition_full.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        time.sleep(0.08)
json.dump(results, open('_nutrition_full.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('FINISHED', done, flush=True)
