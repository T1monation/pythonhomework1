import os
import random

# Создаем тестовую папку, в которой создадим 30 файлов, записывая в них произвольное количество чисел с
# плавающей точкой.
try:
    os.makedirs('test dir')
except FileExistsError:
    pass
for i in range(1, 31):
    with open(f'test dir\pfile{i}.txt', 'w', encoding='utf-8') as f:
        temp_list = [random.random() for el in range(1, random.randint(1, 50))]
        for el in temp_list:
            f.write(f'{el}\n')

# собираем в список размер полученных файлов
dir_list = os.listdir('test dir')
size_list = []
for file in dir_list:
    size_list.append(os.stat(f'test dir\{file}').st_size)

# создаем список ключей для словаря
key_list = [i for i in range(100, 1001, 100)]
n = 0

# "Просеиваем" список размеров, и создаем словарь
result_dict = {}
for key in key_list:
    for el in size_list:
        if (key - 100) < el <= key:
            n += 1
    result_dict.setdefault(key, n)
    n = 0

print(size_list)  # Размеры файлов
print(result_dict)  # Итоговай словарь
