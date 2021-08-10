class Cells:
    def __init__(self, c):
        self.c = c

    def __add__(self, other):
        self.c = self.c + other.c
        return self.c

    def __mul__(self, other):
        self.c = self.c * other.c
        return self.c

    def __sub__(self, other):
        if abs(self.c - other.c) > 0:
            self.c = abs(self.c - other.c)
            return self.c
        else:
            print('Разность ячеек меньше нуля')

    def __floordiv__(self, other):
        self.c //= other.c
        return self.c

    def make_order(self, a):
        for i in range(self.c // a):
            print('*' * a, end='\n')
        print('*' * (self.c % a), end='')


x = Cells(12)
y = Cells(15)
x + y
x.make_order(9)
