import requests
import datetime
from decimal import Decimal


def currency_rates(input_code):
    input_code = input_code.upper()  # Нивилируем регистр входных двнных кода валюты
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')  # Запрашиваем данные сайта банка
    content = response.content.decode(encoding=response.encoding)
    char_code = []
    nominal_name = []
    currency_exchange = []
    result_dic = {}
    for el in content.split('CharCode>')[1:]:  # Из content фильтруем код валюты, и сохраняем в отделный список
        char_code.append(el.split('<')[0])
    for el in content.split('Date="')[1:]:  # Из content фильтруем дату курса, и сохраняем в переменную
        current_date = (el.split('"')[0])
        # Преобразуем полученную дату в формат datetime
        current_date = datetime.datetime.strptime(current_date, "%d.%m.%Y")
    for el in content.split('Name>')[1:]:  # Из content фильтруем название валюты, и сохраняем в отделный список
        nominal_name.append(el.split('<')[0])
    for el in content.split('Value>')[1:]:  # Из content фильтруем курс валюты, и сохраняем в отделный список
        el = el.split('<')[0]
        el = el.replace(",", ".")
        currency_exchange.append(el)
    for code, name, curr in zip(char_code, nominal_name, currency_exchange):
        result_dic.setdefault(code, [name, curr])  # Формируем словарь, ключ = код валюты

    if result_dic.get(input_code):
        return result_dic[input_code][0], Decimal(result_dic[input_code][1]), current_date.strftime("%d.%m.%Y")
    else:
        return None
