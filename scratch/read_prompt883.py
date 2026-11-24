with open('scratch/user_prompt_883.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's print out the sections
print("--- FULL PROMPT 883 START ---")
print(text[:3000])
print("--- NEXT PART ---")
print(text[3000:6000])
print("--- NEXT PART ---")
print(text[6000:9000])
print("--- NEXT PART ---")
print(text[9000:12000])
print("--- NEXT PART ---")
print(text[12000:])

