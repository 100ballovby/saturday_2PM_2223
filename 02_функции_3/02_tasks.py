from functools import reduce

# Используя функцию map() печатайте квадрат
# каждого числа округленный до 3х знаков

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Используя функцию filter() печатайте только те
# имена, у которых меньше 7 букв

my_names = ["олимпиада", "закат", "программа", "python", "код"]

# используя функцию reduce() напечатайте произведение этих чисел
my_numbers = [4, 6, 9, 23, 5]

# Поправьте все три выражения.
map_result = list(map(lambda x: round(x * x, 3), my_floats))
filter_result = list(filter(lambda name: len(name) < 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)