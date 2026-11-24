import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache'
}

# Verify Host page
r_host = requests.get(f"https://boloupgo.app/host?t={time.time()}", headers=headers)
print("=== Host Page ===")
print("Status:", r_host.status_code)
print("Has boloup-host-nobg.png:", "boloup-host-nobg.png" in r_host.text)
print("Has boloup-host-cutout.png:", "boloup-host-cutout.png" in r_host.text)
host_hero = re.search(r'<div class="hero-visual"[^>]*>.*?</div>\s*</div>', r_host.text, re.DOTALL)
if host_hero:
    print("Host Hero Tag:", host_hero.group(0))

# Verify Agent page
r_agent = requests.get(f"https://boloupgo.app/agent?t={time.time()}", headers=headers)
print("\n=== Agent Page ===")
print("Status:", r_agent.status_code)
print("Has boloup-agent-nobg.png:", "boloup-agent-nobg.png" in r_agent.text)
print("Has boloup-agent-full.png:", "boloup-agent-full.png" in r_agent.text)
agent_hero = re.search(r'<div class="hero-visual"[^>]*>.*?</div>\s*</div>', r_agent.text, re.DOTALL)
if agent_hero:
    print("Agent Hero Tag:", agent_hero.group(0))

# Verify Home page still intact
r_home = requests.get(f"https://boloupgo.app/?t={time.time()}", headers=headers)
print("\n=== Home Page ===")
print("Status:", r_home.status_code)
print("Has boloupgo-app-nobg.png:", "boloupgo-app-nobg.png" in r_home.text)

