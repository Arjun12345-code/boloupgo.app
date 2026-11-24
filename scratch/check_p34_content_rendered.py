from inspect_site import session
import re, json

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r = session.get("https://boloupgo.app/wp-json/wp/v2/pages/34?context=edit", headers=headers)
p = r.json()
print("content rendered len:", len(p.get('content', {}).get('rendered', '')))
print("content rendered has nobg:", 'boloupgo-app-nobg.png' in p.get('content', {}).get('rendered', ''))
print("content rendered has hero:", 'boloupgo-hero.png' in p.get('content', {}).get('rendered', ''))
print("content raw len:", len(p.get('content', {}).get('raw', '')))
print("content raw has nobg:", 'boloupgo-app-nobg.png' in p.get('content', {}).get('raw', ''))
print("content raw has hero:", 'boloupgo-hero.png' in p.get('content', {}).get('raw', ''))

