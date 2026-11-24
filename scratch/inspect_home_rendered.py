import requests
import re

r = requests.get("https://boloupgo.app/")
with open("scratch/home_rendered.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Saved scratch/home_rendered.html")

# Check what header and footer are rendered
print("Header section in HTML:")
header_matches = re.findall(r'<header[^>]*>.*?</header>', r.text, re.DOTALL)
for hm in header_matches:
    print("Header match:", hm[:200])

print("Footer section in HTML:")
footer_matches = re.findall(r'<footer[^>]*>.*?</footer>', r.text, re.DOTALL)
for fm in footer_matches:
    print("Footer match:", fm[:200])

# Check for elementor widgets
print("Elementor widgets found:", len(re.findall(r'elementor-widget', r.text)))

