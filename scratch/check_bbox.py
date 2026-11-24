from PIL import Image

im = Image.open('assets/images/boloupgo.app_.png')
print("Image size:", im.size)
print("Image info:", im.info)

# Let's check bounding box of non-zero alpha
bbox = im.getbbox()
print("Bounding box of non-zero pixels:", bbox)

