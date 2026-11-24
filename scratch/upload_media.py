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
print("Nonce:", nonce)

headers = {'X-WP-Nonce': nonce}

image_files = [
    'logo-samping.png',
    'boloup-header-logo.png',
    'boloup-ecosystem.png',
    'boloupgo-hero.png',
    'boloup-host-cutout.png',
    'boloup-agent-full.png',
    'BoloUp-Host-Registration-Guide-Step-1.jpg',
    'BoloUp-Host-Registration-Guide-Step-2.jpg',
    'BoloUp-Host-Registration-Guide-Step-3.jpg',
    'BoloUp-Host-Registration-Guide-Step-4.jpg',
    'BoloUp-Agency-Registration-Step-1-1.png',
    'BoloUp-Agency-Registration-Step-2-1.png',
    'BoloUp-Agency-Registration-Step-3-1.png',
    'BoloUp-Agency-Registration-Step-4.jpg',
    'BoloUp-AgentHost-Withdraw.jpg',
    'boloup-agent-add-new-host-part-1.jpg',
    'boloup-agent-add-new-host-part-2.jpg',
    'cropped-boloup.png'
]

# Check existing media
r_media = session.get("https://boloupgo.app/wp-json/wp/v2/media?per_page=100", headers=headers)
existing_media = {}
if r_media.status_code == 200:
    for m in r_media.json():
        title = m['title']['rendered']
        src = m['source_url']
        filename = os.path.basename(src)
        existing_media[filename] = src
        print(f"Existing: {filename} -> {src}")

uploaded_mapping = {}

for img_name in image_files:
    if img_name in existing_media:
        uploaded_mapping[img_name] = existing_media[img_name]
        print(f"Already exists: {img_name} -> {existing_media[img_name]}")
        continue
    
    file_path = os.path.join('assets/images', img_name)
    if not os.path.exists(file_path):
        print(f"File not found locally: {file_path}")
        continue
    
    content_type = 'image/jpeg' if img_name.lower().endswith(('.jpg', '.jpeg')) else 'image/png'
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    upload_headers = {
        'X-WP-Nonce': nonce,
        'Content-Disposition': f'attachment; filename="{img_name}"',
        'Content-Type': content_type
    }
    
    r_up = session.post("https://boloupgo.app/wp-json/wp/v2/media", headers=upload_headers, data=file_data)
    if r_up.status_code in [200, 201]:
        res_json = r_up.json()
        uploaded_url = res_json['source_url']
        uploaded_mapping[img_name] = uploaded_url
        print(f"Uploaded {img_name} successfully -> {uploaded_url}")
    else:
        print(f"Failed to upload {img_name}: {r_up.status_code} - {r_up.text[:200]}")

import json
with open("scratch/media_mapping.json", "w") as f:
    json.dump(uploaded_mapping, f, indent=2)
print("Saved scratch/media_mapping.json")

