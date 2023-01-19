'''
Множества в Python - это "контейнер", который сожержит в себе уникальные элементы в неупорядоченном виде
'''

# {} !!!! dict
# set()
# a = {'a:1'} -> dict/словарь
# a = {1, 2, 3} -> set/множество

# set1 = {8, 1, 1, 11, 1, 1, 1, 4, 3, 2, 8, 3, 11}
# print(set1) #{1, 2, 3, 4, 8, 11}
# print(type(set1)) #<class 'set'>

# ls = ['Hello', 'Hello', 'hello', 'John', 'Snow', 'John']
# print(ls) #['Hello', 'Hello', 'hello', 'John', 'Snow', 'John']
# res = set(ls)
# print(res) #{'hello', 'Snow', 'John', 'Hello'}
# res = list(res)
# print(res) #['hello', 'Snow', 'John', 'Hello']
# print(type(res)) #<class 'list'>


# ls = [1, 2, 4, 'a', False, True, 'n', 'b']
# str1 = 'Hello world'
# ls.extend(str1) #[1, 2, 4, 'a', False, True, 'n', 'b', 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# # print(ls)
# res = set(ls) #{False, 1, 2, 4, 'e', 'a', 'o', 'r', 'w', ' ', 'l', 'd', 'n', 'b', 'H'}
# print(res)

'''FIFO (first in first out) / LIFO (last in first out)'''
# set1={1,2,3,4,5,6,7,8,9}
# set1.pop() #{2, 3, 4, 5, 6, 7, 8, 9} - удаляет первый элемент
# print(set1)


'''remove/discard'''

# remove -> error
# discard -> None
# set1 = {1,2,3,4,5}
# set1.remove(20) #error потому что нет такого элемента
# print(set1.discard(20)) #None - нет ошибки
# set1.add(15)
# print(set1) #{1, 2, 3, 15}

'''frozenset'''
# frozenset - такой же как set, только неизменяемый
# a = {1,2,3,4,5}
# b = frozenset([1,2,3,4,5])
# print(a, type(a)) #{1, 2, 3, 4, 5} <class 'set'>
# print(b, type(b)) #frozenset({1, 2, 3, 4, 5}) <class 'frozenset'>




'''
Создайте кортеж из 8-ми кортежей учащихся ВУЗов. В кортеже будут присутствовать следующие поля: имя студента, возраст, оценка за семестр, город проживания. Ваш код будет принимать этот кортеж, вычислять среднюю оценку по всем учащимся и выводить на печать следующее сообщение: “Ученики {список имен студентов через запятую} в этом семестре хорошо учатся!”. В список студентов, которые выводятся по результатам работы функции, попадут лишь те, у которых оценка за семестр равна или выше средней по всем учащимся.
'''
# кортеж(имя, возраст, оценка, город)

# students = (
#     ('Елена', '13', 9, 'Москва'),
#     ('Ольга', '11', 7.9, 'Иваново'),
#     ('Елизавета', '14', 9.1, 'Тверь'),
#     ('Дмитрий', '12', 5.2, 'Челябинск'),
#     ('Максим', '15', 6.1, 'Самара'),
#     ('Николай', '11', 8.7, 'Владивосток'),
#     ('Артур', '13', 5.8, 'Екатеринбург'),
#     ('John', '13', 10, 'WinterFell')
# )

# marks = []
# for x in students:
#     marks.append(x[2])

# print(marks) #[9, 7.9, 9.1, 5.2, 6.1, 8.7, 5.8, 10]
# avg_mark = sum(marks) / len(marks)
# print(avg_mark) #7.725

# good_students = {}
# for student in students:
#     if student[2] > avg_mark:
#         good_students.update({student[0]: student[2]})
        
# str1 = f'{good_students}'
# print(f'Ученики {str1[1:-1]} в этом семестре хорошо учатся!') 
# Ученики 'Елена': 9, 'Ольга': 7.9, 'Елизавета': 9.1, 'Николай': 8.7, 'John': 10 в этом семестре хорошо учатся!

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 102, 121}

# if robert&kail and merri&robert:
#     print("kail merri")
# elif merri&robert:
#     print("merri")
# elif robert&kail:
#     print("kail")
# else:
#     print('no one')
    






print(dir(set))