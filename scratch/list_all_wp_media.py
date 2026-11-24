from inspect_site import session
import re

admin_res = session.get('https://boloupgo.app/wp-admin/')
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}
r = session.get('https://boloupgo.app/wp-json/wp/v2/media?per_page=100', headers=headers)
for m in r.json():
    print(f"{m['id']}: {m['slug']} -> {m['source_url']}")

