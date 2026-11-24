import requests
from PIL import Image
from io import BytesIO

urls = {
    'host': 'http://boloupgo.app/wp-content/uploads/2026/11/host.jpg',
    'agent': 'http://boloupgo.app/wp-content/uploads/2026/11/agent.jpg'
}

for name, url in urls.items():
    r = requests.get(url, timeout=30)
    print(f"{name} download status: {r.status_code}, length: {len(r.content)}")
    if r.status_code == 200:
        im = Image.open(BytesIO(r.content))
        print(f"{name} format: {im.format}, size: {im.size}, mode: {im.mode}")
        im.save(f"scratch/{name}_raw.jpg")

