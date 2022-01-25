from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def textile_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def textile_consumption(self):
        return f'Расход ткани на пальто {self.name} составит {(float(self.size) / 6.5 + 0.5):.2f} погонных метра'


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def textile_consumption(self):  # Размер указываем в сантиметрах, и переводим в метры
        return f'Расход ткани на костюм {self.name} составит {(float(self.height) / 100 * 2 + 0.3):.2f} погонных метра'


coat_1 = Coat('Guchi', 56)
print(coat_1.textile_consumption())

suit_1 = Suit('Armani', 196)
print(suit_1.textile_consumption)
