import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\c5e8e287-0b24-4c8e-a459-38d2b9d902bc\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for l in lines[-10:]:
        obj = json.loads(l)
        if 'media' in obj:
            print("Media found:", obj['media'])

