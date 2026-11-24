import re

with open("scratch/live_front.html", "r", encoding="utf-8") as f:
    html = f.read()

# Look for data-elementor-id or elementor elementor-XX
el_ids = re.findall(r'data-elementor-id="(\d+)"', html)
print("data-elementor-id found:", el_ids)

el_classes = re.findall(r'elementor-(\d+)', html)
print("elementor-{id} classes found:", list(set(el_classes)))

# Check body classes
body_match = re.search(r'<body[^>]*class="([^"]*)"', html)
if body_match:
    print("Body classes:", body_match.group(1))

