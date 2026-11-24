import requests

r1 = requests.get("https://boloupgo.app/style.css")
r2 = requests.get("https://boloupgo.app/wp-content/themes/hello-elementor/style.css")

print("https://boloupgo.app/style.css status:", r1.status_code, "length:", len(r1.text))
print("https://boloupgo.app/wp-content/themes/hello-elementor/style.css status:", r2.status_code, "length:", len(r2.text))

