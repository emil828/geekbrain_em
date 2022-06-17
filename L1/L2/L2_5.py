# Lesson 2.5

my_list = [7, 5, 3, 3, 2]

num = int(input('Enter any number: '))
my_list.append(num)

new_list = sorted(my_list)
new_list.reverse()

print(new_list)
