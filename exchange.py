import utils
import sys

# При запуске из консоли передавать параметром код валюты, регистр неважен
# В блоке try выполняется код с вызовом из консоли, в блоке except выполняется код ели запускать сам файл
try:
    if sys.argv[1]:
        print(utils.currency_rates(sys.argv[1]))
except:
    a = input('Введите код валюты: ')
    print(utils.currency_rates(a))
    rezult = utils.currency_rates(a)[1] # Выделяем из кортежа значение курса
    print(rezult)  # проверяем значение и тип данных курса валюты
    print(type(rezult))
    print(utils.currency_rates('USD'))
    print(utils.currency_rates('eur'))
