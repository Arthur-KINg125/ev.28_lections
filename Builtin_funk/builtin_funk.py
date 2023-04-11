# def hello():
#     return 'hello'

# x = lambda: 'hello'
# print(x())
# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 5))

# x = lambda num1, num2, degree=None: (num1 * num2) ** degree if degree else num1 * num2

# print(x(2, 2, 3))
# print(x(5, 5))

# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# print(my_doubler(50))

# list_ = ['hello', 'bil', 'john', 'daniel', 'mil', 'vlad']

# a = sorted(list_, key=len, reverse=True)
# print(a)

# dict_ = {
#     'john': 500,
#     'tirion': 160_000,
#     'sanchar': 20,
#     'ayana': 100_00,
# }

# new_dict = sorted(dict_.items(), key = lambda x: x[1], reverse=True)
# print(new_dict)

'''
map(function, iterable) -  применяется к кпждому элементу внутри iterable функцию, которую мы ей передаем в function, закидывая в результат те данные, которые возвращает функция. В результате мы получим mapobject(iterator), в котором хранятся все наши данные.
'''

# ls = ['1', '2', '3']

# new_list = map(int, ls)
# print(new_list)


# new_list = list(map(lambda x: str.capitalize, ls))
# print(new_list)

# names = ['john', 'aria', 'baku', 'bakberdi', 'lilo']

# # hello, mr/mrs john

# new_names = list(map(lambda x: f'hello, mr/mrs {x}', names))
# print(new_names)

'''
Функция высшего порядка - функция, которая принимает в качестве аргемента др. функцию
'''
'''
Filter(function, iterable) - применяет ко всем элементам iterable функцию, которую мы передали и возвращает filterobject( итератор) только с теми элементами, для которых функция вернула True
'''

# ls = ['one', 'lili', 'oleg', 'billi']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)

# enumerate(iterable) - пронумеровывает каждый элемент внутри iterable ее собственным индексом

# ls = ['str1', 'str2', 'str3']
# new_list = list(enumerate(ls))
# print(new_list)

