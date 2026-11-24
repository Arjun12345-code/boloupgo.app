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
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r_p34 = session.get("https://boloupgo.app/wp-json/wp/v2/pages/34?context=edit", headers=headers)
p34_meta = r_p34.json().get('meta', {})
el_data = p34_meta.get('_elementor_data', '')
data_obj = json.loads(el_data)
html_str = data_obj[0]['elements'][0]['elements'][0]['settings']['html']
print("Start of html_str in page 34:")
print(html_str[:400])
print("\nEnd of html_str in page 34:")
print(html_str[-400:])

