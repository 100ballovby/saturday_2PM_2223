from rest_class import Restaurant


r_1 = Restaurant('Michelle', 'European', 10, 22)
tables = int(input('Сколько столов в ресторане? '))
r_1.select_tables_count(tables)
tables_list = [i + 1 for i in range(tables)]  # наполнить список столов по количеству
orders_list = []

for i in range(4):
    dish = input('Название блюда: ')
    price = float(input('Цена блюда: '))
    r_1.update_menu(dish, price)

r_1.open_restaurant()
while True:
    choice = int(input('Введите 1, чтобы открыть заказ или 2, чтобы его закрыть.'))
    if choice == 1:
        t = int(input('Номер стола'))
        d = input('Введите блюда через пробел: ')
        r_1.make_order(orders_list, t, d.split())
    if choice == 2:
        num = int(input('Номер заказа: '))
        r_1.close_order(orders_list, num - 1)

    print(f'Активные заказы: {orders_list}')



