# Lesson 5.4

nums = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('test4.txt', 'w', encoding='utf-8') as new_file_w:
    with open('test4_1.txt', 'r', encoding='utf-8') as new_file_r:
        for line in new_file_r:
            new_file_w.writelines([line.replace(line.split()[0], nums[line.split()[0]])])
