"""
    Мой маленький складик)

    Для создания своего склада я позволил себе уточнить и слегка модифицировать ТЗ, что бы оно было менее абстрактным, и
более приближенным к реальности.

    Имеем современный склад (возможно тот, в котором нет людей, и роботизированные манипуляторы загружают и разгружают)
для крупного маркетплейса. Есть родительский класс OfficeEquipment,  в котором описанны общие, интересующие прежде всего
кладовщиков, атрибуты:
  - type_equipment - тип обарудования,
  - weight - его вес (т. к. проект учебный пренебрегаем объемом, иначе ....),
  - brand_name - название бренда,
  - model_name - название модели конкретного образца,
  - item_id - уникальный! номер, который присваевается еденице товара при обработке накладной,
  - storage_id - идентификатор стелажа, присваеваеться в результате погрузки на определенный стелаж,
item_id - условный стикер, который клеят на единицу товара при поступлении его на склад, погрузке и выгрузке на стелаж,
и отправлении потребителю, отделу т т.д.
Классы  Printer, Scanner, Copier  наследуют от  OfficeEquipment и "обрастают" атрибутами параметров конкретного
оборудования. В каждом тз этик классов реализован метод валидации входных данный на соответствие типо этих данных через
альтернативный конструктор класса (метод valid()).

    Реализован класс Shelving  - стелаж, на котором будут храниться товары. У данного класса есть атрибуты:
  _shelving_load  - общая нагрузка на стелаж
  - items_load - атрибут, в котором ведеться учет фактической загрузки стелажа, при добавлении товара на стелаж,
сравниваем с _shelving_load, что бы избежать перегрузки
    item_list  - список погруженных на стелаж товаров, в него щаписываеться атрибут item_id классов, унаследованных от
OfficeEquipment
    Основной фичей Shelving это "магический" метод __iadd__(self, other), который описывает, как загружать на стелаж
товары любого класса, унаследованные от OfficeEquipment

    Класс Storage служит для создания и управления всеми процессами склада.
Его атрибуты:
    shelving_dict - словарь, в котором хранятся все стелажи Shelving, где ключ - номер(id) стелажа, а значение класс
Shelving
    id_set множество, используещееся для хранения уникальных id товаров. при запросах на
добавление/поиск/выгрузку(удаление) товаров со склада, используеться как "быстрая" проверка на наличие id на складе,
что бы избежать лишней переборки словаря shelving_dict
    storage_equipment_list список, состоящий из классов всех товаров добавленных на склад.
    shelving_num - количество стелажей на складе, т.е. фактически размер склада.
    Методы класса Storage:
    create_shelving - инициализирует склад, т.е. заполняет его стеложами количеством shelving_num
    show_storage и show_equipment выводят в консоль содержание shelving_dict и storage_equipment_list соответственно
    add_to_shelving_one()  - добавляем на склад одну еденицу товара, аргумент - класс товара
    add_to_shelving_many() - добавляем на склад любое количество едениц товара, аргумент - список из классов
    find_item() - поиск товара на складе по атрибуту класса товара item_id, аргументы item_id, internal_find_flag
Для пользовательского поиска - internal_find_flag=False
    remove_item_one() - отгрудаем/удаляем со склада одну еденицу товара, аргумент атрибут класса товара item_id
    remove_item_many() - отгрудаем/удаляем со склада любое количество едениц товара, аргумент список из атрибутов класса
товара item_id
    upload_shelving_dict() выгрузка в файл shelving_dict и storage_equipment_list, аргумент - file_name, в резулютате
работы метода создается два файла вида {file_name}_storage.yaml и {file_name}_items.yaml в которых выгружаються
shelving_dict и storage_equipment_list соответственно. С сериализацией в YAML только знакомлюсь, функция
эксперементальная,  планирую добавить возможность загрузки склада из файл.

    Немного о логике работы - при добавлении товара мы добавляем целиком класс товара, на основании этого формируем
shelving_dict(карта - что где валяется) и storage_equipment_list(что вообще еть на складе). После добавления у нас есть
item_id и все дальнейние операции мы проводим ариентируясь исключительно на этот уникальный атрибут.

    P.S. Добавляйте пожалуйста "стоп-слово" в домашнем задании, а то, как у нас в группе в телеге написали, так и до
    коммерческой разработки недалеко)
"""
import yaml
import datetime


class ShelvingFullError(Exception):
    pass


class ExistInShelvingError(Exception):
    pass


class OfficeEquipment:

    def __init__(self, type_equipment, weight, brand_name, model_name,
                 item_id=None, storage_id=None, ):
        self.weight = weight
        self.type_equipment = type_equipment
        self.brand_name = brand_name
        self.model_name = model_name
        self.item_id = item_id
        self.storage_id = storage_id


class Printer(OfficeEquipment):
    def __init__(self, type_equipment, weight, brand_name, model_name,
                 item_id=None, storage_id=None, duplex_print=False):
        super().__init__(type_equipment, weight, brand_name, model_name, item_id, storage_id)
        self.duplex_print = duplex_print

    def __str__(self):
        return f'Принтер {self.brand_name, self.model_name}, серийный номер {self.item_id}, с возможностью ' \
               f'двухсторонней печати: {"да" if self.duplex_print else "нет"} ' \
               f'{f"стелаж хранения {self.storage_id}" if self.storage_id else " "}'

    @staticmethod
    def valid(type_equipment, weight, brand_name, model_name,
              item_id, storage_id=None, duplex_print=False):
        try:
            assert type(type_equipment) == str
            assert type(weight) == int or type(weight) == float
            assert type(brand_name) == str
            assert type(model_name) == str
            assert type(item_id) == int
            assert type(storage_id) == str or storage_id is None
            assert type(duplex_print) == bool
        except AssertionError:
            print(f'Неправильный тип вводимых данных для {type_equipment} {item_id}')
        else:
            return Printer(type_equipment, weight, brand_name, model_name,
                           item_id, storage_id, duplex_print)


class Scanner(OfficeEquipment):
    def __init__(self, type_equipment, weight, brand_name, model_name, scan_resolution,
                 item_id=None, storage_id=None, duplex_scan=False):
        super().__init__(type_equipment, weight, brand_name, model_name, item_id, storage_id)
        self.scan_resolution = scan_resolution
        self.duplex_scan = duplex_scan

    def __str__(self):
        return f'Сканер {self.brand_name, self.model_name}, серийный номер {self.item_id}, с возможностью ' \
               f'двухстороннего сканирования: {"да" if self.duplex_scan else "нет"} ' \
               f'{f"стелаж хранения {self.storage_id}" if self.storage_id else " "}'

    @staticmethod
    def valid(type_equipment, weight, brand_name, model_name, scan_resolution,
              item_id, storage_id=None, duplex_scan=False):
        try:
            assert type(type_equipment) == str
            assert type(weight) == int or type(weight) == float
            assert type(brand_name) == str
            assert type(model_name) == str
            assert type(scan_resolution) == str
            assert type(item_id) == int
            assert type(storage_id) == str or storage_id is None
            assert type(duplex_scan) == bool
        except AssertionError:
            print(f'Неправильный тип вводимых данных для {type_equipment} {item_id}')
        else:
            return Scanner(type_equipment, weight, brand_name, model_name, scan_resolution,
                           item_id, storage_id, duplex_scan)


class Copier(OfficeEquipment):
    def __init__(self, type_equipment, weight, brand_name, model_name, scan_resolution,
                 item_id, storage_id=None, duplex_scan=False, duplex_print=False):
        super().__init__(type_equipment, weight, brand_name, model_name, item_id, storage_id)
        self.scan_resolution = scan_resolution
        self.duplex_scan = duplex_scan
        self.duplex_print = duplex_print

    def __str__(self):
        return f'МФУ {self.brand_name, self.model_name}, серийный номер {self.item_id}, с возможностью ' \
               f'двухсторонней печати: {"да" if self.duplex_print else "нет"}, ' \
               f'двухстороннего сканирования: {"да" if self.duplex_scan else "нет"}, ' \
               f'{f"стелаж хранения {self.storage_id}" if self.storage_id else " "}'

    @staticmethod
    def valid(type_equipment, weight, brand_name, model_name, scan_resolution,
              item_id, storage_id=None, duplex_scan=False, duplex_print=False):
        try:
            assert type(type_equipment) == str
            assert type(weight) == int or type(weight) == float
            assert type(brand_name) == str
            assert type(model_name) == str
            assert type(scan_resolution) == str
            assert type(item_id) == int
            assert type(storage_id) == str or storage_id is None
            assert type(duplex_scan) == bool
            assert type(duplex_print) == bool
        except AssertionError:
            print(f'Неправильный тип вводимых данных для {type_equipment} {item_id}')
        else:
            return Copier(type_equipment, weight, brand_name, model_name, scan_resolution,
                          item_id, storage_id, duplex_scan, duplex_print)


class Shelving:
    _shelving_load = 400
    items_load = 0
    item_list = []

    def __init__(self, shelving_id, ):
        self.shelving_id = shelving_id
        self.item_list = self.item_list.copy()

    def __str__(self):
        return f'Стелаж №{self.shelving_id} грузоподъемностью {self._shelving_load}, ' \
               f'содержит следующие складские позиции:\n' \
               f'{self.item_list}'

    def __iadd__(self, other):
        if other.item_id in self.item_list:
            raise ExistInShelvingError
        elif self.items_load + other.weight > self._shelving_load:
            raise ShelvingFullError
        else:
            self.item_list.append(other.item_id)
            self.items_load += other.weight
            return self


class Storage:
    shelving_dict = {}
    id_set = set()
    storage_equipment_list = []

    def __init__(self, shelving_num):
        self.shelving_num = shelving_num

    @property
    def create_shelving(self):
        self.shelving_dict.clear()
        self.shelving_dict = {f'shelving_{key:04d}': key for key in range(1, self.shelving_num + 1)}
        for key in self.shelving_dict:
            self.shelving_dict[key] = Shelving(f'{key}')
        return self.shelving_dict

    @property
    def show_storage(self):
        for k in self.shelving_dict:
            print(self.shelving_dict[k])

    @property
    def show_equipment(self):
        for item in self.storage_equipment_list:
            print(item)

    def add_to_shelving_one(self, obj):
        if obj.item_id in self.id_set:
            print(f'{obj.type_equipment}: {obj.item_id} уже находится на складе!')
        else:
            for key in self.shelving_dict:
                try:
                    temp_obj = self.shelving_dict.get(key)
                    temp_obj += obj
                except ShelvingFullError:
                    print(f"Перегруз стелажа:\n{key}")
                    pass
                except ExistInShelvingError:
                    print(f'{obj.type_equipment}: {obj.item_id} уже находится на стелаже {key}')
                    pass
                else:
                    self.id_set.add(obj.item_id)
                    obj.storage_id = key
                    self.storage_equipment_list.append(obj)
                    break

    def add_to_shelving_many(self, item_list):
        for el in item_list:
            self.add_to_shelving_one(el)

    def find_item(self, item_id, internal_find_flag=False):
        if item_id in self.id_set:
            for key in self.shelving_dict:
                if not internal_find_flag:
                    if item_id in self.shelving_dict[key].item_list:
                        return f'Позиция с id-номером {item_id} находиться на стелаже' \
                               f' {self.shelving_dict[key].shelving_id}'
                else:
                    if item_id in self.shelving_dict[key].item_list:
                        return key
        else:
            if not internal_find_flag:
                return f'Позиция с id-номером {item_id} на складе не найдена'
            else:
                raise ExistInShelvingError

    def remove_item_one(self, item_id):
        try:
            if item_id in self.id_set:
                found_key = self.find_item(item_id, True)
                self.shelving_dict[found_key].item_list.remove(item_id)
                for el in self.storage_equipment_list:
                    if el.item_id == item_id:
                        self.storage_equipment_list.remove(el)
            else:
                raise ExistInShelvingError
        except (ExistInShelvingError, KeyError):
            print(f'Неверный id-номер {item_id} для выгрузки со склада')
        else:
            print(f'Позиция с id-номером {item_id} выгруженна со склада')

    def remove_item_many(self, item_list):
        for el in item_list:
            self.remove_item_one(el)

    def upload_shelving_dict(self, storage_name):
        try:
            with open(f'{storage_name}_storage.yaml', 'x', encoding='utf-8') as f_dict:
                yaml.dump(f'Состояние склада на {datetime.datetime.now()}', f_dict)
                yaml.dump(self.shelving_dict, f_dict)
            with open(f'{storage_name}_items.yaml', 'x', encoding='utf-8') as f_list:
                yaml.dump(f'Состояние товаров на складе на {datetime.datetime.now()}', f_list)
                yaml.dump(self.storage_equipment_list, f_list)
        except FileExistsError:
            print(f'Файл {storage_name} существует, введите другое имя склада')


printer_1 = Printer.valid('Printer', 3, 'HP', '1010', 10155)
scaner_1 = Scanner.valid('Scanner', 3, "epson", 'fd-34k', '3000x2000', 17485)
copier_1 = Copier.valid('Copier', 8, 'Xerox', 'fg_897', '3000x2000', 758465, duplex_print=True, duplex_scan=True)
my_storage = Storage(5)
print(printer_1)
my_storage.create_shelving
my_storage.add_to_shelving_many([printer_1, scaner_1, copier_1])
my_storage.show_storage

print(my_storage.id_set)
printer_2 = Printer('Printer', 300, 'HP', '1010', 10156)
printer_7 = Printer('Printer', 5, 'HP', '1010', 10158)
printer_8 = Printer('Printer', 200, 'HP', '1010', 10159)
printer_list = [printer_1, printer_2, printer_7, printer_8]
#
my_storage.add_to_shelving_many(printer_list)

my_storage.upload_shelving_dict('my_storage')
# my_storage.show_storage
# print(my_storage.find_item(10158))
my_storage.remove_item_one(10158)
# my_storage.show_storage
# print(my_storage.find_item(10158))
# del_list = [10156, 10155, 10156]
# my_storage.remove_item_many(del_list)
# my_storage.show_storage
# my_storage.show_equipment
my_storage.remove_item_one(758465)
# my_storage.show_storage
# my_storage.show_equipment
