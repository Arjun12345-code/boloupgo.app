with open('scratch/live_functions.php', 'r', encoding='utf-8') as f:
    text = f.read()

print("Functions length:", len(text))
# Let's see the last 1500 chars of live_functions.php
print("--- End of live_functions.php ---")
print(text[-2000:])

