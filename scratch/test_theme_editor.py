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

r_editor = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor")
print("Theme editor status:", r_editor.status_code)
nonce_match = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_editor.text)
print("Theme editor nonce found:", nonce_match.group(1) if nonce_match else "None")

