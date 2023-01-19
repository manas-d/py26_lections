# Операторы сравнения 
# Условные операторы
# Логические операторы

# операторы сравнения
# <, >, ==, <=, >=, !=(не равно)
 
# num1 = 18
# num2 = 18
# print(num1 >= num2)
# stroka1 = 'Aaaaa!'
# stroka2 = 'Aaaab!'
# print(stroka1 == stroka2)
# print(ord('H'))
# print(ord('W'))
# print(chr(1100))

# text = 'Hello world! My name is John!'

# if ord(text[5]) == 72:
#     print('Yes')
# else:
#     print ('Nooo!')

"""Условные операторы - они созданы, чтобы программа могла выполнять разные участки кода в зависимости от условия"""
# if, elif, else

# if <condition>:
#     <body if>
#     <body if> # сработает только если true
# elif <condition>:
#     <body elif>
# elif <condition>
#     <body elif>
# else:
#     <body else> # сработает только если во всех остальных false

# string = input('Enter smt: ')

# if string == 'Hello':
#     print ('Hello stranger!')
# elif string == 'John':
#     print ('Welcome back John Snow!')
# elif string == 'Mercedes':
#     print ('Mercedes Benz S class')
# else:
#     print ('Совпадений не найдено')

# print ('The end!')

# email = input ('Enter Email: ')
# password1 = input ('Enter password: ')
# if len(password1) < 8:
#     raise Exception ('Password too short! (password need at least 8 characters!)')

# password2 = input ('Enter password confirmation: ')
# if password1 != password2:
#     raise Exception ('Password didn\'t match')
# else:
#     print ('Successfully signed up')

# age = input ('Enter your age: ')

# if age.isdigit ():
#     age = int(age)
#     print (f'Your age: {age}!')
# else:
#     raise Exception('Enter the valid age (only digits)!')

# if age > 80:
#     raise Exception('Invalid age!')

# if age < 18:
#     print (f'Chuvak prihodi cherez {18-age} let/goda!')
# else:
#     print('Ty prohodish po vozrastu! Welcome!')

"""Логические операторы"""
# and -> логическое И
# or -> логическое ИЛИ
# not -> логическое отрицание

"""Операторы идентификации"""
# in -> проверяет наличие элемента внутри массива или строки
# is -> сравнивает ячейки памяти
# == сравнивает значения
# is not -> отрицательное сравнение двух ячеек
"""AND"""
# my_age = 20
# other_age = 18
# result = my_age == 21 and other_age == 18
#             # false               #true
#                         #FALSE
# print (result)
"""OR"""
# my_age = 20
# other_age = 18
# result = my_age == 21 or other_age == 18
            # false               #true
                        #TRUE (false если оба значения неверны)
# print (result)
"""NOT"""
# result = not my_age == 21
                #false
# print(result) #true - переворачивает булевые значения


# cash = int(input ('Enter your cash: '))
# if cash > 1_000 and cash < 10_000:
#     print ('Sredne!')
# elif cash >= 10_000 and cash < 100_000:
#     print ('Mnogo!')
# elif cash >= 100_000:
#     print ('Krasavchik!')
# else:
#     print ('Pechalno!')


# is_google_user = False
# is_github_user = False
# is_age_less_21 = True
# user_coin = 0

# if (is_google_user or is_github_user) and (is_age_less_21 or user_coin>5000):
#     print ('You can enter the system!')
# else:
#     print('Sorry! You couldn\'t enter!')

# str1 = 'Hello world!'
# choise = input('Enter the character: ')

# if choise in str1:
#     print (f'Символ {choise} есть в строке: "{str1}"!')
# else:
#     print (f'Символа {choise} нет в строке: "{str1}"!')

# a=5
# b=10
# if a<b and b>=10:
#     print(True)
# else:
#     print(False)



# x=int(input())
# y=int(input())

# if x%y == 0:
#    print('x делится на y')
#    print ('Частное: ', int(x/y))
# else:
#     print('x не делится на y')
#     print ('Частное: ', x//y)
#     print ('Остаток: ', x%y)

 
'''Задание 21
Даны три стороны треугольника a, b, c (inputs). Определите тип треугольника с заданными сторонами.
Выведите одно из четырех слов: rectangular для прямоугольного треугольника, acute для остроугольного треугольника, obtuse для тупоугольного треугольника или impossible, если треугольника с такими сторонами не существует.'''

# a,b,c=int(input()), int(input()), int(input())

# if a>b and a>c and a**2==b**2+c**2 or b>a and b>c and b**2==a**2+c**2 or c>a and c>b and c**2==a**2+b**2:
#     print('rectangular')
# elif a>b and a>c and a**2<b**2+c**2 or b>a and b>c and b**2<a**2+c**2 or c>a and c>b and c**2<a**2+b**2:
#     print('acute')
# elif a>b and a>c and a**2>b**2+c**2 or b>a and b>c and b**2>a**2+c**2 or c>a and c>b and c**2>a**2+b**2:
#     print('obtuse')
# else:
#     print('impossible')

