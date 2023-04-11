# num1 = 1

# while num1 >= 0:
#     num1 = input('Vveditee chislo: ')
#     if num1[0] == '-' and num1[1:].isdigit():
#         num1 = int(num1)
#     else:
#         num1 = 1

# print('error')

#-------------------------------------------------------------------------- 
# from random import randint


# ls = []
# for x in range(0, 100):
#     ls.append(randint(0,100))

# ls.sort()
# print(ls, len(ls))

# res = []
# for x in ls: 
#     if x not in res:
#         res.append(x)

# print(res, len(res))

#---------------------------------------------------------------------------

# x1 = int(input('Vvedite 1 coordinatu: '))
# y1 = int(input('Vvedite 2 coordinatu: '))
# ladya = [x1, y1]


# x2 = int(input('Vvedite 1 coordinatu keda idet ladya: '))
# y2 = int(input('Vvedite 2 coordinatu kuda idet ladya: '))
# target = [x2, y2]

# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)

# ----------------------------------------------------------------------------------
# import random 

# ls = ['Plov', 'Besh-Barmak', 'Kurdak', 'Oromo', 'Lagman']
# p = 0 
# b = 0
# k = 0
# o = 0
# l = 0

# for x in range(0, 1_000):
#     meal = random.choice(ls)
    
#     if meal.lower() == 'Besh-barmak':
#         p += 1
#     elif meal.lower() == 'Kuurdak':
#         b += 1
#     elif meal.lower() == 'Oromo':
#         k += 1
#     elif meal.lower() == 'Plov':
#         o += 1
#     else:
#         l +=1

# print('Результат: ')
# print(f'')

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# 1) nums = [2, 7, 11, 15]
# target = 9
# 0, 1 ------------ 2 + 7 = 9

# 2) nums = [4, 11, 2, 5, 1, 6]
# taget = 8
# 2, 5 ------------------ 2 + 6 = 8
 
# nums = [4, 11, 2, 5, 1, 6]  
# target = 8

# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num != nums[i]:
#             print(f'Otvet: {i}, {nums.index(num)}')
#             break

# decorators
# Scope
# Built in func.

# Decorators - функция высшего порядка(функ. которая принимает др функцию в качестве аргумента)

# def decorator(func):
#     def wrapper():
#         print(f'this function named {func.__name__}')
#         return func()
#     return wrapper
# n = 5
# @decorator
# def hello():
#     print('Hello')

# hello()

# def sq(func):
#     def wrapper(num):
#         nums = func(num)
#         return list(map(lambda x: x ** 2, nums))
#     return wrapper

# @sq
# def func(num: int):
#     return list(range(1, num))

# @sq
# def func2(num):
#     return list(range(1, num, 2))

# print(func(5))
# print(func(6))


