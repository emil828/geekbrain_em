# Lesson 5.3

with open(r'c:\python\test2.txt', 'r', encoding='utf-8') as new_file:
    salary_total = 0
    salary_count = 0
    for line in new_file:
        emp_list = line.split()
        for i in range(len(emp_list)):
            if emp_list[i].isdigit():
                salary = int(emp_list[i])
                salary_total += salary
                salary_count += 1
                if salary >= 20000:
                    print(emp_list[0])
    print('Average salary is:', salary_total / salary_count)
