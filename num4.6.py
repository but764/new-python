from itertools import count, cycle


def list_numbers(num):
    for el in count(num):
        if el <= 10:
            print(el)
        else:
            break


list_numbers(3)


def list_cycle(*argv):
    i = 0
    for el in cycle(argv):
        print(el)
        i += 1
        if i > 10:
            break


list_cycle(True, 2, 'hello')
