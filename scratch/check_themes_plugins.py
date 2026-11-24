import requests
import re
from inspect_site import session

r = session.get("https://boloupgo.app/wp-admin/themes.php")
active_theme = re.findall(r'<div class="theme active[^"]*"[^>]*data-slug="([^"]+)"', r.text)
print("Active theme:", active_theme)
all_themes = re.findall(r'data-slug="([^"]+)"', r.text)
print("All themes:", set(all_themes))

r_plugins = session.get("https://boloupgo.app/wp-admin/plugins.php")
all_plugins = re.findall(r'data-slug="([^"]+)"', r_plugins.text)
print("All plugins:", set(all_plugins))

