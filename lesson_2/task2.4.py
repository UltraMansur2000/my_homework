# Способ с созданием вспомогательных списков
list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(list)):
    str = list[i].split()
    print(f'Привет, {str[-1].capitalize()}')
print('-'*20)

# Способ со срезом элемента
space = 0
list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(list)):
    for e in range(len(list[i])):
        if list[i][e] == ' ':
            space = e
    name = list[i][space + 1:].capitalize()
    print(f'Привет, {name}')
