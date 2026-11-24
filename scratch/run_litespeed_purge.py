from inspect_site import session
import re
from html import unescape

r_admin = session.get("https://boloupgo.app/wp-admin/")
# Look for litespeed purge links in wp-admin
purge_links = re.findall(r'href="([^"]*lscwp_ctrl=purge[^"]*)"', r_admin.text, re.IGNORECASE)
print("Purge links in wp-admin:", purge_links)

# Also check admin bar
admin_bar_links = re.findall(r'href="([^"]*purge_all[^"]*)"', r_admin.text, re.IGNORECASE)
print("Admin bar purge_all links:", admin_bar_links)

# Let's check litespeed admin page
r_ls = session.get("https://boloupgo.app/wp-admin/admin.php?page=litespeed-toolbox")
toolbox_links = re.findall(r'href="([^"]*LSCWP_CTRL=purge[^"]*)"', r_ls.text)
print("Toolbox purge links:", len(toolbox_links))
for tl in toolbox_links[:10]:
    full_url = unescape(tl)
    if not full_url.startswith('http'):
        full_url = "https://boloupgo.app/wp-admin/" + full_url
    print("Visiting purge URL:", full_url)
    res = session.get(full_url)
    print("Purge status:", res.status_code)

