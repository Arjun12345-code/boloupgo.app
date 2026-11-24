import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    head = re.search(r'<head>(.*?)</head>', c, re.DOTALL)
    if head:
        print(f"=== {f} HEAD ===")
        print(head.group(1).strip())

