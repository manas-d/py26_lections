# Анотация свойств (@property(getter setter))


# class Person:
#     __name = 'John'
#     __age = 22
#     __code = '+996'
#     __number = '555666777'
#     __full_number = __code + __number

#     @property
#     def name(self):
#         '''The name property'''
#         print(self.__name)
#         # return self.__name

#     @name.setter
#     def name(self, value):
#         print('Setter')
#         if not isinstance(value, str):
#             print('Invalid value!!!')
#             return
#         self.__name = value

#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or not 0<value<170:
#             print('Ivalid value')
#             return
#         self.__age = value

#     @property
#     def number(self):
#         name = input('Vvedite svoe imya: ')
#         if self.__name != name:
#             print('Invalid name!')
#             return
#         print(self.__full_number)

#     @number.setter
#     def number(self, value:list):
#         '''value must be list, first pair code and second number!'''
#         if value['code'] != '+996':
#             print('must be Kyrgyzstan number!')
#         elif len(value['number']) != 9:
#             print("Invalid number") 
#         self.__code = value['code']
#         self.__number = value['number']
#         self.__full_number = self.__code + self.__number

# obj = Person()
# obj.name
# obj.name = 'Raychel'
# obj.name 
# obj.age 
# obj.number
# obj.number = {'code':'+55', 'number':'777777777'}
# obj.number
# obj.number = {'code':'+996', 'number':'700123456'}
# obj.number

'''================================================================='''

class Circle:
    def __init__(self, radius) -> None:
        self.__radius = radius

    @property
    def radius (self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise Exception('Invalid value. Must be an int or float object')
        self.__radius = value

circle = Circle(42)
print(circle.radius)
circle.radius = 15
print(circle.radius)
