with open('scratch/user_prompt_0.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Page Contact', text)]
for idx in matches:
    print(text[idx:idx+800])
    print("=" * 40)

