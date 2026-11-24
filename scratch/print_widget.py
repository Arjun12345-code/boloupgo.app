import requests
import re

r = requests.get("https://boloupgo.app/?nocache=1")
widget_match = re.search(r'data-widget_type="html.default">(.*?)</div>\s*</div>\s*</div>', r.text, re.DOTALL)
if widget_match:
    print("Widget start (1000 chars):")
    print(widget_match.group(1)[:1000])
    print("\nWidget end (1000 chars):")
    print(widget_match.group(1)[-1000:])
else:
    print("Widget match not found directly, looking for section:")
    sec = re.findall(r'<section[^>]*id="([^"]+)"', r.text)
    print("Sections found:", sec)

