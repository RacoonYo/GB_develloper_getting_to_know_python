# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# 6782 -> 23
# 0,56 -> 11

sum_of_num = 0

num = input('write real number: ')

for char in num:
    if char.isdigit():
        sum_of_num += int(char)

print(sum_of_num)
