# Lesson 5.1

with open(r'c:\python\test.txt', 'w') as new_file:
    line = ' '
    for i in range(100):
        line = input('Enter any text: ')
        print(line, file=new_file)
        if line == '':
            break
