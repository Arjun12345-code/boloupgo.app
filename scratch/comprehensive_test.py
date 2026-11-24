import requests
import re
from html import unescape

login_url = "https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
})

# Purge LiteSpeed
r_ls = session.get("https://boloupgo.app/wp-admin/admin.php?page=litespeed-toolbox")
links = re.findall(r'href="([^"]*purge[^"]*)"', r_ls.text, re.IGNORECASE)
for l in list(set(links))[:5]:
    fl = unescape(l)
    if not fl.startswith('http'):
        fl = "https://boloupgo.app/wp-admin/" + fl
    session.get(fl)

pages_to_test = [
    ('Page Home', 'https://boloupgo.app/'),
    ('Page Host', 'https://boloupgo.app/host/'),
    ('Page Agent', 'https://boloupgo.app/agent/'),
    ('Page Contact', 'https://boloupgo.app/contact/')
]

client = requests.Session()
headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}

all_passed = True

for name, url in pages_to_test:
    r = client.get(url, headers=headers)
    print(f"\n==========================================")
    print(f"TESTING: {name} ({url})")
    print(f"HTTP Status: {r.status_code}")
    
    title = re.search(r'<title>([^<]+)</title>', r.text)
    print(f"Title: {title.group(1).strip() if title else 'MISSING'}")
    
    meta_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', r.text)
    print(f"Meta Description: {meta_desc.group(1).strip() if meta_desc else 'MISSING'}")
    
    has_header = ('brand-logo' in r.text and 'class="header"' in r.text)
    has_footer = ('footer-grid' in r.text and 'class="footer"' in r.text)
    has_style_css = ('/style.css' in r.text or '--color-primary' in r.text)
    
    print(f"Header component present: {has_header}")
    print(f"Footer component present: {has_footer}")
    print(f"Sitewide CSS linked: {has_style_css}")
    print(f"HTML Size: {len(r.text)} bytes")
    
    if not (r.status_code == 200 and has_header and has_footer and has_style_css and title and meta_desc):
        all_passed = False

print(f"\n==========================================")
print(f"OVERALL STATUS: {'ALL CHECKS PASSED PERFECTLY!' if all_passed else 'SOME CHECKS NEED ATTENTION'}")

