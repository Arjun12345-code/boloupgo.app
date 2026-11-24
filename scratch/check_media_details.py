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

r = session.get("https://boloupgo.app/wp-json/wp/v2/media/31", headers=headers)
print("Media 31 status:", r.status_code)
if r.status_code == 200:
    data = r.json()
    print("Media 31 title:", data.get('title'))
    print("Media 31 source_url:", data.get('source_url'))
    print("Media 31 media_details:", json.dumps(data.get('media_details'), indent=2))

