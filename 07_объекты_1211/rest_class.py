from datetime import datetime


class Restaurant:
    opened = False

    def __init__(self, name, cuisine, opens, close):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.open_r = opens
        self.close_r = close
        self.__num_of_tables = 0  # __ не даст поменять параметр напрямую (инкапсуляция - сокрытие данных класса)
        self.menu = {}  # параметр экземпляра нельзя задать через экземпляр, но можно будет обновлять методом

    def describe_restaurant(self):
        print(f'Welcome to "{self.restaurant_name}", '
              f'our cuisine type is {self.cuisine_type}.')

    def open_restaurant(self):
        now = datetime.now()  # фиксирую время во время вызова метода
        if self.open_r < now.hour < self.close_r:  # если вызов метода происходит между 10 и 18 часами дня
            opened = True
            print(f'{self.restaurant_name} is opened now!')
        elif 5 < now.hour < self.open_r:
            time = self.open_r - now.hour
            opened = False
            print(f'We are closed now, come in {time} hours.')
        else:
            opened = False
            print(f'We are closed now, see you tomorrow!')

    def make_order(self, o_l, table_num, dishes):
        """
        Метод, который вызывается для записи заказа в кипер.
        :param o_l: список заказов для смены
        :param table_num: номер столика
        :param dishes: список заказанных блюд
        :return: none
        """
        o_l.append({table_num: dishes})

    def close_order(self, o_l, order_num):
        """
        Метод закрытия заказа и удаления заказа из списка
        :param o_l: список заказов для смены
        :param order_num: номер заказа
        :return:
        """
        o_l.pop(order_num)

    def select_tables_count(self, num):
        """
        Задает количество столов в ресторане. Менять значение количества столов может только
        этот метод и никто более, потому что параметр с количеством
        столов запривачен (инкапсулирован)
        :param num: количество
        :return: количество столов для всего ресторана
        """
        self.__num_of_tables = num

    def update_menu(self, key, price):
        """
        Метод обновления блюд и стоимости меню
        :param key: блюдо, которое нужно заменить
        :param price: цена блюда
        :return: None
        """
        self.menu[key] = price
