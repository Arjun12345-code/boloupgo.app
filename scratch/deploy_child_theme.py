import requests
import re
import json
import zipfile
import io

login_url = "https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
})

with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

theme_header = """/*
Theme Name: Hello Elementor Child - BoloUp Go
Theme URI: https://boloupgo.app/
Description: Custom high-conversion design for BoloUp Go
Author: BoloUp Go Development Team
Author URI: https://boloupgo.app/
Template: hello-elementor
Version: 1.0.0
Text Domain: hello-elementor-child
*/

"""

child_css = theme_header + css_content

functions_php = """<?php
/**
 * Hello Elementor Child Theme Functions
 * Enqueues sitewide style.css
 */

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-go-child-style',
        get_stylesheet_directory_uri() . '/style.css',
        array(),
        '1.0.0'
    );
}, 20);

// Disable WordPress default admin bar on front-end for clean view
add_filter('show_admin_bar', '__return_false');
"""

with open("header.html", "r", encoding="utf-8") as f:
    header_raw = f.read()
with open("footer.html", "r", encoding="utf-8") as f:
    footer_raw = f.read()

with open("index.html", "r", encoding="utf-8") as f:
    home_raw = f.read()
home_body = re.search(r'<body[^>]*>(.*?)</body>', home_raw, re.DOTALL)
home_body_content = home_body.group(1).strip() if home_body else home_raw

front_page_php = f"""<?php
/**
 * Front Page Template for BoloUp Go
 */
get_header();
?>
{header_raw}
<main>
{home_body_content}
</main>
{footer_raw}
<?php
get_footer();
"""

with open("host.html", "r", encoding="utf-8") as f:
    host_raw = f.read()
host_body = re.search(r'<body[^>]*>(.*?)</body>', host_raw, re.DOTALL)
host_body_content = host_body.group(1).strip() if host_body else host_raw

page_host_php = f"""<?php
/**
 * Template Name: BoloUp Go Host Page
 * Template Post Type: page
 */
get_header();
?>
{header_raw}
<main>
{host_body_content}
</main>
{footer_raw}
<?php
get_footer();
"""

with open("agent.html", "r", encoding="utf-8") as f:
    agent_raw = f.read()
agent_body = re.search(r'<body[^>]*>(.*?)</body>', agent_raw, re.DOTALL)
agent_body_content = agent_body.group(1).strip() if agent_body else agent_raw

page_agent_php = f"""<?php
/**
 * Template Name: BoloUp Go Agent Page
 * Template Post Type: page
 */
get_header();
?>
{header_raw}
<main>
{agent_body_content}
</main>
{footer_raw}
<?php
get_footer();
"""

with open("contact.html", "r", encoding="utf-8") as f:
    contact_raw = f.read()
contact_body = re.search(r'<body[^>]*>(.*?)</body>', contact_raw, re.DOTALL)
contact_body_content = contact_body.group(1).strip() if contact_body else contact_raw

page_contact_php = f"""<?php
/**
 * Template Name: BoloUp Go Contact Page
 * Template Post Type: page
 */
get_header();
?>
{header_raw}
<main>
{contact_body_content}
</main>
{footer_raw}
<?php
get_footer();
"""

# Build zip buffer
zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    zip_file.writestr('hello-elementor-child/style.css', child_css)
    zip_file.writestr('hello-elementor-child/functions.php', functions_php)
    zip_file.writestr('hello-elementor-child/front-page.php', front_page_php)
    zip_file.writestr('hello-elementor-child/template-host.php', page_host_php)
    zip_file.writestr('hello-elementor-child/template-agent.php', page_agent_php)
    zip_file.writestr('hello-elementor-child/template-contact.php', page_contact_php)

zip_buffer.seek(0)
zip_data = zip_buffer.getvalue()

with open("scratch/hello-elementor-child.zip", "wb") as f:
    f.write(zip_data)
print("Created scratch/hello-elementor-child.zip (size:", len(zip_data), "bytes)")

# Upload theme via theme-install.php?upload
r_upload_page = session.get("https://boloupgo.app/wp-admin/theme-install.php?upload")
nonce = re.search(r'name="_wpnonce"\s+value="([^"]+)"', r_upload_page.text).group(1)
print("Got theme upload nonce:", nonce)

files = {
    'themepackage': ('hello-elementor-child.zip', zip_data, 'application/zip')
}
data = {
    '_wpnonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-install.php?upload',
    'install-theme-submit': 'Install Now'
}

r_install = session.post("https://boloupgo.app/wp-admin/update.php?action=upload-theme", data=data, files=files)
print("Theme upload status:", r_install.status_code)
print("Install result text:", "Theme installed successfully" in r_install.text or "Destination folder already exists" in r_install.text)

# Look for activate link
activate_match = re.search(r'href="([^"]*action=activate[^"]*)"', r_install.text)
if activate_match:
    activate_url = activate_match.group(1).replace('&amp;', '&')
    if not activate_url.startswith('http'):
        activate_url = "https://boloupgo.app/wp-admin/" + activate_url
    print("Found activate URL:", activate_url)
    r_act = session.get(activate_url)
    print("Activation status:", r_act.status_code, "wp-admin" in r_act.url)
else:
    print("Activate link not in response, checking themes.php...")
    r_themes = session.get("https://boloupgo.app/wp-admin/themes.php")
    act_link = re.search(r'href="([^"]*action=activate&amp;stylesheet=hello-elementor-child[^"]*)"', r_themes.text)
    if act_link:
        full_act = act_link.group(1).replace('&amp;', '&')
        if not full_act.startswith('http'):
            full_act = "https://boloupgo.app/wp-admin/" + full_act
        print("Found activate in themes.php:", full_act)
        r_act2 = session.get(full_act)
        print("Activation result:", r_act2.status_code)
    else:
        print("Checking if child theme is visible in themes.php")

