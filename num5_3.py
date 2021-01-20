# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


with open('file3.txt', 'r', encoding='utf-8') as f:
    employees = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'средняя зп = {round(sum(employees.values())/ len(employees), 3)}\n'
          f' оклад меньше 20000 {[e[0] for e in employees.items() if e[1] < 20000]}')

