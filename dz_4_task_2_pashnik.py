# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def find_simple_divisor(n):
    divisors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            divisors.append(i)
        i += 1

    if n > 1:
        divisors.append(n)

    return divisors


test_date = [
    [152, [2, 2, 2, 19]],
    [16, [2, 2, 2, 2]],
    [1569, [3, 523]]
]

for i, j in test_date:
    assert find_simple_divisor(i) == j
