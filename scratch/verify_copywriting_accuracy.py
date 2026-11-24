import requests

pages = {
    'home': {
        'url': 'https://boloupgo.app/',
        'strings': [
            "BoloUp Go – Live, Connect, Discover, and Earn More",
            "Discover BoloUp Go, a social entertainment app for live video, voice rooms, chat, gifts, and earning opportunities to join as a Host or Agent.",
            "Live More. Connect More. Discover BoloUp Go.",
            "BoloUp Go is a social space for real-time connection. Bringing live video, voice rooms, conversations, creators, and income together in one place, whether you want to host or build a team behind the scenes.",
            "Explore BoloUp Go",
            "BoloUp Go Happens Live",
            "BoloUp Go is a social entertainment app where people can meet, talk, watch live content, and share moments as they happen.",
            "Join a live room, discover new creators, take part in conversations, send gifts, or simply find people who share your interests. For users who want to go further, BoloUp Go also offers opportunities to participate as a Host or Agent.",
            "Host or Agent: Choose How You Want to Grow",
            "Creates live content and interacts directly with viewers.",
            "Builds, manages, and supports a team of Hosts.",
            "People who enjoy being on camera, entertaining, talking, or sharing their interests.",
            "People who enjoy recruiting talent, building teams, and supporting creators.",
            "Growing an audience and creating stronger viewer engagement.",
            "Growing an active Host team and developing agency performance.",
            "Receive support through viewer interaction and eligible Host programs.",
            "Access agency opportunities, events, and rewards.",
            "More Ways to Connect on BoloUp Go",
            "Discover live broadcasts, join conversations, play games, and experience moments as they happen.",
            "Not every connection needs a camera. Join voice rooms, chat with other users, and keep conversations going beyond the live stream.",
            "Make live moments more expressive with gifts, visual effects, social activities, and various interactive features available inside the app.",
            "Why People Join BoloUp Go",
            "From casual conversations to live entertainment, BoloUp Go gives you different ways to discover people and content that match your interests.",
            "Users who want a more active role can explore becoming a Host or building a network as an Agent.",
            "Watch, talk, chat, host, or manage a team. BoloUp Go gives different types of users room to participate in ways that fit them.",
            "Getting Started with BoloUp Go Is Simple",
            "Install BoloUp Go, create your account.",
            "Watch live streams, join rooms, and discover hosts",
            "Explore the dedicated Host and Agent opportunities.",
            "What is BoloUp Go?",
            "What is the difference between a BoloUp Go Host and Agent?",
            "Do I have to become a Host or Agent to use BoloUp Go?",
            "There’s More Than One Way to Be Part of BoloUp Go",
            "Get Started with BoloUp Go"
        ]
    },
    'host': {
        'url': 'https://boloupgo.app/host/',
        'strings': [
            "BoloUp Go Host – Go Live, Connect & Grow",
            "Become a BoloUp Go Host, create live content, connect with viewers, receive gifts, and grow with agency support",
            "Make Every Live Moment Count as a BoloUp Go Host",
            "Bring your personality on screen, start conversations, and turn viewers into a community. As a BoloUp Go Host, you can create live experiences, receive gifts, and earn through every interaction.",
            "Become a BoloUp Go Host",
            "More Than Going Live, Build Something of Your Own",
            "Make every stream feel like yours. Talk, entertain, share your interests, and give viewers a reason to come back.",
            "Viewers can show their appreciation through virtual gifts while you focus on creating engaging live experiences.",
            "Joining an agency connects you with additional guidance as you learn the platform, develop your style, and build your audience and income.",
            "How to Become a BoloUp Go Host",
            "Install the app and create your account using one of the available sign-up options.",
            "Open your profile, locate Become Host, and tap Join to begin.",
            "Open the Join Agency form and enter the Agency ID (2527626) provided by your chosen agency.",
            "Review the agency information shown after submitting the ID to make sure you are joining the right team.",
            "Open the Authentication Center from your profile and follow the instructions shown on screen.",
            "Once your application and verification are approved, your account can officially begin its journey as a BoloUp Go Host.",
            "How to Withdraw Your BoloUp Go Host Earnings",
            "Log in to BoloUp Go and head to your profile page.",
            "Open Diamonds to see your eligible balance and payout settings.",
            "Select Withdraw Method and review the payout options currently available in your region.",
            "Open Withdrawal Info and enter the required bank, e-wallet, Payoneer, USDT, or other supported payout details shown in your account.",
            "Choose how much you want to withdraw. Your balance needs to meet the current minimum withdrawal requirement.",
            "Double-check your payout information and amount, then submit your withdrawal request.",
            "What is a BoloUp Go Host?",
            "Do I need an agency to become a BoloUp Go Host?",
            "How does a BoloUp Go Host earn?",
            "Can I withdraw my own Host earnings?",
            "Which withdrawal methods are available?",
            "Your Next Audience Is Waiting",
            "Start as a BoloUp Go Host"
        ]
    },
    'agent': {
        'url': 'https://boloupgo.app/agent/',
        'strings': [
            "BoloUp Go Agent – Build & Grow Your Host Team",
            "Become a BoloUp Go Agent, recruit Hosts, manage your network, support creators, and explore earning opportunities through team activity.",
            "Build the Team Behind the Live with BoloUp Go Agent",
            "Prefer building a team instead of the livestreaming spotlight? As a BoloUp Go Agent, you can recruit promising Hosts, guide them, manage your team, and create earning opportunities with the team you build.",
            "Become a BoloUp Go Agent",
            "Build People. Grow a Network. Create Opportunities.",
            "Find creators with potential and bring them together under one agency you can manage and develop over time.",
            "Your progress as an Agent is connected to eligible activity from the Hosts and network you manage, giving team growth a real purpose.",
            "Help Hosts understand the platform, stay active, solve challenges, and build stronger live experiences for their viewers.",
            "How to Register as a BoloUp Go Agent",
            "https://share.bololinks.com/home/scode/47282",
            "Register using one of the available sign-in methods and complete the basic profile information requested in the app.",
            "Open your profile, go to the Authentication Center, and follow the instructions shown on screen to complete verification.",
            "Access the agency invitation link provided to you (contact us for the link). If the invitation prompt does not appear immediately, check System Messages inside BoloUp Go.",
            "Make sure the agency information shown in the invitation is correct before continuing.",
            "Confirm the invitation to complete your Agent registration and begin accessing your agency features.",
            "How to Withdraw as a BoloUp Go Agent",
            "Log in to BoloUp Go and go to your profile page.",
            "Tap Diamonds to view your eligible balance and withdrawal settings.",
            "Open Withdraw Method to see the payout options currently available for your account and region.",
            "Select one of the available methods, which may include bank transfer, e-wallet, Payoneer, or USDT depending on your location.",
            "Tap Withdrawal Info and carefully connect the payout account you want to use.",
            "Choose the amount you want to withdraw. Make sure your eligible balance meets the current minimum withdrawal requirement.",
            "Check the amount and payment information one more time, then tap Withdraw to send your request.",
            "Turn Connections into a Growing Host Team",
            "Go to your profile and tap My Agency to enter your Agent dashboard.",
            "Select Host Invite (Link) to generate an invitation for potential Hosts.",
            "Copy the link provided by BoloUp Go.",
            "Send your invitation through messaging apps, social media, or directly to people you want to recruit.",
            "For a direct invitation, choose Host Invite (ID) instead.",
            "Add the Host ID and verification code provided by the Host, check that the information is correct, and submit the invitation.",
            "What does a BoloUp Go Agent do?",
            "How can a BoloUp Go Agent earn?",
            "Can I invite a Host who already belongs to another agency?",
            "Great Hosts Need a Strong Support",
            "Start as a BoloUp Go Agent"
        ]
    },
    'contact': {
        'url': 'https://boloupgo.app/contact/',
        'strings': [
            "Contact BoloUp Go – Support & Help",
            "Contact BoloUp Go for help with your account, Host or Agent registration, withdrawals, agency questions, and other platform support."
        ]
    }
}

s = requests.Session()
all_ok = True

for page_key, data in pages.items():
    r = s.get(data['url'])
    # Replace HTML entities for clean comparison
    text = r.text.replace('&amp;', '&').replace('&#8211;', '–').replace('&#8217;', '’').replace('&#038;', '&')
    print(f"\n--- Checking copy for {page_key.upper()} ---")
    page_ok = True
    for phrase in data['strings']:
        if phrase not in text:
            print(f"  [FAIL] Missing: '{phrase}'")
            page_ok = False
            all_ok = False
        else:
            print(f"  [OK] Found: '{phrase[:50]}...'")
    if page_ok:
        print(f"--> {page_key.upper()} COPY MATCH: 100% PERFECT!")

print(f"\n==========================================")
print(f"FINAL RESULT: {'ALL STRINGS 100% ACCURATE & VERIFIED!' if all_ok else 'SOME STRINGS FAILED'}")

