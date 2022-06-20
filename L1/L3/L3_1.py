# Lesson 3.1

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Division to O is prohibited'


x = int(input('Enter dividend: '))
y = int(input('Enter divider: '))

print(division(x, y))
