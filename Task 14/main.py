import math
import sys


def is_two_power(number):
    p = 0
    res = 0
    while p <= number:
        if math.pow(2, p) <= number:
            res += 1
        p += 1
    return res


try:
    num = int(input("Введите число: "))
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

if num < 0:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

print(is_two_power(num))
