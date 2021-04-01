from random import randint
import sys

while True:
    n = randint(0, 100)
    is_win = False
    print("Игра начинается")

    for i in range(0, 5):
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("Вы ввели недопустимое значение")
            sys.exit(1)

        if num == n:
            print("Поздравляю! Вы угадали")
            is_win = True
            break
        elif num < n and is_win is False:
            print("Загаданное число больше")
        elif num > n and is_win is False:
            print("Загаданное число меньше")

    if not is_win:
        print(f"Вы проиграли. Было загадано: {n}")

    choice = int(input("Хотите начать сначала? (1 - ДА ): "))
    if choice != 1:
        break
