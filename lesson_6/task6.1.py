info = []
with open('nginx_logs.txt', 'r') as f:
    for i in f:
        i = i.split()
        info.append((i[0], i[5].replace('"', ''), i[6]))
print(info)