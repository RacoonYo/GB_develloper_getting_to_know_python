# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

list_of_num = []

num_n = input('write number: ')

for i in range(1, int(num_n) + 1):
    try:
        list_of_num.append(list_of_num[-1] * i)
    except IndexError:
        list_of_num.append(i)

print(list_of_num)

