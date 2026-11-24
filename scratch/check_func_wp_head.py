with open('scratch/live_functions.php', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('add_action(\'wp_head\'')
if idx == -1:
    idx = text.find('add_action( \'wp_head\'')
print(text[idx:idx+1500])

