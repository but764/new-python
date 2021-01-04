name = input('Введите имя - ')
last_name = input('Введите фамилию - ')
date = int(input('дата рождения' ))
city = input('В каком городе живете? ')
email = input('email')
num_fon = input('Номер телефона ')

def my_func (name, last_name, date, city, email, num_fun):
    return ''.join([name, last_name, date, city, email, num_fun])

print(my_func())