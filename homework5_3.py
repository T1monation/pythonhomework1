def gen_tutor_klass(list_1, list_2):
    """
    Функция, которая принимает на вход два списка, и возвращает кортежи
    состоящие из элементов двух списков
    """
    list_1_copy = list_1.copy()
    list_2_copy = list_2.copy()
    if list_1_copy > list_2_copy:  # Учитываем условие если tutors больше klasses
        while len(list_2_copy) < len(list_1_copy):
            list_2_copy.append(None)
    elif list_1_copy < list_2_copy:  # Учитываем условие если tutors меньше klasses
        while len(list_1_copy) < len(list_2_copy):
            list_2_copy.pop()
    for item_1, item_2 in zip(list_1_copy, list_2_copy):
        yield (item_1, item_2)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Константин', 'Федор'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

people = gen_tutor_klass(tutors, klasses)
print(people)
print(type(people))
try:
    while True:
        print(next(people))

except StopIteration:
    pass
