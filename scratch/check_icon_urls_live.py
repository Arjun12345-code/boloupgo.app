import urllib.request

urls = [
    'https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-150x150.png',
    'https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-300x300.png',
    'https://boloupgo.app/wp-content/uploads/2026/11/boloup.png',
    'https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            print(f"{u} -> status {resp.status}, size {len(resp.read())}")
    except Exception as e:
        print(f"{u} -> error: {e}")

