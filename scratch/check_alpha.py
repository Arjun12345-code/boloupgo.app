from PIL import Image
import numpy as np

im = Image.open('assets/images/boloupgo.app_.png').convert('RGBA')
arr = np.array(im)
alpha = arr[:, :, 3]
print("Unique alpha values:", np.unique(alpha)[:20])
print("Percent alpha == 0:", np.mean(alpha == 0) * 100)
print("Percent alpha == 255:", np.mean(alpha == 255) * 100)
print("Percent intermediate alpha:", np.mean((alpha > 0) & (alpha < 255)) * 100)

# Also check RGB where alpha > 0
rgb = arr[:, :, :3]
print("RGB min where alpha > 0:", [rgb[:, :, i][alpha > 0].min() for i in range(3)])
print("RGB max where alpha > 0:", [rgb[:, :, i][alpha > 0].max() for i in range(3)])

