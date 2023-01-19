'''
Функция высшего порядка - это функция, которая в качестве аргумента принимает другую функцию.

Декоратор - это функция, которая позволяет без изменения кода обернуть другую функцию для того, чтобы расширить функционал обернутой функции.
'''

# def decorator(func):
#     print(f'Called Func name: {func.__name__}') #2
#     return func() #3: call func #6: return 'Hello'


# def hello():
#     print('Vsem privet!') #4
#     return 'Hello' #5

# def john():
#     print('Hello my name is John Snow!')
#     return 'John Snow'

# # hello()
# # john()
# a = decorator(hello) # вызов №1 # Called Func name: hello # Vsem privet!
# b = decorator(john) # Called Func name: john # Hello my name is John Snow
# print(a,b) # Hello John Snow

'----------------------------------------------------------------------------------'

# from typing import Callable


# def benchmark(func: Callable):
#     import time
#     start = time.time()
#     res = func()
#     finish = time.time()
#     print(f'Время выполнения функции {func.__name__} заняло {finish - start}')
#     return res

# def loop():
#     i = 1
#     range_number = 100_000
#     while i < range_number:
#         # print(i)
#         i += 1
#     return i

# print(benchmark(loop))

'----------------------------------------------------------------------------------'

# Pythonic way -> @decorator
# Синтаксический сахар -> это красота кода

# from typing import Callable

# def benchmark(func: Callable):
#     def wrapper(): #2
#         import time
#         start = time.time()
#         res = func() #3 #содержит в себе функцию loop
#         finish = time.time()
#         print(f'Время выполнения функции {func.__name__} заняло {finish - start}')
#         return res
#     return wrapper

# @benchmark #оборачиваем функцию loop в функцию benchmark
# def loop(): #4
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1
#     return i

# @benchmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         i += 1
#         ls.append(i)
#     return ls

# print(loop()) #1 #вызывает benchmark -> wrapper -> res=func() -> loop
# add()

'----------------------------------------------------------------------------------'

# def strong(func):
#     def wrapper (*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrapper

# @div #3
# @strong #2
# @div #1
# def john():
#     return 'John Snow'

# print(john())

'----------------------------------------------------------------------------------'

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвана {func.__name__}(),\n{args} {kwargs}')
#         origin_result = func(*args, **kwargs)
#         print(f'Trace: вызвана {func.__name__}(),\nвернула {args} {kwargs}')
#         return origin_result
#     return wrapper

# @trace
# def say (name, line):
#     return f'{name}: {line}'

# print(say('John', line = 'Snow'))

'----------------------------------------------------------------------------------'

# def func():
#     print('hello world')
#     return func

# func()()()()()() # выведет 'hello world' 6 раз
# # Вывод:
# # hello world
# # hello world
# # hello world
# # hello world
# # hello world
# # hello world

'----------------------------------------------------------------------------------'

# users = ['Nurkamila']

# def login_required(post):    # post
#     def wrapper(user, post_):   # user, post_
#         if user in users:
#             return post(user, post_)
#         else:
#             return 'There is no such user'
#     return wrapper


# @login_required
# def post(user, post_):
#     return 'Succesfully posted'

# print(post('Aigerim', 'cakes'))
# print(post('Nurkamila', 'cakes'))
