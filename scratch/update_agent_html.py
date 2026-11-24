import re

with open('agent.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Step 3, remove old Step 4 row, and update Step 4 & 5
# Match from <!-- Step 1 & 2 & 3: Part 1 visual --> to </section> before FAQs
invite_pattern = r'<!-- Step 1 & 2 & 3: Part 1 visual -->.*?</div>\s*</div>\s*</div>\s*</section>'
m = re.search(invite_pattern, content, re.DOTALL)
if m:
    new_invite_inner = '''<!-- Step 1 & 2 & 3: Part 1 visual -->
        <div class="step-alt-row" id="invite-step-1">
          <div class="step-alt-visual" onclick="openLightbox(this)" data-src="https://boloupgo.app/wp-content/uploads/2026/11/boloup-agent-add-new-host-part-1.jpg" data-alt="Turn Connections into a Growing Host Team - Invite Link">
            <div class="step-alt-frame">
              <img src="https://boloupgo.app/wp-content/uploads/2026/11/boloup-agent-add-new-host-part-1.jpg"
                alt="Turn Connections into a Growing Host Team - Invite Link" width="1093" height="820" loading="lazy" class="step-alt-img">
              <div class="step-zoom-badge" aria-label="Zoom image">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16" aria-hidden="true"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
              </div>
            </div>
          </div>
          <div class="step-alt-content">
            <div class="step-number">1</div>
            <h3 class="step-title">Step 1 – Open My Agency</h3>
            <p class="step-desc">
              Go to your profile and tap My Agency to enter your Agent dashboard.
            </p>
            <div style="margin-top: 1.5rem;">
              <div class="step-number accent">2</div>
              <h3 class="step-title">Step 2 – Choose Host Invite (Link)</h3>
              <p class="step-desc">
                Select Host Invite (Link) to generate an invitation for potential Hosts.
              </p>
            </div>
            <div style="margin-top: 1.5rem;">
              <div class="step-number">3</div>
              <h3 class="step-title">Step 3 – Copy Your Invitation Link</h3>
              <p class="step-desc">
                Copy the link provided by BoloUp Go and share it with potential hosts
              </p>
            </div>
          </div>
        </div>

        <!-- Step 4 & 5: Part 2 visual -->
        <div class="step-alt-row" id="invite-step-4">
          <div class="step-alt-visual" onclick="openLightbox(this)" data-src="https://boloupgo.app/wp-content/uploads/2026/11/boloup-agent-add-new-host-part-2.jpg" data-alt="Turn Connections into a Growing Host Team - Invite by ID">
            <div class="step-alt-frame">
              <img src="https://boloupgo.app/wp-content/uploads/2026/11/boloup-agent-add-new-host-part-2.jpg"
                alt="Turn Connections into a Growing Host Team - Invite by ID" width="1097" height="830" loading="lazy" class="step-alt-img">
              <div class="step-zoom-badge" aria-label="Zoom image">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16" aria-hidden="true"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
              </div>
            </div>
          </div>
          <div class="step-alt-content">
            <div class="step-number accent">4</div>
            <h3 class="step-title">Step 4 – Invite a Specific Host by ID</h3>
            <p class="step-desc">
              For a direct invitation, choose Host Invite (ID) instead.
            </p>
            <div style="margin-top: 1.5rem;">
              <div class="step-number">5</div>
              <h3 class="step-title">Step 5 – Enter the Host Details</h3>
              <p class="step-desc">
                Add the Host ID and verification code provided by the Host, check that the information is correct, and submit the invitation.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>'''
    content = content[:m.start()] + new_invite_inner + content[m.end():]
    print("Replaced invite tutorial successfully!")
else:
    print("Could not match invite_pattern!")

# 2. Update CTA button
cta_pattern = r'<a href="#registration"[^>]*id="cta-start-agent"[^>]*>.*?</a>'
new_cta_btn = '<a href="https://boloup.onelink.me/PDV4/je5ueb58" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg" id="cta-start-agent">\n            Start as a BoloUp Go Agent\n          </a>'
content, count = re.subn(cta_pattern, new_cta_btn, content, flags=re.DOTALL)
print(f"Replaced CTA button ({count} times)")

with open('agent.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("agent.html saved successfully!")
