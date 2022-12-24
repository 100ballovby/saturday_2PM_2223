n = input('Введи число: ')

try:  # попробовать
    n = int(n)  # преобразовать переменную n в int
    print(5 / n)  # вывести n
except ValueError:  # если возникает ValueError
    print('Это не число!')
except ZeroDivisionError:
    print('На ноль делить нельзя!')

print(n * 9)  # здесь n все еще строка, если блок try не сработал

