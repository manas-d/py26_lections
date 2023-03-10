# Типы данных в питоне

# 1. NoneType - ничего, пустота -> None
# 2. Boolean - истина или ложь -> True/False
# 3. str() -> строки -> "Hello world", 'Hello world'
# 4. Числовые типы данных
    # a) integer - int() - целое число ->  -1, 2, 555
    # b) float() - Число с плавающей точкой/Дробные числа -> 1.5, 15.2
    # c) complex() - 3+5i6 (используется для datascience и ml)
# 5. Списковые типы данных (коллекция)
   # a. list (массив/список) -> [1, 2, 4, True, 'hello'] - можно редактировать, представляем как ящик или коробку для хранения данных
   # b. tuple (кортеж) -> (1, 2, 3, None) - нельзя редактировать
   # c. range (последовательность) -> range(1, 10) - последовательность чисел С 1 ДО 10 (10 не вкл)
# 6. set() -> множества -> {1,2,3,4,5,6,8}
# 7. dict (словари) -> содержит данные в себе в виде ключа и значения {1: 'one', 2: 'two'}
    # john snow : +996 700 700 700 - каждому ключу (john snow) соответствует значение (номер)

# **********************************

# Mutable (изменяемые типы данных)
    # 1. list
    # 2. set
    # 3. dict
# Immutable (неизменяемые типы данных)
    # 1. nonetype
    # 2. boolean
    # 3. int, float, complex
    # 4. str
    # 5. range
    # 6. tuple
    # 7. frozenset
#---------------------------------------

# num=5
# stroka - 'Hello world! My name is John!'

'''Стандартный вывод данных'''
"""
в пайтоне для вывода данных в терминал 
используется встроенная функция print()
"""

# stroka = 'Hello world! My name is John Snow!'
# print(stroka)
# print(27+5)

"""
Стандартный ввод данных через терминал
используется функция input()
"""
# a = input('Введите число: ')
# print (a)
