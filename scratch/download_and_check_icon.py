import urllib.request
from PIL import Image

urllib.request.urlretrieve('https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-150x150.png', 'scratch/live_icon_150.png')
urllib.request.urlretrieve('https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png', 'scratch/live_icon_full.png')

im1 = Image.open('scratch/live_icon_150.png')
print("live_icon_150 mode:", im1.mode, "size:", im1.size)
im2 = Image.open('scratch/live_icon_full.png')
print("live_icon_full mode:", im2.mode, "size:", im2.size)

