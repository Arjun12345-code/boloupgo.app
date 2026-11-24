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

r_f = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=footer.php&theme=hello-elementor")
nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_f.text).group(1)

with open("footer.html", "r", encoding="utf-8") as f:
    footer_component = f.read()

new_footer_php = f"""<?php
/**
 * The template for displaying the footer.
 *
 * @package HelloElementor
 */
if ( ! defined( 'ABSPATH' ) ) {{
	exit; // Exit if accessed directly.
}}
?>

{footer_component}

<?php wp_footer(); ?>
</body>
</html>
"""

post_data = {
    'nonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=footer.php&theme=hello-elementor',
    'action': 'update',
    'file': 'footer.php',
    'theme': 'hello-elementor',
    'newcontent': new_footer_php,
    'submit': 'Update File'
}

r_post = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data)
success = "File edited successfully" in r_post.text or "file-edited-successfully" in r_post.url
print("Updated hello-elementor/footer.php:", success)

