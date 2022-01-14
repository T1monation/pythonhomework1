import sys

if len(sys.argv) == 3:
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        n = 0
        line = f.readline()
        some_dict = {}
        while line:  # В цикле формируем словарь из
            n += 1
            some_dict.setdefault(n, f.tell())
            if n == int(sys.argv[1]):
                find_var = n
            line = f.readline()
            start_pos = f.tell()
        if int(sys.argv[1]) > n or int(sys.argv[1]) <= 0:  # если номер введенной строки несуществует
            print('Введенного номера строки не существует!')
            exit(1)
        if sys.argv[1] == '1':
            f.seek(0)
            f.write(f'{sys.argv[2]:<5}\n')
            # Сдвигаем символ переноса для записи числа, меньшего по знакам, чем в примере
        else:
            f.seek(some_dict[find_var - 1])
            f.write(f'{sys.argv[2]:<5}\n')
