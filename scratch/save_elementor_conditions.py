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

# Get elementor Common nonce
r_editor = session.get("https://boloupgo.app/wp-admin/post.php?post=32&action=elementor")
print("Editor page status:", r_editor.status_code)

ajax_nonce_match = re.search(r'"ajax":\{"url":"[^"]+","nonce":"([^"]+)"\}', r_editor.text)
if not ajax_nonce_match:
    ajax_nonce_match = re.search(r'"nonce":"([^"]+)"', r_editor.text)

print("Ajax nonce match:", ajax_nonce_match.group(1) if ajax_nonce_match else "not found")
ajax_nonce = ajax_nonce_match.group(1) if ajax_nonce_match else None

# Elementor Pro Theme Builder save conditions action
# Action: elementor_pro_theme_builder_save_conditions
if ajax_nonce:
    # 1. Header condition
    payload_h = {
        'action': 'elementor_pro_theme_builder_save_conditions',
        '_nonce': ajax_nonce,
        'post_id': 32,
        'conditions': ['include/general']
    }
    r_cond_h = session.post("https://boloupgo.app/wp-admin/admin-ajax.php", data=payload_h)
    print("Save Header conditions response:", r_cond_h.status_code, r_cond_h.text[:200])

    # 2. Footer condition
    payload_f = {
        'action': 'elementor_pro_theme_builder_save_conditions',
        '_nonce': ajax_nonce,
        'post_id': 33,
        'conditions': ['include/general']
    }
    r_cond_f = session.post("https://boloupgo.app/wp-admin/admin-ajax.php", data=payload_f)
    print("Save Footer conditions response:", r_cond_f.status_code, r_cond_f.text[:200])

