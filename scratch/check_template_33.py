import requests
import re
import json

session = requests.Session()
login_url = 'https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
})

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

# Check template 33
r = session.get("https://boloupgo.app/wp-json/wp/v2/templates/33", headers=headers)
if r.status_code != 200:
    r = session.get("https://boloupgo.app/wp-json/wp/v2/posts/33", headers=headers)
if r.status_code != 200:
    r = session.get("https://boloupgo.app/wp-json/wp/v2/elementor_library/33", headers=headers)

print("Template 33 status:", r.status_code)
if r.status_code == 200:
    print("Title:", r.json().get('title'))
    content = r.json().get('content', {}).get('rendered', '')
    print("Content preview:", content[:300])

