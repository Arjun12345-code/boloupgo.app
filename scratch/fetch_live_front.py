import requests

r = requests.get("https://boloupgo.app/")
with open("scratch/live_front.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Saved scratch/live_front.html, length:", len(r.text))

# Let's search for "boloupgo-hero"
import re
matches = re.findall(r'.{0,100}boloupgo-hero.{0,100}', r.text)
for m in matches:
    print("Match:", m)

