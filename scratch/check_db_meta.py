from inspect_site import session
import re

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r_p34 = session.get("https://boloupgo.app/wp-json/wp/v2/pages/34?context=edit", headers=headers)
p34_json = r_p34.json()
el_data = p34_json.get('meta', {}).get('_elementor_data', '')
print("Actual _elementor_data length in DB:", len(el_data))
print("Start of _elementor_data:", el_data[:300])

