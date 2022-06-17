# Lesson 5.2

string_count = 0
with open(r'c:\python\test1.txt', 'r') as new_file:
    for line in new_file:
        string_count += 1
        word_count = len(line.split())
        print('Number of lines:', string_count, '.', 'Number of words:', word_count)
