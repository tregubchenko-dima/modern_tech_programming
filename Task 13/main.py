import sys
import math


def is_simple(a):
    for i in range(2, a-1):
        if a % i == 0:
            return "составное"
    return "простое"


try:
    num = int(input("Введите число: "))
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

if num < 2:
    print("Число должно быть больше 1")
    sys.exit(1)

print(f"Число {num}", is_simple(num))
