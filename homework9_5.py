class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки ручкой')


class Penсil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки карандашом')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки маркером')


Stationery.draw('Test')

blue_pen = Pen('Документы')
blue_pen.draw()

black_pencil = Penсil('Рисунок')
black_pencil.draw()

yellow_handle = Handle('Правка')
yellow_handle.draw()
