'''ПРИНЦИПЫ ООП:

1. Наследование
2. Инкапсуляции
3. Полиморфизм

4. Абстракция
5. Композиции
6. Агрегация
'''
#----------------------------------------------------------
"""
Наследование в ООП позволяет принимать родительские методы и атрибуты для дочернего класса.

Родительский класс
Дочерний класс 
"""

# class Animal:
#     def print_info(self):
#         print('I\'m an animal')

# class Croco(Animal): # в скобках указываем родительский класс
#     pass

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# croco = Croco()
# croco.print_info()

#----------------------------------------------------------

# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f'This animal is {self.name}: {self.golos}')

#     def eat(self):
#         print(f'This animal is {self.name}: {self.meal}')

# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meal = 'meat'
#     griva = True

#     def say(self):
#         print(f'King of Animals The {self.name}')

#     def info(self):
#         print(f'{self.name} griva: {self.griva}')

# class Dog(Animal):
#     name = 'dog'
#     golos = 'bark'
#     meal = 'meat'

# class Koala(Animal):
#     name = 'koala'
#     golos = 'roar'
#     meal = 'efkalipt'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say() #This animal is dog: bark
# rex.eat() #This animal is dog: meat

# simba.say() #This animal is lion: roar
# simba.eat() #This animal is lion: meat
# simba.info() #lion griva: True

# julian.say() #This animal is koala: roar
# julian.eat() #This animal is koala: efkalipt

#----------------------------------------------------------

# class Person:
#     def info(self):
#         print('I\'m person from Bishkek!')

# class Student(Person):
#     def info(self):
#         super().info()
#         print('I\'m studying at Manas University!')

# obj = Student()
# obj.info() #I'm person from Bishkek! I'm studying at Manas University!

# obj2 = Person()
# obj2.info() #I'm person from Bishkek!

#----------------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def get_info(self):
#         return {'brand':self.brand, 'model':self.model, 'price':self.price}
    
# class MacBook(Laptop):
#     def __init__(self, brand, model, price, year, display):
#         super().__init__(brand, model, price)
#         self.year = year
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['display'] = self.display
#         return repr
    
# class Aser(Laptop):
#     def __init__(self, brand, model, price, videocard, display):
#         super().__init__(brand, model, price)
#         self.videocard = videocard
#         self.display = display
    
#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] = self.videocard
#         repr['display'] = self.display
#         return repr

# mac = MacBook('Apple', 'Air', 1000, 2022, 13)
# print(mac.get_info()) #{'brand': 'Apple', 'model': 'Air', 'price': 1000, 'year': 2022, 'display': 13}

# aser = Aser('Aser', 'Swift', 600, 'Gforce 3040', 'XRGB 14')
# print(aser.get_info()) #{'brand': 'Aser', 'model': 'Swift', 'price': 600, 'videocard': 'Gforce 3040', 'display': 'XRGB 14'}

#----------------------------------------------------------

class Employee:
    bonus = 1.5

    def __init__(self, first_name, last_name, salary) -> None:
        self.name = f'{first_name} {last_name}'
        self.salary = salary

    def get_info(self):
        return f'Name: {self.name}, salary: {self.salary}'
    
    def give_increase(self):
        self.salary = self.salary * self.bonus

    def __str__(self) -> str:
        return self.get_info()
    

class Developer(Employee):
    def __init__(self, first_name, last_name, salary, language) -> None:
        super().__init__(first_name, last_name, salary)
        self.prog_lang = language

    def get_info(self):
        info = super().get_info()
        info += f', Prog Language: {self.prog_lang}'
        return info
    

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, devs=[]):
        super().__init__(first_name, last_name, salary)
        self.devs = devs
    
    def add_devs(self, developer):
        self.devs.append(developer)

    def show_devs(self):
        return [x.get_info() for x in self.devs]


dev1 = Developer('John', 'Snow', 1500, 'Python')
dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
dev3 = Developer('Larry', 'Page', 1500, 'JS')
dev4 = Developer('Tirion', 'Lanister', 1000, 'Python')

man1 = Manager('Jaime', 'Lanister', 2000)
man2 = Manager('Dastan', 'Katana', 4000, [dev3, dev2])

print(f'Manager {man1.get_info()} has {man1.show_devs()} developers!')
print(f'Manager {man2.get_info()} has {man2.show_devs()} developers!')

man1.add_devs(dev1)
man1.add_devs(dev4)
man2.add_devs(dev1)

print('\nAfter:')
print(f'Manager {man1.get_info()} has {man1.show_devs()} developers!')
print(f'Manager {man2.get_info()} has {man2.show_devs()} developers!')

dev1.give_increase()
man2.give_increase()

print(dev1)
print(man2)

