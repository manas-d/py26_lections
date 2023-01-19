"""ЦИКЛЫ"""

# while <expression>:
#     <body>

#-----------------------------------------------------

# i = 0
# while i < 10:
#     i += 1
#     print(f'цикл выполнился {i} раз')

#-----------------------------------------------------

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != "john" and name2.lower() != 'raychel':
#     name1 = input('Введите имя1:')
#     name2 = input('Введите имя2:')
#     i += 1
#     if i >= 5:
#         print('Вы использовали все попытки!')
#         break
# else:
#     print('Вы ввели верное имя!')

#-----------------------------------------------------
# Моржовый оператор

# user = {'username': 'John', 'password':'ilovepython123'}
# i = 3
# while (password := input (f'{user["username"]} input password: ') != user['password']):
#     i -= 1
#     if i == 0:
#         print('You are blocked for 5 days')
#         break
# else:
#     print(f'Welcome {user["username"]}')

#-----------------------------------------------------
#Без моржового оператора

# user = {'username': 'John', 'password':'ilovepython123'}
# i = 3
# password = None
# while password != user['password']:
#     if i == 0:
#         print('You are blocked for 5 days')
#         break
#     i -= 1
#     password = input (f'{user["username"]} input password: ')
    
# else:
#     print(f'Welcome {user["username"]}')

#-----------------------------------------------------

# for <variable> in <iterable object>:
#     <body>

# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_[::-1])
# print(i) #<list_iterator object at 0x10075d040>
# print(next(i)) #0 #9
# print(next(i)) #1 #8
# print(next(i)) #2 #7
# print(next(i)) #3 #6

#-----------------------------------------------------

# import random

# ls = []

# for x in range(1,101):
#     ls.append(random.randint(1,1000))

# print(ls)
# ls.sort()
# print(ls)

# ls = set(ls)
# ls = list(ls)
# ls.sort()
# res = []
# for x in ls:
#     if x%2 == 0:
#         res.append(x)
# print(res)

#-----------------------------------------------------

#Дано число 100
#Делители 1,2,4,5,10,20,25,50,100

# x = 23436
# res = []
# for i in range(1,x+1):
#     if x%i==0:
#         res.append(i)
# print(res)
"Этот код затрудняется при вычислении больших чисел"

# x = 190123132
# res = [1, x]
# for i in range(2, int((x**0.5)+1)):
#     if x%i==0:
#         res.extend({i, x//i})

# res.sort()
# print(res)
"Этот код легко справляется с вычислением больших чисел"

#-----------------------------------------------------

