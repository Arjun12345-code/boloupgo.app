from inspect_site import session
import re
import json

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

# Check page 34
r_p34 = session.get("https://boloupgo.app/wp-json/wp/v2/pages/34?context=edit", headers=headers)
p34 = r_p34.json()
el = p34.get('meta', {}).get('_elementor_data', '')

print("Is boloupgo-hero.png in page 34 _elementor_data?", "boloupgo-hero.png" in el)
print("Is boloupgo-app-nobg.png in page 34 _elementor_data?", "boloupgo-app-nobg.png" in el)

# Check all elementor library templates
r_el = session.get("https://boloupgo.app/wp-json/wp/v2/elementor_library?per_page=100", headers=headers)
for t in r_el.json():
    t_id = t['id']
    r_t = session.get(f"https://boloupgo.app/wp-json/wp/v2/elementor_library/{t_id}?context=edit", headers=headers)
    t_data = r_t.json().get('meta', {}).get('_elementor_data', '')
    if "boloupgo-hero.png" in str(t_data):
        print(f"Found in elementor_library ID {t_id} ({t['title']['rendered']})")

# Check all pages
r_pages = session.get("https://boloupgo.app/wp-json/wp/v2/pages?per_page=100", headers=headers)
for p in r_pages.json():
    pid = p['id']
    r_p = session.get(f"https://boloupgo.app/wp-json/wp/v2/pages/{pid}?context=edit", headers=headers)
    p_data = r_p.json().get('meta', {}).get('_elementor_data', '')
    if "boloupgo-hero.png" in str(p_data):
        print(f"Found in Page ID {pid} ({p['title']['rendered']})")

