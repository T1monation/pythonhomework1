from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

# Решение "в лоб")
start = perf_counter()
result_1 = []
for el in src:
    if src.count(el) == 1:
        result_1.append(el)
print(result_1)
print(1, perf_counter() - start)

# Решение с оптимизацией (быстрее)
start = perf_counter()
result_2 = [el for el in src if src.count(el) == 1]
print(result_2)
print(2, perf_counter() - start)

# Решение через множество (еще быстрее)
start = perf_counter()
unique_nums = set()
repeated_nums = set()
for num in src:
    if num in repeated_nums:
        continue
    if num in unique_nums:
        unique_nums.discard(num)
        repeated_nums.add(num)
        continue
    unique_nums.add(num)
result_3 = [num for num in src if num in unique_nums]
print(result_3)
print(3, perf_counter() - start)

# Решение через словари
start = perf_counter()
result_dict_1 = {}
for el in src:
    result_dict_1.setdefault(el)
result_4 = result_dict_1.keys()
print(list(result_4))
print(4, perf_counter() - start)

# Еще одно решение через словари
start = perf_counter()
result_dict_2 = {el: None for el in src}
print(list(result_dict_2))
print(5, perf_counter() - start)
