import re
import json
import urllib.request

RE_LOG_STR = re.compile(r"([\d\.|\w\:]+)\W+\[([\w/\:]+\b\s[+]\d{4})\]\s+\"(\w+)\s([\/\w]+)\s[\.\w\/]+\"\s(\d+)\s(\d+)")
# В паттерне учитывается наличие как ipv4 так и ipv6 адресов

def log_parse(log_str):
    log_obj = RE_LOG_STR.match(log_str)

    return [log_obj.group(1),
            log_obj.group(2),
            log_obj.group(3),
            log_obj.group(4),
            log_obj.group(5),
            log_obj.group(6)]

file = 'nginx_logs.txt'
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
print(f'Загружаем файл {file} по адресу:\n'
      f'{url}')
urllib.request.urlretrieve(url, file)
print(f'Файл {file} успешно загружен.')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f, \
        open('log_parse.json', 'w', encoding='utf-8') as f_w:
    for line in f:
        try:
            tem_list = log_parse(line)
        except:
            print('oops!')
            print(line)
            pass
        else:
            json.dump(tem_list, f_w)

    print('Работа скрипта завершена')
