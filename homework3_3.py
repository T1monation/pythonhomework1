def thesaurus(*names):
    """
    Function sorts the list by first letter
    """
    result_dic = {}
    for name in names:  # Извлекаем список имен из кортежа *names
        if name:
            name_list = name.copy()
    pass_list = []
    for item in name_list:  # Заполняем пустой словарь ключами и пустыми списками для каждого ключа
        result_dic[item[0]] = pass_list
    for key in result_dic.keys():  # Перебираем словарь по ключам
        add_list = []
        for name in name_list:  # Сравниваем первую букву имени из списка и ключем
            if name[0] == key:
                add_list.append(name)  # Формируем список совпадений имен с ключем
            result_dic[key] = add_list  # Записываем получившийся список по ключу в словарь
    return result_dic


people_list = ['Мария', 'Мирон', 'Михаил', 'Андрей', 'Артем', 'Николай', 'Никита', 'Георгий']
print(thesaurus(people_list))
