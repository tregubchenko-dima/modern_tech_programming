import sys
import math

try:
    h1, m1 = map(int, input("Введите время прибытия первого человека: ").split(":"))
    h2, m2 = map(int, input("Введите время прибытия второго человека: ").split(":"))
except ValueError:
    print("Вы ввели некоректное значение")
    sys.exit(1)

time1 = h1 * 60 + m1
time2 = h2 * 60 + m2

if math.fabs(time1-time2) > 15:
    print("Встреча не состоится")
else:
    print("Встреча состоится")
