"""
генератор = (что вычислить, сколько раз, условие)
"""
a = (i ** 2 for i in range(1, 5))

for elem in a:
    print(elem)

