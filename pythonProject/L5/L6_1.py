# Lesson 6.1

import time


class TrafficLight:

    def __init__(self):
        self.__color = 'green'

    def running(self):
        print('red')
        time.sleep(7)
        print('yellow')
        time.sleep(2)
        print('green')
        time.sleep(5)


tlight = TrafficLight()
tlight.running()