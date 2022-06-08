# Lesson 4.1

from sys import argv

script_name, man_hours, rate, bonus = argv

salary = int(man_hours) * int(rate) + int(bonus)

print(salary)