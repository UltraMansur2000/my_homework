list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(list)):
    if list[i].isdigit():
        if len(list[i]) == 1:
            list[i] = '"0{}"'.format(list[i])
        else:
            list[i] = '"{}"'.format(list[i])

    elif '+' in list[i] or '-' in list[i]:
        if len(list[i]) == 2:
            list[i] = '"{}0{}"'.format(list[i][0], list[i][1])
        else:
            list[i] = '"{}"'.format(list[i])

print(' '.join(list))
