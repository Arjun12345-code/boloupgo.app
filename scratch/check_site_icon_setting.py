from inspect_site import session
import re

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r = session.get("https://boloupgo.app/wp-json/wp/v2/settings", headers=headers)
settings = r.json()
print("site_icon:", settings.get('site_icon'))
print("site_logo:", settings.get('site_logo'))

