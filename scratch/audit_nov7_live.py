import urllib.request
import re
import html

session_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch(url):
    req = urllib.request.Request(url, headers=session_headers)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8')

results = []

def check(condition, message):
    if condition:
        results.append(f"PASS: {message}")
        print(f"PASS: {message}")
    else:
        results.append(f"FAIL: {message}")
        print(f"FAIL: {message}")

print("=== 1. FAVICON CHECK ===")
try:
    req = urllib.request.Request('https://boloupgo.app/favicon.ico', headers=session_headers)
    with urllib.request.urlopen(req) as resp:
        check(resp.status == 200, f"/favicon.ico status {resp.status}")
        check('image' in resp.headers.get('Content-Type', ''), f"/favicon.ico content-type {resp.headers.get('Content-Type')}")
except Exception as e:
    check(False, f"/favicon.ico failed: {e}")

print("\n=== 2. NAVBAR & FOOTER CHECK (on https://boloupgo.app/) ===")
home_html = fetch('https://boloupgo.app/')

# Navbar
check('https://share.bololinks.com/home/scode/47282' in home_html and 'Become Agent' in home_html, "Navbar has 'Become Agent' link to 47282")
check('https://boloup.onelink.me/PDV4/bd52e5xj' in home_html and 'Become a Host' in home_html, "Navbar has 'Become a Host' link to bd52e5xj")
check('alt="BoloUp Go' in home_html or 'aria-label="BoloUp Go' in home_html, "Navbar logo brand is BoloUp Go")

# Footer
check('BoloUp Go is a social space for real-time connection. Bringing live video, voice rooms, conversations, creators, and income together in one place.' in home_html, "Footer has exact new tagline")
check('Become a Host</a></li>' not in home_html and 'Become an Agent</a></li>' not in home_html, "Footer has removed Become a Host & Become an Agent links")
check('href="https://boloup.onelink.me/PDV4/bd52e5xj"' in home_html and 'Download BoloUp Go' in home_html, "Footer Download BoloUp Go links to bd52e5xj")

print("\n=== 3. PAGE HOME CHECK ===")
check('Live More. Connect More. Discover BoloUp Go.' in home_html, "Home Hero Headline verbatim")
check('Explore BoloUp Go' in home_html and 'Download App' in home_html, "Home Hero CTAs present")
check('Get Started with BoloUp Go' in home_html, "Home Bottom CTA verbatim")

print("\n=== 4. PAGE HOST CHECK ===")
host_html = fetch('https://boloupgo.app/host')
check('Make Every Live Moment Count as a BoloUp Go Host' in host_html, "Host Hero Headline verbatim")
check('Learn More About Host' in host_html and 'Download App' in host_html, "Host Hero CTAs present")
check('How to Become a BoloUp Go Host' in host_html, "Host Registration Tutorial Headline verbatim")
check('Step 1 – Download and Create Your Account' in host_html, "Host Step 1 verbatim")
check('Step 2 – Open Become Host' in host_html, "Host Step 2 verbatim")
check('Step 3 – Enter Your Agency ID' in host_html and '2527626' in host_html, "Host Step 3 verbatim")
check('Step 4 – Complete Face Verification' in host_html, "Host Step 4 verbatim")
check('Step 5 – Complete Your Host Application' in host_html, "Host Step 5 verbatim")
check('Start as a BoloUp Go Host' in host_html and 'https://boloup.onelink.me/PDV4/bd52e5xj' in host_html, "Host Bottom CTA verbatim")

print("\n=== 5. PAGE AGENT CHECK ===")
agent_html = fetch('https://boloupgo.app/agent')
check('Build the Team Behind the Live with BoloUp Go Agent' in agent_html, "Agent Hero Headline verbatim")
check('Learn More About Agent' in agent_html and 'https://boloup.onelink.me/PDV4/je5ueb58' in agent_html, "Agent Hero CTA Download links to je5ueb58")
check('How to Register as a BoloUp Go Agent' in agent_html, "Agent Registration Headline verbatim")
check('Step 1 – Download BoloUp' in agent_html, "Agent Step 1 verbatim")
check('Step 2 – Register &amp; Finish and Verification' in agent_html or 'Step 2 – Register & Finish and Verification' in agent_html, "Agent Step 2 verbatim")
check('Step 3 – Open Your Agency Registration Invitation' in agent_html and 'https://share.bololinks.com/home/scode/47282' in agent_html, "Agent Step 3 verbatim with invitation link")
check('Step 4 – Accept the Agency Invitation' in agent_html, "Agent Step 4 verbatim")

check('Turn Connections into a Growing Host Team' in agent_html, "Agent Invite Headline verbatim")
check('Step 1 – Open My Agency' in agent_html, "Agent Invite Step 1 verbatim")
check('Step 2 – Choose Host Invite (Link)' in agent_html, "Agent Invite Step 2 verbatim")
check('Step 3 – Copy Your Invitation Link' in agent_html and 'share it with potential hosts' in agent_html, "Agent Invite Step 3 verbatim")
check('Step 4 – Invite a Specific Host by ID' in agent_html, "Agent Invite Step 4 verbatim")
check('Step 5 – Enter the Host Details' in agent_html, "Agent Invite Step 5 verbatim")
check('Step 6' not in agent_html.split('Turn Connections into a Growing Host Team')[1].split('Frequently Asked Questions')[0], "Agent Invite Tutorial has exactly 5 steps (no Step 6)")

check('Great Hosts Need a Strong Support' in agent_html, "Agent CTA Headline verbatim")
check('Start as a BoloUp Go Agent' in agent_html and 'https://boloup.onelink.me/PDV4/je5ueb58' in agent_html, "Agent Bottom CTA links to je5ueb58")

print("\n=== 6. PAGE CONTACT CHECK ===")
contact_html = fetch('https://boloupgo.app/contact')
check('Contact BoloUp Go – Support &amp; Help' in contact_html or 'Contact BoloUp Go – Support & Help' in contact_html, "Contact Title/H1 verbatim")
check('https://wa.me/6285353344593' in contact_html and 'WhatsApp' in contact_html, "Contact has WhatsApp button")
check('https://t.me/boloupcustomerservice' in contact_html and 'Telegram' in contact_html, "Contact has Telegram button")
check('Download BoloUp Go App' not in contact_html, "Old Download BoloUp Go App button removed from Contact")
check('Back to Home' not in contact_html, "Old Back to Home button removed from Contact")

print("\n=== 7. CSS CENTERING CHECK ===")
css_text = fetch('https://boloupgo.app/style.css')
check('justify-content: center !important' in css_text and 'text-align: center !important' in css_text, "CSS has strict center alignment for cta-actions")

fails = [r for r in results if r.startswith("FAIL")]
print("\n" + "="*50)
print(f"AUDIT SUMMARY: {len(results) - len(fails)} PASSED, {len(fails)} FAILED")
print("="*50)
