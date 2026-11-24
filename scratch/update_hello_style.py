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
nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_s.text).group(1)

with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

theme_header = """/*
Theme Name: Hello Elementor
Theme URI: https://elementor.com/hello-theme/?utm_source=wp-themes&utm_campaign=theme-uri&utm_medium=wp-dash
Description: A plain-vanilla & lightweight theme for Elementor page builder
Author: Elementor Team
Author URI: https://elementor.com/?utm_source=wp-themes&utm_campaign=author-uri&utm_medium=wp-dash
Version: 3.5.1
Text Domain: hello-elementor
*/

"""

full_style = theme_header + css_content

post_data = {
    'nonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=style.css&theme=hello-elementor',
    'action': 'update',
    'file': 'style.css',
    'theme': 'hello-elementor',
    'newcontent': full_style,
    'submit': 'Update File'
}

r_post = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data)
success = "File edited successfully" in r_post.text or "file-edited-successfully" in r_post.url
print("Updated hello-elementor/style.css:", success)

# Verify public stylesheet URL
r_check = session.get("https://boloupgo.app/wp-content/themes/hello-elementor/style.css")
print("Public style.css status:", r_check.status_code, "Length:", len(r_check.text), "Has --color-primary:", "--color-primary" in r_check.text)

