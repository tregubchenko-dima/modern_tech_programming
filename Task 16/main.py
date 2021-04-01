import sys
import re

try:
    n = int(input("Введите число: "))
    tickets = [i for i in input().split()]
    if n != len(tickets):
        print("Ошибочный ввод")
        sys.exit(1)
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

exp = "a[a-z][0-9][0-9]55661"
res = re.findall(exp, ' '.join(tickets))

if len(res) == 0:
    print(-1)
    sys.exit(1)

print(' '.join(res))
