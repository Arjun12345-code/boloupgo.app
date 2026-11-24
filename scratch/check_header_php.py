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

r_h = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=header.php&theme=hello-elementor")
content_match = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r_h.text, re.DOTALL)
from html import unescape
if content_match:
    print("header.php content:")
    print(unescape(content_match.group(1)))

