def bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


def print_bmi(bmi: float):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif bmi >= 30:
        print("Obesity")


try:
    weight, height = map(float, input().split())
    height = height / 100
except ValueError:
    print("Вы ввели недопустимое значение")
    exit(1)

if weight <= 0 or height <= 0:
    print("Вы ввели недопустимые значения")
    exit(1)

print_bmi(bmi(weight, height))

