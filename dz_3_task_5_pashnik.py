# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

result_list = []
negative_val_list = []
positive_vel_list = []

num = int(input('write number: '))

for i in range(1, num + 1):
    if - i == - 1:
        negative_val_list.append(1)
    elif - i == - 2:
        negative_val_list.append(-1)
    else:
        negative_val_list.append(negative_val_list[i - 3] - negative_val_list[i - 2])

negative_val_list.reverse()

for i in range(num + 1):
    if i == 0:
        positive_vel_list.append(0)
    elif i == 1:
        positive_vel_list.append(1)
    else:
        positive_vel_list.append(positive_vel_list[i - 1] + positive_vel_list[i - 2])

result_list = negative_val_list + positive_vel_list
print(result_list)

