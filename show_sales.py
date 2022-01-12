import sys

""" В каждом блоке ветвления мы открываем файл, для того, что бы избежать ошибки, когда курсор уже блуждает
по файлу, и может быть некоректный перебор строк в файле. Учитывая, что согласно заданию, предпологаеться 
однократный консольный запуск, на производительность это не повлияет.
"""
if len(sys.argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        n = 0
        for line in f:
            n += 1
            if n == int(sys.argv[1]):
                print(line[:-1])

elif len(sys.argv) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        n = 0
        for line in f:
            n += 1
            if int(sys.argv[1]) <= n <= int(sys.argv[2]):
                print(line[:-1])
else:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line[:-1])
