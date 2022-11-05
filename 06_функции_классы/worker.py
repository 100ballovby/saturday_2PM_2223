from arch import Number  # импортировал из файла arch класс Number

five = Number(5)  # создал экземпляры класса Number
seven = Number(7)

print(five, seven)
print(five.sqrt())  # вычисляю квадратный корень
print(seven.is_positive())  # определяю знак числа
print(five.power(3))  # возвожу в степень 3
