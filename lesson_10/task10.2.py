from abc import ABC, abstractmethod


class Methods(ABC):
    @abstractmethod
    def calc_1(self):
        pass

    @abstractmethod
    def calc_2(self):
        pass


class Clothes(Methods):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def calc_1(self):
        return self.v / 6.5 + 0.5

    @property
    def calc_2(self):
        return 2 * self.h + 0.3


x = Clothes(1, 1)
print('{0:.3f}'.format(x.calc_1 + x.calc_2))