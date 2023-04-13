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

# try:
#     inp1 = int(input('Vvedite: '))
#     inp2 = int(input('Vvedite: '))
#     res = inp1 + inp2
# except ValueError:
#     # if inp1 or inp2 != int():
#     res = inp1 + inp2
# else:
#     print(res)

# try:
#     inp1 = input('Vvedite: ')
#     inp2 = input('Vvedite: ')
#     print(int(inp1) + int(inp2))
# except:
#     print(inp1 + inp2)

# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['fark'])
# except KeyError:
#     print('Нет такого ключа!')

# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#     print(list_[11])
# except:
#     print('Нет такого элемента!')

# suitcase = []
# suitcase.append('shoes')
# suitcase.append('t-shirt')
# suitcase.append('glasses')
# suitcase.append('phone')
# suitcase.append('cream')
# suitcase.remove('shoes')
# suitcase.insert(0, 'crocs')
# print(suitcase)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []
# for x in nums:
#     if x < 5:
#         res.append(x)

# print(res)

# def func11(list_, tuple_):
#     return print(list_, tuple_)

# func11([1, 2, 3, 4], (1, 2, 3, 4))

# list_ = list(input('Vvedite list: '))
# tuple_ = tuple(input('Vvedite tuple: '))
# print(list_, tuple_)

# list_ = input('Vvedite chisla: ').split(' ')
# tuple_ = tuple(list_)
# print(list_)
# print(tuple_)

# list_ = [1, 2, 3, 4]
# new_list = []
# for x in list_:
#     new_list.append(str(x))

# print(new_list)

# for i in range(1, 10):
#     i -= 5
# print(i)

# for i in range(9, 4, -3):
#     print(i)

# try:
#     age = int(input('Vvedite chislo: '))
#     if age < 18:    
#         raise ValueError('Доступ запрещен')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')
