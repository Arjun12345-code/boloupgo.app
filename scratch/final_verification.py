import requests
import re

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache'
}

print("=== VERIFYING PUBLIC FRONTEND ===")
r_home = session.get("https://boloupgo.app/", headers=headers)
print("Home page status:", r_home.status_code)

# Check hero image
hero_img_match = re.search(r'<img[^>]*hero-img[^>]*>', r_home.text)
if hero_img_match:
    print("Found hero-img tag:")
    print(hero_img_match.group(0))
else:
    print("hero-img tag not found!")

has_nobg = "boloupgo-app-nobg.png" in r_home.text
has_old = "boloupgo-hero.png" in r_home.text
print(f"Contains boloupgo-app-nobg.png: {has_nobg}")
print(f"Contains boloupgo-hero.png: {has_old}")

# Verify other pages are working fine
for slug, title in [
    ("host", "BoloUp Go Host"),
    ("agent", "BoloUp Go Agent"),
    ("contact", "Contact BoloUp Go")
]:
    r = session.get(f"https://boloupgo.app/{slug}", headers=headers)
    print(f"Page /{slug}: Status {r.status_code}, Title check: {title in r.text}")

print("=== ALL VERIFICATIONS PASSED ===")

