from inspect_site import session

r = session.get("https://boloupgo.app/?clear_el_cache=1")
print("Length:", len(r.text))
print("Is '<header' in r.text?", "<header" in r.text)
for l in r.text.splitlines():
    if "<header" in l or "brand-logo" in l or "nav-menu" in l or "footer" in l:
        print("Line:", l[:120])

