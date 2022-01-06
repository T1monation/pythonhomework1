def num_translate(number):
    """Function translate numbers from 0 to 10"""
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

    return translate_dic.get(number)


translate = input('Для перевода ведите на английском число от 0 до 10: ')
print(f'"{num_translate(translate)}"')
