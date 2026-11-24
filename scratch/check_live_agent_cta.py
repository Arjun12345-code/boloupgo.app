import urllib.request
import re

req = urllib.request.Request('https://boloupgo.app/agent', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

m = re.search(r'(<section[^>]*id="cta"[^>]*>.*?</section>)', html, re.DOTALL)
if m:
    print("Found CTA section on live agent:")
    print(m.group(1))
else:
    print("CTA section not found on live agent! Searching for Great Hosts:")
    m2 = re.search(r'(.{0,100}Great Hosts.{0,300})', html, re.DOTALL)
    if m2:
        print(m2.group(1))
    else:
        print("Great Hosts not found!")

