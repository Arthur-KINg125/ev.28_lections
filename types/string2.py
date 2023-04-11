
# print(dir(str))
# print(dir(int))

# a = 'Hello'
# b = "JOhn"
# # print(a != b)
# # print('abc' == 'abc')

# # print(a > b)
# # print(a < b)

# print('a') # 97 -> 11000001
# print('a' != 'b')
# print('hello' > 'harry') #True
# print('abc' > 'abc') #False

# # Len() - возвращает кол-во символов в строке
# a = 'Hello'
# b = 'John Snow'
# print(len(a) < len(b))
# print(len(a),

# методы строк
# replace(old, new, [count]) - меняет в строке символы old на new, если вы укажете count, то заменит count раз

# text = 'hahahaha'
# result = text.replace('a', 'e', 2)
# print(text)
# print(f'result after replace: {result}')

# str1 = 'Hello world! My name is John Snow!'
# res = str1.replace('John Snow', 'Tirion Lanister')
# print(res)

#strip() - Убирает пробельные символы в начале и в конце строки 
#rstrip, lstrip
# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))
# print(dir(str))
 
# isdigit - проверяют
# isnumeric - состоит ли наша строка 
# isdecimal - полностью из чисел

# num = input('Vvedite chislo: ')
# print(f'Vvedeno chislo?:  {num.isdigit()}')

# num = input('Vvedite chislo: ')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('ve vveli ne chisla')

# text = '\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())

# isalnum() -> проверяет состоит ли наша строка из чисел и символов латинского алфавита и кириллицы
# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha() -> состоит ли наша строка полностью из символов алфавита 

# text = 'Hello world'
# res = text. replace(' ', '')
# print(res)
# print(res.isalpha())

# islower()
# isupper()
# istitle()
# str1 = 'Is My Name'
# print(str1.islower())
# print(str1.istitle())
# str2 = 'RRTYU IS GODLIKE'
# print(str2.isupper())
# index(value, [start], [end]) - выводит индекс значения value, которые мы передаем в нашей строке.

# text = 'hello john snow'
# print(text.index('john', 2, 5))

# text = "Hello world! My name is John Snow! " #o
# res = text.index('o')
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)

# count(value, [start]) - считает кол-во вхождения value в нашу строку

# text = 'hello o o o hello'
# print(text.count('o'))
# print(text.count('hello'))
# print(text.count('Berserk'))

# split(separator) - дробит нашу строку на несколько частей по разделителю, все части строк сохраняются в типе list

# text = 'Let me speak by my heart in english! Cause my name is John Snow!' 

# res = text.split(' ')
# print(res)
# print(len(res))


# a = 'hello#hello#hello#hello'
# res = a.split('#')
# print(res)

# 'connector'.join(list) -> соединяет по connector строки которые находились в list

# text = 'Let me speak by my heart in english! Cause my name is John Snow!' 
# res = text.split(' ')
# print(res)
# str1 = ' '.join(res)
# print(str1)


# find(value, [start], [end]) - делает тоже самое, что и индекс, но если не нашел, то вернется -1

# text = 'hello'
# print(text.find('l'))
# print(text.find('lytui')), type(text.find('lytui'))
# print('John Snow')

# swapcase() - переводит все символы в противоположенный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello WorLd, JOHN snow'
# print(f'Original: {text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр


#             # john.capitalize() -> john
# name = input('Vvedite imya: ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# Fio = 'john edart snow'
# print(Fio.title())

# print(dir(str))                                                   