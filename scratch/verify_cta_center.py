import requests
import re
import time

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache'
}

# 1. Verify CSS
r_css = session.get(f"https://boloupgo.app/style.css?t={time.time()}", headers=headers)
print("style.css length:", len(r_css.text))
has_cta_actions = ".cta-actions" in r_css.text
has_center_important = "justify-content: center !important" in r_css.text
print(f"CSS has .cta-actions: {has_cta_actions}")
print(f"CSS has justify-content: center !important: {has_center_important}")

# 2. Verify Page /agent
r_agent = session.get(f"https://boloupgo.app/agent?t={time.time()}", headers=headers)
print("Page /agent status:", r_agent.status_code)
cta_agent_match = re.search(r'<div class="cta-banner">.*?</div>\s*</div>\s*</section>', r_agent.text, re.DOTALL)
if cta_agent_match:
    print("Agent CTA Banner:")
    print(cta_agent_match.group(0))
else:
    print("Agent CTA Banner not found directly via regex, searching substring:")
    pos = r_agent.text.find("Great Hosts Need a Strong Support")
    if pos != -1:
        print(r_agent.text[pos:pos+400])

# 3. Verify Page /host
r_host = session.get(f"https://boloupgo.app/host?t={time.time()}", headers=headers)
print("Page /host status:", r_host.status_code)
pos_h = r_host.text.find("Your Next Audience Is Waiting")
if pos_h != -1:
    print(r_host.text[pos_h:pos_h+300])

# 4. Verify Page /
r_home = session.get(f"https://boloupgo.app/?t={time.time()}", headers=headers)
print("Page / status:", r_home.status_code)
pos_home = r_home.text.find("There’s More Than One Way to Be Part of BoloUp Go")
if pos_home != -1:
    print(r_home.text[pos_home:pos_home+300])

