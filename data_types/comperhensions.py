'''Условие 1'''
# list -> 0: 200 -> num % 2 == 0

# ls = list(range(0, 201, 2))
# print(ls)

'''Условие 2'''
# list -> 0: 300 -> num % 2 == 0 and num % 3 == 0

# ls = []
# for x in range (0, 300):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
# print(ls)

'''Условие 3'''
# list -> 0: 100 -> x % 2 == 0: x **2, x

# ls = []
# for x in range (0, 100):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     else:
#         ls.append(x)
# print(ls)
'''--------------------------------------------------------------------'''
'''ГЕНЕРАТОРЫ'''

# list comperhensions - генераторы списков
# list comperhensions - упрощенный подход к созданию списков, который задействует цикл FOR, а так же конструкции IF / ELSE для определения условий в генерации

''' newlist = [expression for item in iterable <if condition = True]'''

'''Условие 1'''
# list -> 0: 200 -> num % 2 == 0
'''-------------------------------------------------'''
# ls = [x for x in range (0, 200) if x % 2 == 0]
# print(ls)

'''Условие 2'''
# list -> 0: 300 -> num % 2 == 0 and num % 3 == 0

# ls = []
# for x in range (0, 300):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
# print(ls)
'''-------------------------------------------------'''
# ls = [x for x in range (0, 300) if x % 2 == 0 and x % 3 == 0]
# print(ls)

'''Условие 3'''
# list -> 0: 100 -> x % 2 == 0: x **2, x

# ls = []
# for x in range (0, 100):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     else:
#         ls.append(x)
# print(ls)

'''-------------------------------------------------'''

# ls = [x**2 if x % 2 == 0 else x for x in range(0, 100)]
# print(ls)


'''--------------------------------------------------------------------'''

# ls = [x**2 for x in range (1, 11)]
# print(ls)

'''--------------------------------------------------------------------'''

# ls = [x**3 if x % 2 != 0 else x + 100  for x in range (1, 11)]
# print(ls)

'''--------------------------------------------------------------------'''

# ls = list(range(0,11))
# i = 0
# for x in ls:
#     i += 1
#     if i == 4:
#         i = 0
#         index = ls.index(x)
#         ls.insert (index, 'John')
# print(ls)

'''--------------------------------------------------------------------'''

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# result = [x + 10 if x % 2 ==0 else x ** 2 for inner in ls for x in inner]
# print(result) #[1, 12, 9, 14, 25, 16, 49, 18, 81]

'''--------------------------------------------------------------------'''

# from datetime import datetime
# from time import sleep

# start = datetime.now()

#1 решение
#ls = [x for x in range(1, 100_000_000)] #2 sec
#2 решение
# ls = []
# for x in range (1, 100_000_000):
#     ls.append(x) # 7 sec

# finish = datetime.now()
# print(finish - start)

'''--------------------------------------------------------------------'''

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'lemon']
# ls = [x for x in fruits if x != 'apple']
# print(ls) #['banana', 'kiwi', 'mango', 'lemon']





# fruits = ['apple', 'banana', 'kiwi', 'mango', 'lemon', 'mandarin']
# ls = [x for x in fruits if not x.startswith('m')]
# print(ls) #['apple', 'banana', 'kiwi', 'lemon']




# fruits = ['apple', 'banana', 'kiwi', 'mango', 'lemon', 'mandarin']
# ls = [x.upper() for x in fruits if not x.startswith('m')]
# print(ls) #['apple', 'banana', 'kiwi', 'lemon']

'''--------------------------------------------------------------------'''

# a = {x for x in range(1, 11)}
# print(a)
# print(type(a))
'''--------------------------------------------------------------------'''

# dict_ = {x: x ** 2 for x in range (1, 15)}
# print(dict_)

'''--------------------------------------------------------------------'''

# dict_ = {
#         'a': 1, 'b': 2, 'c': 3,'d': 4,
#         'e': 5, 'f': 6, 'g': 7,'h': 8
#         }
# # 'a': 'odd', 'b': 'even'
# newdict  = {
#     k: 'odd' if v % 2 != 0 else 'even' 
#     for k, v in dict_.items()
#     }
# print(newdict)


# list_ = [1, 2, 3, 4]
# for i in range(0, len(list_) + 1):
#     print(list_[i])
