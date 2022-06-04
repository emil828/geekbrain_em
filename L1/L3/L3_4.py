def power(a, b):
    return a ** b


# def power_cycle(a, b):
#     for i in range(1, abs(b) + 1):
#         a = (1 / a) * (1 / a)
#     return a


x = int(input('Enter a positive number: '))
y = int(input('Enter a negative number: '))

print(power(x, y))
# print(power_cycle(x, y))
