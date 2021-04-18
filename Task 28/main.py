def print_factorization(n: int) -> None:
    data = []
    i = 2

    while i * i < n:
        if n % i == 0:
            data += [[i, 0]]
            while n % i == 0:
                n //= i
                data[len(data) - 1][1] += 1
        i += 1

    if n > 1:
        data += [[n, 1]]

    sorted(data, key=lambda pair: pair[0])

    i = 0
    for divider, count in data:
        char = '' if i == 0 else '*'
        i += 1

        if count <= 1:
            print(f'{char}{divider}', end='')
        else:
            print(f'{char}{divider}^{count}', end='')


try:
    n = int(input("Введите число: "))
except ValueError:
    print("Вы ввели недопустимое значение")
    exit(1)

print_factorization(n)
