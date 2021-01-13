list = [12, 'plant', True, 75.2, None, [1, 2], {22, 4}, bytearray]
def my_type(el):
    for el in range(len(list)):
        print(type(list[el]))
    return
my_type(list)