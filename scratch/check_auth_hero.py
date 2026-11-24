from inspect_site import session
import re

r = session.get("https://boloupgo.app/")
imgs = re.findall(r'<img[^>]*hero-img[^>]*>', r.text)
for im in imgs:
    print('Logged-in Hero img tag:', im)
print('Has boloupgo-app-nobg.png in logged-in?', 'boloupgo-app-nobg.png' in r.text)
print('Has boloupgo-hero.png in logged-in?', 'boloupgo-hero.png' in r.text)

