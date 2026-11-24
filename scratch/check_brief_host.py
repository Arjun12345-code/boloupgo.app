with open('scratch/user_prompt_883.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Page Host\nHero')
if idx == -1:
    idx = text.find('Page Host')
print(text[idx:idx+2500])

