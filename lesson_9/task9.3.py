class Worker:

    def __init__(self, name=None, surname=None, position=None, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.cash = {'wage': wage, 'bonus': bonus}
        self._income = self.cash


class Position(Worker):

    def get_full_name(self):
        print(f'ФИО:{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{self._income["wage"] + self._income["bonus"]} - итоговая зарплата')


x = Position('Игорь', 'Абдулов', 'Стажёр', 1000000000000, 1000000000000)
x.get_full_name()
x.get_total_income()
