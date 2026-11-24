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

# Check Elementor Pro Theme Builder conditions in options or AJAX
r_theme_builder = session.get("https://boloupgo.app/wp-admin/admin.php?page=elementor-app#/site-editor")
print("Theme builder page status:", r_theme_builder.status_code)
# Search for nonce or config
config_match = re.search(r'elementorCommon\s*=\s*({.*?});', r_theme_builder.text)
if config_match:
    print("elementorCommon config found")

# Check template 32 meta
r_t32 = session.get("https://boloupgo.app/wp-json/wp/v2/elementor_library/32?context=edit", headers=headers)
print("Template 32 status:", r_t32.status_code)
if r_t32.status_code == 200:
    print("Template 32 meta keys:", r_t32.json().get('meta', {}).keys())
    print("Template 32 _elementor_conditions:", r_t32.json().get('meta', {}).get('_elementor_conditions'))

