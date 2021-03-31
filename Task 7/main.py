import math
import sys


print("Выберите один из вариантов расчета площади треугольника:\n1)длины сторон\n2)координаты вершин")
option = input("Выбор(1/2): ")

if option == '1':
    try:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))
    except ValueError:
        print("Вы ввели недопустимое значение")
        sys.exit(1)

    if a <= 0 or b <= 0 or c <= 0:
        print("Вы ввели недопустимое значение")
        sys.exit(1)

    p = (a + b + c)/2
    try:
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    except ValueError:
        print("Нельзя извлечь корень из отрицательного числа")
        sys.exit(1)

elif option == '2':
    try:
        ax, ay = map(float, input("Введите A(x,y): ").split())
        bx, by = map(float, input("Введите B(x,y): ").split())
        cx, cy = map(float, input("Введите C(x,y): ").split())
    except ValueError:
        print("Вы ввели недопустимое значение")
        sys.exit(1)

    s = math.fabs((bx - ax) * (cy - ay) - (cx - ax) * (by - ay))/2

else:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

if s > 0:
    print("S = ", s)
else:
    print("Недопустимое значение")
    sys.exit(1)
