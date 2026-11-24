import requests
import re

r = requests.get('https://boloupgo.app/', headers={'Cache-Control': 'no-cache', 'Pragma': 'no-cache'})
print('Status:', r.status_code)
imgs = re.findall(r'<img[^>]*hero-img[^>]*>', r.text)
for im in imgs:
    print('Hero img tag:', im)
print('Has boloupgo-app-nobg.png?', 'boloupgo-app-nobg.png' in r.text)

