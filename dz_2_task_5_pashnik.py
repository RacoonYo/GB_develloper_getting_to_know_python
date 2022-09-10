# Реализуйте алгоритм перемешивания списка.

from random import randint
mix_list = []

input_date = input('write the elements of the list separated by a space:\n')

start_list = input_date.split(' ')

for i in range(len(start_list)):
    mix_list.append(start_list.pop(randint(0, len(start_list) - 1)))

print(mix_list)
