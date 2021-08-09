class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Отрисовка с помощью ручки в файле {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Отрисовка с помощью карандаша в файле {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Отрисовка с помощью маркера в файле {self.title}')


x = Handle('draw.png')
y = Handle('draw.png')
z = Handle('draw.png')
x.draw()
y.draw()
z.draw()
