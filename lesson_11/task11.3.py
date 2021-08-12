class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


a = []
num = 'start'
while num != "stop":
    try:
        num = input('Введите число для будущего массива:')
        if not num.replace('-', '').isdigit():
            raise MyException('Введёная информация не является числом!')
    except MyException as err:
        print(err)
    else:
        a.append(int(num))
print(a)
