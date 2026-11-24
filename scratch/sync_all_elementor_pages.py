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

# 1. Update Pages 34, 35, 36, 37
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
    
    # Extract body content (without header or footer)
    body_match = re.search(r'<body[^>]*>(.*?)</body>', raw, re.DOTALL)
    body_content = body_match.group(1).strip() if body_match else raw
    
    elementor_data = make_elementor_html_structure(p['slug'], body_content)
    
    payload = {
        "title": p['title'],
        "content": body_content,
        "template": "elementor_header_footer",
        "meta": {
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page",
            "_elementor_data": json.dumps(elementor_data),
            "_elementor_page_settings": {
                "template": "elementor_header_footer"
            },
            "_yoast_wpseo_title": p['title'],
            "_yoast_wpseo_metadesc": p['desc']
        }
    }
    
    r_up = session.post(f"https://boloupgo.app/wp-json/wp/v2/pages/{p['id']}", headers=headers, json=payload)
    print(f"Updated page {p['slug']} (ID {p['id']}): Status {r_up.status_code}")

# 2. Update Template 33 (Footer) if applicable
with open('footer.html', 'r', encoding='utf-8') as f:
    footer_content = f.read().strip()

footer_elementor = make_elementor_html_structure('footer', footer_content)
payload_footer = {
    "title": "BoloUp Go Footer",
    "content": footer_content,
    "meta": {
        "_elementor_edit_mode": "builder",
        "_elementor_data": json.dumps(footer_elementor)
    }
}
r_foot = session.post("https://boloupgo.app/wp-json/wp/v2/elementor_library/33", headers=headers, json=payload_footer)
if r_foot.status_code != 200:
    r_foot = session.post("https://boloupgo.app/wp-json/wp/v2/posts/33", headers=headers, json=payload_footer)
print(f"Updated footer template (ID 33): Status {r_foot.status_code}")

# 3. Trigger cache flush and DB fixes
r_flush = session.get("https://boloupgo.app/?boloup_fix_all=1")
print("Cache flush triggered:", r_flush.status_code, r_flush.text[:50])
