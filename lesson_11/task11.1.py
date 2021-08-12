class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def format(cls, data):
        day, month, year = data.split('-')
        return cls(day, month, year)

    @staticmethod
    def validation(obj):
        if int(obj.day) > 31:
            raise ValueError('numbers must be in range [1,31]')
        if int(obj.month) > 12:
            raise ValueError('month must be in range [1,12]')
        if int(obj.year) > 2021:
            raise ValueError('year must be lower than 2021')


D = Data.format('30-10-2001')
print(D.day)
Data.validation(D)
