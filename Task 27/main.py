def sort(arr, element):
    arr.append(element)
    j = len(arr) - 2
    while j >= 0 and arr[j] < element:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = element


num = input("Введите кол-во сигналов: ")
signals = list(map(int, input('Сигналы: ').split(' ')))
visible = []

for signal in signals:
   sort(visible, signal)
   print(*visible[-5:])