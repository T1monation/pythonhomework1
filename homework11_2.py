class MyDivByZero(Exception):
    pass


print('Программа для деление на число, вводимое пользоаптелем, для выхода введите "e"')
while True:
    a = input('Введите  число для диления: ')
    if a == 'e':
        break
    else:
        try:
            if a == '0':
                raise MyDivByZero("Делить на 0 нельзя!")
            print(f'Результат деления 100 / {a} = ', 100 / float(a))
        except MyDivByZero as e1:
            print(e1)
        except ValueError:
            print('Пользовательский ввод должен содержать только числа')
