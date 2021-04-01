import sys
import math


def math_pow(a, power):
    count = 0
    power = math.fabs(power)
    res_num = a
    while count < power - 1:
        res_num *= a
        count += 1
    return res_num


try:
    num = float(input())
    p = int(input())
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

if p == 0:
    res = 1
elif num == 0:
    res = 0
elif p < 0:
    res = 1/math_pow(num, p)
else:
    res = math_pow(num, p)

print(f"{num} в степени {p} =", res)
