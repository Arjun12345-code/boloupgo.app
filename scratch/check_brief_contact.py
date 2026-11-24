with open('scratch/user_prompt_883.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Page Contact')
print("--- ALL OCCURRENCES OF Page Contact ---")
import re
for m in re.finditer(r'Page Contact', text):
    p = m.start()
    print(text[p:p+500])
    print("=" * 40)

