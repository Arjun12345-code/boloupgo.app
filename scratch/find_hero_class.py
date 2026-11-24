import glob

for f in glob.glob('*.*'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
        if 'class="hero"' in c:
            print(f'Found class="hero" in {f}')
        if 'class="hero-section' in c:
            print(f'Found class="hero-section" in {f}')

for f in glob.glob('scratch/*.*'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
        if 'class="hero"' in c:
            print(f'Found class="hero" in {f}')

