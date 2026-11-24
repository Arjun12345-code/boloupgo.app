import base64

with open('scratch/favicon.ico', 'rb') as f:
    data = f.read()

b64 = base64.b64encode(data).decode('ascii')
print("Base64 length:", len(b64))

with open('scratch/favicon_b64.txt', 'w') as out:
    out.write(b64)

