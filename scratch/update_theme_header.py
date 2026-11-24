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
nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_h.text).group(1)

with open("header.html", "r", encoding="utf-8") as f:
    header_component = f.read()

new_header_php = f"""<?php
/**
 * The template for displaying the header
 *
 * @package HelloElementor
 */
if ( ! defined( 'ABSPATH' ) ) {{
	exit; // Exit if accessed directly.
}}

$viewport_content = apply_filters( 'hello_elementor_viewport_content', 'width=device-width, initial-scale=1' );
?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="<?php echo esc_attr( $viewport_content ); ?>">
	<link rel="profile" href="https://gmpg.org/xfn/11">
	<link rel="stylesheet" href="/style.css">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

{header_component}
"""

post_data = {
    'nonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=header.php&theme=hello-elementor',
    'action': 'update',
    'file': 'header.php',
    'theme': 'hello-elementor',
    'newcontent': new_header_php,
    'submit': 'Update File'
}

r_post = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data)
success = "File edited successfully" in r_post.text or "file-edited-successfully" in r_post.url
print("Updated hello-elementor/header.php:", success)

