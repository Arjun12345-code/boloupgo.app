from PIL import Image
import numpy as np

im = Image.open('assets/images/boloupgo.app_.png').convert('RGBA')
arr = np.array(im)
alpha = arr[:, :, 3]

mask = alpha > 10
y_min, y_max = np.where(mask)[0].min(), np.where(mask)[0].max()
x_min, x_max = np.where(mask)[1].min(), np.where(mask)[1].max()

print(f"Opaque bounding box: X=[{x_min}, {x_max}], Y=[{y_min}, {y_max}]")

print("Corner 1 (y_min, x_min):", arr[y_min, x_min])
print("Corner 2 (y_min, x_max):", arr[y_min, x_max])
print("Corner 3 (y_max, x_min):", arr[y_max, x_min])
print("Corner 4 (y_max, x_max):", arr[y_max, x_max])

print("Sample at y=y_min+20, across x from x_min to x_max (step 100):")
for x in range(x_min, x_max, 100):
    print(f"  x={x}: RGBA={arr[y_min+20, x]}")
