import requests
import re
import json

login_url = "https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
}, timeout=30)

admin_res = session.get("https://boloupgo.app/wp-admin/", timeout=30)
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)

uploads = [
    {
        'file_path': 'assets/images/boloup-host-nobg.png',
        'filename': 'boloup-host-nobg.png',
        'key': 'host'
    },
    {
        'file_path': 'assets/images/boloup-agent-nobg.png',
        'filename': 'boloup-agent-nobg.png',
        'key': 'agent'
    }
]

results = {}

for u in uploads:
    with open(u['file_path'], 'rb') as f:
        data = f.read()
    
    headers = {
        'X-WP-Nonce': nonce,
        'Content-Disposition': f'attachment; filename="{u["filename"]}"',
        'Content-Type': 'image/png'
    }
    
    r = session.post("https://boloupgo.app/wp-json/wp/v2/media", headers=headers, data=data, timeout=60)
    print(f"Upload {u['key']} status: {r.status_code}")
    if r.status_code in [200, 201]:
        res = r.json()
        print(f"Uploaded {u['key']} successfully! ID: {res['id']} -> {res['source_url']}")
        results[u['key']] = {
            'id': res['id'],
            'url': res['source_url']
        }
    else:
        print(f"Upload error {u['key']}: {r.text[:200]}")

with open("scratch/uploaded_heroes.json", "w") as f:
    json.dump(results, f, indent=2)
print("Saved scratch/uploaded_heroes.json")

