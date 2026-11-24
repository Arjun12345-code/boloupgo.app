with open('scratch/live_style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'cta-banner|cta-actions|cta-title', text)]
for idx in matches:
    print(text[max(0, idx-50):min(len(text), idx+200)])
    print("=" * 60)

