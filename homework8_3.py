from time import perf_counter
from functools import wraps


def type_wrap(callback):
    @wraps(callback)
    def wrapper(*args):
        func = callback(*args)
        type_list = [f'{callback.__name__}({arg}: {type(arg)})' for arg in args]
        print(type_list)
        return func

    return wrapper


def timer_wrap(callback):
    @wraps(callback)
    def wrapper(*args):
        start = perf_counter()
        func = callback(*args)
        print(start - perf_counter())
        return func

    return wrapper


@timer_wrap
@type_wrap
def calc_cube(*num):
    """ Function calculates cube of a number"""
    result = [el ** 3 for el in num]
    return result


print(calc_cube(4, 6, 8, 6))
help(calc_cube)
