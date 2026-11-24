with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.btn\b|\.cta-actions|\.cta-banner|\.cta-title', text)]
for idx in matches:
    print(text[max(0, idx-30):min(len(text), idx+120)].replace('\n', ' '))

