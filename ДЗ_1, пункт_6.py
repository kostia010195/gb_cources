# Задание_6

while True:
    days = 1
    first_km = float(input("Начальное расстояние: "))
    fin_km = float(input("Финальный результат: "))
    if first_km <= 0 or fin_km < 0:
        print("Проверьте правильность ввода показателей!")
    else:
        while first_km < fin_km:
            first_km += first_km * 0.1
            days += 1

        print("Бегун пробежит нужное количество километров на", days, "день")
        break
