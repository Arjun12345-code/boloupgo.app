with open("scratch/home_rendered.html", "r", encoding="utf-8") as f:
    text = f.read()

print("home_rendered.html total length:", len(text))
# Check if it was truncated by requests or if server returned it
print("Ends with:", text[-300:])
print("Is </html> in text?", "</html>" in text)
print("Is </body> in text?", "</body>" in text)

