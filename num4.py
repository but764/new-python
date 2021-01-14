x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))


def my_func(x, y):
    first_variant = x ** y
    for i in range(1, -y, 1):
        x *= x
    second_variant = 1 / x
    return first_variant, second_variant


print(my_func(x, y))