import requests

r = requests.get("https://boloupgo.app/")
print("Is custom_css in rendered HTML?", "--color-primary" in r.text)
if "--color-primary" in r.text:
    print("YES! Elementor Kit 6 Custom CSS is ALREADY rendered sitewide!")
else:
    print("Not found in HTML directly. Looking for css files:")
    for l in r.text.splitlines():
        if 'stylesheet' in l and 'css' in l:
            print("  ", l.strip()[:150])

