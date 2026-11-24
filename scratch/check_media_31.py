import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png")
print("Status:", r.status_code, "Length:", len(r.content))
im = Image.open(BytesIO(r.content))
print("Size:", im.size, "Mode:", im.mode)

