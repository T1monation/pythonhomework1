# Функция для определения склонения слова "процент" и вывод на печать
def persent_print(number):
    if 11 <= number <= 19:
        print(f'{number} процентов')
    elif 5 <= number % 10 <= 9 or number % 10 == 0:
        print(f'{number} процентов')
    elif 2 <= number % 10 <= 4:
        print(f'{number} процента')
    elif number % 10 == 1:
        print(f'{number} процент')


for i in range(1, 101):
    persent_print(i)
