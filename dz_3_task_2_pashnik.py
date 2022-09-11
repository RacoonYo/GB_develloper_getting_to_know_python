# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и
# предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

result_list = []

list_of_num = list(map(int, input('write the elements of the list separated by a space:\n').split(' ')))

for i in range(len(list_of_num) // 2):
    result_list.append(list_of_num[i] * list_of_num[(len(list_of_num) - 1) - i])

if len(list_of_num) % 2 != 0:
    result_list.append(list_of_num[len(list_of_num) // 2] ** 2)

print(result_list)
