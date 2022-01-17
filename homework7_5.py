import os
import random
import json

# Создаем тестовую папку, в которой создадим 30 файлов, записывая в них произвольное количество чисел с
# плавающей точкой.
try:
    os.makedirs('test dir')
except FileExistsError:
    pass
for i in range(1, 30):
    with open(f'test dir\pfile{i}.txt', 'w', encoding='utf-8') as f:
        temp_list = [random.random() for el in range(1, random.randint(1, 50))]
        for el in temp_list:
            f.write(f'{el}\n')

# собираем в список кортеж из размера полученных файлов, и их расширения
dir_list = os.listdir('test dir')
size_list = []
for file in dir_list:
    size_list.append((os.stat(f'test dir\{file}').st_size, os.path.splitext(file)[1]))

# создаем список ключей для словаря
key_list = [i for i in range(100, 1001, 100)]

# "Просеиваем" список размеров, и создаем словарь
n = 0
result_dict = {}
for key in key_list:
    temp_list.clear()
    n = 0
    for el in size_list:
        if (key - 100) < el[0] <= key:
            n += 1
            temp_list.append(el[1])
    temp_var = temp_list.copy()
    result_dict.setdefault(key, (n, temp_var))
print(size_list) # список кортежей из размера полученных файлов, и их расширения
print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(result_dict) # Итоговай словарь

with open('result7_5.json', 'w', encoding='utf-8') as f:
    json.dump(result_dict, f)