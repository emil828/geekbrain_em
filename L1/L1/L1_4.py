# Lesson 1.4

num = int(input("Enter any number: "))

maxx = 0
while num > 10:
    temp_max = num % 10
    num //= 10
    if temp_max > maxx:
        maxx = temp_max

print(maxx)
