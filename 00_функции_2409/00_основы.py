def average(seq: list) -> float:
    res = 0
    summ = 0
    for number in seq:
        summ += number
    res = summ / len(seq)
    return res

marks = [5, 7, 9, 10, 8, 9, 5, 6, 7, 4]
a = average()  # сохраняю результат работы функции
print(a)
b = a ** 2 ** 3 / 15
print(b)

