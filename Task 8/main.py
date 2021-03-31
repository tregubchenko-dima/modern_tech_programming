import sys


a, sign, b = input("Введите пример: ").split()

try:
    a = float(a)
    b = float(b)
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

if sign == "+":
    res = a + b
elif sign == "-":
    res = a - b
elif sign == "*":
    res = a * b
elif sign == "/":
    try:
        res = a / b
    except ZeroDivisionError:
        print("Деление на нуль. Нельзя делить на нуль.")
        sys.exit(1)
else:
    print("Вы ввели недопустимый оператор")
    sys.exit(1)

print(f"{a} {sign} {b} =", res)
