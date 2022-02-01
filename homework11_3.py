import re


class MyInputTypeError(Exception):
    pass


print('Программа для формирования пользовательского списка чисел, вводить только числа!\n'
      'Для выхода и вывода итогового списка введите "exit"')
user_list = []
# Для проверки данных используем регулярные вырожения. Считаем, что пользователь может ввести целое число (int),
# дробное число (float). Дробное число в Python должно вводиться через точку, однако сделаем посладбения для
# пользователя, и принимаем вводимые дробные числа через запятую.
pattern_int = re.compile(r'[\d]+')
pattern_float_dot = re.compile(r'[\d]+\.[\d]+')
pattern_float_comma = re.compile(r'[\d]+\,[\d]+')

while True:
    a = input('Введите  число: ')
    if a == 'exit':
        break
    else:
        try:
            if re.fullmatch(pattern_int, a):
                pass
            elif re.fullmatch(pattern_float_dot, a):
                pass
            elif re.fullmatch(pattern_float_comma, a):
                a = a.replace(',', '.')
            else:
                raise MyInputTypeError
            user_list.append(a)
        except MyInputTypeError:
            print('Вводимые данные должны быть числом!')

print(user_list)
