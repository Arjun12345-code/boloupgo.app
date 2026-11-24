from PIL import Image
import rembg
import os

input_path = 'assets/images/boloupgo.app_.png'
output_path = 'assets/images/boloupgo-app-nobg.png'

print("Opening image...")
im = Image.open(input_path)
print("Removing background with rembg...")
result = rembg.remove(im)

# Get bounding box of result to trim empty transparent space
bbox = result.getbbox()
print("Result bbox:", bbox)
if bbox:
    cropped_result = result.crop(bbox)
    cropped_result.save(output_path, format='PNG')
    print(f"Saved {output_path}, size={cropped_result.size}")
else:
    result.save(output_path, format='PNG')
    print(f"Saved {output_path}, size={result.size}")

print("File size:", os.path.getsize(output_path))

