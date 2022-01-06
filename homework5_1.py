def gen_num(n):
    """
     Генератор нечетных чисел
    :param n: Число, до которого работает генератор (включительно)
    :return: нечетные числа от 1 до n
    """
    for num in range(1, n + 1):
        if num % 2 != 0:
            yield num


count = int(input('Веедите число, включая которое будет работать генератор: '))
nums = gen_num(count)
print(nums)
print(type(nums))
print(*nums)
