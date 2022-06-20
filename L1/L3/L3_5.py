# Lesson 3.5

symbols = '!@#$%^&*()'


def num_func(numbers):
    res = 0
    for i in range(len(numbers)):
        if numbers[i] in symbols:
            break
        res += int(numbers[i])
    return res


numbers = input('Enter any numbers: ').split()

print(num_func(numbers))