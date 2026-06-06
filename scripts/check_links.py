import re, glob, os, posixpath, sys

DIST = os.path.join(os.path.dirname(__file__), "..", "dist")
os.chdir(DIST)
pages = glob.glob("**/*.html", recursive=True)
bad = []
checked = 0
for p in pages:
    pp = p.replace(os.sep, "/")
    d = posixpath.dirname(pp)
    html = open(p, encoding="utf-8").read()
    for href in re.findall(r'href="([^"#?]+)"', html):
        if href.startswith(("http", "mailto:", "//")):
            continue
        checked += 1
        tgt = href.lstrip("/") if href.startswith("/") else posixpath.normpath(posixpath.join(d, href))
        if tgt.endswith((".html", ".css", ".js", ".json", ".svg", ".xml", ".webmanifest")):
            cands = [tgt]
        else:
            cands = [tgt, posixpath.join(tgt, "index.html")]
        if not any(os.path.exists(c) for c in cands):
            bad.append((pp, href, tgt))

print(f"pages: {len(pages)} | links checked: {checked} | broken: {len(bad)}")
for b in bad[:30]:
    print("  BROKEN", b)
sys.exit(1 if bad else 0)
