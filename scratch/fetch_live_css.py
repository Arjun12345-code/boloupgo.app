import urllib.request

req = urllib.request.Request('https://boloupgo.app/style.css', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    css = resp.read().decode('utf-8')

with open('scratch/live_style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Saved scratch/live_style.css, length:", len(css))

