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
    print("Purged via:", fl[:80])

# Verify Frontend URLs
urls = [
    ('Home Page', 'https://boloupgo.app/'),
    ('Host Page', 'https://boloupgo.app/host/'),
    ('Agent Page', 'https://boloupgo.app/agent/'),
    ('Contact Page', 'https://boloupgo.app/contact/')
]

client = requests.Session()
# Clear client cache header
headers = {'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}

print("\n" + "="*50)
for name, url in urls:
    r = client.get(url, headers=headers)
    print(f"\n[PAGE: {name}] -> {url}")
    print(f"Status Code: {r.status_code}")
    
    # Title
    t_m = re.search(r'<title>([^<]+)</title>', r.text)
    print(f"Title: {t_m.group(1).strip() if t_m else 'NONE'}")
    
    # Meta Description
    d_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', r.text)
    print(f"Meta Description: {d_m.group(1).strip() if d_m else 'NONE'}")
    
    # Components verification
    has_header = ('brand-logo' in r.text and 'class="header"' in r.text)
    has_footer = ('footer-grid' in r.text and 'class="footer"' in r.text)
    has_css = ('style.css' in r.text or '--color-primary' in r.text)
    has_hero = ('hero-title' in r.text)
    
    print(f"Verified Header: {has_header}")
    print(f"Verified Footer: {has_footer}")
    print(f"Verified Stylesheet Link/CSS: {has_css}")
    print(f"Verified Hero Section: {has_hero}")
    print(f"HTML Size: {len(r.text)} bytes")

print("="*50)

