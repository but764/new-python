from functools import reduce

new_list = [i for i in range(99, 1001) if i % 2 == 0]
list_reduce = reduce(lambda x, y: x+y, new_list)
print(list_reduce)
