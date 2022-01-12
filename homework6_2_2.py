with open('new_data_2.txt', 'r', encoding='utf-8') as f:
    # Вариант с построчным чтением из файла (размер файла > размера ОЗУ)
    temp_dict = {}
    max_value = 0
    for line in f:
        temp_var = temp_dict.setdefault(line.split(' ')[0], 1)
        if temp_var == 0:
            continue
        elif temp_var > 0:
            temp_dict[line.split(' ')[0]] = temp_var + 1
        if max_value < temp_dict[line.split(' ')[0]]:
            max_value = temp_dict[line.split(' ')[0]]
            key_origin = line.split(' ')[0]

print(f'Максимальное число запросов - {max_value}')
print(f'Спамер  - {key_origin}')
