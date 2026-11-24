from PIL import Image

im = Image.open('assets/images/cropped-boloup.png')
# Convert RGBA
im = im.convert('RGBA')
# Save as ICO with multiple sizes (16, 32, 48)
im.save('scratch/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
print("Saved scratch/favicon.ico successfully!")

import os
print("ICO size:", os.path.getsize('scratch/favicon.ico'))

