some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in some_list[:]:  # В данном цикле ищем наличие чисел и обрамляем из ссимволом "
    for i in range(len(item)):
        if item[i].isdigit():
            flag = True  # Переменную flag используем для контроля у item наличия чисел
        else:
            flag = False
    if flag:
        n = some_list.index(item)
        if item[0].isdigit():  # здесь анализируем и добавляем разрядность числам
            item = f'{(int(item)):02d}'
            print(item)
        else:
            item = f'{item[0]}{(int(item[1:])):02d}'
            print(item)
        some_list[n] = item
        some_list.insert((n + 1), '"')
        some_list.insert(n, '"')

print(some_list)

new_str = " ".join(some_list)
print(new_str)
