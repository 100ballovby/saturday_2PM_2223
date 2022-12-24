from worker import Struct, menu


# создаю экземпляр класса массива структур, с которым буду работать
students = Struct('full_name', 'address', 'group', 'rate')

action = 0  # это запуск цикла
while action != 7:
    menu()  # меню будет вызываться на каждом повторении цикла
    action = int(input())
    if action == 1:
        students.create_struct_array()
        print('Добавлено!\n\n')
    elif action == 2:
        print(*students.dictionary.keys(), sep=" | ")
        key = input('По какому параметру сортируем?')
        students.sort_sctruct_array(key)
        print('Отсортировано!\n\n')
    elif action == 3:
        rate = input('Введите значение рейтинга: ')
        stud_i = students.search_struct_array(rate)
        print(f'Имя студента: {students.array[stud_i]}')
    elif action == 4:
        stud_n = int(input('Введите порядковый номер студента: '))
        students.edit_struct(stud_n)
    elif action == 5:
        stud_n = int(input('Введите порядковый номер студента, чтобы его удалить или -1, чтобы удалить всех: '))
        students.delete_student(stud_n)
    elif action == 6:
        students.show_all()
    else:
        print('Такого действия нет!')

