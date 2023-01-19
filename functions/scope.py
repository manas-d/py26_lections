'''SCOPE - Области видимости и пространства'''

# def func():
#     var = 15
#     return var * 2

# print(var)

# print(func())

'''Область видимости и пространства имен (scopes) определяет контекст переменной, в рамках которого мы можем ее использовать.'''

# a = 5
# print(a)            #глобальная область видимости
# def func():
#     print(a)        #локальная область видимости
# func()

'''
built-in (Встроенная) - print, len, max
global (Глобальная) - 
enclosed (Нелокальная, nonlocal) - 
local (Локальная) - 
'''

# x = 200     

# def func():
#     print(x, '!')
#     # x += 100
#     var = 100

# print(var)
# func()

'''---------------------------------------------'''

# a = 10          #global
# print()         #built-in

# def hello():    #global
#     a = 'hello world' #local
#     print(a, 'local inside at func')        

# hello()
# print(a, 'global')


'''LEGB описывает последовательность поиска имен
Local -> Enclosed -> Global -> Built-in'''


# enclosed

# x = 'global' #global
# print(x, '1')

# def enclosed():
#     x = 'enclosed' #enclosed
#     def local():
#         x = 'local' #local
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')

'''---------------------------------------------'''

# a = 10

# def func():
#     print(a)
#     a1 = 'local'
#     print(a1)

# func()

'''---------------------------------------------'''

# i = 0

# def increment():
#     i = i + 1

# increment()

'''
global -> позволяет изменять значения глобальной переменной, находясь в локальной (local) или замкнутой (enclosed) области видимости

nonlocal -> позволяет изменять значение не локальной переменной, находясь в локальной области видимости
'''

# var = 100

# def increment():
#     global var
#     var += 1

# print(var) #100
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var) #105

'''---------------------------------------------'''

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter()
# print(c) #<function counter.<locals>.increment at 0x1050809d0>
# print(c()) #1
# print(c()) #2
# print(c()) #3
# print(c()) #4
# print(c()) #5
# print(c()) #6
# print(c()) #7
# b = counter()
# print(c()) #8
# print(b()) #1
# print(b()) #2
# print(c()) #9

'''---------------------------------------------'''

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# i = counter()

# for x in range(0, 100):
#     if x % 3 == 0 and x % 5 == 0:
#         res = i()
#         print(res)

# print(f'Result: {res}')

'''---------------------------------------------'''

# print(len(dir(__builtins__))) #152

# 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'


'''---------------------------------------------'''

# globals(), locals()

# a = 5
# b = 6
# c = 7 
# def func():
#     john = 'John Snow'
#     print(locals())

# print(globals()) 
# print()
# func()

'''---------------------------------------------'''

# Дан список внутри которого список из трех чисел. Нужно найти максимальную сумму среди всех списков.

# ls = [[100,2,3], [300,3,5], [5,5,5,500], [45,45,6]] 

# result = max(sum(x) for x in ls)
# print(result)


def get_info(name:str, name2:str):
  name = input('Enter name: ')
  name2 = input('Enter name2: ')
  def generate_password(pswd):
    nonlocal name
    nonlocal name2
    pswd = name + name2 + str(range(0,9))
    return pswd

print(get_info('oleg', 'ivanov'))