class ComplexNums:
    def __init__(self, n):
        self.n = n

    def __mul__(self, other):
        return self.n * other.n

    def __add__(self, other):
        return self.n + other.n


x = ComplexNums(3)
y = ComplexNums(5)
print(x * y)
print(x + y)
