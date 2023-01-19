'''СЛОВАРИ 36'''
# a = {'a': 10, 'b': 9, 'c': 3}
# result = a.get('a') * a.get('b')*a.get('c')
# print(result)


'''find max and min list in lists'''
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


# a = {'x': 1, 'y': 2, 'z': 1}
# print(a['y'])


'''extra task'''

# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())

# for i in range(3):
#     if (i + 1) == inp2:
#         a[i].add(inp1)
#     else: a[i].add("default value")

# print(a)

'''extra task 2'''

# set1 = {i*2 for i in range(5)}
# set2 = {i*2+1 for i in range(5)}

# if set1 & set2:
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')


# a = {'a': 1, 'b': 2, 'c': 1}

# for k, v in a.items():
#     print(v)
'''
a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
b = {}
for k, v in list(a.items()):
    if v%2==0:
        b[k]=2
print(b)
'''

''' 3'''
# name_of_list = ['1234567']
# new_list = name_of_list[0]
# i = len(new_list)

# if i%2==0:
#     new_list = name_of_list[0][i//2:] + name_of_list[0][:i//2]
# else:
#     new_list = name_of_list[0][i//2+1:] + name_of_list[0][:i//2+1]

# print(list(new_list))


''' 4
list_ = ['world', 'hello'] 
list_.reverse()
print(list_)
''''''
'''
# list1=[11, 23, 45, 7, 9] 
# list2=[21, 4, 16, 8, 10] 
# list1.extend(list2)
# print(sum(list1))
'''

'''
# inp = input()
# list_ = []
# for i in inp:
#     list_.append(i)
# print(list_) #['1', ',', '2', ',', '3', ',', '4', ',', '5']
'''
'''
# list_ = [20, 10, 20, 1, 100]
# myMin = list_[0]

# for i in list_:
#     if list_[i] < myMin : myMin=list_[i]
# print('min_number =', myMin)
'''
'''

# Типы данных. Списки. Цикл for. Таск 20

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# res = int()
# for i in list_:
#     if type(i) == int and str(i).isdigit():
#         res += i
# print(res)

# '''CALCULATOR   '''
# inp1 = int(input('Введите первое число: '))
# inp2 = int(input('Введите второе число: '))
# operation = input('Выберите операцию из следующих +-*/%**// : ')

# if operation == '+':
#     print('Ответ:', inp1+inp2)
# elif operation == '-':
#     print('Ответ:', inp1-inp2)
# elif operation == '*':
#     print('Ответ:', inp1*inp2)
# elif operation == '/':
#     print('Ответ:', inp1/inp2)
# elif operation == '%':
#     print('Ответ:', inp1%inp2)
# elif operation == '**':
#     print('Ответ:', inp1**inp2)
# elif operation == '//':
#     print('Ответ:', inp1//inp2)
# else:
#     print('Ответ: Данной операции нет в системе')

'''
Типы данных. Списки. Цикл for. Таск 21

str_list = ['abc', 'xyz', 'aba', '1221']
indexs = []
for i in str_list:
    if i[0] == i[-1]:
        indexs.append(str_list.index(i))

print(indexs)
'''


# size = 3
# list1 = [0, range(size)]

# print(list1)

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# dict1 = {}
# for k, v in dict_.items():
#   for x,y in v.items():
#     dict1.setdefault(k,y)
# print(dict1)

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()
# for k,v in dict_.items():
#     if key == k:
#         print("Key is present in the dictionary")
#     else:
#         print("Key is not present in the dictionary")
#     break