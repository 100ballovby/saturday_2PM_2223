from operator import itemgetter


class Struct:
    def __init__(self, *args):
        """
        Сбор экземпляра класса характеризуется тем,
        что при создании объявляется список и структура.
        Ключи структуру передаются в неограниченном количестве
        при помощи args.
        :param args:
        """
        self.array = []
        self.dictionary = {}
        for value in args:
            self.dictionary[value] = ''

    def create_struct_array(self):
        """
        Функция получает список, добавляет в нее словарь и
        возвращает измененный список
        :param arr: список словарей
        :return: список с добавленным словарем
        """
        new_dict = {}  # словарь постоянно будет очищаться
        for key in self.dictionary.keys():
            new_dict[key] = input(f'Value of key {key}: ')
        self.array.append(new_dict)

    def sort_sctruct_array(self, key):
        """
        Функция сортирует список словарей и возвращает его
        :param key: ключ, по которому происходит сортировка
        :return: отсортированный список словарей
        """
        self.array.sort(key=itemgetter(key))

    def search_struct_array(self, val: str) -> int:
        """
        Функция осуществляет линейный поиск по списку словарей
        и возвращает индекс совпавшего по условию элемента списка
        :param val: искомое значение
        :return: индекс
        """
        for i in range(len(self.array)):
            if self.array[i]['rate'] == val:  # если в каком-то элементе списка ключ rate совпадает с искомым значением
                return i

    def edit_struct(self, index: int) -> list:
        """
        Функция будет изменять словарь по индексу в списке словарь
        :param index: порядковый номер словаря
        :return: список словарей
        """
        if index >= len(self.array):  # если искомый индекс больше длины массива
            print("Nothing here!")
            return self.array  # вернуть список словарей в изначальном виде
        else:
            for key in self.array[index].keys():  # перебираю ключи найденного словаря
                """
                input, если ничего не написать, возвращает пустую строчку '',
                эта пустая строка интерпретируется как значение false.
                Операция или - логическое сложение - 0 + 1 = 1 (False or True = True)
                В данном случае я вместо написания полноценного условия, попросил 
                программу принять решение: возврат_инпута ИЛИ старое значение. 
                В случае, если в инпуте не будет ничего - это False, 
                при не написании чего-либо в инпут, 
                у ключа останется старое значение. 
                """
                self.array[index][key] = input(f'Value of key {key}: ') or self.array[index][key]

    def show_all(self):
        for i in range(len(self.array)):  # повторить по количеству студентов раз
            print(f'Студент №{i + 1}')
            for key in self.array[i]:  # перебираю ключи в словаре i
                print(f'{key}: {self.array[i][key]};')
            print()  # разделю инфу о студентах пустой строкой

    def delete_student(self, number):
        if number == -1:
            self.array = []
        else:
            self.array.pop(number-1)



def menu():
    print("""
    Выберите действие:
    1 - Ввод массива структур 
    2 - Сортировка массива структур 
    3 - Поиск в массиве структур
    4 - Изменение массива структур 
    5 - Удаление структуры из массива 
    6 - Вывод массива структур;
    7 - Выход. 
    """)
