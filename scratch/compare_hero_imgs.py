from PIL import Image
import os

files = ['boloupgo.app_.png', 'boloupgo.png', 'boloupgo-nobg.png', 'boloupgo-hero.png']
for f in files:
    p = os.path.join('assets/images', f)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{f}: size={im.size}, mode={im.mode}, file_size={os.path.getsize(p)}")

