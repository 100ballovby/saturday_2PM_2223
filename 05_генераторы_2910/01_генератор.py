import random as r

r_list = [x for x in range(20)]
"""
for x in range(20):
    r_list.append(x)
"""
print(r_list)
# наполнить список 10 случайными числами
r_list = [r.randint(-100, 100) for x in range(10)]
print(r_list)
# наполнить список 25 случайными трехзначными числами,
# если они кратны 3 или 6 и они не находятся в списке
r_list = [r.randint(100, 999) for x in range(10)
          if (x % 3 == 0 or x % 6 == 0) and x not in r_list]
print(r_list)
# циклов в генераторе списка может быть несколько
tbd = [str(x) + str(y) for x in range(3) for y in range(x + 3)]
print(tbd)
"""
tbd = []
for x in range(3):
    for y in range(x + 3):
        tbd.append(str(x) + str(y))
"""



