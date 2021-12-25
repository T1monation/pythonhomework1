def num_translate_adv(number):
    """Function translate numbers from 0 to 10, with capital and non-capital letters"""
    translate_dic = {'zero': 'ноль',
                     'one': 'один',
                     'two': 'два',
                     'tree': 'три',
                     'four': 'четыре',
                     'five': 'пять',
                     'six': 'шесть',
                     'seven': 'семь',
                     'eihgt': 'восемь',
                     'nine': 'девять',
                     'ten': 'десять'
                     }

    if number[0].isupper():  # Проверяем на наличие первой заглавной буквы
        number = number.lower()  # Преобразуем строку к строчным буквам
        if translate_dic.get(number):
            return translate_dic.get(
                number).capitalize()  # Если первая буква была заглавная возвращаем строку с заглавной
        else:
            return None
    else:
        return translate_dic.get(number)  # Если первая буква не была заглавной, возвращаем все строчные


translate = input('Для перевода ведите на английском число от 0 до 10: ')
print(f'"{num_translate_adv(translate)}"')
