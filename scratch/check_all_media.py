import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\c5e8e287-0b24-4c8e-a459-38d2b9d902bc\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        obj = json.loads(line)
        if 'media' in obj and obj['media']:
            print(f"Line {i}: {obj['media']}")

