from inspect_site import session
import re

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r_set = session.post("https://boloupgo.app/wp-json/wp/v2/settings", headers=headers, json={
    "site_icon": 31
})
print("Set site_icon status:", r_set.status_code)
print("Updated settings site_icon:", r_set.json().get('site_icon') if r_set.status_code == 200 else r_set.text[:200])

# Trigger cache flush
r_flush = session.get("https://boloupgo.app/?boloup_fix_all=1")
print("Cache flush triggered:", r_flush.status_code)

