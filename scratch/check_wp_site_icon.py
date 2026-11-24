import requests
import json

session = requests.Session()
login_url = 'https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.get(login_url)

login_data = {
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
}

r = session.post(login_url, data=login_data)

# Let's check wp-admin/options-general.php or customizer or REST API
r = session.get('https://boloupgo.app/wp-json/wp/v2/settings')
print("Settings status:", r.status_code)
if r.status_code == 200:
    print(r.json())
else:
    # Try with basic auth or check options in admin
    print("Could not get settings via REST API:", r.status_code, r.text[:200])

