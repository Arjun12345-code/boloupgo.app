import requests
import re

session = requests.Session()
login_url = 'https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.get(login_url)

login_data = {
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
}

r = session.post(login_url, data=login_data)
print("Login status:", r.status_code)

editor_url = 'https://boloupgo.app/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor'
r = session.get(editor_url)
m = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
if m:
    import html
    code = html.unescape(m.group(1))
    with open('scratch/live_functions.php', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Saved scratch/live_functions.php, length:", len(code))
else:
    print("Could not find textarea for functions.php")
