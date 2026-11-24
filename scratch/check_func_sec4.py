with open('scratch/live_functions.php', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// 4. Set Exact Meta Titles')
print(text[idx:idx+1500])

