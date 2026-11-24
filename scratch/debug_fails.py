import urllib.request
import re

req = urllib.request.Request('https://boloupgo.app/host', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

print("Length of host_html:", len(html))

# Check hero headline
m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
if m:
    print("Host H1:", repr(m.group(1).strip()))

# Check registration headline
m2 = re.search(r'How to Register[^<\n]+', html)
if m2:
    print("Found registration heading:", repr(m2.group(0)))
else:
    print("Did not find 'How to Register' in host_html")

# Check Step 1 in host_html
m3 = re.search(r'Step 1[^<\n]+', html)
if m3:
    print("Found Step 1:", repr(m3.group(0)))

# Check Contact headline
req2 = urllib.request.Request('https://boloupgo.app/contact', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req2) as resp:
    c_html = resp.read().decode('utf-8')
m_c = re.search(r'<h1[^>]*>(.*?)</h1>', c_html, re.DOTALL)
if m_c:
    print("Contact H1:", repr(m_c.group(1).strip()))

