class Worker:
    name = 'user_name'
    surname = 'user_surname'
    position = 'user_position'
    _wage = 0
    _bonus = 0
    _income = {'wage': _wage, 'bonus': _bonus}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = wage
        self._bonus = bonus
        self._income = {'wage': self._wage, 'bonus': self._bonus}


class Position(Worker):
    def full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker_1 = Position('Иван', 'Грозный', 'Царь', 1000, 500)
print(worker_1.full_name())
print(worker_1.get_total_income())
print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
print(worker_1._wage)
print(worker_1._bonus)
print(worker_1._income)
