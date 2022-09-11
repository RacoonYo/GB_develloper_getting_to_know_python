# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной
# позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

result_sum = 0

list_of_num = input('write the elements of the list separated by a space:\n').split(' ')

for i in range(1, len(list_of_num), 2):
    result_sum += int(list_of_num[i])

print(f'result summa: {result_sum}')
