'''
    ИНКАПСУЛЯЦИЯ:
1.  Связь данных с методами, которые должны управлять этими атрибутами.
2.  Механизм языка, который позволяет ограничить доступ к определенным компонентам класса.
3.  Один класс - одна задача.
'''

'''Инкапсуляция как связь'''

# class Phone:
#     number = '+996700700700'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')

# my_phone = Phone()
# print(my_phone.number)
# my_phone.print_number() # Мой номер: +996700700700

'''Инкапсуляция как управление доступом
3 уровня доступа в питоне:
    1. Публичный (public) - number, print_number
    2. Защищенный (_protected, parent/child) - _number, наследуется только на 1 класс
    3. Приватный (__private) - доступен только в текущем классе, не наследуется
'''

# class Car:
#     _country = 'Germany'

#     def __init__(self):
#         self.marka = 'Mercedes Benz' #public
#         self._model = 'W140' #protected
#         self.__motor = 'ABC' #private

# obj = Car()
# print(obj.marka)
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)

'========================================================='

# class Phone:
#     username = 'John Snow'
#     _caller = 'Jamie Lanister'
#     __count_of_calls = 15

#     def call(self):
#         print(f'{self._caller} звонит!')

#     def __increment_of_calls(self):
#         self.__count_of_calls += 1

#     def turn_on(self):
#         print(f'{self.username} взял трубку!')
#         self.__increment_of_calls()

#     def get_count(self):
#         print(self.__count_of_calls)

# obj = Phone()
# obj.get_count() #15
# obj.call() #Jamie Lanister звонит!
# obj.turn_on() #John Snow взял трубку!
# obj.get_count() #16

'========================================================='

'''GETTER & SETTER
Они используются для получения и установки значений в защищенные атрибуты, чтобы избежать прямого доступа к защищенному атрибуту, и еще с помощью сеттеров и гетторов можно добавлять логику проверки при получении данных
'''

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.age = 0

#     def display_info(self):
#         print(f'My name is {self.name}, I\'m {self.age} years old!')

# john = Person('John')
# john.display_info() #My name is John, I'm 0 years old!
# john.name = None
# john.age = -18
# john.display_info() #My name is None, I'm -18 years old!

'''==='''

# class Person:
#     def __init__(self, name) -> None:
#         self.__name = name
#         self.__age = 0

#     def display_info(self):
#         print(f'My name is {self.__name}, I\'m {self.__age} years old!')

#     #getter
#     def get_name(self): return self.__name

#     #setter
#     def set_name(self, name): 
#         if not isinstance(name, str):
#             print('Invalid value for name!')
#         else:
#             self.__name = name

#     #getter
#     def get_age(self): return self.__age

#     #setter
#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print('Invalid value for age!')
#         else:
#             self.__age = age

# john = Person('John')
# john.display_info() #My name is John, I'm 0 years old!
# john.set_name(None) #Invalid value for name!
# john.set_age(-18) #Invalid value for age!
# john.display_info() #My name is John, I'm 0 years old!

# john.set_name('Jamie')
# john.set_age(24)
# john.display_info() #My name is Jamie, I'm 24 years old!

'========================================================='

# class Russia():
#     __name = 'Russian Federation'
#     __population = 0

#     def get_population(self): return self.__population

#     def set_population(self, num): 
#         if not isinstance(num, int) or num < 0:
#             print('Invalid value for population!')
#         else:
#             self.__population = num
    
#     def get_name(self): return self.__name

#     def display_info(self):
#         print(f'Population of {self.get_name()}: {self.get_population()}')

# obj = Russia()
# obj.set_population(143_000_000)
# obj.display_info()
# obj.__name

'========================================================='

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.__age = 0

#     def _age_increment(self):
#         self.__age += 1

#     def birthday(self):
#         print(f'Today is {self.name}s birthday!!!')
#         self._age_increment()

#     def display_info(self):
#         print(self.name, self.__age)

# obj = Person('John')
# obj.display_info()
# obj.birthday()
# obj.display_info()

'========================================================='

# def func():
#     print('helloworld')
#     return func
# func()()()()()