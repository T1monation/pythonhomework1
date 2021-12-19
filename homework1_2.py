
new_list = []
for i in range(1, 1001):  # формируем список кубов нечетных чисел
    if i % 2 != 0:
        new_list.append(i ** 3)


# при желании можем просмотреть список убрав "#" строкой ниже
# print(new_list)


# Функция для проверки условия суммы цифр числа / 7, если условие выполняеться, функция возвращает это же число,
# ксли условие не выполняется - функция возвращает 0
def division_7(number):
    number_1 = number % 10
    number_2 = (number % 100) // 10
    number_3 = (number % 1000) // 100
    number_4 = (number % 10000) // 1000
    number_5 = (number % 100000) // 10000
    number_6 = (number % 1000000) // 100000
    number_7 = (number % 10000000) // 1000000
    number_8 = (number % 100000000) // 10000000
    number_9 = (number % 1000000000) // 100000000
    sum_number = number_1 + number_2 + number_3 + number_4 + number_5 + number_6 + number_7 + number_8 + number_9
    if sum_number % 7 == 0:
        return number
    else:
        return 0


result_one = 0
result_two = 0

# В одном цикле мы перебираем весь список,  в переменную result_one мы сохраняем сумму значений из фунции division_7
#  в переменную result_two тоже самое, чтолько увеличенное на 17
for i in range(len(new_list)):
    result_one += division_7(new_list[i])
    # if division_7(new_list[i]) > 0:
    #    print('a', division_7(new_list[i]))
    result_two += division_7(new_list[i] + 17)
    # if division_7(new_list[i] + 17) > 0:
    #    print('b', division_7(new_list[i] + 17))

print('Результат задачи: ', result_one)
print('Результат задачи, с увеличением на 17:', result_two)
