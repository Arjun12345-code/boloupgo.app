from PIL import Image
import glob

icon_files = [
    'assets/images/boloup-avatar-32x32.png',
    'assets/images/boloup-avatar-180x180.png',
    'assets/images/boloup-avatar-192x192.png',
    'assets/images/boloup-avatar-270x270.png',
    'assets/images/cropped-boloup.png',
    'assets/images/icon-only.png',
    'assets/images/boloup-app-icon.png'
]

for f in icon_files:
    try:
        im = Image.open(f)
        print(f, im.size, im.mode)
    except Exception as e:
        print(f, "Error:", e)

