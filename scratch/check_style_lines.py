with open("style.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- Section 15 CTA ---")
for i in range(820, 855):
    print(f"{i+1}: {lines[i]}", end='')

print("\n--- Media 992px ---")
for i in range(1100, 1115):
    print(f"{i+1}: {lines[i]}", end='')

