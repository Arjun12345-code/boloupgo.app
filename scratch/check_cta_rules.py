with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'#cta-start-agent|\.cta-actions|\.cta-banner', text)]
for idx in matches:
    print(text[max(0, idx-20):min(len(text), idx+150)])
    print("=" * 40)

