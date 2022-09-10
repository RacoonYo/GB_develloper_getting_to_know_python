# Задайте список из n чисел последовательности Sn = (Sn-1 + 3) и выведите на экран их сумму.
#
#  Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

list_of_num = []

num_n = input('write number: ')

for i in range(1, int(num_n) + 1):
    try:
        list_of_num.append(list_of_num[-1] + 3)
    except IndexError:
        list_of_num.append(i + 3)

print(sum(list_of_num))