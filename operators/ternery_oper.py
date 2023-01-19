#sentens = input("Vvedite predlojenye: ")
#if sentens [-1]=-*7*  
#print ('vopros1telnoe predlojeniy'")
#else:
#print ('ne voprositelnoe")
#print('Voprositel\'noe predlojeniye!' if sentens[-1] == "?" else 'Normal one!')

#print('Voprositel\'noe predlojeniye!' if sentens[-2:] == "?!" else 'Normal one!')

#---------------------------------------------------------

# #Ternary operators (тернарыный условный оператор) - это конструкция, аналогичная if/else по своему действию, но при этом записывается в одну строчку
# number = 18
# result = 'even number' if number % 2 == 0 else 'odd number'
# print(result)
# # <выражение срабатывает если в условии True> if <условие> else <выражение если в условии> False

#---------------------------------------------------------

# num = int(input('Vvedite chislo: '))
# res = num - 100 if num < 100 else num * 2
# print(res)

#---------------------------------------------------------

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max/min: ')
# res = max(ls) if choice.lower().strip() == 'max'else min(ls)
# print(res)
# index = ls.index(res)
# ls[index] = min(ls)

#---------------------------------------------------------

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max/min: ')
# if choice.lower().strip() == 'max':
#     res = max(ls)
#     print(res)
#     num_index = ls.index(res)
#     ls[num_index] = min(ls)
#     print(ls)
# elif choice.lower().strip() == 'min':
#     res = min(ls)
#     print(res)
#     num_index = ls.index(res)
#     ls[num_index] = max(ls)
#     print(ls)
# else:
#     res = 'Invalid choise'
# print(res)

#---------------------------------------------------------

'''ТЕРНАРНЫЙ УСЛОВНЫЙ ОПЕРАТОР НУЖЕН ТОЛЬКО ДЛЯ ПРОСТЫХ ЗАДАЧ (ПОИСК МАХ/МИН), НО ДЛЯ ПРИСВОЕНИЯ ДАННЫХ  И ДРУГИХ СЛОЖНЫХ КОНСТРУКЦИЙ НУЖНО ИСПОЛЬЗОВАТЬ СТАНДАРТНЫЙ УСЛОВНЫЙ ОПЕРАТОР'''

#---------------------------------------------------------

'''Calculator'''

# from string import digits

# symbols = digits + '-' + '.'
# flag = True

# while flag:
#     is_correct_number = True
#     num1 = input('Введите первое число: ')
#     for x in num1:
#         if not x in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num2 = input('Введите второе число: ')
#     for x in num2:
#         if not x in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)

#     operator = input('Введите операцию (+,-,*,/): ')
#     if operator == '+':
#         print(f'Результат: {num1+num2}')
#     elif operator == '-':
#         print(f'Результат: {num1-num2}')
#     elif operator == '*':
#         print(f'Результат: {num1*num2}')
#     elif operator == '/':
#         print(f'Результат: {num1/num2}')
#     else:
#         print('Вы ввели неправильную операцию!')

#     choice = input('Хотите продолжить (yes/no)?')
#     if choice.lower().strip() == 'no':
#         flag = False
#         print('Пока')

#---------------------------------------------------------


'''крестики/нолики'''

