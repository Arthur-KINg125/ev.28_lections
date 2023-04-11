# str1 = 'kkkkkkkkkkkkkkkkkkkqqqqqqqqqqqqqqqqqqqqqqq'

# def get_reversed (strings):
#     # print(strings[::-1])
#     spisok = strings.split()[::-1]
#     # print(spisok[::-1])
#     return ' '.join(spisok)

# print(get_reversed(str1))
        
# def sum_of_args(a, b, c=5, d=5): #параметры 
#     return a + b + c + d

# result = sum_of_args(1,2,3,4) # аргументы
# print(result)

# res = sum_of_args
# # print(res, type(res))
# print(res(5, 6, 7, 8))
# print(sum_of_args(5, 5))

# ------------------------------------------------------------
#позиционные и именновагые аргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param a')
#     print(c, 'is stored in param a')

# printParams(5, 10, 15)
# printParams(c = 5, b = 15, a = 10)

# def sum_of_args(a, b, c=5, d=5): #параметры 
    # return a + b + c + d

# print(sum_of_args(5,10,15,20))
# print(sum_of_args(a=5, c=20, b = 10, d = 15))

# ---------------------------------------
# оператор *

# a = [1,2,3]
# b = [4,5,6]
# c = {[*a, *b]}
# print(c)

# ''''===============================

# def printScores(student, *args):
#     print(f'Name of student: {student}')
#     print(f'AVG: {sum(args)/ len(args)}')

#     for x in args:
#         print('score', x)



# def printPetNames(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(kwargs)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)    
#         else:
#             print(f'{pet}:{name}')

# printPetNames('John Snow', dog='Pluto', cat='Garfild', fish=['Nemo', 'Dori', 'Batya'], turtle='Leonardo')

# def get_some_data(a, b *args, **kwargs):
#     print('параметры a и b: ', a, b)
#     print('аргументы:', args)
#     print('именнованные аргументы:', kwargs)

# get_some_data(1,2,3,4,5, lang ='Python', car ='BMW')

#--------------------------------------

# def generate_random_string(len_):
#     import string as s
#     import random
#     symbols = s.ascii_letters + s.digits

#     # print(s.ascii_letters, )
#     res = list(
#         random.choice(symbols) for i in range(0,len_)
#     ) + list(random.choice(s.punctuation))
#     random.shuffle(res)
#     return ''.join(res)

# print(generate_random_string(15))

# result = isEven(6)
# print(result)
# print(isEven(5))