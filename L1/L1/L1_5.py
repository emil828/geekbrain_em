# Lesson 1.5

profit = int(input("Enter your profit: "))
expenses = int(input("Enter your expenses: "))

income = profit - expenses

if income >= 0:
    print('You are in profit')
else:
    print('You are in loss')
