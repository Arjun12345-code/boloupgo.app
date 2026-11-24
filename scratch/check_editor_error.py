from fix_functions_purge import r_post
import re

notices = re.findall(r'<div[^>]*class="notice[^"]*"[^>]*>(.*?)</div>', r_post.text, re.DOTALL)
print("Notices:", notices)
error = re.findall(r'<p>(.*?)</p>', r_post.text)
print("Paragraphs in response:", error[:5])

