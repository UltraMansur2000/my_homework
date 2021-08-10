def type_logger(func):
    cubes = {}
    def wrapper(*args):
        nonlocal cubes
        for i in args:
            if cubes.get(i) is None:
                cubes[i] = func(i)
            print(f'{func.__name__}({i}: {type(i)})')
        return cubes

    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

print(calc_cube(5,23,4))
