# Lesson 4

class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print('New car: ', self.name, 'color', 'is police?', self.is_police)

    def go(self):
        print(self.name, 'car is going')

    def stop(self):
        print(self.name, 'car stopped')

    def turn(self, direction):
        print(self.name, 'car turned to', direction)

    def show_speed(self):
        print(self.name, 'cars speed is', self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.name, 'cars speed is', self.speed)


class WorkCar(Car):
    def show_speed(self):
        print(self.name, 'cars speed is', self.speed)


class Sportcar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar('Bus', 'yellow', 50)
town_car.turn(0)
town_car.show_speed()

work_car = WorkCar('Truck', 'blue', 70)
work_car.go()
work_car.show_speed()

police_car = PoliceCar('Police', 'white', 120)
police_car.stop()
police_car.show_speed()
print(police_car.is_police)
