import requests
import re
from html import unescape

brief_data = {
    'home': {
        'url': 'https://boloupgo.app/',
        'file': 'index.html',
        'meta_title': 'BoloUp Go – Live, Connect, Discover, and Earn More',
        'meta_desc': 'Discover BoloUp Go, a social entertainment app for live video, voice rooms, chat, gifts, and earning opportunities to join as a Host or Agent.',
        'texts': [
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
            "Live Video",
            "Discover live broadcasts, join conversations, play games, and experience moments as they happen.",
            "Voice Rooms and Chat",
            "Not every connection needs a camera. Join voice rooms, chat with other users, and keep conversations going beyond the live stream.",
            "Gifts and Interactive Experiences",
            "Make live moments more expressive with gifts, visual effects, social activities, and various interactive features available inside the app.",
            "Why People Join BoloUp Go",
            "Find Your Kind of Community",
            "From casual conversations to live entertainment, BoloUp Go gives you different ways to discover people and content that match your interests.",
            "Turn Participation into Opportunity",
            "Users who want a more active role can explore becoming a Host or building a network as an Agent.",
            "Connect & Earn in Your Own Way",
            "Watch, talk, chat, host, or manage a team. BoloUp Go gives different types of users room to participate in ways that fit them.",
            "Getting Started with BoloUp Go Is Simple",
            "Step 1 – Download and Join",
            "Install BoloUp Go, create your account.",
            "Step 2 – Explore the Community",
            "Watch live streams, join rooms, and discover hosts",
            "Step 3 – Choose Your Next Step",
            "Explore the dedicated Host and Agent opportunities.",
            "Frequently Asked Questions",
            "What is BoloUp Go?",
            "BoloUp Go is a social entertainment app built around live video, voice rooms, chat, gifts, and interactive experiences that help people connect in real time.",
            "What is the difference between a BoloUp Go Host and Agent?",
            "A Host focuses on creating live content and interacting with viewers, while an Agent focuses on recruiting, managing, and supporting Hosts within an agency network.",
            "Do I have to become a Host or Agent to use BoloUp Go?",
            "No. You can use BoloUp Go to explore live content, join conversations, chat, and interact with other users. Host and Agent roles are additional options for people who want to participate more actively.",
            "There’s More Than One Way to Be Part of BoloUp Go",
            "Get Started with BoloUp Go"
        ]
    },
    'host': {
        'url': 'https://boloupgo.app/host',
        'file': 'host.html',
        'meta_title': 'BoloUp Go Host – Go Live, Connect & Grow',
        'meta_desc': 'Become a BoloUp Go Host, create live content, connect with viewers, receive gifts, and grow with agency support',
        'texts': [
            "Make Every Live Moment Count as a BoloUp Go Host",
            "Bring your personality on screen, start conversations, and turn viewers into a community. As a BoloUp Go Host, you can create live experiences, receive gifts, and earn through every interaction.",
            "Become a BoloUp Go Host",
            "More Than Going Live, Build Something of Your Own",
            "Create Your Own Live Space",
            "Make every stream feel like yours. Talk, entertain, share your interests, and give viewers a reason to come back.",
            "Turn Viewer Support into Rewards",
            "Viewers can show their appreciation through virtual gifts while you focus on creating engaging live experiences.",
            "Grow & Earn with Agency Support",
            "Joining an agency connects you with additional guidance as you learn the platform, develop your style, and build your audience and income.",
            "How to Become a BoloUp Go Host",
            "Step 1 – Download BoloUp Go",
            "Install the app and create your account using one of the available sign-up options.",
            "Step 2 – Find Become Host",
            "Open your profile, locate Become Host, and tap Join to begin.",
            "Step 3 – Join an Agency",
            "Open the Join Agency form and enter the Agency ID (2527626) provided by your chosen agency.",
            "2527626",
            "Step 4 – Check the Agency Details",
            "Review the agency information shown after submitting the ID to make sure you are joining the right team.",
            "Step 5 – Complete Face Verification",
            "Open the Authentication Center from your profile and follow the instructions shown on screen.",
            "Step 6 – Wait for Approval",
            "Once your application and verification are approved, your account can officially begin its journey as a BoloUp Go Host.",
            "How to Withdraw Your BoloUp Go Host Earnings",
            "Step 1 – Open Your Profile",
            "Log in to BoloUp Go and head to your profile page.",
            "Step 2 – Tap Diamonds",
            "Open Diamonds to see your eligible balance and payout settings.",
            "Step 3 – Choose Withdraw Method",
            "Select Withdraw Method and review the payout options currently available in your region.",
            "Step 4 – Connect Your Payout Account",
            "Open Withdrawal Info and enter the required bank, e-wallet, Payoneer, USDT, or other supported payout details shown in your account.",
            "Step 5 – Enter Your Withdrawal Amount",
            "Choose how much you want to withdraw. Your balance needs to meet the current minimum withdrawal requirement.",
            "Step 6 – Review and Withdraw",
            "Double-check your payout information and amount, then submit your withdrawal request.",
            "Frequently Asked Questions",
            "What is a BoloUp Go Host?",
            "A BoloUp Go Host creates live content and interacts with viewers in real time. Hosts can chat, entertain, share their interests, build an audience, and receive gifts.",
            "Do I need an agency to become a BoloUp Go Host?",
            "The current Host registration process includes joining an agency by entering an Agency ID before completing account verification.",
            "How does a BoloUp Go Host earn?",
            "Hosts can receive virtual gifts from viewers during their live sessions. Other rewards or incentives may depend on current BoloUp Go and agency program rules.",
            "Can I withdraw my own Host earnings?",
            "Yes. Eligible Hosts can request withdrawals directly from their account once their balance meets the applicable requirements.",
            "Which withdrawal methods are available?",
            "BoloUp supports several payout options, including bank transfer, e-wallet, Payoneer, and USDT in supported regions. The options shown in your account depend on your location.",
            "Your Next Audience Is Waiting",
            "Start as a BoloUp Go Host"
        ]
    },
    'agent': {
        'url': 'https://boloupgo.app/agent',
        'file': 'agent.html',
        'meta_title': 'BoloUp Go Agent – Build & Grow Your Host Team',
        'meta_desc': 'Become a BoloUp Go Agent, recruit Hosts, manage your network, support creators, and explore earning opportunities through team activity.',
        'texts': [
            "Build the Team Behind the Live with BoloUp Go Agent",
            "Prefer building a team instead of the livestreaming spotlight? As a BoloUp Go Agent, you can recruit promising Hosts, guide them, manage your team, and create earning opportunities with the team you build.",
            "Become a BoloUp Go Agent",
            "Build People. Grow a Network. Create Opportunities.",
            "Create Your Own Host Network",
            "Find creators with potential and bring them together under one agency you can manage and develop over time.",
            "Grow Through Your Team",
            "Your progress as an Agent is connected to eligible activity from the Hosts and network you manage, giving team growth a real purpose.",
            "Be the Support Behind the Stream",
            "Help Hosts understand the platform, stay active, solve challenges, and build stronger live experiences for their viewers.",
            "How to Register as a BoloUp Go Agent",
            "Step 1 – Download BoloUp Go",
            "https://share.bololinks.com/home/scode/47282",
            "Step 2 – Create Your Account",
            "Register using one of the available sign-in methods and complete the basic profile information requested in the app.",
            "Step 3 – Complete Face Verification",
            "Open your profile, go to the Authentication Center, and follow the instructions shown on screen to complete verification.",
            "Step 4 – Open the Agency Invitation",
            "Access the agency invitation link provided to you (contact us for the link). If the invitation prompt does not appear immediately, check System Messages inside BoloUp Go.",
            "Step 5 – Review the Agency Details",
            "Make sure the agency information shown in the invitation is correct before continuing.",
            "Step 6 – Accept the Invitation",
            "Confirm the invitation to complete your Agent registration and begin accessing your agency features.",
            "How to Withdraw as a BoloUp Go Agent",
            "Step 1 – Open Your Profile",
            "Log in to BoloUp Go and go to your profile page.",
            "Step 2 – Enter the Diamonds Section",
            "Tap Diamonds to view your eligible balance and withdrawal settings.",
            "Step 3 – Select Withdraw Method",
            "Open Withdraw Method to see the payout options currently available for your account and region.",
            "Step 4 – Choose a Payout Option",
            "Select one of the available methods, which may include bank transfer, e-wallet, Payoneer, or USDT depending on your location.",
            "Step 5 – Add Your Payment Details",
            "Tap Withdrawal Info and carefully connect the payout account you want to use.",
            "Step 6 – Enter the Amount",
            "Choose the amount you want to withdraw. Make sure your eligible balance meets the current minimum withdrawal requirement.",
            "Step 7 – Review and Submit",
            "Check the amount and payment information one more time, then tap Withdraw to send your request.",
            "Turn Connections into a Growing Host Team",
            "Step 1 – Open My Agency",
            "Go to your profile and tap My Agency to enter your Agent dashboard.",
            "Step 2 – Choose Host Invite (Link)",
            "Select Host Invite (Link) to generate an invitation for potential Hosts.",
            "Step 3 – Copy Your Invitation Link",
            "Copy the link provided by BoloUp Go.",
            "Step 4 – Share It with Potential Hosts",
            "Send your invitation through messaging apps, social media, or directly to people you want to recruit.",
            "Step 5 – Invite a Specific Host by ID",
            "For a direct invitation, choose Host Invite (ID) instead.",
            "Step 6 – Enter the Host Details",
            "Add the Host ID and verification code provided by the Host, check that the information is correct, and submit the invitation.",
            "Frequently Asked Questions",
            "What does a BoloUp Go Agent do?",
            "A BoloUp Go Agent focuses on recruiting, managing, and supporting Hosts. The role is less about being on camera and more about helping a network of creators stay active and grow.",
            "How can a BoloUp Go Agent earn?",
            "Agent earnings can come from eligible commissions connected to Host activity, Host earnings, and other network activity covered by the current BoloUp agency program. Actual earnings depend on performance and applicable program rules.",
            "Can I invite a Host who already belongs to another agency?",
            "Not immediately. A Host who is already part of another agency must first complete the process of leaving that agency before joining a new one.",
            "Great Hosts Need a Strong Support",
            "Start as a BoloUp Go Agent"
        ]
    },
    'contact': {
        'url': 'https://boloupgo.app/contact',
        'file': 'contact.html',
        'meta_title': 'Contact BoloUp Go – Support & Help',
        'meta_desc': 'Contact BoloUp Go for help with your account, Host or Agent registration, withdrawals, agency questions, and other platform support.',
        'texts': [
            "Contact BoloUp Go – Support & Help",
            "Contact BoloUp Go for help with your account, Host or Agent registration, withdrawals, agency questions, and other platform support."
        ]
    }
}

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

overall_passed = True

for page_key, data in brief_data.items():
    print(f"\n==========================================")
    print(f"AUDITING PAGE: {page_key.upper()}")
    print(f"==========================================")
    
    with open(data['file'], 'r', encoding='utf-8') as f:
        local_content = unescape(f.read())
    
    res = session.get(data['url'], headers=headers)
    live_content = unescape(res.text)
    
    # Meta title check
    local_has_title = data['meta_title'] in local_content
    live_has_title = data['meta_title'] in live_content
    print(f"Meta Title: Local={'OK' if local_has_title else 'FAIL'} | Live={'OK' if live_has_title else 'FAIL'} ({data['meta_title']})")
    if not (local_has_title and live_has_title): overall_passed = False

    # Meta desc check
    local_has_desc = data['meta_desc'] in local_content
    live_has_desc = data['meta_desc'] in live_content
    print(f"Meta Desc:  Local={'OK' if local_has_desc else 'FAIL'} | Live={'OK' if live_has_desc else 'FAIL'}")
    if not (local_has_desc and live_has_desc): overall_passed = False

    # Copywriting items check
    missing_local = []
    missing_live = []
    for item in data['texts']:
        if item not in local_content:
            missing_local.append(item)
        if item not in live_content:
            missing_live.append(item)
    
    print(f"Copywriting checks ({len(data['texts'])} points):")
    if not missing_local and not missing_live:
        print(f"  -> ALL {len(data['texts'])} COPY POINTS 100% MATCHED on both Local & Live!")
    else:
        if missing_local:
            print(f"  -> Missing in LOCAL: {missing_local}")
            overall_passed = False
        if missing_live:
            print(f"  -> Missing in LIVE: {missing_live}")
            overall_passed = False

print(f"\n==========================================")
print(f"OVERALL AUDIT RESULT: {'ALL PASS 100%' if overall_passed else 'SOME ITEMS FAILED'}")
print(f"==========================================")
