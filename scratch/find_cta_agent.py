import glob

targets = ['Start as a BoloUp Go Agent', 'Great Hosts']
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
        for t in targets:
            if t in c:
                print(f'Found "{t}" in {f}')

