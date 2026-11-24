from PIL import Image
import numpy as np

im = Image.open('assets/images/boloupgo.app_.png').convert('RGBA')
arr = np.array(im)
alpha = arr[:, :, 3]

# Where is alpha > 0?
y_indices, x_indices = np.where(alpha > 10)
print(f"X range: {x_indices.min()} to {x_indices.max()}")
print(f"Y range: {y_indices.min()} to {y_indices.max()}")

# Let's check a column slice at x=1400 (near right edge)
print("Col x=1400 alpha values (every 100 rows):", [alpha[y, 1400] for y in range(0, 1024, 100)])
print("Col x=1400 RGB values (every 100 rows):", [list(arr[y, 1400, :3]) for y in range(0, 1024, 100)])

# Let's check a column slice at x=768 (center)
print("Col x=768 alpha values (every 100 rows):", [alpha[y, 768] for y in range(0, 1024, 100)])
print("Col x=768 RGB values (every 100 rows):", [list(arr[y, 768, :3]) for y in range(0, 1024, 100)])

# Let's check a column slice at x=500
print("Col x=500 alpha values (every 100 rows):", [alpha[y, 500] for y in range(0, 1024, 100)])

# Let's check a column slice at x=1000
print("Col x=1000 alpha values (every 100 rows):", [alpha[y, 1000] for y in range(0, 1024, 100)])

