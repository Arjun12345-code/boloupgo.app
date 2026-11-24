import requests
import re
from inspect_site import session

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r_t33 = session.get("https://boloupgo.app/wp-json/wp/v2/elementor_library/33?context=edit", headers=headers)
print("Template 33 _elementor_conditions:", r_t33.json().get('meta', {}).get('_elementor_conditions'))

