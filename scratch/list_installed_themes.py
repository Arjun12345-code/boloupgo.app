import requests
import re
from inspect_site import session

r = session.get("https://boloupgo.app/wp-admin/themes.php")
# Look for theme names and slugs in wp.themes
theme_slugs = re.findall(r'"id":"([^"]+)"', r.text)
print("Theme slugs found in wp-admin/themes.php:", set(theme_slugs))

