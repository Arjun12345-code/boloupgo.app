with open('scratch/user_prompt_0.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Page Contact')
print(text[idx:idx+1500])

