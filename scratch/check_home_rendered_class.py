with open("scratch/home_rendered.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("home_rendered.html has class='hero':", 'class="hero"' in text)
print("home_rendered.html has class='hero-section':", 'class="hero-section"' in text)

