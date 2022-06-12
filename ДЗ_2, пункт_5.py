# Задание_5 Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

number = int(input("Введите выдуманное место в рейтинге: "))
my_list = [9, 6, 5, 4, 3, 1]
x = my_list.count(number)
for num in my_list:
    if x > 0:
        i = my_list.index(number)
        my_list.insert(i+x, number)
        break
    else:
        if number > num:
            j = my_list.index(num)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
