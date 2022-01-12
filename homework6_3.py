with open('users.csv', 'r', encoding='utf-8') as f_u, \
        open('hobby.csv', 'r', encoding='utf-8') as f_h:
    user_list = [user[:-1] for user in f_u]     # Формируем списки строк из файлов
    hobby_list = [hobby[:-1] for hobby in f_h]  #
if len(user_list) < len(hobby_list):  # Выходим с кодом 1 если в файле, хранящем данные о хобби, больше записей, чем в
    exit(1)                           # файле с ФИО
else:
    while len(user_list) > len(hobby_list):
        hobby_list.append(None)
    result_dict = {key: value for key, value in zip(user_list, hobby_list)}
    print(result_dict)
