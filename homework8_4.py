from functools import wraps


def valid_type_wrap(valid_fanc):
    def type_wrap(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            if valid_fanc(*args):
                return result
            else:
                raise ValueError(f'wrong value {args}')

        return wrapper

    return type_wrap


# @valid_type_wrap(lambda x: x > 0) # Аргумент с этой функцией проверяет положительное ли входно число
@valid_type_wrap(lambda y: y % 3 == 0)  # Аргумент с этой функцией проверяет делиться ли число на 3
def calc_cube(num):
    """ Function calculates the cube of a number"""
    return num ** 3


x = 6

print(calc_cube(x))
help(calc_cube)
