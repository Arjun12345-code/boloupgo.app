import requests
import re
from inspect_site import session

r = session.get("https://boloupgo.app/")
print("Home status:", r.status_code)
# Look for theme link
theme_match = re.findall(r'/themes/([^/]+)/', r.text)
print("Themes referenced in HTML:", set(theme_match))
print("Title:", re.findall(r'<title>([^<]+)</title>', r.text))

