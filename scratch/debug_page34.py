from inspect_site import session
import re, json

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r = session.get("https://boloupgo.app/wp-json/wp/v2/pages/34?context=edit", headers=headers)
p = r.json()
el = p.get('meta', {}).get('_elementor_data', '')
print('Type of el:', type(el))
if isinstance(el, str):
    parsed = json.loads(el)
else:
    parsed = el

print("Length of parsed elements:", len(parsed))

def search_text(obj, target):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if target in str(v):
                print(f"Target '{target}' found in key '{k}': {str(v)[:150]}")
            search_text(v, target)
    elif isinstance(obj, list):
        for item in obj:
            search_text(item, target)

print("--- Searching for boloupgo-app-nobg.png ---")
search_text(parsed, "boloupgo-app-nobg.png")

print("--- Searching for boloupgo-hero.png ---")
search_text(parsed, "boloupgo-hero.png")

