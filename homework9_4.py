class Car:
    speed = 60
    color = 'Black'
    name = 'Car_Name'
    is_police = False
    direction = None
    speed_limit = 0

    def __init__(self, name, speed, color, direction, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.direction = direction

    def car_go(self):
        print('Wruuum!')
        print(f'Car {self.name} rides!')

    def car_stop(self):
        print('Sh-h-h-h-h-h...')
        print(f'Car {self.name} stopped.')

    def car_turn(self):
        print(f'Car {self.name} turn {self.direction}')

    def show_speed(self):
        print(f'Car speed is {self.speed}')

    def show_car(self):
        print(self.car_go())
        print(self.show_speed())
        print(self.car_turn())
        print(self.car_stop())


class TownCar(Car):
    def __init__(self, name, speed, color, direction, is_police=False, town_car_work=False):
        super().__init__(name, speed, color, direction, is_police)
        self.town_car_work = town_car_work

    def show_speed(self):
        print(f'Car speed is {self.speed}')
        if int(self.speed) > 60:
            print(f'Car {self.name} goes faster then speed limit {self.speed_limit}!')

    def work_car(self):
        if self.town_car_work:
            print('Taxi arrived')


class WorkCar(Car):
    def __init__(self, name, speed, color, direction, is_police=False, cleaning=False):
        super().__init__(name, speed, color, direction, is_police)
        self.cleaning = cleaning

    def show_speed(self):
        print(f'Car speed is {self.speed}')
        if int(self.speed) > 40:
            print(f'Car {self.name} goes faster then speed limit {self.speed_limit}!')

    def cleaning_garbage(self):
        if self.cleaning:
            print('No garbage is here')


class SportCar(Car):
    def __init__(self, name, speed, color, direction, is_police=False, convertible=False):
        super().__init__(name, speed, color, direction, is_police)
        self.convertible = convertible

    def roof_open(self):
        if self.convertible:
            print('Lest ride! Roof is open!')


class PoliceCar(Car):
    def __init__(self, name, speed, color, direction, is_police=True, police_siren=False):
        super().__init__(name, speed, color, direction, is_police)
        self.police_siren = police_siren

    def police_siren_work(self):
        if self.police_siren:
            print('Wee-oo, Wee-oo, Wee-oo')


print('~~~~~~~~~Police~~~~~~~~~~')
police = PoliceCar("UAZ", 1000, 'White/Blue', 'Left', True, True)
police.show_car()
police.police_siren_work()

print('~~~~~~~~~Taxi~~~~~~~~~~')
taxi = TownCar('London Cab', 65, 'Black', 'Right', town_car_work=True)
taxi.show_car()
taxi.work_car()

print('~~~~~~~~~Garbage truck~~~~~~~~~~')
garbage_truck = WorkCar('Iveco', 45, 'Green', 'Back', cleaning=True)
garbage_truck.show_car()
garbage_truck.cleaning_garbage()

print('~~~~~~~~~Ferrari~~~~~~~~~~')
ferrari = SportCar('Ferrari California', 320, 'Red', 'Strait', convertible=True)
ferrari.show_car()
ferrari.roof_open()
