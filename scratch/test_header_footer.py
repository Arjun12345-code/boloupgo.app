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

with open("header.html", "r", encoding="utf-8") as f:
    header_html = f.read()

header_data = {
    "title": "BoloUp Go Header",
    "status": "publish",
    "meta": {
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "header",
        "_elementor_data": json.dumps(make_elementor_html_structure("header", header_html)),
        "_elementor_conditions": ["include/general"]
    }
}

r_h = session.post("https://boloupgo.app/wp-json/wp/v2/elementor_library", headers=headers, json=header_data)
print("Create Header template status:", r_h.status_code)
if r_h.status_code in [200, 201]:
    h_id = r_h.json().get('id')
    print("Created Header template ID:", h_id)
else:
    print("Header error:", r_h.text[:300])

with open("footer.html", "r", encoding="utf-8") as f:
    footer_html = f.read()

footer_data = {
    "title": "BoloUp Go Footer",
    "status": "publish",
    "meta": {
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "footer",
        "_elementor_data": json.dumps(make_elementor_html_structure("footer", footer_html)),
        "_elementor_conditions": ["include/general"]
    }
}

r_f = session.post("https://boloupgo.app/wp-json/wp/v2/elementor_library", headers=headers, json=footer_data)
print("Create Footer template status:", r_f.status_code)
if r_f.status_code in [200, 201]:
    f_id = r_f.json().get('id')
    print("Created Footer template ID:", f_id)
else:
    print("Footer error:", r_f.text[:300])

