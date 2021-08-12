class MyOwnZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


num = int(input('Введите число:'))
d = int(input('Введите делитель:'))
try:
    if d == 0:
        raise MyOwnZeroDivisionError('Делить на ноль нельзя!')
except MyOwnZeroDivisionError as err:
    print(err)