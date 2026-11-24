import os
from PIL import Image

image_files = [
    'logo-samping.png',
    'boloup-header-logo.png',
    'boloup-ecosystem.png',
    'boloupgo-hero.png',
    'boloupgo.png',
    'boloup-host-cutout.png',
    'boloup-agent-full.png',
    'BoloUp-Host-Registration-Guide-Step-1.jpg',
    'BoloUp-Host-Registration-Guide-Step-2.jpg',
    'BoloUp-Host-Registration-Guide-Step-3.jpg',
    'BoloUp-Host-Registration-Guide-Step-4.jpg',
    'BoloUp-Agency-Registration-Step-1-1.png',
    'BoloUp-Agency-Registration-Step-2-1.png',
    'BoloUp-Agency-Registration-Step-3-1.png',
    'BoloUp-Agency-Registration-Step-4.jpg',
    'BoloUp-AgentHost-Withdraw.jpg',
    'boloup-agent-add-new-host-part-1.jpg',
    'boloup-agent-add-new-host-part-2.jpg',
    'cropped-boloup.png'
]

for img_name in image_files:
    p = os.path.join('assets/images', img_name)
    if os.path.exists(p):
        with Image.open(p) as im:
            print(f"'{img_name}': {{ 'width': {im.width}, 'height': {im.height} }},")

