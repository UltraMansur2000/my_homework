with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby = f.read().split('\n')
    hobby = hobby[:-1]
with open('users.csv', 'r', encoding='utf-8') as f:
    a = f.read().replace('\n', ',').split(',')

names = [' '.join(a[m:m + 3]) for m in range(0, len(a) - 1, 3)]
n_h = {names[i]: hobby[i] if i < len(hobby) else None for i in range(len(names))}
print(n_h)
