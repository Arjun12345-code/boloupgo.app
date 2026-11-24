from PIL import Image
import numpy as np

im = Image.open('assets/images/boloupgo.app_.png')
print("Image size:", im.size)
print("Image mode:", im.mode)

# Convert to RGBA
im_rgba = im.convert('RGBA')
arr = np.array(im_rgba)
print("Corner pixels (top-left, top-right, bottom-left, bottom-right):")
print("Top-left [0, 0]:", arr[0, 0])
print("Top-right [0, -1]:", arr[0, -1])
print("Bottom-left [-1, 0]:", arr[-1, 0])
print("Bottom-right [-1, -1]:", arr[-1, -1])

