from PIL import Image
import numpy as np

im = Image.open('assets/images/boloupgo.app_.png')
# Crop to bounding box
bbox = im.getbbox()
print("bbox:", bbox)
cropped = im.crop(bbox)
cropped.save('scratch/hero_cropped.png')
print("Saved scratch/hero_cropped.png, size:", cropped.size)

# Let's inspect the cropped image
arr = np.array(cropped)
print("Cropped shape:", arr.shape)

# Let's check what the background of the cropped image is
# Check corners of cropped:
print("Cropped [0, 0]:", arr[0, 0])
print("Cropped [0, -1]:", arr[0, -1])
print("Cropped [-1, 0]:", arr[-1, 0])
print("Cropped [-1, -1]:", arr[-1, -1])

# Check along the top edge of cropped:
print("Top edge alpha > 10 count:", np.sum(arr[0, :, 3] > 10))
print("Bottom edge alpha > 10 count:", np.sum(arr[-1, :, 3] > 10))
print("Left edge alpha > 10 count:", np.sum(arr[:, 0, 3] > 10))
print("Right edge alpha > 10 count:", np.sum(arr[:, -1, 3] > 10))

