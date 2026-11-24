from inspect_site import session
import re

r = session.get("https://boloupgo.app/?clear_el_cache=1")
body_match = re.search(r'<body[^>]*>(.*)', r.text, re.DOTALL)
if body_match:
    print("First 1500 chars of body:")
    print(body_match.group(1)[:1500])

