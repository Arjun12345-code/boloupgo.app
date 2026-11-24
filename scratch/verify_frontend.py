import requests
import re

session = requests.Session()
pages_to_test = [
    ('Home', 'https://boloupgo.app/'),
    ('Host', 'https://boloupgo.app/host/'),
    ('Agent', 'https://boloupgo.app/agent/'),
    ('Contact', 'https://boloupgo.app/contact/')
]

for name, url in pages_to_test:
    r = session.get(url)
    print(f"\n--- Testing {name}: {url} ---")
    print(f"Status: {r.status_code}")
    title = re.search(r'<title>([^<]+)</title>', r.text)
    print(f"Title: {title.group(1) if title else 'None'}")
    meta_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', r.text)
    print(f"Meta Description: {meta_desc.group(1) if meta_desc else 'None'}")
    print(f"Has Header: {'header' in r.text.lower() and 'brand-logo' in r.text}")
    print(f"Has Footer: {'footer' in r.text.lower() and 'footer-grid' in r.text}")
    print(f"Has Custom CSS: {'style.css' in r.text or '--color-primary' in r.text}")
    print(f"HTML Length: {len(r.text)} bytes")

