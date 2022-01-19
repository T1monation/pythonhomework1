import re

# В паттерне регулярного вырожения учтены домены гос. организаций вида @nnn.gov.vv, или британии  @nnn.co.uk
RE_EMAIL = re.compile(r"([\w\.\-]+)@(\w+\.[a-z]+$|\w+\.\w+\.[a-z]+$)")


def email_parse(email):
    return {'username': RE_EMAIL.match(email).group(1), 'domain': RE_EMAIL.match(email).group(2)}


mail_list = ('someone@geekbrains.ru',
             '4timonaton@gmail.com',
             'angry-ronny@hotmail.com',
             'ask.me@69flag.by',
             'uzgs@mvd.gov.by',
             'someone@geekbrainsru',
             'someonegeekbrains.ru',
             'someo ne@geekbrainsru',
             'someone@geekbrain s.ru',
             'someone@geekbrains.ru5')

result_list = []
for el in mail_list:
    try:
        a = email_parse(el)
    except AttributeError as e:
        # Так как конструкция RE_EMAIL.match(email) при не соответсявии аргумента паттерну выдает None,
        # применение атрибута .group() вызывает ошибку AttributeError: 'NoneType' object has no attribute 'group' .
        # В блоке except перехватываем эту ошибку, т.к. email адрес не прошел валидацию
        print(f'Email адрес "{el}" неправильный!!')
    else:
        result_list.append(a)
print(result_list)
