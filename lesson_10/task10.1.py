class Matrix:
    def __init__(self, a):
        self.a = a
        for i in range(1, len(self.a)):
            if len(self.a[i]) != len(self.a[i - 1]):
                raise IndexError('wrong matrix')

    def __str__(self):
        return '\n'.join(str(self.a).replace('], [', 'a').replace('[', '').replace(']', '').replace(',', '').split('a'))

    def __add__(self, other):
        for i in range(min(len(self.a), len(other.a))):
            if len(self.a[i]) != len(other.a[i]):
                raise IndexError('wrong Matrix')
            for j in range(len(self.a[i])):
                self.a[i][j] += other.a[i][j]
        return self.a


x = Matrix([[23, 123], [100, 20], [23, 123]])
print(x, end='\n\n')
y = Matrix([[23, 123], [100, 20], [23, 123]])
a = Matrix(x + y)
print(a)