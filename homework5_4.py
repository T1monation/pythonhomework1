src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[n] for n in range(len(src)) if src[n] > src[n - 1] and n > 0]
print(result)
