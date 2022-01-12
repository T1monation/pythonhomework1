import sys


def user_hobby(file_user='users.csv', file_hobby='hobby.csv', file_result='users_hobby.txt'):
    with open(file_user, 'r', encoding='utf-8') as f_u, \
            open(file_hobby, 'r', encoding='utf-8') as f_h, \
            open(file_result, 'w', encoding='utf-8') as f_w:
        while True:
            line_1 = f_u.readline()[:-1]
            line_2 = f_h.readline()[:-1]
            f_w.write(f'{line_1}: {line_2}\n')
            if line_1 and not line_2:
                line_2 = None
            elif line_2 and not line_1:
                exit(1)
            elif not line_1:
                break


# В этом ветвлении мы закладываем возможность передавать разное количество и состав аргументов при запуске из консоли
if sys.argv[1]:
    user_hobby(sys.argv[1])
elif sys.argv[2]:
    user_hobby(sys.argv[1], sys.argv[2])
elif sys.argv[3]:
    user_hobby(sys.argv[1], sys.argv[2], sys.argv[3])
