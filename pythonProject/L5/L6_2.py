# Lesson 6.2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass = 1.25

    def asphalt_mass(self):
        return self._length * self._width * self._mass


new_road = Road(5000, 20)
new_road_mass = new_road.asphalt_mass()
print(new_road_mass)
