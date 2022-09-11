# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_of_num = list(map(float, input('write the elements of the list separated by a space:\n').split(' ')))

fractional_list = [i % 1 for i in list_of_num if i % 1 != 0]

print(round(max(fractional_list) - min(fractional_list), 5))
