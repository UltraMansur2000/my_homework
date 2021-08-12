class Instruments(Exception):
    def __init__(self, txt):
        self.txt = txt


class Validation(Exception):
    def __init__(self, txt):
        self.txt = txt


class WareHouse:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class OfficeEquipment:
    instruments = {}
    deliveries = {}

    def __init__(self, date, name):
        self.date = date
        self.name = name

    @staticmethod
    def get(instr):
        if OfficeEquipment.instruments.get(instr.name) is not None:
            OfficeEquipment.instruments[instr.name] += 1
        else:
            OfficeEquipment.instruments[instr.name] = 1

    @staticmethod
    def delivery(instr, place, k):
        try:
            if not str(k).isdigit():
                raise Validation('Задано неверное количество')
        except Validation as err:
            print(err)
        else:
            try:
                if OfficeEquipment.instruments.get(instr.name) is None:
                    raise Instruments(f'На складе отсуствует товар {instr.cls} - {instr.name}')
                elif OfficeEquipment.instruments[instr.name] == 0:
                    raise Instruments(f'На складе закончился инструмент под названием {instr.cls} - {instr.name}')
            except Instruments as err:
                print(err)
            else:
                OfficeEquipment.instruments[instr.name] -= k
                OfficeEquipment.deliveries[place] = [instr.cls, instr.name, k]


class Printer(OfficeEquipment):
    def __init__(self, date, name, use, cls='Printer'):
        super().__init__(date, name)
        self.use = use
        self.cls = cls


class Scanner(OfficeEquipment):
    def __init__(self, date, use, name, cls='Scanner'):
        super().__init__(date, name)
        self.use = use
        self.cls = cls


class Xerox(OfficeEquipment):
    def __init__(self, date, use, name, cls='Xerox'):
        super().__init__(date, name)
        self.use = use
        self.cls = cls


x = Printer('12.08.2021', 'FX-100023', 'Paper')
y = Printer('12.08.2021', 'FX-100024', 'Paper')
z = Printer('12.08.2021', 'FX-100025', 'Paper')
OfficeEquipment.get(x)
OfficeEquipment.get(y)
OfficeEquipment.get(z)
print(OfficeEquipment.instruments)
OfficeEquipment.delivery(x, "Geekbrains", 1)
print(OfficeEquipment.deliveries)
