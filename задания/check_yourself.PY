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
def mul(num):
    res = []
    res.append(num ** 2)
    return res

num = 3
print(mul(num))
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

