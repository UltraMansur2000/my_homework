list = [57.8, 46.51, 97, 25, 35, 51.2, 49.9, 34, 40, 52.23]
string = []
for i in range(len(list)):
    list[i] = str(float(list[i]))
    ind = list[i].find('.')
    if len(list[i][ind + 1:]) == 1:
        list[i] = list[i].replace('.', '.0')
    string.append('{} руб {} коп'.format(list[i][:ind], list[i][ind + 1:]))

print(', '.join(string))
string.sort()
reversed_string = string[::-1]

print('По возрастанию: {}'.format(', '.join(string)))
print('По убыванию: {}'.format(', '.join(string)))
print('Пять самых дорогих товаров: {}'.format(', '.join(string[-5:])))
