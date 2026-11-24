import requests
import re
from html import unescape

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
nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_h.text).group(1)
content_match = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r_h.text, re.DOTALL)
header_code = unescape(content_match.group(1))

# Check if already has favicon
if 'cropped-boloup' not in header_code:
    icon_tags = """\t<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-150x150.png">\n\t<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-300x300.png">\n\t<link rel="apple-touch-icon" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-300x300.png">\n\t"""
    header_code = header_code.replace("<?php wp_head(); ?>", icon_tags + "<?php wp_head(); ?>")
    
    post_data = {
        'nonce': nonce,
        '_wp_http_referer': '/wp-admin/theme-editor.php?file=header.php&theme=hello-elementor',
        'action': 'update',
        'file': 'header.php',
        'theme': 'hello-elementor',
        'newcontent': header_code,
        'submit': 'Update File'
    }
    r_up = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data)
    print("Updated header.php:", "File edited successfully" in r_up.text or "file-edited-successfully" in r_up.url)
else:
    print("Favicon already in header.php")

# Trigger cache purge
session.get("https://boloupgo.app/?boloup_fix_all=1")

