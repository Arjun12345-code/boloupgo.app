import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    styles = re.findall(r'style="([^"]*)"', c)
    if styles:
        print(f"=== {f} has {len(styles)} inline styles ===")
        for s in styles:
            print(f"  style=\"{s}\"")

