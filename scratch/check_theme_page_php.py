from inspect_site import session
import re
from html import unescape

r = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=page.php&theme=hello-elementor")
content_match = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r.text, re.DOTALL)
if content_match:
    print("page.php content:")
    print(unescape(content_match.group(1)))
else:
    print("Could not get page.php")

