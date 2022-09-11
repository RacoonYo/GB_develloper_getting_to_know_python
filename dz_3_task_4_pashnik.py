# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#  простое решение
num = int(input('write number: '))
print(bin(num)[2:])

#  сложное решение
# num = int(input('write number: '))
# remainder_list = []
# binary_num = ''
# flag = True
#
# while flag:
#     remainder_list.append(str(num % 2))
#     if num // 2 < 2:
#         flag = False
#     num = num // 2
#
# remainder_list.append('1')
# remainder_list.reverse()
#
# print(''.join(remainder_list))