"""
(!) Создать список из чисел от 0 до 9 в
произвольном количестве.

1) Переставить 0 в начало списка,
остальные элементы не трогать.
"""
# чтобы вставить элемент в список на определенное место
# используется метод .insert(index, element)
import random as r
rlist = [r.randint(0, 9) for x in range(r.randint(10, 100))]
print(rlist)


def zero_to_start(arr):
    for i in range(len(arr)):
        if arr[i] == 0:  # если элемент списка = 0
            arr.insert(0, arr[i])  # вставить этот элемент на место индекса 0
            arr.pop(i+1)  # удалить его из списка (i+1, потому что индексы смещены из-за вставки элемента)
    return arr
print(zero_to_start(rlist))
# если просто нужно поставить нули в начало
rlist.sort()
print(rlist)

"""
Написать функцию, которая найдет и забросит в новый список 
все элементы, которые больше среднего значения списка не 
более, чем на 3. Добавить элемент в список - .append(element)
"""
mid = sum(rlist) / len(rlist)
new_list = []
for i in range(len(rlist)):
    if mid < rlist[i] < mid + 3:
        new_list.append(rlist[i])

print(mid, new_list)

