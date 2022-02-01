import datetime


class DateValidationError(Exception):
    pass


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extractor(cls, date):
        date_list = [int(el) for el in date.split('-')]
        return date_list

    @staticmethod
    def valid_date(date):
        """ Валидируем строку даты с помощью модуля datatime. Проверка идет как на соответствие формату dd-mm-yyyy,
            так и на корректность введенной даты, т.е. ошибка поднимаеться при вводе 32 дня, 13 месяца...
            При прохождении валидации, срабатывает как альтернативный конструктор."""
        try:
            date_form = datetime.datetime.strptime(date, '%d-%m-%Y')
        except (ValueError, DateValidationError):
            print(f'Date string "{date}" does not match format in "dd-mm-yyyy"')
        else:
            return Date(datetime.datetime.strftime(date_form, '%d-%m-%Y'))


# строка с датой которая пройдет валидацию:
date_string = '14-11-1989'
new_date = Date.valid_date(date_string)  # Получаем экземпляр класса с данными прошедшими валидацию
print(new_date)
print(new_date.date)
print(new_date.extractor(new_date.date))  # Получаем список из чисел даты
print(Date.extractor(date_string))

# Строка которая валидацию непройдет:
wrong_date = '32-12-2001'
else_date = Date.valid_date('32-12-2001')
else_date = Date(wrong_date)  # По условию задачи класс может принимать и невалидные данные
print(else_date.extractor(wrong_date))
print(Date.extractor(wrong_date))
