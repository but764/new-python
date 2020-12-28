profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
result = profit - costs
if result > 0:
    print(f"Фирма работает с прибылью.{result} ")
    print(f"Выручка составила {result / costs: .3f}")
    workers = int(input("Введите количество сотрудников фирмы? "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.3f}")
elif result < 0:
    print(f"Фирма работает в ноль - {-result}")
else:
    print(f"Фирма работает в убыток")
