import urllib.request
import re

urls = [
    'https://boloupgo.app/',
    'https://boloupgo.app/host',
    'https://boloupgo.app/agent',
    'https://boloupgo.app/contact'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            favicons = re.findall(r'<link[^>]*rel=[\'"][^\'"]*icon[^\'"]*[\'"][^>]*>', html, re.I)
            print(f"URL: {u}")
            print(f"  Favicons found ({len(favicons)}):")
            for f in favicons:
                print(f"    {f}")
            # Also check if /favicon.ico exists
    except Exception as e:
        print(f"Error fetching {u}: {e}")

# Check favicon.ico directly
try:
    req = urllib.request.Request('https://boloupgo.app/favicon.ico', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        print(f"https://boloupgo.app/favicon.ico status: {resp.status}, length: {len(resp.read())}")
except Exception as e:
    print(f"https://boloupgo.app/favicon.ico error: {e}")

