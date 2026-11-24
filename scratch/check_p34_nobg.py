from inspect_site import session
import json
import re

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r = session.get("https://boloupgo.app/wp-json/wp/v2/pages/34?context=edit", headers=headers)
p = r.json()
el = p.get('meta', {}).get('_elementor_data')
print("Has boloupgo-app-nobg.png in _elementor_data?", "boloupgo-app-nobg.png" in str(el))
print("Has boloupgo-app-nobg.png in post_content?", "boloupgo-app-nobg.png" in p.get('content', {}).get('raw', ''))
print("post_content len:", len(p.get('content', {}).get('raw', '')))

