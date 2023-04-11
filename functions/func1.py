#    найти квадрат, куб, результат деления на 100 
# num1 = 5 
# -> {
#     '2': 25, '3': 125, '100': 0.05, 'num': 5
# }

# num1 = 5
# print({'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1 / 100})
# num2 = 16
# print({'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 / 100})
# num3 = 28 
# print({'num': num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3 / 100})
# num4 = 1154
# print({'num': num4, '2': num4** 2, '3': num4 ** 3, '100': num4 / 100})
# num5 = 31
# print({'num': num5, '2': num5 ** 2, '3': num5 ** 3, '100': num5 / 100})

# DRY - Don't repeat yourself

# num1 = 5

# num2 = 16

# num3 = 28 

# num4 = 1154

# num5 = 31

# def operations(num):
#     print({'num': num, '2': num ** 2, '3': num **3, '100': num / 100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)

#--------------------------------------------------
# Функия - это именнованая часть программы, которая содержит в себе определенный набор инструкций, и может вызываться в др частях программы столько раз сколько угодно

# def name_of_func(<a, b> # параметры ):
#     <body> # код, какая-то догика которая будет давать конечный результат
#     #<return #  operator который помогает вернуть результат

# name_of_func(5, 6 #аргументы) 

# параметры функции - это переменные, которые будут принимать данные от пользователья и хранить в себе эти данные.

# аргументы функции - это данные, которые мы передаем в функции, в моменте вызова.

# ls = [1,2,3,4,5]
# str1 = 'Hello world s vami Kani i John Snow!'

# def our_len(obj):
#     i = 0 
#     print(obj)
#     for x in obj:
#         i  += 1
#         print(f'result: {i}')

# our_len(ls)
# our_len(str1)

# def isEven(obj):
#     if obj % 2 == 0:
#         return True
#     else:
#         return False
    
# print(isEven(5))


# words = ['Slava', 'Lol', 'kazak']
# def get_polindrom(words):
#     result = []
#     for word in words:
#         if word.lower() == word [::-1].lower():
#             result.append(word)
#     return result
    
# polindrom_words = get_polindrom(words)
# print(polindrom_words)

# def get_percenage(money, period):
#     if money < 30000:
#         raise ValueError('Вложить можно более 30000')
#     if period < 3:
#         raise ValueError('Период должен быть не менее 3 лет')
#     year = 0
#     while year < period:
#         money += money * 0.1
#         year += 1
#     return money

# try:
#     money = float(input('Vvedite Summu: '))
#     period = int(input('Vvedite period: '))
#     print(get_percenage(money, period))
# except ValueError:
#     print('Nepravil\'nyi Vvod')

# def test_func(a=1, b=4):
#     pass

# test_func()

# def range(first, last, step=1):
#     pass

# range(1, 4)


# def isEven(num: int) -> bool:
#     return True if num % 2 == 0 else False\
# print(isEven(5))

# max

# try: 
#     n  = int(input('Vvedite'))
# except ValueError: 
#     print('Invalid number! ')
# else:
#     DICT_ = [True: x ** 2 for x in range(1, 501) if x % n == 0]
# print(__dict__)
