import sys

try:
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
try:
    print("a / b = ", a / b)
except ZeroDivisionError:
    print("Деление на нуль. Нельзя делить число на нуль")
