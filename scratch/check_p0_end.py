with open('scratch/user_prompt_0.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- End of prompt 0 (last 2000 chars) ---")
print(text[-2000:])

