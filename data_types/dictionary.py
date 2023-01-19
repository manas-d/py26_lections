# ['John', 'Snow', 24, 500, '+995700123123', 'Winterfell']
# obj = {'name': 'John, "last_name': 'Snow', 'age': 24, 'cash': 500, 'phone_number': '+995700123123'}
# print(obj['name'])
# print(obj['cash'])
# print()

# dict() - словарь -> упорядоченная коллекция элементов (python 3.7 -> ordered). Каждый элемент внутри словаря содержится в паре ключ: значение. Литералами являеются {''}. 
# Ключи должны быть неизменяемым типом данных (str, int, tuple etc.), тогда как значениями могут выступать любые типы данных.

# thisdict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print(thisdict)
# print(type(thisdict))

#ассоциативный массив, hash table, object(js), structure == dictionary(py)

# user_info = {'first_name': 'John', 
#             'last_name': 'Snow', 
#             'age': 23, 
#             'email': 'johnsnow73@gmail.com', 
#             'role': 'moderator', 
#             #[1,2,3]: 'list', #error
#             #'first_name': 'Raychel' #нельзя указывать дубликаты, будут отображаться вторые данные
#             }
# print(user_info)
# print(user_info.get('first_name')) # None
# print(user_info['first_name1']) # error


#------------------------------------------------
# user_info = {'first_name': 'John', 
#             'last_name': 'Snow', 
#             'age': 23, 
#             'email': 'johnsnow73@gmail.com', 
#             'role': 'moderator'}

# print(dir(dict))

# print(user_info.values()) #dict_values(['John', 'Snow', 23, 'johnsnow73@gmail.com', 'moderator'])
# print(user_info.keys()) #dict_keys(['first_name', 'last_name', 'age', 'email', 'role'])
# print(user_info.items()) #dict_items([('first_name', 'John'), ('last_name', 'Snow'), ('age', 23), ('email', 'johnsnow73@gmail.com'), ('role', 'moderator')]) #TUPLE

# for x in user_info:
#     print(x) 
#first_name
#last_name
# age
# email
# role

# for x in user_info.values():
#     print(x) 
# John
# Snow
# 23
# johnsnow73@gmail.com
# moderator

# for key, value in user_info.items(): 
#     print(key, value) 
# first_name John
# last_name Snow
# age 23
# email johnsnow73@gmail.com
# role moderator


#------------------------------------------------

# dict_ = {1: 15, 2: 11, 3: 18, 4: 5, 5: 21} # задача: возвести в квадрат нечетные значения словаря

# for key, value in dict_.items():
#     if key % 2 == 0:
#         print (key, 'четное')
#     else:
#         print (key, 'нечетное')
#         dict_ [key] = value ** 2

# print(dict_) #{1: 225, 2: 11, 3: 324, 4: 5, 5: 441}

#------------------------------------------------

'''изменения словаря'''

# dict_ = {'name': 'John', 'age': 24}
# print(dict_) #{'name': 'John', 'age': 24}
# dict_['age'] = 23 #изменения
# dict_['address'] = 'winterfell' #добавление ключа и значения
# print(dict_) #{'name': 'John', 'age': 23, 'address': 'winterfell'}

'''UPDATE метод для изменения данных в dict()'''

# dict_ = {'name': 'John', 'age': 24}
# print(dict_) #{'name': 'John', 'age': 24}
# dict_.update({'age': 18, 'address': 'winterfell'})
# print (dict_) #{'name': 'John', 'age': 18, 'address': 'winterfell'}


#------------------------------------------------


'''FROMKEYS'''

#fromkeys - быстрое создание словаря из ключей


# keys = ['one', 'two', 'three']

# new_dict = dict.fromkeys(keys, 'value') #{'one': 'value', 'two': 'value', 'three': 'value'}
# print(new_dict) 


# dict_={}
# ls = list(range(1, 101))

# new_dict = dict_.fromkeys(ls, ' value')
# print(new_dict)



#------------------------------------------------

'''SETDEFAULT'''

# setdefault - работает так же как и метод get(), но если нет такого ключа, то он создаст новый

# dict_ = {'name': 'John', 'age': 24}
# print(dict_.setdefault('age', 35)) #24 но не установится новое значение, тк значение уже есть
# print(dict_.setdefault('name')) #John
# print(dict_.setdefault('phone', '1234567')) #1234567 - устанавливает новое значение
# print(dict_) #{'name': 'John', 'age': 24, 'phone': None}


#------------------------------------------------

'''POP, POPITEM УДАЛЕНИЕ ИЗ СЛОВАРЯ'''

#pop(key) - удаляет элемент по ключу

# dict_={'name': 'John', 'last_name': 'Snow', 'address': 'winterfell'}
# print(dict_) #{'name': 'John', 'last_name': 'Snow', 'address': 'winterfell'}
# removed=dict_.pop('address')
# print(removed) # показывает удаленное значение
# print(dict_) #{'name': 'John', 'last_name': 'Snow'}

# popitem() - удаляет последние ключ и значение

# dict_={'name': 'John', 'last_name': 'Snow', 'address': 'winterfell'}
# print(dict_) #{'name': 'John', 'last_name': 'Snow', 'address': 'winterfell'}
# removed=dict_.popitem()
# print(removed) #('address', 'winterfell')
# print(dict_) #{'name': 'John', 'last_name': 'Snow'}
# key, value = removed
# print(key, value)


''' Примеры: '''

# roles = {
#     0: 'Moderator',
#     1: 'Admin',
#     2: 'Customer',
#     3: 'Vendor'
# }

# users = {
#     '1': {'username': 'JohnSnow', 'role': roles[1]},
#     '2': {'username': 'JamieLanister', 'role': roles[2]},
#     '3': {'username': 'Mufasa', 'role':roles[3]}
# }

# product = {
#     'id': 1,
#     'title': 'Iphone 14 pro max',
#     'description': 'Lorem Ipsum',
#     'price': 200
# }
# i = '1'
# while i == '1' or '2':
    
#     i = input('\nВведите что хотите сделать:\n\nЕсли хотите просмотреть товар, то нажмите 1\nЕсли хотите изменить товар, то нажмите 2\nЕсли хотите выйти, то нажмите 3 или что-то другое\n\nВаш выбор:   \n')
#     if i == '1':
#         print(product)

#     elif i == '2':
#         id_user = input('\nВведите Ваш ID:  \n')
#         if not users.get (id_user):
#             print('\nНет такого юзера!\n')

#         elif users.get (id_user)['role'] == roles[1]:
#             print(users.get(id_user))
#             choise = input('\nВведите что изменить (title, description, price):   \n')
#             new = input(f'\nВведите новое значение {choise}:  \n')
#             product.update({choise: new})
#             print ('\nUpdated!\n')
#         else:
#             print(users.get(id_user))
#             print('\nСорри только админ может редактировать! У тебя нет разрешения!\n')



print(dir(dict))




