from inspect_site import session
import re

r = session.get("https://boloupgo.app/wp-admin/theme-editor.php?theme=hello-elementor")
# Find files list
m = re.search(r'<div id="templateside">(.*?)</div>', r.text, re.DOTALL)
if m:
    print("templateside:", m.group(1)[:1500])
else:
    print("templateside not found. Any select or list?")
    for line in r.text.splitlines():
        if 'file=' in line:
            print(line.strip())

