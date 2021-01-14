def fact(n):
    list_numbers = 1
    for i in range(1, n+1):
        list_numbers *= i
    yield list_numbers


for el in fact(4):
    print(el)