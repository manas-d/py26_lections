'''
Магические методы (dunder - duble underscore)- методы, у которых два нихних подчеркивания в начале и в конце. Магия в том, что мы их не вызываем напрямую, а они вызываются в оперделенный момент либо они вызываются оперделенными операторами или функициями.
'''

# res = 5 + 5 #__add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))


'''Магические методы, которые срабатывают при помоши оператора :'''

# eq(self, other)-> ==  : 5 == 7 seelf: 5 other: 7
# ne(self, other)-> !=
# lt(self, other)->  < ;  le -> <=
#__gt__(self, other) ->  > ;  ge ->  >=


# sub ->(self, other)  div -> /
# mul -> *  mod ->  %
# floordiv -> // add -> +
#__pow__ -> **

#=======================================

# class MyClass:
#     def __init__(self, string):
#         self.string = string


#     def __add__(self, other):
#         print('add сработал')
#         print(self, '!!!')
#         print(other, '****')
#         res = self.string+other.string
#         return MyClass(res)

#     def __str__(self) -> str:
#         return self.string


# obj1 = MyClass('John')
# obj2 = MyClass('Jamie')
# obj3 = MyClass('Lanister')
# res = obj1 + obj2 + obj3
# print(res)
# print(res.string)

#=======================================

# class Word(str):
#     def __new__(cls, word):
#         word = word.replace(' ', '')
#         return super().__new__(cls, word)

#     def __init__(self, word) -> None:
#         self.word = word

#     def __gt__(self, other:str) -> bool:
#         print('gt сработал')
#         print(self, "!!!!")
#         print(other, '****')
#         return len(self) > len(other)
    
# obj1 = Word('John           ')
# obj2 = Word('Hello World')
# print(obj1 > obj2)

"""
Конструктор -> __new__(cls)
Инициализатор -> __init__(self)
Вызываются, когда создаем объект
"""

# class Converter(float):
#     def __new__(cls, __x):
#         print('new сработал')
#         print(cls, '!!!')
#         print(__x, 'xxxx')
#         if __x<50:
#             raise ValueError('x меньше 50!')
#         return super().__new__(cls, __x)

#     def __init__(self, x) -> None:
#         print('init сработал')
#         print(self, '?????')
#         self.numer = x

# obj1 = Converter(65)
# print(obj1)

'''
Дандер методы строкового отображения объектов 
__str__ -> для отображения строки которую будут видеть пользователи
__repr__ -> строковую информацию о том, как создать объект
__len__ --> len(obj)
__repr__ --> repr(obj)
'''
'''eval('6+6') -> 6+6'''

# class Base:
#     def __init__(self, string) ->None:
#         self.string = string

#     def __str__ (self) -> str:
#         return f'Объект: {self.string}'
    
#     def __repr__(self) -> str:
#         return f'Base("string")'
    
#     def __len__(self):
#         return 5
    
# user = Base('Hello John')
# print(user)
# print(repr(user)) 
# obj1 = eval(repr(user)) #Base("string")
#             # Base("string")
# obj1 = Base('string')
# print(obj1)

#=======================================

# class Person:
#     def __init__(self, attrs:dict) -> None:
#         # self.name = attrs['name']
#         # self.a = 5 == setattr(self, 'a', 5)
#         for key, value in attrs.items():
#             setattr(self, key, value)
    

# alice = Person({'name':'Alice Rose', 'income':100000, 'eyes':'brown'})
# john = Person({'email':'JohnSnow@gmail.com', 'last_name':'Snow'})
# print(f'{alice.name} -- {alice.income} -- {alice.eyes}')
# print(f'{john.email} -- {john.last_name}')

#=======================================

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls
        
#     def __getitem__(self, index):
#         print(self.ls[index-1])

# x = MyList(['123', 'hello',2,4,5])
# x[1]
# x[2]
# x[3]

#=======================================

"""__iter__ - вызывается, когда итерируем объект"""

class A:
    def __iter__(self):
        for i in range (1,10):
            print('Iter method')
            yield i

x = A()
for i in x:
    print(i)