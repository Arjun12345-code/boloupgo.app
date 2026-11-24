with open('scratch/live_functions.php', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'style\.css', text)]
print("style.css occurrences in live_functions.php:", len(matches))
for idx in matches:
    print(text[max(0, idx-50):min(len(text), idx+100)])

