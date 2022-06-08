# Lesson 1.7

start = int(input("Start in km: "))
target = int(input("Target in km: "))

day = 1

while start <= target:
    start = start + start * 0.1
    day += 1

print('You reached your target on', day, 'day')

