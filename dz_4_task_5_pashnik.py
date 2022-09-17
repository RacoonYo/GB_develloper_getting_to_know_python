# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму
# многочленов.

sum_pol_dict = {}
sum_pol = ''
free_mem = 0

with open('polynomial_1.txt', 'r') as p1:
    polynomial_1 = p1.read()

with open('polynomial_2.txt', 'r') as p2:
    polynomial_2 = p2.read()

pol_1_list = polynomial_1.split(' + ')
pol_2_list = polynomial_2.split(' + ')
sum_pol_list = pol_1_list + pol_2_list

for i in sum_pol_list:
    if '^' in i:
        coef, deg = i.split('x^')
        if sum_pol_dict.get(deg):
            sum_pol_dict[deg] += int(coef)
        else:
            sum_pol_dict[deg] = int(coef)
    else:
        free_mem += int(i)

for key, value in sum_pol_dict.items():
    sum_pol += f'{value}x^{key} + '

with open('sum_polynomial.txt', 'w') as sp:
    sp.write(f'{sum_pol}{free_mem} = 0')

