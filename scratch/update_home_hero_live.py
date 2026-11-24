import requests
import json
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

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce_match = re.search(r'"nonce":"([^"]+)"', admin_res.text)
nonce = nonce_match.group(1) if nonce_match else None
headers = {'X-WP-Nonce': nonce}

def make_elementor_html_structure(section_id, html_content):
    return [
        {
            "id": section_id + "_sec",
            "elType": "section",
            "isInner": False,
            "settings": {
                "layout": "full_width",
                "gap": "no"
            },
            "elements": [
                {
                    "id": section_id + "_col",
                    "elType": "column",
                    "isInner": False,
                    "settings": {
                        "_column_size": 100
                    },
                    "elements": [
                        {
                            "id": section_id + "_widget",
                            "elType": "widget",
                            "isInner": False,
                            "widgetType": "html",
                            "settings": {
                                "html": html_content
                            }
                        }
                    ]
                }
            ]
        }
    ]

with open("index.html", "r", encoding="utf-8") as f:
    raw = f.read()

body_match = re.search(r'<body[^>]*>(.*?)</body>', raw, re.DOTALL)
body_content = body_match.group(1).strip() if body_match else raw

elementor_data = make_elementor_html_structure("home", body_content)

payload = {
    "title": "BoloUp Go – Live, Connect, Discover, and Earn More",
    "template": "elementor_header_footer",
    "meta": {
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "wp-page",
        "_elementor_data": json.dumps(elementor_data),
        "_elementor_page_settings": {
            "template": "elementor_header_footer"
        },
        "_yoast_wpseo_title": "BoloUp Go – Live, Connect, Discover, and Earn More",
        "_yoast_wpseo_metadesc": "Discover BoloUp Go, a social entertainment app for live video, voice rooms, chat, gifts, and earning opportunities to join as a Host or Agent."
    }
}

r_up = session.post("https://boloupgo.app/wp-json/wp/v2/pages/34", headers=headers, json=payload)
print(f"Updated Home page (ID 34): Status {r_up.status_code}")

# Clear Elementor cache & transient
session.get("https://boloupgo.app/?clear_el_cache=1")

# Purge LiteSpeed
r_ls = session.get("https://boloupgo.app/wp-admin/admin.php?page=litespeed-toolbox")
links = re.findall(r'href="([^"]*purge[^"]*)"', r_ls.text, re.IGNORECASE)
for l in list(set(links))[:5]:
    fl = unescape(l)
    if not fl.startswith('http'):
        fl = "https://boloupgo.app/wp-admin/" + fl
    session.get(fl)

# Verify public frontend
client = requests.Session()
r_check = client.get("https://boloupgo.app/", headers={'Cache-Control': 'no-cache', 'Pragma': 'no-cache'})
print("Live Home Page Status:", r_check.status_code)
has_new_hero = "boloupgo-app-nobg.png" in r_check.text
print("Has boloupgo-app-nobg.png on live site?", has_new_hero)
if has_new_hero:
    print("SUCCESS! New transparent hero image is LIVE on https://boloupgo.app/!")
else:
    print("Checking if old image is still cached or in text...")
    for l in r_check.text.splitlines():
        if "hero-img" in l or "boloupgo" in l and "img" in l:
            print("  ", l.strip()[:140])

