import requests
import json
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

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce_match = re.search(r'"nonce":"([^"]+)"', admin_res.text)
nonce = nonce_match.group(1) if nonce_match else None
headers = {'X-WP-Nonce': nonce}

with open("header.html", "r", encoding="utf-8") as f:
    header_html = f.read()

with open("footer.html", "r", encoding="utf-8") as f:
    footer_html = f.read()

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

pages = [
    {
        'id': 34,
        'slug': 'home',
        'title': 'BoloUp Go – Live, Connect, Discover, and Earn More',
        'file': 'index.html',
        'desc': 'Discover BoloUp Go, a social entertainment app for live video, voice rooms, chat, gifts, and earning opportunities to join as a Host or Agent.'
    },
    {
        'id': 35,
        'slug': 'host',
        'title': 'BoloUp Go Host – Go Live, Connect & Grow',
        'file': 'host.html',
        'desc': 'Become a BoloUp Go Host, create live content, connect with viewers, receive gifts, and grow with agency support'
    },
    {
        'id': 36,
        'slug': 'agent',
        'title': 'BoloUp Go Agent – Build & Grow Your Host Team',
        'file': 'agent.html',
        'desc': 'Become a BoloUp Go Agent, recruit Hosts, manage your network, support creators, and explore earning opportunities through team activity.'
    },
    {
        'id': 37,
        'slug': 'contact',
        'title': 'Contact BoloUp Go – Support & Help',
        'file': 'contact.html',
        'desc': 'Contact BoloUp Go for help with your account, Host or Agent registration, withdrawals, agency questions, and other platform support.'
    }
]

for p in pages:
    with open(p['file'], 'r', encoding='utf-8') as f:
        raw = f.read()
    
    # Extract body content
    body_match = re.search(r'<body[^>]*>(.*?)</body>', raw, re.DOTALL)
    body_content = body_match.group(1).strip() if body_match else raw
    
    # Prepend header and append footer
    full_composite_html = (
        '<link rel="stylesheet" href="/style.css">\n' +
        header_html + "\n<main>\n" +
        body_content + "\n</main>\n" +
        footer_html
    )
    
    elementor_data = make_elementor_html_structure(p['slug'], full_composite_html)
    
    payload = {
        "title": p['title'],
        "template": "elementor_canvas",
        "meta": {
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page",
            "_elementor_data": json.dumps(elementor_data),
            "_elementor_page_settings": {
                "template": "elementor_canvas"
            },
            "_yoast_wpseo_title": p['title'],
            "_yoast_wpseo_metadesc": p['desc']
        }
    }
    
    r_up = session.post(f"https://boloupgo.app/wp-json/wp/v2/pages/{p['id']}", headers=headers, json=payload)
    print(f"Updated page {p['slug']} (ID {p['id']}): Status {r_up.status_code}")

print("All 4 pages updated in Elementor Canvas!")

