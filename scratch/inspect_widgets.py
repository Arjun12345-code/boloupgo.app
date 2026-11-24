import requests
import re

r = requests.get("https://boloupgo.app/")
# Find where the elementor-widget-html is
widgets = re.findall(r'<div class="elementor-widget-container">(.*?)</div>', r.text, re.DOTALL)
print(f"Found {len(widgets)} widget containers")
for i, w in enumerate(widgets):
    print(f"Widget {i} length: {len(w)}")
    print(f"Widget {i} start: {w[:300]}")
    print(f"Widget {i} end: {w[-300:]}")

