import requests
import json
import re

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

with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

r_kit = session.get("https://boloupgo.app/wp-json/wp/v2/elementor_library/6?context=edit", headers=headers)
if r_kit.status_code == 200:
    kit_data = r_kit.json()
    meta = kit_data.get('meta', {})
    page_settings = meta.get('_elementor_page_settings') or {}
    if isinstance(page_settings, str):
        try:
            page_settings = json.loads(page_settings)
        except:
            page_settings = {}
    
    page_settings['custom_css'] = css_content
    
    update_data = {
        "meta": {
            "_elementor_page_settings": page_settings
        }
    }
    
    r_update = session.post("https://boloupgo.app/wp-json/wp/v2/elementor_library/6", headers=headers, json=update_data)
    print("Update Kit 6 status:", r_update.status_code)
    if r_update.status_code == 200:
        print("Successfully updated Kit 6 custom_css! (length:", len(css_content), "chars)")
    else:
        print("Update failed:", r_update.text[:300])
else:
    print("Failed to fetch Kit 6:", r_kit.status_code)

