from alcohol import Alcohol
import math


def find_more_alcohol(m, list):
    min_price_item = min([i.get_price() for i in list])
    list_res = []
    v = 0
    while m >= min_price_item:
        max = math.floor(list[0].get_v() * m / list[0].get_price())
        res = None
        for i in list:
            temp = math.floor(i.get_v() * math.floor(m / i.get_price()))
            if temp >= max:
                max = temp
                res = i
        v += max
        list_res.append(f"{res.get_name()} {math.floor(m / res.get_price())}")
        m = m - res.get_price() * math.floor(m / res.get_price())
    if not list_res:
        list_res.append("-1")
    else:
        list_res.append(f"{v}")
        list_res.append(f"{m}")
    return list_res


try:
    money = int(input())
    variants = int(input())
except ValueError:
    print("Вы ввели недопустимое значение")
    exit(1)

if money < 0 or variants < 1:
    print("Вы ввели недопустимое значение")
    exit(1)

list_alcohol = []
for i in range(0, variants):
    name, price, v = input().split()
    price = int(price)
    v = int(v)
    if price < 1 or v < 1:
        print("Вы ввели недопустимое значение")
        exit(1)
    list_alcohol.append(Alcohol(name, price, v))

list_res = find_more_alcohol(money, list_alcohol)
print('\n'.join(list_res))








