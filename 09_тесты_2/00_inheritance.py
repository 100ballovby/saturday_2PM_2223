class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1


# Наследование
class NonDecreasingCounter(Counter):  # в скобках указывается класс-предок
    def decrement(self):
        pass


n1 = Counter()
for i in range(10, 0, -1):
    n1.decrement()
print(n1.value)
for i in range(15):
    n1.increment()
print(n1.value)

n2 = NonDecreasingCounter()
for i in range(10, 0, -1):
    n2.decrement()
print(n2.value)
for i in range(15):
    n2.increment()
print(n2.value)

print(f'Метод декремент класса NonDecreasingCounter {n2.decrement}')
# когда вы переписываете метод, его владельцем становится класс-наследник
print(f'Метод инкремент класса NonDecreasingCounter {n2.increment}')
# когда вы просто унаследуете метод из класса, его владельцем будет родитель
