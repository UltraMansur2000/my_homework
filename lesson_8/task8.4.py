def val_checker(func1):
    def val_checker2(func2):
        def wrapper(num):
            if func1(num):
                print(func2(num))
            else:
                raise ValueError('write num > 0')

        return wrapper
    return val_checker2


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(2)