import requests
import re
from inspect_site import session

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r_p34 = session.get("https://boloupgo.app/wp-json/wp/v2/pages/34?context=edit", headers=headers)
p34_data = r_p34.json()
print("Page 34 content rendered len:", len(p34_data.get('content', {}).get('raw', '')))
print("Page 34 content raw:", p34_data.get('content', {}).get('raw', '')[:400])

