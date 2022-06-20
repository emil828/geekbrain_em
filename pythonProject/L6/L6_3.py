# Lesson 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        # wage = 0
        # bonus = 0
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname

    def get_full_profit(self):
        return sum(self._income.values())


worker1 = Position('Emil', 'Mehdiyev', 'employee', {'profit': 10000, 'bonus': 15000})

print(worker1.get_full_name())
print(worker1.get_full_profit())
