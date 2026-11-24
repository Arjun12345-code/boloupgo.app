from inspect_site import session
import re
from html import unescape

r = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor")
m = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
if m:
    content = unescape(m.group(1))
    print("Length:", len(content))
    print("Last 400 chars:")
    print(content[-400:])

