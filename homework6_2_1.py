import json

with open('new_data.txt', 'r', encoding='utf-8') as f:
    # вариант решения с загрузкой всего файла в оперативную память
    new_list = json.load(f)

temp_dict = {}
max_value = 0
for el in new_list:
    temp_var = temp_dict.setdefault(el[0], 1)
    if temp_var == 0:
        continue
    elif temp_var > 0:
        temp_dict[el[0]] = temp_var + 1
    if max_value < temp_dict[el[0]]:
        max_value = temp_dict[el[0]]
        key_origin = el[0]

# for key in temp_dict:
#     if max_value < temp_dict[key]:
#         max_value = temp_dict[key]
#         key_origin = key

print(f'Максимальное число запросов - {max_value}')
print(f'Спамер  - {key_origin}')