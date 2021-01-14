while True:
        days = 1
        start = float(input("результат первого дня "))
        finish = float(input("итоговый результат "))
        if start <= 0 or finish < 0:
                print("Неправильное значение")
        else:
                while start < finish:
                        start *= 1.1
                        days += 1

                print(f"спортсмен достигнет результата за {days} дней")
                break
