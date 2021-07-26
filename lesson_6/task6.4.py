with open('users.csv', 'r', encoding='utf-8') as f:
    names = [i.replace('\n', '').replace(',', ' ') for i in f]
with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby = [i for i in f]

with open('hobby_names.txt', 'w', encoding='utf-8') as f:
    for i in range(len(names)):
        if i < len(hobby):
            f.write(': '.join([names[i], hobby[i].lower()]))
        else:
            f.write(': '.join([names[i], 'None\n']))
