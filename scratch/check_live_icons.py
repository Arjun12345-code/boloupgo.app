import requests
import re
import time

r = requests.get(f"https://boloupgo.app/agent?t={time.time()}")
icons = re.findall(r'<link[^>]*icon[^>]*>', r.text)
print("Icons found in live /agent:")
for ic in icons:
    print(ic)

r2 = requests.get(f"https://boloupgo.app/?t={time.time()}")
icons2 = re.findall(r'<link[^>]*icon[^>]*>', r2.text)
print("Icons found in live /:")
for ic in icons2:
    print(ic)

