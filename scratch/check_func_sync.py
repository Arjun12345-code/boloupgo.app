with open('scratch/live_functions.php', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// 1. Sync style.css')
print(text[idx-50:idx+600])

