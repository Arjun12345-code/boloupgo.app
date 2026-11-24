import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    cta_matches = re.findall(r'<section[^>]*class="[^"]*cta[^"]*"[^>]*>.*?</section>', c, re.DOTALL)
    for m in cta_matches:
        print(f"=== {f} ===")
        print(m[:400])
        print("...")

