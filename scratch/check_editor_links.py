from inspect_site import session
import re

r = session.get("https://boloupgo.app/wp-admin/theme-editor.php?theme=hello-elementor")
print("Status:", r.status_code)
# Search for files listed
matches = re.findall(r'<li[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r.text)
for m in matches[:15]:
    print(m)

