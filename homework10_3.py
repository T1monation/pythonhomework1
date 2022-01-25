class Cell:
    def __init__(self, cell_type, cell_number, order_number):
        self.cell_type = cell_type
        self.cell_number = cell_number
        self.order_number = order_number

    def __str__(self):
        return f'Клетка типа: {self.cell_type}, Количество ячеек в клетке: {self.cell_number}'

    def __add__(self, other):
        return Cell(f'{self.cell_type}[+]{other.cell_type}', self.cell_number + other.cell_number, self.order_number)

    def __sub__(self, other):
        if self.cell_number > other.cell_number:
            return Cell(f'{self.cell_type}[-]{other.cell_type}',
                        self.cell_number - other.cell_number, self.order_number)
        else:
            raise ValueError(f'Количество ячеек клетки {other.cell_type} больше {self.cell_type}')

    def __mul__(self, other):
        return Cell(f'{self.cell_type}[*]{other.cell_type}',
                    self.cell_number * other.cell_number,
                    self.order_number)

    def __truediv__(self, other):
        return Cell(f'{self.cell_type}[//]{other.cell_type}', self.cell_number // other.cell_number, self.order_number)

    @property
    def make_order(self):
        temp_str = f'Ячейки клетки {self.cell_type}, по {self.order_number} шт. в строке:\n'
        for i in range(1, self.cell_number):
            temp_str += '*'
            if i % self.order_number == 0:
                temp_str += '\n'
        return temp_str


cell_1 = Cell('Animal', 48, 4)
print(cell_1)
cell_2 = Cell('Plant', 52, 6)
print(cell_2)
print('Сложение клеток:')
cell_add = cell_1 + cell_2
print(cell_add)
print('Вычитание клеток:')
cell_sub = cell_2 - cell_1
print(cell_sub)
# print('Вычитание клеток с ошибкой:')
# cell_sub = cell_1 - cell_2
print('Умножение клеток:')
cell_mul = cell_1 * cell_2
print(cell_mul)
print('Целочисленное деление клетки:')
cell_truediv = cell_2 / cell_1
print(cell_truediv)
print("~~~~~~~~~~~~~~~~")
print(cell_2.make_order)
