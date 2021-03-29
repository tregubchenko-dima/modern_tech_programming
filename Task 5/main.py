import sys


try:
    x0, v0, t = map(float, input("Введите x0, v0, t: ").split())
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

a = 9.8
xt = x0 + v0 * t - a*t*t/2

print("x(t) = ", xt)
