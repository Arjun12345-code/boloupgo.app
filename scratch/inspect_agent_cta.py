with open("agent.html", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("Start as a BoloUp Go Agent")
start = max(0, pos - 800)
end = min(len(text), pos + 800)
print(text[start:end])

