# Lesson 5.6

with open('test6.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    for line in text:
        new = ''
        for el in line:
            new = ''.join([new, (el if el in '0123456789' else ' ')])
        res = [int(i) for i in new.split()]
        print(f'{line.split()[0]} - {sum(res)} часов')
