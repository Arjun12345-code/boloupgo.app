import requests

r = requests.get("https://boloupgo.app/?nocache=1")
print("Has 'brand-logo'?", "brand-logo" in r.text)
print("Has 'footer-grid'?", "footer-grid" in r.text)
print("Has 'Live More. Connect More'?", "Live More. Connect More" in r.text)
print("Has 'style.css'?", "style.css" in r.text)

