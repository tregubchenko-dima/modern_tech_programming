import math
import sys


try:
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)


def print_two(num1, num2):
    print("x1 = ", num1)
    print("x2 = ", num2)


D = b * b - 4 * a * c

if a == 0:
    print("x = ", -c / b)
elif b == 0 and c < 0:
    print_two(math.sqrt(-c / a), -math.sqrt(-c / a))
elif c == 0:
    print_two(0, -b / a)
elif (a == 0 and c == 0) or (b == 0 and c == 0):
    print("x = ", 0)
elif D > 0:
    print_two((-b + math.sqrt(D)) / 2 * a, (-b - math.sqrt(D)) / 2 * a)
elif D == 0:
    print("x = ", -b / 2 * a)
else:
    print("Нет корней")
