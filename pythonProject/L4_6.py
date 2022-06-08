# Lesson 4.6

from itertools import count
from itertools import cycle

my_list = []

for i in count(3):
	if i > 10:
		break
	else:
		my_list.append(i)

print(my_list)

c = 0

for i in cycle(my_list):
	if c > 25:
		break
	print(i)
	c += 1

