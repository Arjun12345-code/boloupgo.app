import requests
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

r_s = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor")
print("style.css in theme editor status:", r_s.status_code)
nonce_match = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_s.text)
print("style.css editor nonce:", nonce_match.group(1) if nonce_match else "None")

