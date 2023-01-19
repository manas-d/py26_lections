#TUPLES
#tuple() - кортеж, неизменяемый тип данных

# thistuple = (5,)
# print(thistuple) #(5,)
# print(type(thistuple)) #<class 'tuple'>

# mytuple = 'apple', 'pineapple', 'pen'
# print(mytuple) #('apple', 'pineapple', 'pen')
# print(type(mytuple)) #<class 'tuple'>

# a, b, c = 5, 10, 15
# print(a)
# print(b)
# print(c)

# for x in range(1, 5):   #1) x = 1
#     print(x)            #2) x = 2

# dict1 = {1: 'one', 2: 'two', 3: 'three'}
# print(dict1.items())
# for x, y in dict1.items():
#     print(x, y)

# a = [(1, 2), (3, 4), (5, 6)]
# for x, y in a:
#     print(x, y)

# ls = list(range(1, 100_001))
# tp = list(range(1, 100_001))
# print(ls)
# print(len(ls))
# print("LIST", ls.__sizeof__())
# print("TUPLE", tp.__sizeof__())

# tuple_ = (1,2,3,4,5)
# del tuple_[-1]
# print(tuple_)

# ls = [1,2,3,4,5]
# del(ls[-1])
# print(ls)

# print(dir(tuple))

# tuple_ = (1,2,3,4,5,56,7,8,2,2,2,2,2)
# print(tuple_.index(5))
# print(tuple_.count(2))

# tp = ('apple', 'cherry', 'banana', 'john')
# for x in tp:
#     print(x)
#     print(x*3)

# i= 0
# while i < 50:
#     print(i)
#     i += 1  #инкремент i = i + 1
            #Дикремент i -= i

# tp = ('apple', 'cherry', 'banana', 'john')
# x = 0
# while x < len(tp):
#     print(tp[x], f'index: {x}')
#     x += 1

# +*
# a = (1,2,3)
# b = (4,5,6)
# print(a*5)
# print('123'*5)

# c = (5,)
# a = ()
# # c + = c
# # print(c)
# for x in range(1, 101):
#     a += c

# print(a)

#TASK #1

# 1) input:
# tp = (1, 8, 3, 4, 5, 8, 8, 9, 2)
# target = 8
# output/result: result = (8, 3, 4, 5, 8)

# 2) input:
# tp = (1,2,3,8,5,1,2)
# target = 8
# # output/result: result = (8,5,1,2)


# first = tp.index(8)
# print(first) #1
# print(tp[first+1:].index(8) +first+1) #5
# print(tp.index(8, first +1)) #5

#РЕШЕНИЕ

# if tp.count(target) > 1:
#     first = tp.index(target)
#     second = tp.index(target, first +1)
#     result = tp[first: second+1]
# else:
#     first = tp.index(target)
#     result = tp[first:]

# print(tp, target)
# print(result)

# TASK #2

# ) Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#1
# nums = [2,7,11,15]
# target = 9
# result = [0, 1] ----- 2+7=9
                        # 9 - 2 = 7
                        # 9 - 7 = 2

#2
# nums = [4, 11, 2, 5, 1, 6]
# target = 8
# result = 2 5

#РЕШЕНИЕ

# for x in nums:
#     num = target - x
#     if num in nums:
#         if num == x:
#             continue
#         print(nums.index(x), nums.index(num)) #0 1
#         break

