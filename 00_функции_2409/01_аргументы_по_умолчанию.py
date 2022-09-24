def average(seq: list = [1, 2, 4, 6]) -> float:
    res = 0
    summ = 0
    for number in seq:
        summ += number
    res = summ / len(seq)
    return res

marks = [5, 7, 9, 10, 8, 9, 5, 6, 7, 4]
a = average()  # сохраняю результат работы функции
b = average(marks)
print(a)
print(b)
