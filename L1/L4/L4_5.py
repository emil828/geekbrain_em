# Lesson 4.5

from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]

def mult(a, b):
	return a + b


print(reduce(mult, my_list))

