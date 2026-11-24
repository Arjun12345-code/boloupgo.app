import requests

r = requests.get("https://boloupgo.app/")
print("Is 'brand-logo' in HTML?", "brand-logo" in r.text)
print("Is 'footer-grid' in HTML?", "footer-grid" in r.text)
print("Is 'Live More. Connect More' in HTML?", "Live More. Connect More" in r.text)

# Check elementor data on page 34
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
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

r_p34 = session.get("https://boloupgo.app/wp-json/wp/v2/pages/34?context=edit", headers=headers)
p34_meta = r_p34.json().get('meta', {})
print("Page 34 template:", r_p34.json().get('template'))
print("Page 34 _elementor_edit_mode:", p34_meta.get('_elementor_edit_mode'))
print("Page 34 _elementor_template_type:", p34_meta.get('_elementor_template_type'))
el_data = p34_meta.get('_elementor_data', '')
print("Page 34 _elementor_data len:", len(el_data))
print("Is 'brand-logo' in _elementor_data?", "brand-logo" in el_data)

