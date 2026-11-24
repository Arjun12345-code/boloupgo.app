with open('scratch/live_functions.php', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'icon|favicon', text, re.I)]
print("Icon/favicon occurrences in live_functions.php:", len(matches))
for idx in matches:
    print(text[max(0, idx-100):min(len(text), idx+200)])
    print("-" * 50)

