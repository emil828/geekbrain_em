# Lesson 5.5

with open(r'c:\python\test4.txt', 'w') as new_file:
    new_file.write(input('Enter numbers: '))

with open(r'c:\python\test4.txt', 'r') as new_file:
    for line in new_file:
        num_list = line.split()
    total_summ = 0
    for i in range(len(num_list)):
        total_summ += int(num_list[i])

print('Total summ is:', total_summ)