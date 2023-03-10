# Множественные наследование - это когда класс наследование от двух или более классов




# class Auto:
#     def play_music_at_station(self):
#         print('Music ids playing!')


#     def ride(self):
#         print('We\'re riding on the ground!')


# class Plane:
#     def play_music_at_station(self):
#         print('Listining Ed Sheren!')


#     def fly(self):
#             print('We\'re flaying')



# class FutureAuto(Auto, Plane):
#     pass



# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()



# class A:
#     def print_A(self):
#         print('A')


# class B:
#     def print_B(self):
#         print('B')


# class C:
#     def print_C(self):
#         print('C')

# class MyClass(A,B,C):
#     pass


# obj = MyClass()
# obj.print_A()
# obj.print_B()
# obj.print_C()
# print(MyClass.mro())



# class Test:
#     pass

# a = Test()
# print(dir(a))
# print(dir(a))

# Проблема ромба(решена с помошью mro)
'''Mro (Method Resolution Order) - механизм для коректного поиска родительских методов. Был создан для решение проблемы робма, котороя  появилось после введение класса  object  в пайтон. Поиск идет таким образом что если у родитнельских классов один общий предок , то идет поиск в ширину.'''

# class Zero:
#     def say(self):
#         print('class Zero!')


# class First(Zero):
#     # def say(self):
#     #     print('class First')
#     ...

# class Second(Zero):
#     ...
#     # def say(self):
#     #     print('class Second')


# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('My CLass')


# obj = MyClass()
# obj.say()
# print(MyClass.mro())


# проблема перекрестного наследование 

# class Y:
#     pass

# class X:
#     pass
# class A(X,Y):
#     pass
# class B(X, Y):
#     pass
# class MyMro(type):
#     def mro(cls) -> list[type]:
#         return [cls, A, B, X, Y, object]

# class MyClass(A,B, metalass=MyMro):
#     pass

# obj = MyClass()
# print(MyClass.mro())



# class  RadioMixin:
#     def play_music(self):
#         title_py = 'title'
#         print( "Песня называется {title_py}")

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class  Amphibian(Auto,Boat):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# obj.play_music()

# import datetime
# class Clock:
#     def current_time(self):
#         print('14:10:41')

# class Alarm:
#     def on(self):
#         print('')

#     def off(self):
#         print('09:00:00')

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         print('Будильник включён')

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

# import datetime
# class Clock:
#     def current_time(self):
#         dt_now = datetime.datetime.today().strftime("%H:%M:%S")
#         print(dt_now)

# class Alarm:

#     @staticmethod
#     def on():
#         print('Будильник включен')

#     @staticmethod
#     def off():
#         print('Будильник выключен')

# class AlarmClock(Clock, Alarm):
#     @staticmethod
#     def alarm_on():
#         Alarm.on()

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()


import abc 

class Coder():
    count_code_time = 0
    @abc.abstractmethod
    def get_info(self):
        pass
    @abs.abstractmethod
    def coding(self):
        pass

class Backend(Coder):
    def init(self, experience, languages_backend):
        self.experience = experience
        self.languages_backend = languages_backend
        get_info = get_info(self)
        coding = coding(self)
        print(f'Python разработчик, уровень: Junior, потрачено {self.count_code_time} часов на программирование')