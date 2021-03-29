import sys


def print_values(num1, num2):
    print("a = ", a)
    print("b = ", b)
    print()


try:
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
except ValueError as ex:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

print_values(a, b)

# Обмен значениями с доп переменной
c = a
a = b
b = c
print_values(a, b)

# Обмен значениями без доп переменной
a = a + b
b = a - b
a = a - b
print_values(a, b)