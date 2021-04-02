import sys
from random import randint


def get_most_popular(map):
    values = list(map.values())
    max_value = max(values)
    popular = list(filter(lambda key: map[key] == max_value, list(map.keys())))
    result = [str(i) for i in popular]
    return ' '.join(result)


numbers = list(range(0, 37))
unused_numbers = list(range(0, 37))
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
most_popular = {}
red_count = 0
black_count = 0

while True:
    try:
        num = int(input())
    except ValueError:
        print("Вы ввели недопустимое значение")
        sys.exit(1)

    if num <= -2 or num > 36:
        print("Вы ввели недопустимое значение")
        sys.exit(1)
    elif num == -1:
        break

    rand_num = randint(0, len(numbers)-1)

    if rand_num in unused_numbers:
        unused_numbers.remove(rand_num)

    if rand_num in most_popular:
        most_popular[rand_num] = most_popular[rand_num]+1
    else:
        most_popular[rand_num] = 1

    print(get_most_popular(most_popular))
    print(' '.join(map(str, unused_numbers)))

    if numbers[rand_num] in red_numbers:
        red_count += 1
    else:
        black_count += 1

    print(f"{red_count} {black_count}")
    print()


