import re

for filename in ['host.html', 'agent.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    hero_img = re.findall(r'<div class="hero-visual".*?</div>\s*</div>\s*</div>', c, re.DOTALL)
    print(f"=== {filename} Hero Visual ===")
    if hero_img:
        print(hero_img[0])
    else:
        # Search for hero img tag
        imgs = re.findall(r'<img[^>]*hero[^>]*>', c)
        print(imgs)

