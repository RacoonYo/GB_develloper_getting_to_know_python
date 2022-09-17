# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

polynomial = ''

k = int(input('enter the degree of the polynomial: '))

coef_list = [randint(0, 100) for i in range(k + 1)]

for i in range(k + 1):
    if coef_list[i] != 0:
        if i == 0:
            polynomial = f'{coef_list[i]} + '
            continue
        polynomial += f'{coef_list[i]}x^{i} + '

with open('polynomial.txt', 'w') as f:
    f.write(f'{polynomial.rstrip(" + ")} = 0')

print(coef_list)  # для понимания какие коофициенты у многочлена
