"""Тип данных - строки"""

'''Строки - это набор последовательных символов, которые мы используем для хранения и представления текстовой информации'''

# name = 'John Snow'
# '       012345678'
#         # J=0
#         # o=1
#         # h=2
#         # n=3
#         # ...

# print (name[5]) #[5] - срез по индексу

# age = 2512 у чисел типа данных int нет индексации, только если обернуть число в тип str (текстовый формат)

""" СРЕЗЫ """

'''Срезы по индексам - это когда мы получаем определенную часть строки при помощи индексов'''

# print (name[0]) - выведет символ J

# Срезы [start : end : step]
'''     start - 0 символ / начальный индекс, по умолчанию стоит 0 индекс'''
'''     end - конец среза, который не включается в индексирование, по умолчанию берет до конца'''
'''     step - шаг среза, который указывает количество пропускаемых символов, по умолчанию стоит 1'''

# name = 'John Snow Man'
# snow1 = name [5:9] # Переменной 'snow' соответствует знаечение 'name' начиная с 5 до 9 символа
# snow2 = name [5:] # Начиная с 5 символа до конца фразы
# print (snow1) #Snow
# print (snow2) #Snow Man

# name = 'John Snow Man'
# john1 = name [0:4]
# john2 = name [:4]
# print (john1) #John
# print (john2) #John


# name = 'John Snow Man'
# '''     0123456789101112'''
# print (name[:]) # John Snow Man
# print (name[0:13:2]) #Jh nwMn каждый 2-ой символ пропустили (нечетные)
# print (name[0:13:3]) #Jnn n выводится 0й и каждый 3й символ

# name = 'sfsaffn,knfesnesnseknselnfseklfnjelnlevnerlNAMEvnekjv;env n;envelsnvsen n lnlenvelnfelvn enlken e'
# print(name[-1:]) # последний символ (нет 0 символа)
# print (name[-10]) # выведет 10й символ с конца

'''Перевернутая строка'''

# name = 'John Snow Man'
# reversed_name = name 
# print (reversed_name #John Snow Ma - исключен последний символ
# print (reversed_name[::-1]) #naM wonS nhoJ - вывод наоборот 

# name = 'John Snow Man'
# reversed_name_naM = name[12:9:-1] #naM - начало 12 символ (можно ничего не писать, по умолчанию возьмет послелний символ), конец 9 символ, обратный реверс
# reversed_name_wonS = name[8:4:-1] #wonS - начало 8 символ, конец 4 символ, обратный реверс 
# print (reversed_name_naM)
# print (reversed_name_wonS) 

'''Методы - Склеивание строк (конкатенация)'''

# first_name = 'Sultan'
# second_name = 'Talaibekov '
# full_name = first_name + ' ' + second_name
# print (full_name) #Sultan Talaibekov
# print (full_name*3) #Sultan Talaibekov Sultan Talaibekov Sultan Talaibekov 
# print(full_name*2.5) #error

'''Форматирование строк'''

'''
Способы (3 вида):
1. с помощью процента %
2. с помощью (.format())
3. интерполяция строк (f'строка')
'''

# 1. % -> %s

# name1 = input ('Введите свое имя: ')
# age = input ('Введите свой возраст: ')
# print ('Привет, меня зовут ', name, 'Dyikanov')
# print ('Привет, меня зовут '+ name + ' ' + 'Dyikanov')
# age = 25
# print ('Привет, меня зовут %s Dyikanov' %(age))
# print ('Привет, %s, мне %s лет' %(name1, age))

# 2. .format -> {}

# name = input ('Введите свое имя: ')
# age = input ('Введите возраст: ')
# result = 'Привет, мое имя {}, мне {} лет' .format(name, age)
# print (result)

#3. f'строка' -> f'{}'

# name = input ('Введите свое имя: ')
# age = 25
# result = f'Привет, мое имя {name}, мне {age} лет'
# print (result)

'''Экранирование строк'''

# print ('Hello world my name is Anton') # написание в одну строку

# print ('Hello world') 
# print ('my name is Anton') # написание в 2 строки / ручной перенос

'''
\n - перенос строки
\t - горизонтальная табуляция
\v - вертикальная табуляция
'''

# print ('Hello world\nmy name is Anton\nI\'m Sabina\'s mom') # перенос строки с помощью \n

# print ('Hello world\tmy name is Gustavo') # \t заменяет tab

# print('Hello world\vSup') # \v = \n + \t только начинает с конца слова верхней строки


# '''Измерение длины строки'''

# name = 'John Snow'
# print(len(name)) # длина строки
# print(name[0:len(name)//2]) # John

'''==================Методы строк================'''

# print(dir(str)) # список методов

'REPLACE'
# str.replace (старое значение, новое значение, количество) - это метод строк, который меняет старое значение строк на новое, если указать количество, то поменяет столько сколько раз мы указали кол-во

# text = 'ha ha ha ha'
# result = text.replace('a', 'o', 2) #ho ho ha ha
# print (result)

'STRIP'
#str.strip() - метод строк, который убирает пробелы вначале и в конце строки

# text = '   hello world   '
# result = str.strip(text) 
# print (text)
# print (result) # hello world - удаляются пробелы вначале и в конце
# print(len(text)) #17 символов
# print(len(result)) #11 символов

# str.rstrip() - удаление пробела справа (в конце)
# text = '    hello world               '
# result = text.rstrip ()
# print (result) #'    hello world'
# print(len(result)) #15 символов

# str.lstrip() - удаление пробела слева (в начале)
# text = '    hello world               '
# result = text.lstrip ()
# print (result) #'hello world               '
# print(len(result)) #26 символов

'ISDIGIT, ISNUMERIC, ISDECIMAL'

# str.isdigit() 
# str.isnumeric() - эти методы проверяют состоит ли наша строка полностью из чисел
# str.isdecimal() 

# text = '24'
# print (text.isdigit()) #true
# print (text.isnumeric()) #true
# print (text.isdecimal()) #true

# age = input ('Введите свой возраст: ')
# print(age.isdigit())

'ISALPHA'

# str.isalpha() -  это метод строк, который проверяет, состоит ли наша строка только из латиницы или кириллицы, пробел тоже считает за false (потому что не относится к кириллице или латинице)

# text = 'приветмир'
# print(text.isalpha())

'ISALNUM'

# str.isalnum() - это метод, который проверяет на то, что состоит ли наша строка полностью из чисел и символов латиницы или кириллицы

# text = 'lfl3j33foff30fwl$kfnslkfj'
# print (text.isalnum()) # false - потому что есть символ $

# text = 'lfl3j33foff30fwlkfnslkfj'
# print (text.isalnum()) # true - потому что только латинские символы и цифры

'ISLOWER, ISUPPER'

# str.islower - метод строк, который проверяет на нижний регистр
# str.isupper - метод строк, который проверяет на верхний регистр

# text = 'makers'
# print(text.islower()) #true
# print(text.isupper()) #false

# text2 = 'MaKers'
# print(text2.islower()) #false - потому что есть символы верхнего регистра
# print(text2.isupper()) #false - потому что есть символы нижнего регистра

'ISTITLE'

#str.istitle() - метод строк, который проверяет, начинается ли КАЖДОЕ слово в строке с большой буквы (вернхнего регистра) 

# name='sultan'
# name2='Sultan'
# print(name.istitle()) #false - тк с маленькой буквы
# print(name2.istitle()) #true - тк с большой буквы

# text = 'sultan Talaibekov'
# print(text.istitle()) #false - тк первое слово с маленькой буквы


'INDEX'
# str.index(values, start, end) - метод строк, который возвращает индекс заданного значения (values)

# text = 'makers bootcamp'
# print(text.index('a', 7)) #12 ищет в слове bootcamp

'COUNT'
# str.count (values, start) - метод строк, который считает кол-во символов/значений (values) есть в строке

# text = 'makers bootcamp'
# print(text.count('a', 7)) # 1 символ в строке начиная с 7 индекса

# text = 'codingiseasyiasdiasdiadsi'
# print(text.count('i')) #6 - всего таких символов в строке

# print(text.count('i', 5)) #5 - таких символов начиная с 5го индекса

# print(text.count('i', 5, 9)) #1 - таких символов с 5го по 9й индекс (невключительно)

'FIND'

# str.find(values, start, end) - метод строк такой же как и метод INDEX (см.выше), но он не выведет ошибку/исключение, если значения (values) нет в строке, он просто вернет индекс -1

# text = 'makers bootcamp'
# print(text.find('z')) #-1 - тк заданного элемента нет в строке

# text = 'makers bootcamp'
# print(text.index('z')) #not found 

'SWAPCASE'
# str.swapcase() - метод строк, который меняет на противоположный регистр (а->A, A->a, MaKers->mAkERS)

# text = 'Coding Is Easy'
# print(text.swapcase()) # cODING iS eASY

# text2 = 'codingiseasy'
# print(text2.swapcase()) # CODINGISEASY

# text3 = 'CODINGISEASY'
# print(text3.swapcase()) # codingiseasy

# text4 = input('Enter your text: ')
# print(text4.swapcase())

'CAPITALIZE'

# str.calitalize() - это метод строк, который меняет первую букву строки на верхний регистр, остальные на нижний

# text = 'hi my Name is Anton'
# print(text.capitalize()) # Hi my name is anton

'TITLE'

# str.title() - метод строк, который переводит начало каждого слова в строке в верхний регистр

# text = 'hello my name is Anton'
# print(text.title()) # Hello My Name Is Anton

'SPLIT'

# str.split(разделитель) - метод строк, который переводит строку в лист при помощи разделителя

# text = input ('Введите числа через запятую: ')
# print(text.split(','))

# text2 = 'hi my name is Elon Musk'
# print(text2.split()) # ['hi', 'my', 'name', 'is', 'Elon', 'Musk']

'JOIN'

# 'соединитель'.join(list) - это метод строк, который соединяет элементы листа

# list_ = ['12', '23', '54', '25']
# print(''.join(list_)) # 12235425
# print('*'.join(list_)) # 12*23*54*25
# print(' '.join(list_)) # 12 23 54 25

'''TASKS'''
'''
# string1 = "America"
# string2 = "Japan"
# print(string1[0]+string2[0]+string1[len(string1)//2]+string2[len(string2)//2]+string1[-1]+string2[-1])
'''




# psw = '1256790hj'
# print(psw.isalpha())



'''средний балл по предметам'''

# x, y, z = input('Введите свои баллы по математике, английскому и литературе через запятую: ')
# # y = int(input('Введите свои баллы по английскому: '))
# # z = int(input('Введите свои баллы по литературе: '))

# result = (x+y+z)/3

# if result > 69:
#   print (f'Вы допущены к экзаменам. Ваш средний балл составляет {result}')
# else:
#   print (f'Вы не допущены к экзамену. Ваш средний балл составляет {result}')



'''Камень, ножницы, бумага'''
# import random
# ver = 0
# while (ver == 0):
#         player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
#         if (player == 1 or player == 2 or player == 3):
#             ver = 1    
# if player == 1:
#         print("Вы выбрали камень.")  
# if player == 2:
#         print("Вы выбрали ножницы.") 
# if player == 3:
#         print("Вы выбрали бумагу.")  
# comp = random.randint(1, 3)
# if comp == 1:
#         print("Компьютер выбрал камень.") 
# if comp == 2:
#         print("Компьютер выбрал ножницы.")
# if comp == 3:
#         print("Компьютер выбрал бумагу.")
# # определяем победителя
# if player == comp:
#         win = 0
# if player == 1 and comp == 2:
#         win = 1 
# if player == 1 and comp == 3:
#         win = 2 
# if player == 2 and comp == 1:
#         win = 2  
# if player == 2 and comp == 3:
#         win = 1 
# if player == 3 and comp == 1:
#         win = 1
# if player == 3 and comp == 2:
#         win = 2
# if win == 0:
#         print("Ничья!")
# if win == 1:
#         print("Победил игрок!")
# if win == 2:
#         print("Победил компьютер!")

