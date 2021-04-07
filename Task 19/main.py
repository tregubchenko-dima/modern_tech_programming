import itertools


def find_variants(array, count):
    variants = list(itertools.product(arr, repeat=count))
    list_res = []
    for i in variants:
        is_included = True
        for j in array:
            if j not in i:
                is_included = False
                break
        if is_included:
            list_res.append("".join(i))
    return " ".join(list_res)


num = int(input())
arr = input()

print(find_variants(arr, num))




