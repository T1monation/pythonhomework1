with open('users.csv', 'r', encoding='utf-8') as f_u, \
        open('hobby.csv', 'r', encoding='utf-8') as f_h, \
        open('users_hobby.txt', 'w', encoding='utf-8') as f_w:
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
