import requests
import re
import json

login_url = "https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
})

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce_match = re.search(r'"nonce":"([^"]+)"', admin_res.text)
nonce = nonce_match.group(1) if nonce_match else None
headers = {'X-WP-Nonce': nonce}

# Check existing pages
r_pages = session.get("https://boloupgo.app/wp-json/wp/v2/pages?per_page=100", headers=headers)
print("Existing pages:", [(p['id'], p['slug'], p['title']['rendered']) for p in r_pages.json()])

# Check theme mods / customizer or options
r_settings = session.get("https://boloupgo.app/wp-json/wp/v2/settings", headers=headers)
print("Settings status:", r_settings.status_code)
if r_settings.status_code == 200:
    s_data = r_settings.json()
    print("Site title:", s_data.get('title'))
    print("Site description:", s_data.get('description'))
    print("Page on front:", s_data.get('page_on_front'))
    print("Show on front:", s_data.get('show_on_front'))

