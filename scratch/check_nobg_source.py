from PIL import Image
import numpy as np

im_nobg = Image.open('assets/images/boloupgo-nobg.png')
print("boloupgo-nobg.png size:", im_nobg.size)
print("boloupgo-nobg.png mode:", im_nobg.mode)
print("boloupgo-nobg.png bbox:", im_nobg.getbbox())

im_app = Image.open('assets/images/boloupgo.app_.png')
print("boloupgo.app_.png size:", im_app.size)
print("boloupgo.app_.png bbox:", im_app.getbbox())

