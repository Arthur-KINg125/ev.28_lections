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

# def func12(list_, low_up):
#     if low_up == 'lower':
#         return [x.lower() for x in list_]
#     elif low_up == 'upper':
#         return [x.upper() for x in list_]
    
# print(func12(['STRING1', 'STRING2'], 'upper'))

# def func13(string):
#     return [lambda x:string.count(x) for x in string]

# print(func13('Hello'))

# num1 = 88
# num2 = 84
# res = int()
# i = 0
# flag = False
# while i != num2:
#     i += 1
#     res = num1 * num1
#     print(num1 * res)
    
# num1 = 88
# num2 = 84
# i = 0
# while i != num2:
#     i += 1
#     print(num1 ** num1)
        
# class Song:
#     def __init__(self, author, title, year):
#         self.author = author
#         self.title = title
#         self.year = year
        
#     def show_author(self):
#         return(f'Автор этой песни {self.author}')
        
#     def show_title(self):
#         return(f'Название этой песни {self.title}')

#     def show_year(self):
#         return(f'Эта песня вышла в {self.year} году')

        
# Song_ = Song(title = 'Yomi Yori', author = 'ICDD', year = 2014)

# print(Song_.title)
# print(Song_.author)
# print(Song_.year)

# with open('task3.txt', 'w+') as file:
#     file.write('0*1*2*3*4*5*6*7*8*9*')
#     file.seek(0)
#     print(file.read())

# class Class1:
#     def first(self):
#         pass

#     def second(self):
#         pass

# class Class2(Class1):
#     def third(self):
#         pass

#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

# class A:
#     def public(self):
#         return 'public method'

#     def _protected(self):
#         return 'Protected method'

#     def __private(self):
#         return 'Private method'

#     def print_protected(self):
#         self._protected()

#     def print_private(self):
#         self.__private

# obj1 = A()

# print(obj1.public())
# print(obj1.print_protected()) 
# print(obj1.print_private())

# class A:
#     def method1(self):
#         print('Hello World')
    
# class B(A):
#     pass

# b1 = B()
# b1.method1()


# class Car:
#     __speed = 0 
#     def set_speed(self, meaning): 
#         self.__speed = meaning 
#         return self.__speed 
    
#     def show_speed(self): 
#         return self.__speed 
    
# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed())

# class Car:
#     __speed = 0
#     @property
#     def speed(self):
#             return self.__speed

#     @speed.setter
#     def speed(self, new):
#             self.__speed = new
#             return self.__speed 
            
# car1 = Car()
# print(car1.speed)
# car1.speed = 20
# print(car1.speed)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] 

# list_ = [x ** 2 for x in list1]
# print(list_ )

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# int_list = [int(x) for x in str_list]
# print(int_list)

# list_ = [x ** 2 if x % 2 == 0 else x for x in range(1, 11)]

# print(list_)

# list_ = [x == False if x % 2 != 0 else True for x in range(1, 11)]
# print(list_)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(x) <= 4 else 'longer' for x in list_name]
# print(new_list)

# n = int(input('Chislo 1/ 10: '))
# dict_ = {x: x**2 for x in range(1, 501) if x % n == 0}
# print(dict_)

# class Auto():
#     def ride(self):
#         print('Riding on a ground.')

# class Boat():
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 

class RadioMixin: 
    def play_music(self): 
        class_ = 'Space Invaders' 
        print(f'Песня называется {class_}') 
        
class Auto: 
    pass 
        
class Boat(RadioMixin): 
    pass 

class Amphibian(Auto, Boat): 
    pass 

auto = Auto() 
boat = Boat() 
obj = Amphibian() 
obj.play_music()
