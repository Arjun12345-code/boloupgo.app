from inspect_site import session

r = session.get("https://boloupgo.app/")
print("Length for logged in user:", len(r.text))
print("Has 'brand-logo'?", "brand-logo" in r.text)
print("Has 'footer-grid'?", "footer-grid" in r.text)
print("Has 'Live More. Connect More'?", "Live More. Connect More" in r.text)
print("Has 'table-comparison'?", "table-comparison" in r.text)
print("Has 'What is BoloUp Go' / 'BoloUp Go Happens Live'?", "BoloUp Go Happens Live" in r.text)
print("Has 'How to Become a BoloUp Go Host'?", "How to Become a BoloUp Go Host" in r.text)
print("Has LiteSpeed comment?", "Page cached by LiteSpeed" in r.text)

