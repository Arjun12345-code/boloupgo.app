import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\c5e8e287-0b24-4c8e-a459-38d2b9d902bc\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'Last Update Oct 5' in line or 'Last Update Nov 7' in line:
            obj = json.loads(line)
            src = obj.get('source', '')
            if src == 'USER_EXPLICIT':
                c = obj.get('content', '')
                print(f'Line {i}: source={src}, length={len(c)}')
                with open(f'scratch/user_prompt_{i}.txt', 'w', encoding='utf-8') as out:
                    out.write(c)

