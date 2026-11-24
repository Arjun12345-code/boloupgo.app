with open('agent.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="agent-invite-steps"' in l:
        start_idx = i
        break

print("Found agent-invite-steps at line:", start_idx)
for j in range(start_idx, min(len(lines), start_idx + 85)):
    print(f"{j+1}: {repr(lines[j])}")

