# Задание_2 Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = input('Введите числа придуманного списка (разделитель - пробел): ').split()
print("Ваш список", my_list)
if len(my_list) % 2 == 0:
    x = 0
    while x < len(my_list):
        element = my_list[x]
        my_list[x] = my_list[x+1]
        my_list[x+1] = element
        x += 2
else:
    x = 0
    while x < len(my_list) - 1:
        element = my_list[x]
        my_list[x] = my_list[x + 1]
        my_list[x + 1] = element
        x += 2
print(my_list)
