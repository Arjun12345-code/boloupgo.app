import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache'
}

for page in ['/', '/agent', '/host', '/contact']:
    url = f"https://boloupgo.app{page}?t={time.time()}"
    r = requests.get(url, headers=headers)
    icons = re.findall(r'<link[^>]*icon[^>]*>', r.text)
    print(f"=== Page {page} (Status: {r.status_code}) ===")
    for ic in icons:
        print(" ", ic)

