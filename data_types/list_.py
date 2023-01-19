'''============Тип данных - list (списки)=============='''

''' list - это изменяемый тип данных, который представляет собой коллекцию какой-либо последовательности'''

# list_ = [12, 23, True. False, [12, 'astr'], 'str', None, [12, []]]

# index y list

# list_ = [1, 2, 8, 10]
# print (list_[2]) #8
# print (list_[1::2]) #[2, 10] срез

# list_ = [10, 5, 2, 10, [0, 0, 0, 1, 0]]
# print(list_[4][3]) #1 - срезы расположены рядом, а не один в другом

# str_ = 'Helloworld'
# list_ = list(str_) # list() - функция переводит в тип данных "список"
# print (list_) # ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

# list_ = [1, 2, 3, 4, 5, 10, True, False, None, 'str']
# lists_len = len(list_) # len - функция для подсчета элементов
# print(lists_len) # 10

'''============Тип данных - tuple (кортеж)=============='''

''' tuple - неизменяемый тип данных, являющийся последовательностью элементов, литералами являются запятые ,, и круглые скобки()'''

# tuple_ = (1, 2, 3, 4) # tuple - круглые скобки
# list_ = [1, 2, 3, 4] # list - квадратные скобки
# print(tuple_) # (1, 2, 3, 4)
# print(list_) # [1, 2, 3, 4]

'''============RANGE=============='''

# range(start, end, step) - это генератор последовательности
# В новой версии питона это тип данных

# range_ = range(0, 11)
# print(list(range_)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] list()
# print(tuple(range_)) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) tuple()


'''============Циклы (for, while)=============='''

# for - это цикл, который работает до конца итерируемого объекта (Итерировать - перебирать)
# while - это цикл, который работает, пока условие True

# meshok = ['potato', 'tomato', 'onion']
# kastrula = []

# for ovoshi in meshok:
#     kastrula.append(ovoshi)

# print(kastrula) # ['potato', 'tomato', 'onion']


# for i in range(0, 11): # [0,1,2,3,4,5,6,7,8,9,10]
#     print(i**2) # 0,1,4,9,16,25,36,49,64,81,100


# for i in 'makers bootcamp':
#     print(f'Это буква - {i}')

'WHILE'

# i = 0
# while i < 10:
#     print(f'Hello world, это {i} итерация')
#     i+=1 # i =i+1 иначе 0 всегда меньше 10 и будет бесконечный результат


'''BRAKE, CONTINUE'''

# break - это оператор циклов, который ломает цикл и выводит из него
# continue - это оператор циклов, который пропускает итерацию

# i = 0
# while True:
#     if i == 5:
#         break
#     print(f'Hello world, это {i} итерация')
#     i+=1 # i =i+1


# i = 0
# while i < 5:
#     i = i + 1
#     if i == 2:
#         continue
#     print(f'Hello world, это {i} итерация')
    

''' '''''''''''''''''''''''''''''''''''''''' '''
# for i in range(11):
#     if i == 5:
#         break
#     print(f'это {i} итерация') # останавливается на 4 итерации, ломает цикл и закачивает, когда i = 5


# for i in range(11):
#     if i == 5:
#         continue
#     print(f'это {i} итерация') # пропускает 5 итерацию, когда i = 5 и продолжает работу цикла

''' '''''''''''''''''''''''''''''''''''''''' '''

''' =============== Методы list (списков) =============== '''

# print(dir(list)) # dir(list) - функция для просмотра методов листа

''' APPEND() '''

# list.append(element) - это метод листов, который добавляет указанный элемент в конец листа

# list_ = []
# for i in range(0, 11, 2):
#     list_.append(i)

# print(list_) # [0, 2, 4, 6, 8, 10]

'''-------------------------------------------------------'''

# list_ = []
# for i in range(11): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     if i == 0:
#         list_.append(None)
#     elif i % 2 == 0:
#         list_.append(True)
#     else:
#         list_.append(False)

# print(list_) # [True, False, True, False, True, False, True, False, True, False, True]

'''-------------------------------------------------------'''

# list_=[1,2,3,True,False,'Rem']
# list_.append('Anton')
# print(list_) #[1, 2, 3, True, False, 'Rem', 'Anton']

# str_='hohoho'
# str_ = str_.replace('o', 'a')
# print(str_)


''' EXTEND() '''

#list1.extend(list2) - это метод листов, который расширяет первый лист за счет второго листа

# list1=[1,2,3]
# list2=[4,5,6]
# list1.append(list2) # [1, 2, 3, [4, 5, 6]] добавляет вложенный элемент
# print(len(list1)) # 4

# list1=[1,2,3]
# list2=[4,5,6]
# list1.extend(list2) # [1, 2, 3, 4, 5, 6] добавляет распакованный элемент
# print(len(list1)) # 6


''' INSERT() '''

# list.insert(index, element) - это метод листов, который на место index добавляет element

# list_=[0,0,0,0,0,0,0,0,0,0,0]
# list_.insert(5, True)

# print(list_) # [0, 0, 0, 0, 0, True, 0, 0, 0, 0, 0, 0]

'--------------------------------------------------------'

# list_=[25, 12, 1, 'makers', None, [1,2,3,0,5,10]]
# list_[5].insert(5, 'hello') # [25, 12, 1, 'makers', None, [1, 2, 3, 0, 5, 'hello', 10]]

# print(list_)


''' INDEX() '''

# list.index(element, start, end) - это метод листов, который находит индекс указанного элемента

# list_=['NYC', 'Moscow', 'SP', 'Bishkek', 'Osh']
# for city in list_:
#     print(f'Город - {city} под индексом {list_.index(city)}')

# Город - NYC под индексом 0
# Город - Moscow под индексом 1
# Город - SP под индексом 2
# Город - Bishkek под индексом 3
# Город - Osh под индексом 4


''' POP() '''

# list.pop(index) - это метод листов, который удаляет и возвращает элемент по указанному индексу. Если индекс не указать, он удалит последний элемент

# list_=[1, 2, 3, 12, 123, 43, 12, 4, 5]

# pop_element = list_.pop(3) 

# print(list_) # [1, 2, 3, 123, 43, 12, 4, 5]
# print (pop_element) # 12

'-------------------------------------------'

# list_=[1, 2, 3, 12, 123, 43, 12, 4]

# pop_element = list_.pop() 

# print(list_) # [1, 2, 3, 12, 123, 43, 12]
# print (pop_element) # 4


''' REMOVE() '''

# list.remove(element) - это метод листов для удаления какого-либо элемента, если такого элемента нет, то выйдет ошибка

'-------------------------------------------'

# list_=[1,2,3,4,5,6,6,7,'hello']

# list_.remove('hello') # [1,2,3,4,5,6,6,7]

# print(list_)


''' SORT() '''

# list.sort(key=len, reverse=True) - это метод листов для сортировки его элементов

# list_=['SultanTalaibekov', 'SanjarKadyrkulov', 'Aigerim', 'Erkaiym']
# list_.sort() # ['SultanTalaibekov', 'SanjarKadyrkulov', 'Aigerim', 'Erkaiym']
# print(list_)

'-------------------------------------------'

# list_=[1,23,45,46,213,77,9,3]
# list_.sort(reverse=False) # [1, 3, 9, 23, 45, 46, 77, 213]
# print(list_)


''' COUNT() '''

# list.count(element) - это метод листов, который считает сколько элементов есть в листе

# list_=[1,2,25,67,43,23,67,87,100,33,1,1,25,67,67,6,67,87]
# count_list = list_.count(1) # 3 раза встречается число 1
# print(count_list) 


''' COPY(), DEEPCOPY() '''

# list.copy() - это метод листов, который копирует лист поверхностно
# copy.deepcopy(list) - это метод листов, который копирует лист углубленно

# list=[1,2,3,4,5,[1,2,3]]
# copy_list=list.copy()

# list[-1].append(0)

# print(list) # [1,2,3,4,5,[1,2,3]]
# print (copy_list) # [1,2,3,4,5,[1,2,3]]

'-------------------------------------------'

# import copy

# list1=[1,2,3,4,5,[1,2,3]]
# copy_list = copy.deepcopy(list1)

# list1[-1].append(0)

# print(list1) #[1, 2, 3, 4, 5, [1, 2, 3, 0]]
# print(copy_list) #[1, 2, 3, 4, 5, [1, 2, 3]]

'-------------------------------------------'


''' REVERSE() '''

# list.reverse() - это метод листов, который переворачивает лист

# list_ = [1,2,2,3,4,5,6,7,8,9,10]
# list_.reverse() # [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1]
# print(list_)




'''find max and min list'''
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]] 

# if len(lists) == 1:
#     print(f'max_list {lists[0]}')
#     print(f'min_list {None}')
# else:
#     list_of_len = []
#     for x in lists:
#         list_of_len.append(len(x))

#     min_value = min(list_of_len)
#     max_value = max(list_of_len)
#     if min_value == max_value:
#         max_index = list_of_len.index(max_value)
#         print(f'max_list {lists[max_index]}')
#         print(f'min_list {None}')
#     else:
#         min_index = list_of_len.index(min_value)
#         max_index = list_of_len.index(max_value)
#         print(f'max_list {lists[max_index]}')
#         print(f'min_list {lists[min_index]}')



'''find max and min list'''
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]] 

# max_value = max(lists, key=len)
# min_value = min(lists, key=len)

# if max_value == min_value:
#     print(f'max_list {max_value}')
#     print(f'min_list {None}')

# else:   
#     print(f'max_list {max_value}')
    # print(f'min_list {min_value}')

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# for k,v in dict_.items():
#     if v['rating'] > 3:
#         v['likes'] += 0
# print(v['likes'])
'====================================='
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# for x in lists:
    # for y in x:
    # if sum(x[0]) > sum(x[1]):

# print(max(lists))

'====================================='

def collect_all_possibles(list_: list, num: int) -> list:
    try:
        for i in list_:
            print([i+num, 
            i-num,
            i*num, 
            i**num, 
            i//num ])


    except (TypeError, ValueError) as error:
        print([i+num, 
            i-num,
            i*num, 
            i**num, 
            i//num ])

list_ = [
    'hello',
    6, 
    [1,2,3]
]

num = 2

collect_all_possibles(list_, num)