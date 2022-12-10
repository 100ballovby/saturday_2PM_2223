from operator import itemgetter
students = []


def create_struct_array(arr: list) -> list:
    """
    Функция получает список, добавляет в нее словарь и
    возвращает измененный список
    :param arr: список словарей
    :return: список с добавленным словарем
    """
    student = {
        "full_name": "",
        "address": "",
        "group": "",
        "rate": 0.0
    }
    for key in student.keys():
        student[key] = input(f'Value of key {key}: ')
    arr.append(student)
    return arr


def sort_sctruct_array(arr: list) -> list:
    """
    Функция сортирует список словарей и возвращает его
    :param arr: список словарей
    :return: отсортированный список словарей
    """
    arr.sort(key=itemgetter('full_name'))
    return arr


def search_struct_array(arr: list, val: str) -> int:
    """
    Функция осуществляет линейный поиск по списку словарей
    и возвращает индекс совпавшего по условию элемента списка
    :param arr: список словарей
    :param val: искомое значение
    :return: индекс
    """
    for i in range(len(arr)):
        if arr[i]['rate'] == val:  # если в каком-то элементе списка ключ rate совпадает с искомым значением
            return i


def edit_struct(arr: list, index: int) -> list:
    """
    Функция будет изменять словарь по индексу в списке словарь
    :param arr: список словарей
    :param index: порядковый номер словаря
    :return: список словарей
    """
    if index >= len(arr):  # если искомый индекс больше длины массива
        print("Nothing here!")
        return arr  # вернуть список словарей в изначальном виде
    else:
        for key in arr[i].keys():  # перебираю ключи найденного словаря
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
            arr[i][key] = input(f'Value of key {key}: ') or arr[i][key]
        return arr

for i in range(2):
    students = create_struct_array(students)

sort_sctruct_array(students)
stud_index = search_struct_array(students, '5.0')

print(students)
print(students[stud_index]["full_name"])
students = edit_struct(students, 0)
print(students)
