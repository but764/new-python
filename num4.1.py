
def payday():
    try:
        rate = float(input('rate: '))
        output = int(input('output: '))
        bonus = int(input("bonus: "))
        result = rate * output + bonus
        print(f'зарплта сотрудника: ', {result})
    except ValueError:
        return print('Not a number')
payday()




