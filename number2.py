def stringify(name, last_name, date, city, email, phone):
    """Возвращает введенные аргументы в виде строки"""
    return f'Имя: {name}, Фамилия: {last_name}, Год рождения: {date}, ' \
           f'Город проживания: {city}, Email: {email}, Телефон: {phone}.'


string_result = stringify(phone=89911911911, email='sav.com', city='Таганрок',
                          date=1965, last_name='Пупкин', name='Вася')
print(string_result)