# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.142.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi, modf


def digit_pi(d: float) -> float:
    if str(d).find('e-') != -1:
        return round(pi, int(str(d).split('e-')[1]))

    digit = len(str(d).split('.')[1])
    return round(pi, digit)


test_date = [
    [0.001, 3.142],
    [0.001000, 3.142],
    [0.00000001, 3.14159265]
]

for i, j in test_date:
    assert digit_pi(i) == j
