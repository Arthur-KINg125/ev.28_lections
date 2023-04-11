# labels = ['Toyota', 'Porsche']
# for x in labels:
#     print(f'i like brand', x)

# dict1 = {'x':'1', 'y':'2', 'z':'3'}
# a = dict1.get('x')
# print(a)

# name_of_list = ('Helloworld!') # не решено
# len(name_of_list)
# print(name_of_list)

# list_ = ('string', 'integer')
# # new_list = list_[1, 0]
# new_list = [list_[1], list_[0]]
# print(new_list)

# x = float(input('Vvedite chislo: '))
# y = float(input('vvedite chislo: '))
# if x % y == 0:
#     print(x % y)
# elif x % y != 0:
#     print(x % y, x//y)

# x = int(input('Vvedite chislo: '))
# y = int(input('vvedite chislo: '))
# if x % y == 0:
#     print('x делится на y')
#     print(f'Частное: {x//y} ')
# elif x % y != 0:
#     print('x не делится на y')
#     print(f'Частное: {x//y} ')
#     print(f'Остаток: {x % y}')


# decimal = float(10.5)
# print(decimal ** 2)
# print(decimal ** 3)
# print(decimal ** 0.5)

# string = 'python'
# print(string[::-1])

# a = {'x': 1, 'y': 2, 'z': 1}
# print(list(a.keys())[1])
# print(list(a.keys())[0])

# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.popitem())

# a = {'a': 1, 'b': 2, 'c': 1}
# a['d'] = 5
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# del a['a']
# del a['b']
# del a ['c']
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(a.keys())[0])
# print(list(a.keys())[1])
# print(list(a.keys())[2])
# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(a.keys))['a']

# year = float(input('Vvedite chislo-god: '))

# if year // 4 != 0 and year % 100 !=0:
#     print('YES')
# elif year // 400 != 0:
#     print('YES') 
# else:
#     print('NO')


# num = chr(int(input('Vvedite chislo: ')))
# if num.isalpha():
#     print(f'Это буква {num}')
# else: 
#     print(f'Это не буква, а символ {num}')

# def add(x, z):
#     return x + z

# print(add(2, 5))
# # 
# def get_type(arg1, arg2):
#     print(f'{type(arg1)}\n{type(arg2)}')

# get_type(5, '5')



# try:
#     num1 = int(input('Vvedite chislo: '))
#     num2 = int(input('Vvedite chislo: '))
#     res = num1 + num2
# except ValueError:
#     print('Введите число!')
# else: 
#     print(res)