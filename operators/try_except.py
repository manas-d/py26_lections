'''ОБРАБОТКА ИСКЛЮЧЕНИЙ'''
"""ОПЕРАТОР TRY EXCEPT"""

'''Ошибки - связаны с кодом:'''

# SyntaxError
# IndentationError
# TabError

'''Исключения - Invalid values:'''

# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# IndexError
# ValueError
# ImportError
# BaseException - прародитель всех исключений

'''TRY EXCEPT'''

# try:
#     <body try>
# except <Ecxeption>:
#     <body>
# <else>:
#     <body> Только если все ок
# <finally>:
#     <body> Срабатывает в любом случае в конце

'''----------------------------------------------------------------------------------'''

# num1 = int(input('Vvedite chislo: '))
# print(num1)
# print('Important!')

'''-'''

# try:
#     num1 = int(input('Vvedite chislo: '))
# except ValueError:
#     print('Invalid value')
# else:
#     print(num1)
# #finally: Обычно не используют
# print('Important!')

'''----------------------------------------------------------------------------------'''

# try:
#     num1 = int(input('Vvedite 1 chislo: '))
#     num2 = int(input('Vvedite 2 chislo: '))
#     print(num1/num2)
# except (ValueError, ZeroDivisionError) as error:
#     print('Vy vveli nekorrektnye dannye!')
#     print(error)

'''-'''

# try:
#     num1 = int(input('Vvedite 1 chislo: '))
#     num2 = int(input('Vvedite 2 chislo: '))
#     print(num1/num2)
# except Exception as error:
#     print('Vy vveli nekorrektnye dannye!')
#     print(error)

'''----------------------------------------------------------------------------------'''

# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Vvedite index: '))
#     res = list_[index]
#     print(res)
# except ValueError:
#     print('Value error!')
# except IndexError:
#     print('Index error!')

'''----------------------------------------------------------------------------------'''

# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     res = num1/num2
# except ZeroDivisionError:
#     print('Nelzya delit na 0!')
# except ValueError:
#     print('Invalid symbols for int()!')
# else:
#     print(res)
# finally:
#     print('The end!')



    