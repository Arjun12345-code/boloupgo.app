import requests
import re
import base64

login_url = "https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
r_log = session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
})
print("Login status:", r_log.status_code)

# Helper to update theme files via theme-editor.php
def update_theme_file(filename, content):
    editor_url = f"https://boloupgo.app/wp-admin/theme-editor.php?file={filename}&theme=hello-elementor"
    r_get = session.get(editor_url)
    m = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_get.text)
    if not m:
        print(f"Failed to find nonce for {filename}")
        return False
    nonce = m.group(1)
    post_data = {
        'nonce': nonce,
        '_wp_http_referer': f'/wp-admin/theme-editor.php?file={filename}&theme=hello-elementor',
        'action': 'update',
        'file': filename,
        'theme': 'hello-elementor',
        'newcontent': content,
        'submit': 'Update File'
    }
    r_post = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data)
    success = "File edited successfully" in r_post.text or "file-edited-successfully" in r_post.url
    print(f"Updated hello-elementor/{filename}: {success}")
    return success

# 1. Update style.css
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
update_theme_file("style.css", theme_header + css_content)

# 2. Update header.php
with open("header.html", "r", encoding="utf-8") as f:
    header_html = f.read()

header_php = f"""<?php
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
	<link rel="shortcut icon" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png">
	<link rel="icon" type="image/x-icon" href="/favicon.ico">
	<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png">
	<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png">
	<link rel="apple-touch-icon" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

{header_html}
"""
update_theme_file("header.php", header_php)

# 3. Update footer.php
with open("footer.html", "r", encoding="utf-8") as f:
    footer_html = f.read()

footer_php = f"""<?php
/**
 * The template for displaying the footer.
 *
 * @package HelloElementor
 */
if ( ! defined( 'ABSPATH' ) ) {{
	exit; // Exit if accessed directly.
}}
?>

{footer_html}

<?php wp_footer(); ?>
</body>
</html>
"""
update_theme_file("footer.php", footer_php)

# 4. Read favicon_b64.txt
with open("scratch/favicon_b64.txt", "r", encoding="ascii") as f:
    ico_b64 = f.read().strip()

# 5. Read current live_functions.php and inject favicon creation & handlers
with open("scratch/live_functions.php", "r", encoding="utf-8") as f:
    func_text = f.read()

# Replace version '1.0.3' with '1.0.4'
func_text = func_text.replace("'1.0.3'", "'1.0.4'")

# Add favicon block before '// 2. Enqueue Custom CSS'
fav_block = f"""// 1b. Write physical favicon.ico and handle requests
add_action('init', function() {{
    $root_ico = ABSPATH . 'favicon.ico';
    $ico_data = base64_decode('{ico_b64}');
    if (!file_exists($root_ico) || filesize($root_ico) !== strlen($ico_data)) {{
        @file_put_contents($root_ico, $ico_data);
    }}
    if (get_option('site_icon') != 31) {{
        update_option('site_icon', 31);
    }}
    if (isset($_SERVER['REQUEST_URI']) && parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH) === '/favicon.ico') {{
        if (file_exists($root_ico)) {{
            header('Content-Type: image/x-icon');
            header('Content-Length: ' . filesize($root_ico));
            header('Cache-Control: public, max-age=86400');
            readfile($root_ico);
            exit;
        }} else {{
            wp_redirect('https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png', 301);
            exit;
        }}
    }}
}}, 1);

add_action('wp_head', function() {{
    echo '<link rel="shortcut icon" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png">' . "\\n";
    echo '<link rel="icon" type="image/x-icon" href="/favicon.ico">' . "\\n";
    echo '<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png">' . "\\n";
    echo '<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png">' . "\\n";
    echo '<link rel="apple-touch-icon" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png">' . "\\n";
}}, 1);

"""

if '// 1b. Write physical favicon.ico' not in func_text:
    target_str = "// 2. Enqueue Custom CSS"
    func_text = func_text.replace(target_str, fav_block + target_str)

update_theme_file("functions.php", func_text)

print("Theme files updated successfully!")

