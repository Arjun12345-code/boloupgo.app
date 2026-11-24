from PIL import Image
im = Image.open('assets/images/logo-samping.png')
print("logo-samping.png:", im.size, im.mode)
# Let's crop into scratch to view parts or inspect
im.save('scratch/logo_samping_view.png')
print("Saved scratch/logo_samping_view.png")

# Also check other logos
for name in ['boloup-header-logo.png', 'boloup-horizontal-logo.png', 'boloup-logo-highres.png', 'cropped-boloup.png']:
    im2 = Image.open(f'assets/images/{name}')
    print(name, im2.size, im2.mode)

