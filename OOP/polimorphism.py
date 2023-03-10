'''
Функция полиморфизма - len()
'''

# print(len('makers')) #6
# print(len([1,2,3,4,5])) #5
# print(len({1:2, 3:4})) #2

'''
+ (__add__) - метод полиморфизма
'''

# print(5+5) #10
# print('hello'+'world') #helloworld
# print([1,2,3]+[4,5,6]) #[1, 2, 3, 4, 5, 6]

'''
ПОЛИМОРФИЗМ - способность метода обрабатывать данные разных типов (объектов от класса). Обычно это реализуется путем создания базового класса и наличия двух или более подклассов, которые все реализуют (переопределяют) методы с одинаковой сигнатурой (названием).
Широко распрастраненное определение: "Один интерфейс - много реализаций".
'''

# class Animal:
#     def info (self):
#         pass

#     def make_sound(self):
#         pass

# class Dog (Animal):
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a dog. Dogs name is {self.name}, age {self.age}')

#     def make_sound(self):
#         print('Bark bark')

# class Cat (Animal):
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age {self.age}')

#     def make_sound(self):
#         print('Meow meow')

# dog = Dog('Pluto', 9)
# cat = Cat('Garfild', 5)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()
#     print()

'''======================================================'''

# class A:
#     def __len__(self):
#         return 123

# a = A()
# str1 = 'Makers'
# print(len(str1))
# print(len(a))

'''========================================================================================'''

'''
АБСТРАКЦИЯ (Абстрактный класс) - его можно рассматривать как набор методов, которые должны быть реализованы во всех дочерних классах, которые будут унаследованы от абстрактного класса.

Абстрактный метод - это метод, у которого есть объявление, но нет реализации.
'''

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def info (self):
#         pass

# # a = Shape #() #Can't instantiate abstract class Shape with abstract methods area, info

# class Square(Shape):
#     def __init__(self, lenght)->None:
#         super().__init__('Квадрат')
#         self.lenght = lenght

#     def area (self):
#         return self.lenght ** 2

#     def info(self):
#         print(f'Я {self.name}, у меня все углы равны 90 градусам!')

# class Circle(Shape):
#     def __init__(self, radius)->None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area (self):
#         return self.radius **2 * pi

#     def info(self):
#         print(f'Я {self.name}, и я фигура в двумерной плоскости!')

# a = Square(4) 
# b = Circle(4)

# for x in (a,b):
#     x.info()
#     print(x.area())
#     print()

'''======================================================'''

# from abc import ABC, abstractmethod

# class ChessPiese(ABC):
#     # общий метод, который будут использовать все наследники этого класса
#     def take(self):
#         print('Take a chess piece!')

#     # Абстрактный метод, который необходимо переопределить для каждого наследника
#     @abstractmethod
#     def move(self):
#         pass

# class Queen(ChessPiese):
#     def move(self):
#         print('Queen moves where she wants diagonally, vertically and horizontally.')

# class Pawn(ChessPiese):
#     def move(self):
#         print('The pawn can move directly to one cell.')

# q = Queen()
# p = Pawn()
# q.move() #Queen moves where she wants diagonally, vertically and horizontally.
# q.take() #Take a chess piece!
# print()
# p.move() #The pawn can move directly to one cell.
# p.take() #Take a chess piece!

'''======================================================'''
'''ЗАДАЧА:
Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
разряжен).
Также предусмотрите возможность заряжания батареи.
'''

class Phone:
    def __init__(self, os, imei):
        self.__imei = imei
        self.__battery_level = 100
        self.__os = os

    @property
    def battery_level(self):
        if self.__battery_level < 0.5:
            self.__battery_level = 0
            raise Exception('Telefon razryazhen!')
        self.__battery_level -= 0.5
        print(self.__battery_level)
        
    @property
    def get_info(self):
        if self.__battery_level < 0.5:
            self.__battery_level = 0
            raise Exception('Telefon razryazhen!')
        self.__battery_level -= 0.5
        print(f'OS: {self.__os}, IMEI: {self.__imei}')

    def play_music(self):
        if self.__battery_level <= 5:
            self.__battery_level = 0
            raise Exception ('Telefon razryazhen!')
        self.__battery_level -= 5
        print('Slushaem Mirbeka Atabekova!')

    def play_video(self):
        if self.__battery_level <= 10:
            raise Exception ('Nedopustimyi uroven zaryada!')
        self.__battery_level -= 7
        print('Smotrim Toples!')

    def charge_battery(self, sec):
        from time import sleep
        i = 1
        while i <= sec:
            sleep(1)
            if self.__battery_level <100:
                self.__battery_level += 1
                if self.__battery_level > 100:
                    self.__battery_level = 100
            print(f'Zaryad idet! Vash uroven zaryada: {self.__battery_level}')
            i += 1

phone = Phone('IOS 15', '241325-113')
phone.battery_level
phone.get_info
phone.play_music()
phone.play_video()
phone.battery_level
phone.charge_battery(20)
phone.battery_level
