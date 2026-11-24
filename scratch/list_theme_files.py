from inspect_site import session
import re

r = session.get("https://boloupgo.app/wp-admin/theme-editor.php?theme=hello-elementor")
files = re.findall(r'href="theme-editor\.php\?file=([^"&]+)&amp;theme=hello-elementor"', r.text)
print("Files in theme:", files)

