with open('scratch/live_functions.php', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// 2. Enqueue Custom CSS')
print(text[idx:idx+600])

