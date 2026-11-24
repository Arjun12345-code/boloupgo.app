from PIL import Image
import rembg
import os

items = [
    {
        'input': 'scratch/host_raw.jpg',
        'output': 'assets/images/boloup-host-nobg.png',
        'name': 'Host'
    },
    {
        'input': 'scratch/agent_raw.jpg',
        'output': 'assets/images/boloup-agent-nobg.png',
        'name': 'Agent'
    }
]

for item in items:
    print(f"--- Processing {item['name']} ---")
    im = Image.open(item['input'])
    print(f"Original size: {im.size}, mode: {im.mode}")
    print("Removing background with rembg...")
    result = rembg.remove(im)
    bbox = result.getbbox()
    print("Result bbox:", bbox)
    if bbox:
        # Add slight 5px padding if possible within boundaries
        w, h = result.size
        pad = 4
        crop_box = (
            max(0, bbox[0] - pad),
            max(0, bbox[1] - pad),
            min(w, bbox[2] + pad),
            min(h, bbox[3] + pad)
        )
        cropped_result = result.crop(crop_box)
        cropped_result.save(item['output'], format='PNG', optimize=True)
        print(f"Saved cropped {item['output']}, size={cropped_result.size}")
    else:
        result.save(item['output'], format='PNG', optimize=True)
        print(f"Saved full {item['output']}, size={result.size}")
    print(f"File size: {os.path.getsize(item['output'])} bytes")

print("Processing complete!")

