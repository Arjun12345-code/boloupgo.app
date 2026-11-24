with open('agent.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="cta-start-agent"')
print(repr(text[idx-100:idx+150]))

