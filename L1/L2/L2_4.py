# Lesson 4

user_list = input('Enter any text: ')

new_list = user_list.split()

for i in range(len(new_list)):
    print(i + 1, new_list[i])
