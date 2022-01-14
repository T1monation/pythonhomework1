import json
from time import perf_counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f, \
        open('new_data_2.txt', 'w', encoding='utf-8') as new_f:
# Вариант с построчным чтением и записью в файл (размер файла > размера ОЗУ)
     start = perf_counter()
     for line in f:
         remote_adr = line.split(' - - [')[0]
         temp_txt = line.split('] "')[1:]
         temp_txt_2 = temp_txt[0].split(' HTT')[0]
         request_type = temp_txt_2.split(' ')[0]
         requested_resourse = temp_txt_2.split(' ')[1]
         new_f.write(f"{remote_adr} {request_type} {requested_resourse} \n")
     print(1, perf_counter() - start)
