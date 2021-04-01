import sys


def print_fix_sum(s, l1, r1, l2, r2, l2_global):
    if l1 < r1:
        if l1 + l2 == s:
            return f"{l1} {l2}"
        elif l2 < r2:
            num = print_fix_sum(s, l1, r1, l2+1, r2, l2_global)
            if num is not None:
                return num
            if l2 == r2-1:
                return print_fix_sum(s, l1+1, r1, l2_global, r2, l2_global)
    else:
        return "-1"


try:
    s, l1, r1, l2, r2 = map(int, input("Введите значения: ").split())
except ValueError:
    print("Вы ввели недопустимое значение")
    sys.exit(1)

print(print_fix_sum(s, l1, r1, l2, r2, l2))
