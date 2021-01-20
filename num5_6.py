# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

my_dict = {}
with open('file6.txt', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' 'or (i >= '0' and i <= '9')]).split() ))
        my_dict[name] = name_sum
print(f'{my_dict}')