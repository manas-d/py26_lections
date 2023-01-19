# def sum_of_args(a, b, c, d): #parametres
#     return a + b + c + d

# result = sum_of_args(5, 10, 25, 20)
# print(result)


'''-------------------------------------------'''

# позиционные и именованные аргументы

# def printParams (a=None,b=None,c=None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams (a=5,c=15)

'''-------------------------------------------'''

# def sum_of_args(a, b, c, d): #parametres
#     return a + b + c + d

# print(sum_of_args(5,10,15,20)) #arguments (позиционные аргументы) #50
# print(sum_of_args(a=5,c=15,d=20,b=10)) #keyword arguments (именованные аргументы) #50
# print(sum_of_args(5,10,d=20,c=15))  #50

'''-------------------------------------------'''

# оператор * (распаковка элемента)
# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)

'''-------------------------------------------'''

''' *args **kwargs в функциях '''

# def printScores (student, *scores):
#     print(f'Student name: {student}')
#     # print(scores)
#     # print(type(scores))
#     # ls = list(scores)
#     for x in scores:
#         print('Score: ', x)

# printScores('John Snow', 100, 99, 95, 90)

'''-------------------------------------------'''

# def print_pet_names(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')


# print_pet_names('John Snow', dog = 'Rex', cat = 'Garfild', fish = ['Nemo', 'Dori', 'Alex'], turtle = 'Leonardo')

'''-------------------------------------------'''

# def get_some_data (a,b, *args, **kwargs):
#     print('Parametres a and b: ', a, b)
#     print('Arguments: ', args)
#     print('Named arguments: ', kwargs)

# get_some_data(1,2,3,4,5, lang = 'python', name = 'john snow', car = 'bmw m8')
# Parametres a and b:  1 2
# Arguments:  (3, 4, 5)
# Named arguments:  {'lang': 'python', 'name': 'john snow', 'car': 'bmw m8'}

'''---'''

# def get_some_data (a,b, *args, **kwargs):
#     print('Parametres a and b: ', a, b)
#     print('Arguments: ', args)
#     print('Named arguments: ', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])

# get_some_data(1,2,3,4,5, lang = 'python', name = 'john snow', car = 'bmw m8')

'''-------------------------------------------'''

# def generate_random_string (len_):
#     import string as s
#     import random
#     random_str = ''.join(
#         random.choice(s.ascii_letters + s.digits) for i in range(0, len_)
#         )
#     return random_str

# print(generate_random_string(15))

'''-------------------------------------------'''

'''CALCULATOR'''

# def add (a,b): return a+b

# def subtract (a,b): return a-b 

# def multyply (a,b): return a*b

# def divide (a,b): 
#     try: 
#         return a/b
#     except ZeroDivisionError:
#         return 'На 0 делить нельзя'

# def calc(num1, num2): 
#     operator = input('Введите опертор (+-*/): ')
#     if operator == '+': return add(num1, num2)
#     elif operator == '-': return subtract (num1, num2)
#     elif operator == '*': return multyply (num1, num2)
#     elif operator == '/': return divide (num1, num2)
#     esle: print('Вы ввели неверный оператор!')

# def main():
#     try:
#         num1 = float(input('Введите 1 число:'))
#         num2 = float(input('Введите 2 число:'))
#     except ValueError: 
#         print ('Вы ввели некорректные данные!')
#         main()
#         return
#     while True:
#         result = calc(num1, num2)
#         if type(result) == float:
#             print(f'Result: {result}')
#             break
#         else:
#             print(f'Result: {result}')
    
#     question = input('Do you want to continue?(Yes/No): ')
#     if question.lower() == 'yes': 
#         main()
#     else:
#         print('Thank you for using our Calculator! Bye!')

# main()

# '''-------------------------------------------'''

# '''Home Work'''

# if __name__ == '__main__':
#     main()




'''Functions. Таск 15'''

# users = [
# { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer'},
# { 'name': 'Helen', 'age': 35, 'work': 'Nurse'},
# { 'name': 'Bob', 'age': 35, 'work': 'Driver'},
# { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer'},
# { 'name': 'Helga', 'age': 35, 'work': 'IT-HR'}
# ]

# def func15(i):
#     for i in users: 
#         if i['work'].count('IT') > 0:
#             print(f"{i['name']}, скидки в магазине компьютерной техники!")
#     return 

# func15(users)

'''Functions. Таск 17'''


# def func17(list_):
#     res = []
#     for i in list_:
#         i['salary'] = i['salary'] + i['overTime']*200
#         i.popitem()
#     return list_    
# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# print(func17(employees))