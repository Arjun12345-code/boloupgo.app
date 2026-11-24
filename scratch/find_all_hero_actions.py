import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    print(f"=== {f} ===")
    for m in re.finditer(r'<div[^>]*class="[^"]*hero-actions[^"]*"[^>]*>', c):
        start = max(0, m.start() - 100)
        end = min(len(c), m.end() + 100)
        print(c[start:end])
        print("-" * 30)

