import requests

r = requests.get("https://boloupgo.app/wp-content/uploads/elementor/css/post-6.css?ver=1793831645")
print("post-6.css length:", len(r.text))
print("Has --color-primary:", "--color-primary" in r.text)
print("Preview:", r.text[:300])

