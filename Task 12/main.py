import sys


def fact(num):
    count = 0
    res = 1
    while num > count:
        res *= num
        num -= 1
    return res


try:
    p = int(input("Введите число: "))
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

if p < 0:
    print("Вы ввели недопустимое значение")
    sys.exit(1)
else:
    print(f"{p}! =", fact(p))
