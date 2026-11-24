from PIL import Image
import numpy as np

im = Image.open('assets/images/boloupgo.app_.png').convert('RGBA')
arr = np.array(im)

# Look at points in the image
# Let's sample along the borders and center
h, w, _ = arr.shape
print(f"Dimensions: {w}x{h}")

samples = [
    ("Top-left area (100, 100)", arr[100, 100]),
    ("Top-center (50, 768)", arr[50, 768]),
    ("Top-right area (100, 1400)", arr[100, 1400]),
    ("Center (512, 768)", arr[512, 768]),
    ("Bottom-left area (900, 100)", arr[900, 100]),
    ("Bottom-right area (900, 1400)", arr[900, 1400]),
]

for name, val in samples:
    print(f"{name}: RGBA={val}")

# Let's check how many pixels have alpha > 100
print("Count alpha > 100:", np.sum(arr[:, :, 3] > 100))
print("Count alpha > 200:", np.sum(arr[:, :, 3] > 200))
print("Count alpha == 0:", np.sum(arr[:, :, 3] == 0))

