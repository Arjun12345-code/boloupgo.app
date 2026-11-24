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

r_kit = session.get("https://boloupgo.app/wp-json/wp/v2/elementor_library/6?context=edit", headers=headers)
print("Kit 6 status:", r_kit.status_code)
if r_kit.status_code == 200:
    kit_data = r_kit.json()
    print("Kit title:", kit_data.get('title'))
    print("Kit meta keys:", list(kit_data.get('meta', {}).keys()))
    settings = kit_data.get('meta', {}).get('_elementor_page_settings')
    print("Kit _elementor_page_settings type:", type(settings))
    if isinstance(settings, str):
        try:
            settings = json.loads(settings)
        except:
            pass
    if isinstance(settings, dict):
        print("Settings keys:", list(settings.keys()))
        print("Existing custom_css length:", len(settings.get('custom_css', '')))

