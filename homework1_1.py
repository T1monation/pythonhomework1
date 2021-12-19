duration = int(input('Введите время в секундах: '))

if duration // 60 < 1:  # проверяем продолжительность времени < минуты
    print(f'{duration} сек')
elif duration // 3600 < 1:  # проверяем продолжительность времени < часа
    minute_duration = duration // 60
    second_duration = duration % 60
    print(f'{minute_duration} мин {second_duration} сек')
elif duration // 86400 < 1:  # проверяем продолжительность времени < суток
    hour_duration = duration // 3600
    minute_duration = (duration % 3600) // 60
    second_duration = (duration % 3600) % 60
    print(f'{hour_duration} час {minute_duration} мин {second_duration} сек')
elif duration // 86400 >= 1:  # проверяем продолжительность времени >= суток
    day_duration = duration // 86400
    hour_duration = (duration % 86400) // 3600
    minute_duration = ((duration % 86400) % 3600) // 60
    second_duration = ((duration % 86400) % 3600) % 60
    print(f'{day_duration} дн {hour_duration} час {minute_duration} мин {second_duration} сек')
    pass
