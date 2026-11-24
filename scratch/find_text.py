import requests

r = requests.get("https://boloupgo.app/")
idx = r.text.find("Live More. Connect More")
print("Index:", idx)
if idx != -1:
    print("Surrounding text (500 chars before and after):")
    print(r.text[max(0, idx-500):min(len(r.text), idx+500)])

