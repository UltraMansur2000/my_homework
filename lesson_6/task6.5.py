import sys

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    names = [i.replace('\n', '').replace(',', ' ') for i in f]
with open(sys.argv[2], 'r', encoding='utf-8') as f:
    hobby = [i for i in f]

with open(sys.argv[3], 'w', encoding='utf-8') as f:
    for i in range(len(names)):
        if i < len(hobby):
            f.write(': '.join([names[i], hobby[i].lower()]))
        else:
            f.write(': '.join([names[i], 'None\n']))
