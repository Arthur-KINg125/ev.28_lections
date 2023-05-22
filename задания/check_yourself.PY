# List_friends = {'Murat':24, 'Erzhan':21, 'Karina':24, 'Altynai':17, 'Aibek':16}
# for k, v in List_friends.items:
#     if v in List_friends > 16:
#         print('Vy uspeshno proshli!')


# dict_ = dict(Murat=24, Erjan=21, Karina=24, Altynai=17, Aibek=16)

# for x in dict_:
#     if dict_[x] > 17:
#         print(f'{x} proshel! ')
#     else:
#         print(f'{x} ne proshel')

# Создайте словарь, где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
# spisok = {'Ananas': 255, 'yabloko':250, 'banan':235, 'Grusha':240}
# for k, v  in spisok.items():
#     if v % 2 != 0:
#         print(k, v)
# 4) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
# """

# dict_ = {'d':2, 'a':3, 'f':1, 'g':2}
# for v in dict_:



#  Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.\

# dict_ = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# for x in dict



# year = int(input('Vvedite god'))
# if year % 4 and year % 100:
#     print('YES')


"""
1) Создайте список list_ из нечётных целых чисел в промежутке от 1 до 50. Нужно использовать comprehension.
"""
# list_ = [x for x in range(1, 50) if x / 2 !=0]
# print(list_)

"""
2) Создайте список list_ из квадратов всех чисел от 1 до 25 (включительно). Нужно использовать comprehension.
"""
# list_ = [x ** 2 for x in range(1, 25)]
# print(list_)
"""
3) Опишите полный синтаксис конструкции try-except
"""

"""
4) Напишите программу, которая будет получать через input 2 числа num1, num2 и будет печатать их сумму.
Обработайте ошибку, которая возникнет, если пользователь введёт что-то кроме числа и выведите сообщение, например:
Введите число!
"""
# try:
#     num1 = int(input('Vvedite chislo: '))
#     num2 = int(input('Vvedite chislo: '))
#     res = (num1 + num2)
#     print(res)
# except ValueError:
#     print('Vy vveli nepravil\'noe chislo! ')
"""
5) Создайте функцию divide() которая должна принимать 2 числа и возвращать результат их деления.
"""
# def divide(a, b):
#     return a / b
# print(divide(10, 2))


"""
6) Создайте функцию:

is_palindrome() 
которая будет принимать строку и проверить является ли она палиндромом.

Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.

Функция должна возвращать True или False. Нужно учитывать пробелы и регистр 
"""

# def is_palindrome(str_):
#     return str_ == str_[::-1]
# print(is_palindrome('Pop'))


# a = int(input('chislo 1: '))
# b = int(input('chislo 2: '))

# def rezultat (a, b):
#     res = int()
#     res.append(a + b)

# rezultat(a, b)


"""
3) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""

# chisla = [1, 2, 3, 4]

# def proizvedenie(chisla)

"""
2) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""

# param1 = input ()
# param2 = input ()

# def type_arg(param1, param2):
#     print(type(param1))
#     print(type(param2))

# type_arg(param1, param2)

"""
1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# def slozhenie(num1, num2):
#     return print(num1 * num2)

# slozhenie(5, 10)

"""
2) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""
# def type_arg(param1, param2):
#     return print(type(param1), type(param2))

# type_arg(['sas', 'das'], (5, 'dag'))

"""
3) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""
# def proizvedenie(int1, int2):
#     return print(int1 + int2)

# proizvedenie(10, 15)

"""
4) Напишите функцию, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы
"""

"""
5) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
"""
#писать код здесь
"""
6) Дана глобальная переменная num со значением 3. Напишите функцию mul которая будет возвращать квадрат этой переменной и записывать результат в глобальную переменную num. Вызовите функцию три раза, и распечатайте переменную num.
"""
# def mul(num):
#     res = []
#     res.append(num ** 2)
#     return res

# num = 3
# print(mul(num))
"""
7) Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.
"""
#писать код здесь

"""
8) Cоздайте переменную list_ и сохраните в ней список из чисел. Создайте новый список, используя встроенные функции, состоящий из квадратов этих чисел, результат сохраните в новой переменной result и выведите в консоль.

Обязатьльно нужно использовать builtin functions
"""

# def is_palindrome(string):
#     return string == string[::-1]
    

# print(is_palindrome('avatar'))

# int1 = int(input('Vvedite chislo: '))
# int2 = int(input('Vvedite chislo: '))
# def max_num(int1, int2):
#     if int1 > int2:
#         return print(int1)
#     elif int1 < int2:
#         return print(int2)

# max_num(10, 12)

# def multiply_list(list_):
#     n = 1 
#     for i in list_:
#         n *= i
#     return n

# print(multiply_list([1, 2, 3, 4, 5, 6]))

# def func11(num1, num2, num3):
#     if num3 != 0:
#         return (num1 + num2) / num3
#     elif num3 == 0:
#         return num1 + num2

# print(func11(5, 5, 2))

# def mul(num):
#     res = []
#     res.append(num ** 2)
#     # res.append(num)
#     return res

# num = 3
# print(mul(num))

"""
1)	В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
"""
# file = open(file: Some_file, mode: 'r')
"""
2)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""

# from bs4 import BeautifulSoup
# import csv
# import requests

# r = requests.get('https://vesti.kg/')

# def get_html(url: str) -> str:
#     response = requests.get(url)
#     response.text
    
# def get_title(soup: BeautifulSoup):
#     container = soup.find('div', class_='itemListLeading')
#     titles = container.find_all('div', class_='itemContainer itemContainerLast')
#     # res = []
#     # for title in titles:
#     res = list(titles)
#     return print(res)
# def get_




"""
1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение 'Riding on a ground'.

Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.

Создайте класс Amphibian который наследуется от класса Auto и Boat.

Создайте от него объект obj и вызовите все методы.

Ввод:

obj = Amphibian() 
obj.ride() 
obj.swim() 
Вывод:

Riding on a ground 
Floating on water 
"""

# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')
    
# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()
"""
2)Создайте класс ContactList, который должен наследоваться от встроенного класса list.

В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений.

Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.

Примерный ввод:

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 
Метод search_by_name возвращает все строки содержащие подстроку "Olya":

['Ivan Olya', 'Olya Ivan'] 
"""

# class ContactList(list):
#     def search_by_name(self, name):
#         return [contact for contact in self if name.lower() in contact.lower()]

# all_contacts = ContactList(['Olya', 'Ivan', 'Arthur', 'Iskender', 'Arthur', 'Arthur'])
# print(all_contacts.search_by_name('Iskender'))


"""

3) Напишите класс Person, который будет хранить информацию о пользователе. У объекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email).
При инициализации объекта, передавать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными.
Поэтому реализуйте для каждого атрибута методы доступа get и set не используя декораторы property и setter. У вас будут такие методы: get_name, set_name, get_last_name, set_last_name, get_age, set_age, get_email, set_email.
Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран.
Пример:

john = Person()
print(john.get_name()) # None
print(john.get_last_name()) # None
print(john.get_age()) # None
print(john.get_email()) # None
john.set_name('John')
john.set_last_name('Snow')
john.set_age(30)
john.set_email('johnsnow@gmail.com')
print(john.get_name()) # John
print(john.get_last_name()) # Snow
print(john.get_age()) # 30
print(john.get_email()) # johnsnow@gmail.com
"""

"""
1) Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.

У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.

Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.

класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.
"""
# class CreateMixin:
#     def create(self, todo, key):
#         if key in self.todos.keys():
#             return 'Задача под таким ключом есть'
#         self.todos[key] = todo 
#         return self.todos
    
# class DeleteMixin:
#     def delete(self, todo, key):
        
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, data):
#         self.data = data

    

"""
2) Создайте классы Dog и Cat с одинаковым методом voice.

Для собак он должен печатать "Гав", для кошек "Мяу".

Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.

Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().

Ввод:

to_pet(barsik) 
to_pet(rex) 
Вывод:

Мяу 
Гав 
"""

# class Dog:
#     def voice(self):
#         print('гав')

# class Cat:
#     def voice(self):
#         print('мяу')

# barsik = Cat()
# rex = Dog()

# def to_pet(Pet):
#     Pet.voice() 

# to_pet(rex)
# to_pet(barsik)


"""
1)Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов. С помощью list comprehension создайте список из результатов работы метода count обоих объектов.

!!!! 
Обязательное условие: если в классе A или B не переопределить метод count должна выйти ошибка
!!!!

"""

# class A():
#     def count(self):




# class B():
#     ...


"""
2) Создайте 3 класса:
Bird, Animal, Plant
класс Bird должен иметь методы: fly(), grow(), sound(). Animal: sound(), run(), grow(). Plant: grow(), photosynthesize()
каждый метод должен просто принтить действие. Например: def fly(self): print('я лечу')

!!!!
Обязательное условие: использовать абстракцию. Если не переопределить общий метод должна выходить ошибка
!!!!!

"""
# from abc import ABC, abstractmethod


# class Birdabs(ABC):

#     @abstractmethod
#     def fly(self):
#         pass

#     @abstractmethod
#     def grow(self):
#         pass

#     @abstractmethod
#     def sound(self):
#         pass

# class Animalabs(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

#     @abstractmethod
#     def grow(self):
#         pass

#     @abstractmethod
#     def run(self):
#         pass
    
# class Plantabs(ABC):

#     @abstractmethod
#     def grow(self):
#         pass

#     @abstractmethod
#     def photosintyze(self):
#         pass

# class Bird(Birdabs):
#     def fly(self):
#         print('i fly')

#     def grow(self):
#         print('i grow')

#     def sound(self):
#         print('i sound')

# class Animal(Animalabs):
#     def sound(self):
#         print('i sound')

#     def grow(self):
#         print('i grow')

#     def run(self):
#         print('i run')

# class Plant(Plantabs):
#     def grow(self):
#         print('i grow')

#     def photosintyze(self):
#         print('i photosinthezyse')

# bird = Bird()
# bird.grow()

# plant = Plant()
# plant.grow

# animal = Animal()
# animal.grow()

"""
3) Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.
Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, если возраст earth_age равен 20:

!!!!!
обязательное условие: создание абстрактного метода
!!!!!

"""
#писать код здес








#CHECK YOURSELF 11


"""
1) Создайте класс MyString, который будет наследоваться от str.
Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Пример:
example = MyString('String')
example.append('hello')
print(example) -> 'Stringhello'
print(example.pop()) -> 'o'
print(example) -> 'Stringhell'
"""

class MyString(str):
    def append(self, str_):
        self = self + str_
        return self
        
    def pop(self):
        return self[-1]

example = MyString('String')
example.append('hello')
print(example)
print(example.pop())
print(example)


"""
2)Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:
dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"
Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
init - инициализирует значение атрибута amount
update - задаёт объекту новое значение amount
repr - возвращает значение float
str - метод, который реализует логику функции dollarize()
//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
"""

'''WRITE CODE HERE'''

"""
3) Велосипед.
Создайте класс Bike в котором будут инициализированы следующие атрибуты: self.cost
(стоимость)
self.make (производитель)
self.model (модель)
self.year (год выпуска)
self.condition (состояние)
self._sale_price = None (цена для продажи, по умолчанию None)
self.sold = False (продан или нет, по умолчания False)
Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод
для указания цены для продажи, который принимает цену и если она меньше стоимости, то
ставит дефолтную цену для продажи (стоимость + мин. прибыль).
Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость
ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда
возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи.
При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на

True и возвращает прибыль с продажи.
Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте
объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его
атрибутов.
"""

class Bike:
    def __init__(self, cost, make, model, year, condition):
        self.cost = cost
        self.make = make 
        self.model = model
        self.year = year
        self.condition = condition
        self._sale_price = None
        self.sold = False

    def default_price(self, price):
        if price < self.cost:
            self._sale_price = self.cost + self._sale_price

"""
4) Герой.
Разработайте программу по следующему описанию.
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
"герой". У героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, поднимается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""

'''WRITE CODE HERE'''
