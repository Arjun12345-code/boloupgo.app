from inspect_site import session
import re

files_to_check = [
    'header.php', 'footer.php', 'functions.php', 'index.php', 'front-page.php',
    'page.php', 'single.php', 'template-parts/header.php', 'template-parts/footer.php',
    'template-parts/dynamic-header.php', 'template-parts/dynamic-footer.php'
]

for f in files_to_check:
    r = session.get(f"https://boloupgo.app/wp-admin/theme-editor.php?file={f}&theme=hello-elementor")
    if r.status_code == 200 and "boloupgo-hero.png" in r.text:
        print(f"Found in theme file: {f}!")
    elif r.status_code == 200:
        pass
        # print(f"Not in {f}")

print("Theme search complete.")

