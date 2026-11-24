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

r_f = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor")
content_match = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r_f.text, re.DOTALL)
if content_match:
    from html import unescape
    raw_content = unescape(content_match.group(1))
    with open("scratch/hello_functions_original.php", "w", encoding="utf-8") as out:
        out.write(raw_content)
    print("Saved scratch/hello_functions_original.php, length:", len(raw_content))
else:
    print("Could not find textarea")

