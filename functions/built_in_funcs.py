'''Встроенные функции'''

# map
# filter
# lambda
# enumerate
# zip, all, any
# (reduce) - уже не встроенная, сейчас в библиотеке FuncTools


'''Анонимные функции - lambda (такие же функции, только без названия)'''

'''lambda функции могут принимать сколько угодно аргументов, но всегда возвращают одно выражение'''

# def sum_of_args(a,b):
#     res = a + b
#     return res

# print(sum_of_args(1,2))

# a = sum_of_args
# print(a(5,15))

# sum_of_args2 = lambda a,b,c: a+b+c
# print(sum_of_args2(5,15,20))

'''======================================================='''

# x = lambda a,b,c: (a*b)%c
# print(x(11,5,10))

# get_last = lambda ls: ls[-1]
# ls = [1,2,3,4,5,6, True, False, [123],'last']
# print(get_last(ls))

'''======================================================='''

# def myFunc(n):
#     return lambda a: a*n

# myDoubler = myFunc(2)
# print(myDoubler(50))
# print(myDoubler(100))
# print(myDoubler(23))

'''======================================================='''

# dict_ = {'John':50_000, 'Sultan':5, 'Jamie':1000, 'Aigerim':1_000_000}
# res = dict(sorted(dict_.items(), key = lambda x: x[1], reverse = True))
# print(res)

'''======================================================='''

'''map (function, iterable) - применяет функцию к каждому элементу из последовательности и возвращает mapobject (итератор) с результатом'''

# ls = ['one', 'two', 'three', 'four']


# for i in range(0, len(ls)):
#     ls[i] = ls[i].upper()

# print(ls)

'''======'''

# res = list(map(str.upper, ls))
# print(res)

'''======================================================='''

# names = ['John', 'Sultan', 'Jamie', 'Raychel']
# # ['Hello mr/mrs John', 'Hello mr/mrs Sultan', ...]
# res = list(map(lambda name: f'Hello mr/mrs {name}', names))
# print(res)

'''======================================================='''

# dict_ = {1:2, 3:4, 5:6}
        # {1:'2', 3:'4', 5:'6'}


# for k in dict_:
#     dict_[k] = str(dict_[k])

# print(dict_) #{1: '2', 3: '4', 5: '6'}

'''======'''

# res = dict(map ( lambda x: (x[0], str(x[1])), dict_.items()))
# print(res) #{1: '2', 3: '4', 5: '6'}

'''======================================================='''

'''filter(function, iterable) -> применяет ко всем элементам iterable функцию которую мы переделали и возвращает итератор с теми элементами для которых функция вернула True'''

# ls = ['one', 'two', '', 'list', '100', '1', 'John']
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)
# print(res)

# res = list(filter(str.isdigit, res))
# print(res)

# ls  = ['john', 'makers', 'Sultan', 'ono', 'py26', 'Kyrgyzstan', 'mountains']
# res = list(filter(lambda stroka: len(stroka) > 5, ls))
# print(res)

'''======================================================='''

# ls = [
#     {'name': 'Python', 'point': 10},
#     {'name': 'C++', 'point': 6},
#     {'name': 'JS', 'point': 8},
#     {'name': 'Java', 'point': 3},
#     {'name': 'C#', 'point': 0},
# ]

# res = list(filter(lambda dict_: dict_['point'] >= 7, ls))
# print(res)

'''======================================================='''

# users = [
#     {'username':'John', 'comments':['I love you', 'Really good']},
#     {'username':'Raychel', 'comments':[]},
#     {'username':'Steven', 'comments':['Bishkek', 'Python']},
#     {'username':'Hello', 'comments':[]},
#     {'username':'Kira', 'comments':['The best post']}
# ]

# # res = list(filter(lambda dict_: len (dict_['comments']) < 1, users))
# res = list(filter(lambda dict_obj: not dict_obj['comments'], users))
# print(res)

'''======================================================='''

# names = ['Raychel', 'Sultan', 'Aigerim', 'John', 'Kira', 'Bob']
# new_names = list(
#     map(
#         lambda name:f'Your name is {name}!', 
#         filter(lambda x : len(x) > 4, names))
#         )
# print(new_names)

'''======================================================='''

# from functools import reduce

# ls = [1,2,3,4,5,6]
# # sum_ = reduce(lambda a,b: a+b, ls)
# res = reduce(lambda a,b: a * b, ls)
# # print(sum_)
# print(res)

'''======================================================='''

# ls = ['John', 'Sultan', 'Katana', 'Aigerim']
# for i,obj in enumerate(ls): #пронумеровывает элементы по индексам
#     print(i, obj)
# print(enumerate(ls))

'''======================================================='''

# import string as s
# import random

# def generate_rand_str():
#     symbols = s.ascii_letters + s.digits
#     res = ''.join(random.choice (symbols) for i in range(0,10))
#     return res
# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())

'''======================================================='''

# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = '_()$!%+-@'
# q_pass = int(input('Vvedite kolichestvo parolei: '))

# res = {
#     f(choices(ascii_letters, k=10), choices(digits, k = 5), choices(symbols, k=2))
#     for f in repeat(lambda x, y, z : ''.join(set(x+y+z)), q_pass)
# }

# print(res)
# print(f'Qauntity of passwords: {len(res)}')

# from statistics import mean

# dlina = [len(x) for x in res]
# print(f'Average len: {mean(dlina)}')


'''======================================================='''

'''zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой, по их распорядку, в тип данных tuple и возвращает его'''

# ls1 = [1,2,3]
# ls2 = [100,200,300]

# res = list(zip(ls1, ls2)) #[(1, 100), (2, 200), (3, 300)]
# print(res)

'''======================================================='''

# ls1 = [1,2,3,4,5]
# ls2 = [100,200,300,400,500]
# ls3 = [10,20,30]

# res = list(zip(ls1, ls2, ls3)) #[(1, 100, 10), (2, 200, 20), (3, 300, 30)]
# print(res)

'''======================================================='''

''' zip для создания словарей '''

# a = dict([(1,2), (3,4)])
# print(a)
# {1:2, 3:4}.items()
# dict_items[(1,2), (3,4)]

'''======================================================='''

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['apple_r1', 'winterfell', 'jobs', 'watch', '16.0', '10.255.0.1']
# res = dict(zip(d_keys,d_values))
# print(res)

'''======================================================='''

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1' : ['london_r1', 'new globe walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'r2' : ['london_r2', 'North London', 'Cisco', '4451', '16', '10.25.10.11'],
#     'sw1' : ['london_sw1', 'South West', 'Cisco', '3850', '16.4', '10.2.12.12']   
# }

# print(data)
# for k in data:
#     data[k] = dict(zip(d_keys, data[k]))
# print()
# print(data)

'''======================================================='''

'''all(), any()'''

'''all(iterable) - возвращает True, если все элементы внутри объекта истина, иначе возвращает False'''

# all([1,2]) -> True
# all([]) -> True
# all([[]]) -> False
# all(['false', 'john', 5,6,1]) -> True
# all([1,2,3], 5, None) -> False

# print(all([[1,2], 5, 'stroka', True, 1]))

'''======================================================='''

# ip = '10.10.10y.10'
# res = all(i.isdigit() for i in ip.split('.'))
# print(res)

'''======================================================='''

'''any - возвращает True, если хотя бы один элемент истина'''

# ls = [0, 0, 0, '', False, 1]
# print(any(ls))

'''======================================================='''

# ignore = ['rm -rf', 'reset', 'alias']
# command = input('Enter command: ')
# # sudo nano file

# if any(word in command for word in ignore):
#     raise Exception('Invalid command')
# print('Vse ok!')

'''======================================================='''

