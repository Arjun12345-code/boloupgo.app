from inspect_site import session
import re

r = session.get("https://boloupgo.app/")
logos = re.findall(r'<img[^>]*>', r.text)
print(f"Total img tags found: {len(logos)}")
for img in logos:
    print(" ", img)

