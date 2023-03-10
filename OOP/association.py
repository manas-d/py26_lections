'''
АССОЦИАЦИЯ - означает, что внутри одного объекта будет существовать второй объект в качестве атрибута.
Делится на 2 вида: агрегация (слабая связь) и композиция (сильная связь).
'''

'''1. Композиция (сильная связь) - это когда стена не существует одтельно от комнаты, она создается при создании комнаты и полностью управляется классом Комнаты.
Сравнение со стенами в комнате, не могут существовать друг без друга.'''

# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type} wall!'
    
#     def info(self):
#         print('White wall')
    
# class Room:
#     def __init__(self) -> None:
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')

# room = Room()
# print(room.west_wall) #west wall!
# print(room.north_wall) #north wall!
# print(room.north_wall.type) #north
# room.north_wall.info()

'''2. Агрегация (слабая связь) - это когда экземпляр двигателя создается где-то в другом месте и передается в класс Автомобиля в качестве параметра.
Сравнение с двигателем и кузовом авто, они могут существовать порознь и использоваться с другими составляющими.'''

# class Engine:
#     country = 'Germany'
#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f'Engine: {self.power}'
    
# class Car:
#     model = 'Audi'
#     country = 'Germany'

#     def __init__(self, type, engine) -> None:
#         self.type = type
#         self.engine = engine

#     def __str__(self) -> str:
#         return f'{self.model} {self.type} -> {self.engine} {self.engine.country}'
    
# engine = Engine(500)
# car = Car('A8', engine)
# print(car)

'''==============================================================================================='''

# class Battery:
#     _power = 100

#     def power(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         # когда мы создаем объект внутри - это композиция

# class Nokia:
#     def __init__(self, color: str, battery: Battery) -> None:
#         self.color = color
#         self.battery = battery
#         # когда мы принимаем объект в качестве параметра - это агрегация

# iphone = Iphone('Gray')
# del iphone
# # при удалении iphone вместе с ним удаляется и battery

# battery = Battery()
# nokia = Nokia('Black', battery)
# del nokia
# # при удалении nokia, battery остается - то есть могут существовать по отдельности
# nokia2 = Nokia('White', battery)

