import urllib.request

try:
    req = urllib.request.Request('https://boloupgo.app/favicon.ico', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        print("https://boloupgo.app/favicon.ico status:", resp.status, "content-type:", resp.headers.get('Content-Type'), "size:", len(resp.read()))
except Exception as e:
    print("Error:", e)

