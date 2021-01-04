def func(*args):
    try:
        a = int(input('Enter first number - '))
        b = int(input('enter second number - '))
        func = a / b

    except ValueError:
        return "ValueError"
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"
    return func

print(f'result {func()}')
g