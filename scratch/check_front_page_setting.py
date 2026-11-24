from inspect_site import session
import re

admin_res = session.get("https://boloupgo.app/wp-admin/options-reading.php")
print("Reading settings status:", admin_res.status_code)
# Find show_on_front and page_on_front
show_on_front = re.findall(r'name="show_on_front"[^>]*checked[^>]*value="([^"]+)"', admin_res.text)
print("show_on_front:", show_on_front)
page_on_front = re.findall(r'name="page_on_front"[^>]*', admin_res.text)
# Find selected option in page_on_front
selected = re.findall(r'<select[^>]*name="page_on_front"[^>]*>.*?</select>', admin_res.text, re.DOTALL)
if selected:
    opt = re.findall(r'<option[^>]*value="([^"]+)"[^>]*selected[^>]*>([^<]+)</option>', selected[0])
    print("Selected page_on_front:", opt)

# Also let's check what URL https://boloupgo.app/home gives!
r_home = session.get("https://boloupgo.app/home")
print("https://boloupgo.app/home status:", r_home.status_code)
print("Has boloupgo-app-nobg.png in /home?", "boloupgo-app-nobg.png" in r_home.text)
print("Has boloupgo-hero.png in /home?", "boloupgo-hero.png" in r_home.text)

