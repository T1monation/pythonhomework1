def thesaurus_adv(*names):
    """
    Function sorts the list by first letter
    """
    result_dic = {}
    for name in names:  # Извлекаем список имен из кортежа *names
        if name:
            name_list = name.copy()
    temp_list = []
    name_list_rev = []
    for name in name_list:                                           # Принимаем список 'Имя Фамилия"
        temp_list = name.split()                                     # и разворачиваем его к виду 'Фамилия Имя'
        temp_list.reverse()                                          #
        name_list_rev.append(temp_list[0] + ' ' + temp_list[1])      #
    pass_list = []                                                   #
    for item in name_list_rev:  # Заполняем пустой словарь ключами и пустыми списками для каждого ключа
        result_dic[item[0]] = pass_list
    for key in result_dic.keys():  # Перебираем словарь по ключам
        add_list = []
        for name in name_list_rev:  # Сравниваем первую букву имени из списка и ключем
            if name[0] == key:
                add_list.append(name)  # Формируем список совпадений имен с ключем
            result_dic[key] = add_list  # Записываем получившийся список по ключу в словарь
    return result_dic


people_list = ['Мария Иванова', 'Мирон Петров', 'Михаил Кабачков',
               'Андрей Ивлев', 'Артем Касаткин', 'Николай Помидоров',
               'Никита Калиткин', 'Георгий Бидонов']
print(thesaurus_adv(people_list))
