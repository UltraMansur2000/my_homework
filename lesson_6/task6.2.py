info = {}
spam = [0, 0]
Max = 0
with open('nginx_logs.txt', 'r') as f:
    for i in f:
        i = i.split()
        if info.get(i[0]) is not None:
            info[i[0]] += 1
        else:
            info[i[0]] = 1
        if info[i[0]] > spam[1]:
            spam[0] = i[0]
            spam[1] = info[i[0]]
print(f"IP адрес спамера - {spam[0]}  Количество запросов - {spam[1]}")
