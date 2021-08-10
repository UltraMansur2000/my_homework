class Car:

    def __init__(self, speed, color, name, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Go - go {self.name}!')

    def stop(self):
        print(f'Stop')

    def turn(self, direction):
        print(f'Car turned in {direction} direction')

    def show_speed(self):
        print(f'{self.speed} - current speed')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Too high speed - {self.speed}')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Current speed - {self.speed}. Please drive slowly.')
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


x = WorkCar(60, 'Black', 'Lada', False)
x.show_speed()
x.go()
x.turn('left')
x.stop()
