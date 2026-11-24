from PIL import Image

im = Image.open('assets/images/logo-samping.png')
print("logo-samping size:", im.size)

im2 = Image.open('assets/images/boloup-header-logo.png')
print("boloup-header-logo size:", im2.size)

im3 = Image.open('assets/images/boloup-transparent-logo.png')
print("boloup-transparent-logo size:", im3.size)

