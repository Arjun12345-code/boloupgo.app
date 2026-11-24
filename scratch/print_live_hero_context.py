import re

with open("scratch/live_front.html", "r", encoding="utf-8") as f:
    html = f.read()

pos = html.find("boloupgo-hero.png")
start = max(0, pos - 1500)
end = min(len(html), pos + 1500)
print(html[start:end])

