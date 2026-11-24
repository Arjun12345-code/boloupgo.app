import requests
import re
import json

login_url = "https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
res = session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
})

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce_match = re.search(r'"nonce":"([^"]+)"', admin_res.text)
nonce = nonce_match.group(1) if nonce_match else None
print("Nonce found:", nonce)

headers = {'X-WP-Nonce': nonce} if nonce else {}

# 1. Pages
r_pages = session.get("https://boloupgo.app/wp-json/wp/v2/pages?per_page=100", headers=headers)
print(f"Pages status: {r_pages.status_code}")
if r_pages.status_code == 200:
    for p in r_pages.json():
        print(f"Page ID: {p['id']}, Title: {p['title']['rendered']}, Slug: {p['slug']}, Status: {p['status']}, Template: {p.get('template')}")

# 2. Elementor library templates
r_el = session.get("https://boloupgo.app/wp-json/wp/v2/elementor_library?per_page=100", headers=headers)
print(f"Elementor templates status: {r_el.status_code}")
if r_el.status_code == 200:
    for e in r_el.json():
        print(f"Template ID: {e['id']}, Title: {e['title']['rendered']}, Type: {e.get('type')}")

# 3. Media
r_media = session.get("https://boloupgo.app/wp-json/wp/v2/media?per_page=100", headers=headers)
print(f"Media items count: {len(r_media.json()) if r_media.status_code == 200 else 0}")
if r_media.status_code == 200:
    for m in r_media.json():
        print(f"Media: {m['id']} - {m['title']['rendered']} -> {m['source_url']}")

# 4. Plugins
plugins_page = session.get("https://boloupgo.app/wp-admin/plugins.php")
active_plugins = re.findall(r'<tr class="active"[^>]*data-plugin="([^"]+)"', plugins_page.text)
print("Active plugins:", active_plugins)

# 5. Themes
themes_page = session.get("https://boloupgo.app/wp-admin/themes.php")
current_theme = re.search(r'data-slug="([^"]+)"\s+aria-describedby="[^"]*current-theme', themes_page.text)
print("Current theme slug regex:", current_theme.group(1) if current_theme else "not found directly")

# 6. Front page setting
options_reading = session.get("https://boloupgo.app/wp-admin/options-reading.php")
page_on_front = re.search(r'name="page_on_front"[^>]*value="(\d+)"[^>]*selected', options_reading.text)
print("Page on front ID:", page_on_front.group(1) if page_on_front else "not found or default")

