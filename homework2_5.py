prices = [7.52, 2.15, 4.56, 57.02, 25.45, 26.34, 47.56, 64, 124.3, 25.36, 45.23, 45.12, 57.85, 142, 143.45, 52.4178]


def change_list(some_list):  # Функция для преобразования вида списка к виду из ДЗ
    new_list = []
    for item in some_list:
        new_list.append(f'{(int(item // 1)):02d} руб {(int(100 * (item % 1))):02d} коп')
    return new_list


price_str = ', '.join(change_list(prices))  # Вывод списка одной строкой через запятую
print(price_str)

print(change_list(sorted(prices)))  # Вывод списка сортированного по возрастанию

new_prises = (change_list(sorted(prices, reverse=True)))  # Новый список с ценами по убыванию
print(new_prises)

print(change_list(sorted(prices))[-5:])  # Вывод 5 самых дорогих товаров по возрастанию
