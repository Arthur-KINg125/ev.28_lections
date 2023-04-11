# "string-строки"
# "hello world"


# Строки - набор последовательных символов, которые мы используем для хранения и представления текстовой информации.

#Индексация в строке 
# name = "john"
    # John = 0
    # o = 0
    # h = 2
    # n = 3
# print(name)
# print(name[1])
# str1 = "kani"
# print("kani"[-1], "kani"[0])

# str1 = "birthday"
# print(str1[5], str1[6], str1[7])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])

# str1 = "birthday"
# print(str1[5] + str1[6] + str1[7])
# print(str1[0] + str1[1] + str1[2] + str1[3] + str1[4])

# Срезы по индексам
# [start: end: <step>] 

# str1 = 'birthday'
# print(str1[5:])
# print(str1[:5])

# text = 'hello dura, my name is John I\'m North king'
# print(text[:13])
# print(text[::2])
# print(text[::-1])

# Конкатенация строк(соединение)

# a = 'Hello'
# b = 'world'
# c = " "
# print(a + c + b)

# Экранирование - способ записи символов в строку, которые невозможно ввести с клавиатуры

# \n -> перенос строки
# \t - горизантальная табуляция 
# \v - вериткальная табуляция
# \f - перевод страницы
# \r - возврат указателя
# print("\vHello world!\nMy name is John Snow")

# Форматировение строк 
# 1. с помомщью % 
# 2. с использованием .format()
# 3. Инерполяция


#  % 
# name = input('Vvedute imya: ')
# last_name = input('Vvedite Last Name')
# # print('добро пожаловать к нам' + name + " " + last_name + '!')
# print('Hello mr/mrs % %s!' %(name, last_name))

# .format
# name = input("Vvedite imya:)
# last_name = input('Vvedite last_name')
# print('Приветствую вас,{}{}, в наш клуб {}!'.format(name, last_name))

# a = input('Enter mr/mrs: ')
# name = input('Vvedite imya:')
# last_name = input('Vvedite last_name')
# print(f'Hello {a} {name} {last_name}! Welcome to the party!')

# text = "Запомни Питер, с большой Ттттсилой приходит и большая ответственность."
# reversed_text = text[::-1]
# # print(reversed_text)

# i = 0
# count_t = 0
# len_text = len(reversed_text)
# while i < len_text:
#     symbol = reversed_text[i]
#     if symbol == "т" or symbol == 'Т':
#         count_t += 1
#     print(reversed_text[i])
#     i += 1

# print(f'В тексте "т" встретилась {count_t} раз!')

