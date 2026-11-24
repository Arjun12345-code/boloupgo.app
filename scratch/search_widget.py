from inspect_site import session

r = session.get("https://boloupgo.app/")
print("Is 'logo-samping' in r.text?", "logo-samping" in r.text)
print("Is 'BoloUp Go Official - Header' in r.text?", "BoloUp Go Official - Header" in r.text)
print("Is 'elementor-element-home_widget' in r.text?", "elementor-element-home_widget" in r.text)
# Let's print everything inside elementor-element-home_widget
import re
match = re.search(r'<div class="elementor-element elementor-element-home_widget[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*</div>', r.text, re.DOTALL)
if match:
    print("Match found, len:", len(match.group(1)))
    print("Starts with:", match.group(1)[:500])
else:
    print("No match for elementor-element-home_widget")

