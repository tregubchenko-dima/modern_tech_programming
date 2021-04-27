from random import randint
from math import sqrt


def BozoSort(values, asc=True):
    if isinstance(values[0], list):
        list_temp = []
        for i in values:
            for j in i:
                list_temp.append(j)
        values = list_temp

    num1 = randint(0, len(values)-1)
    num2 = randint(0, len(values)-1)

    temp = values[num1]
    values[num1] = values[num2]
    values[num2] = temp

    for i in range(0, len(values)):
        if i >= len(values) - 1:
            return values
        elif asc:
            if values[i] > values[i+1]:
                return BozoSort(values, asc)
        else:
            if values[i] < values[i+1]:
                return BozoSort(values, asc)


try:
    n = int(input('Введите количество чисел n: '))

    if 3 < n <= 100:
        values = list(map(int, input(f'Введите числа: ').split(' ')))
        if n != len(values):
            print('Неверное количество чисел')
            exit(1)

        print(*BozoSort(values))
        print(*BozoSort(values, False))

        size = int(sqrt(n))
        arr = []
        for i in range(0, size):
            arr.append(values[i*size:(i*size)+size])

        print(*BozoSort(arr))
        print(*BozoSort(arr, False))

        print(*BozoSort(values[0:3]))
        print(*BozoSort(values[0:3], False))

    else:
        print('Неверное количество чисел')
        exit(1)

except ValueError:
    print("Вы ввели недопустимое значение")
    exit(1)


