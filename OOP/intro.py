"""ООП-ОБЪЕКТНО-ОРЕНТИРОВАНИЕ ПРОГРАМИРОВАНИЕ"""

# Класс -> Это описание того, как должен выгллядить обхъект, то есть в классе мы описываем какими свойствами (даныыми) и поведением(функциями)должен обладеть объект

# Объект -> это сушность которую мы создаем от класса , у объекта есть состояние свойства(данных)

# Целью создание былло связать данные(атрибуты) с функцими(методы)котроые использовали их

# Свойствами (аттрибуты) называют обычные переменные внутри класса, в которых хрянятся данные определенного объекта

# Методы - это обычные функции которые описывают поведение объекта функции внутрии класса назвыают методами

#----------------------------------------------------

# john = ['John', 'snow', 'King of North', 5000, 30]

# def show_info (human):
#     print(f'Name: {human[0]} {human[1]}, Age: {human[-1]}, Job: {human[2]}, Salary: {human[3]}')

# # show_info(john)

# class Human:
#     def __init__ (self, name, last_name, age, job, salary):
#         self.name = name + ' ' + last_name
#         self.age = age
#         self.job = job
#         self.salary = salary

#     def show_info(self):
#         return f'Name: {self.name}, Age:{self.age}, Job:{self.job}, Salary:{self.salary}'

# john = Human('John', 'Snow', 30, 'King of North', 5000)
# sultan = Human('Sultan', 'Katana', 19, 'Mentor', 1000)

# # print(dir(john))
# print(john.show_info())
# print(john.name)
# print(john.age)
# print('----------')
# print(sultan.show_info())
# print(sultan.name)

'''----------------------------------------------------------'''

# class Dog:
#     #атрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name, color):
#         '''Инициализатор, именно здесь создаются атрибуты объекта'''
#         '''в self прилетает ссылка на объект от класса'''
#         self.name = name #атрибуты объекта
#         self.color = color

#     def bark (self):
#         print(f'{self.name} лает!')

# bobik = Dog('Bobik', 'brown')
# yumi = Dog(name='Yumi', color='white')
# aktosh = Dog('Aktosh', 'gray')

# print(f'Name: {bobik.name}, Age: {bobik.age}, Color: {bobik.color}, Ushi: {bobik.ushi}')
# print(f'Name: {yumi.name}, Age: {yumi.age}, Color: {yumi.color}, Ushi: {yumi.ushi}')
# print(f'Name: {aktosh.name}, Age: {aktosh.age}, Color: {aktosh.color}, Ushi: {aktosh.ushi}')

# bobik.age = 2
# yumi.age = 1
# aktosh.age = 3
# aktosh.ushi = False

# print('After')

# print(f'Name: {bobik.name}, Age: {bobik.age}, Color: {bobik.color}, Ushi: {bobik.ushi}')
# print(f'Name: {yumi.name}, Age: {yumi.age}, Color: {yumi.color}, Ushi: {yumi.ushi}')
# print(f'Name: {aktosh.name}, Age: {aktosh.age}, Color: {aktosh.color}, Ushi: {aktosh.ushi}')

# yumi.bark()

'''----------------------------------------------------------'''

# class Human:
#     age = 0

#     def __init__(self) -> None:
#         print('init worked')
#         self.golod = 100
#         self.raychel = 'raychel'
    
#     def eat(self, meal, doel=True):
#         if doel:
#             self.golod -= 50
#         else: 
#             self.golod -= 25

# obj = Human()
# print(obj.golod)
# obj.eat('burger', doel=False)
# print(obj.golod)