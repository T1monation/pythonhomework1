import json
from time import perf_counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f, \
        open('new_data.txt', 'w', encoding='utf-8') as new_f:

# вариант решения с загрузкой всего файла в оперативную память
    start = perf_counter()
    remote_adr = []
    request_type = []
    requested_resourse = []
    for line in f:
        remote_adr.append(line.split(' - - [')[0])
        temp_txt = line.split('] "')[1:]
        temp_txt_2 = temp_txt[0].split(' HTT')[0]
        request_type.append(temp_txt_2.split(' ')[0])
        requested_resourse.append(temp_txt_2.split(' ')[1])
    result_list = [(arg1, arg2, arg3) for arg1, arg2, arg3 in zip(remote_adr, request_type, requested_resourse)]
    new_f.write(json.dumps(result_list))
    print(2, perf_counter() - start)
