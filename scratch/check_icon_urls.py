import requests

for url in [
    "https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-150x150.png",
    "https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-300x300.png",
    "https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup.png"
]:
    r = requests.get(url)
    print(url, "->", r.status_code, "Length:", len(r.content))

