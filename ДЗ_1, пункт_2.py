# Задание_2

time = int(input("Введите время в секундах: "))
print("Заданное количество времени: ", time, " секунд", sep="")
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print("Данное количество секунд составляет ", f"{hours:02}:{minutes:02}:{seconds:02}")
