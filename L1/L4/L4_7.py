# Lesson 4.7

def generator(num):
	fact = 1
	for i in range(1, num + 1):
		fact *= i
		print(fact)
	yield fact

for i in generator(4):
	print(i)

