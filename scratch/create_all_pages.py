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

pages_def = [
    {
        'slug': 'home',
        'title': 'BoloUp Go – Live, Connect, Discover, and Earn More',
        'file': 'index.html',
        'desc': 'Discover BoloUp Go, a social entertainment app for live video, voice rooms, chat, gifts, and earning opportunities to join as a Host or Agent.'
    },
    {
        'slug': 'host',
        'title': 'BoloUp Go Host – Go Live, Connect & Grow',
        'file': 'host.html',
        'desc': 'Become a BoloUp Go Host, create live content, connect with viewers, receive gifts, and grow with agency support'
    },
    {
        'slug': 'agent',
        'title': 'BoloUp Go Agent – Build & Grow Your Host Team',
        'file': 'agent.html',
        'desc': 'Become a BoloUp Go Agent, recruit Hosts, manage your network, support creators, and explore earning opportunities through team activity.'
    },
    {
        'slug': 'contact',
        'title': 'Contact BoloUp Go – Support & Help',
        'file': 'contact.html',
        'desc': 'Contact BoloUp Go for help with your account, Host or Agent registration, withdrawals, agency questions, and other platform support.'
    }
]

created_page_ids = {}

for p in pages_def:
    with open(p['file'], 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Extract body content
    body_match = re.search(r'<body[^>]*>(.*?)</body>', file_content, re.DOTALL)
    body_html = body_match.group(1).strip() if body_match else file_content
    
    # Check if page already exists
    r_check = session.get(f"https://boloupgo.app/wp-json/wp/v2/pages?slug={p['slug']}", headers=headers)
    existing = r_check.json() if r_check.status_code == 200 else []
    
    page_payload = {
        "title": p['title'],
        "slug": p['slug'],
        "status": "publish",
        "template": "elementor_header_footer",
        "meta": {
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page",
            "_elementor_data": json.dumps(make_elementor_html_structure(p['slug'], body_html)),
            "_elementor_page_settings": {
                "template": "elementor_header_footer"
            },
            "_yoast_wpseo_title": p['title'],
            "_yoast_wpseo_metadesc": p['desc']
        }
    }
    
    if existing:
        page_id = existing[0]['id']
        r_save = session.post(f"https://boloupgo.app/wp-json/wp/v2/pages/{page_id}", headers=headers, json=page_payload)
        print(f"Updated page '{p['slug']}' (ID {page_id}): status {r_save.status_code}")
        created_page_ids[p['slug']] = page_id
    else:
        r_save = session.post("https://boloupgo.app/wp-json/wp/v2/pages", headers=headers, json=page_payload)
        if r_save.status_code in [200, 201]:
            page_id = r_save.json()['id']
            print(f"Created page '{p['slug']}' (ID {page_id}): status {r_save.status_code}")
            created_page_ids[p['slug']] = page_id
        else:
            print(f"Failed to create page '{p['slug']}': status {r_save.status_code} - {r_save.text[:200]}")

print("Created page IDs:", created_page_ids)

# Set Front Page in WordPress Settings
if 'home' in created_page_ids:
    home_id = created_page_ids['home']
    r_set_front = session.post("https://boloupgo.app/wp-json/wp/v2/settings", headers=headers, json={
        "show_on_front": "page",
        "page_on_front": home_id
    })
    print(f"Set static front page to ID {home_id}: status {r_set_front.status_code}")

with open("scratch/pages_mapping.json", "w") as f:
    json.dump(created_page_ids, f, indent=2)

