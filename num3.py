def my_func(num1, num2, num3):
    # Функция возвращает сумму наибольших двух аргументов

    lst = [num1, num2, num3]
    summ = sum(lst) - min(lst)
    return summ


print(my_func(200, 15, 300))