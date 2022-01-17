import shutil
import sys
import os
from shutil import rmtree
import datetime

CONST_LIST = [n for n in range(1, 100) if n % 3 == 0]


def get_dir_list(arg_ca=False, arg_da=False, file_name='config.yaml'):
    """
    Для получения списка путей, с помощью которых мы создаем файлы и папки проекта, читаем файл конфигурации,
    и представляем результат как двухмерный массив, в котором элементы - пути для создания файлов и папок проекта.
    А содержимое элементов - части самого пути
    Скрипт может запускаться с консольными аргументами: 
     - первым аргументом "c", "ca", "da", где "c" - принять рещение по каждой существующей папке,
                                              "ca" - продолжить создание структуры проекта, сохранив существующие 
                                                     папки и их вложения,     
                                              "da" - удалить все существующие папки и их вложения, и создать заново   
     - вторым аргументом передаеться имя файла структуры проекта по умолчанию file_name='config.yaml'       
    Функция создает логфайл, который будет храниться по пути my_project/mainapp/templates/log_path.txt
    В папку my_project/mainapp/templates/ будет сохранен исходный файл структуры создаваемого проекта        
    :param arg_ca: флаг для команды продолжить создание структуры проекта, сохранив существующие папки и их вложения
    :param arg_da: флаг для команды удалить все существующие папки и их вложения, и создать заново
    :param file_name: имя файла, из которого читаем структору проекта
    """
    temp_list = []
    result_list = []
    i = 0
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            i += 1
            temp_list.clear()
            for n in CONST_LIST:
                if line[n - 3: n] == '|--' and (line[n].isalpha() or line[n] == '_'):
                    temp_tuple = (line[n:].strip())
                    temp_list.append(temp_tuple)
                    break
                else:
                    temp_tuple = None
                    temp_list.append(temp_tuple)
            temp_list_var = temp_list.copy()
            result_list.append(temp_list_var)
    max_len = 0
    for el in result_list:
        len_key_rez = len(el)
        if max_len < len_key_rez:
            max_len = len_key_rez
    for n in range(len(result_list)):
        while len(result_list[n]) < max_len:
            result_list[n].append(None)
    for n in range(len(result_list)):
        if n == 0:
            continue
        for j in range(0, max_len):
            if result_list[n][j] is None:
                result_list[n][j] = result_list[n - 1][j]
            else:
                break
    with open('log_path.txt', 'w', encoding='utf-8') as f_log_path:
        f_log_path.write(f'Начинаем  создание структуры проекта {datetime.datetime.today()}\n')
        for el in result_list:
            while el[-1] == None:
                el.pop()
            if '.' in el[-1]:
                is_file = True
            else:
                is_file = False
            temp_list = '/'.join(el)
            try:
                create_starter_tree(temp_list, is_file, arg_ca, arg_da)
            except:
                print(f"Ошибка!")
                f_log_path.write(f'Ошибка при создании элемента проекта: \n'
                                 f'{temp_list}')
            else:
                f_log_path.write(f'{temp_list} успешно создан {datetime.datetime.today()}\n')
        f_log_path.write(f'Структура проекта успешно создана {datetime.datetime.today()}\n')
    print(f'Работа скрипта завершена.\n'
          f'Файлы log_path.txt и {file_name} находятся в каталоге '
          f'my_project/mainapp/templates')
    shutil.move('log_path.txt', 'my_project/mainapp/templates/log_path.txt')
    shutil.copy(file_name, f'my_project/mainapp/templates/{file_name}')


def create_starter_tree(path, is_file, arg_ca=False, arg_da=False):
    """
    Функция для создания элементов структуры проекта
    :param path: путь создания элемента проекта 
    :param is_file: флаг для параметра являеться ли объект файлом
    :param arg_ca: флаг для команды продолжить создание структуры проекта, сохранив существующие папки и их вложения
    :param arg_da: флаг для команды удалить все существующие папки и их вложения, и создать заново
    """
    user_ansver = "__"
    try:
        if is_file:
            with open(path, 'x', encoding='utf-8'):
                pass
        else:
            os.mkdir(path)
    except FileExistsError as e1:
        if arg_ca or arg_da:
            pass
        else:
            print(f"Ошибка {e1}\n"
                  f"Хотите оставить папку, удалить со всеми вложениями и создать заново, "
                  f"или завершить работу скрипта?")
            user_ansver = input('[c] - продолжить, [d] - удалить и создать заново, '
                                '[e] - завершить работу скрипта.\n')
        if arg_ca or user_ansver.lower() == 'c':
            pass
        elif arg_da or user_ansver.lower() == 'd':
            if is_file:
                with open(path, 'w', encoding='utf-8'):
                    pass
            else:
                rmtree(os.path.join(path))
                os.makedirs(os.path.join(path))
        elif user_ansver.lower() == 'e':
            print('Работа скрипта завершена')
            exit(0)
        else:
            print('Ошибка ввода, работа скрипта завершена')
            exit(1)
    except TypeError as e2:
        print(f'Ошибка {e2}')
    except OSError as e3:
        print(f'Ошибка {e3}')
    except Exception as e4:
        print(f'Ошибка {e4}')


arg_ca = False
arg_da = False
file_name = None
if len(sys.argv) == 1:
    print(f"Хотите оставить существующие папки, удалить со всеми вложениями и создать заново, "
          f"принять рещение по каждой существующей папке "
          f"или завершить работу скрипта?")
    user_ansver = input('[c] - принять рещение по каждой существующей папке,\n'
                        '[e] - завершить работу скрипта.\n'
                        '[ca] - продолжить создание структуры проекта, сохранив существующие '
                        'папки и их вложения,\n'
                        '[da] - удалить все существующие папки и их вложения, и создать заново.\n'
                        'Введите символ: ')
    if user_ansver.lower() == 'ca':
        arg_ca = True
    elif user_ansver.lower() == 'da':
        arg_da = True
    elif user_ansver.lower() == 'c':
        pass
    elif user_ansver.lower() == 'e':
        print('Работа скрипта завершена')
        exit(0)
    else:
        print('Ошибка ввода, работа скрипта завершена')
        exit(1)
    get_dir_list(arg_ca, arg_da)
elif 2 <= len(sys.argv) <= 3:
    if sys.argv[1] == 'ca':
        arg_ca = True
    elif sys.argv[1] == 'da':
        arg_da = True
    elif sys.argv[1] == 'c':
        pass
    else:
        print('Неправильно введен консольный аргумент')
        exit(1)
    if len(sys.argv) == 3:
        file_name = sys.argv[2]
        get_dir_list(arg_ca, arg_da, file_name)
    else:
        get_dir_list(arg_ca, arg_da)
