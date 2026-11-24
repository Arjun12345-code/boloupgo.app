import requests
import re
import os

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

file_path = 'assets/images/boloupgo-app-nobg.png'
filename = 'boloupgo-app-nobg.png'

with open(file_path, 'rb') as f:
    file_data = f.read()

upload_headers = {
    'X-WP-Nonce': nonce,
    'Content-Disposition': f'attachment; filename="{filename}"',
    'Content-Type': 'image/png'
}

r_up = session.post("https://boloupgo.app/wp-json/wp/v2/media", headers=upload_headers, data=file_data)
print("Upload status:", r_up.status_code)
if r_up.status_code in [200, 201]:
    res_json = r_up.json()
    new_url = res_json['source_url']
    print(f"Uploaded successfully! ID: {res_json['id']} -> {new_url}")
    with open("scratch/new_hero_url.txt", "w") as f:
        f.write(new_url)
else:
    print("Upload error:", r_up.text[:300])

