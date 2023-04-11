# sentence = input('Vvedite predlojenie:' )
# # if sentence[-1] == '?':
# #     print('Yes, voprositel\'noe!')
# # else:
# #     print('No, normal one!')

# print('Yes, voprositel\'no!' if sentence[-1] == '?' else 'No, normal one!')

# #----------------------------------------------------
# Ternary operators(Тернарный оператор) - это конструкция которая, по своему действию аналогична конструкции if, else,
#  но при этом записывается в одну строчку

# number = int(input('Vvedite chislo: '))
# res = 'even number' if number % 2 ==0 else 'odd number'
#     #четное                                 #нечетное
# print(res)

# <выражение если True> if <условие> else <выражение если False>

# ls = [55, 65, 75 , 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max/min: ')
# res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# print(res)
# if choice.lower().strip() == 'max':
#     print(max(ls))
# # elif choice.lower().strip() == 'min':
# #     print(min(ls))
# # else:
# # #     print('invalid choice!')
# # res = max(ls) if choice.lower().strip() == 'max' else min(ls) if choice.lower().strip() == 'min' else "Invalid choice!"

# #--------------------------------------------------------------------- MEGA-CALCULATOR!!!!!!
# flag = True
# symbols = '0123456789' + '-' + '.'

# while flag:
#     num1 = input('number 1: ')
#     is_correct_number = True
#     for x in num1:
#         if x not in symbols:
#             print('Вы ввели не правильное число!')
#             is_correct_number = False
#             break

#     if not is_correct_number:
#         continue



#     num2 = input('number 2:')
#     for x in num2:
#         if x not in symbols:
#             print('Вы ввели не правильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue
    
#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     # print(num1, type(num1))
#     # print(num2, type(num2))
#     operator = input('Vvedite operator(+, -, *, /): ')
#     if operator == '+':
#         print({num1 + num2})
#     elif operator == '-':
#         print({num1 - num2})
#     elif operator == '*':
#         print({num1 * num2})
#     elif operator == '/':
#         if num2 == 0:
#             print('Na nol\' delit\' nel\'zya')
#         else:
#             print({num1 % num2})
#     else:
#         print('Vy vveli nevernyi operator!')

#     choice = input('Hotite prodolzhit\'(yes/no)?')
#     if choice.lower().strip() == 'no':
#         flag = False
#         print('Goodbye!')

        
        
        








    # if '-' in num1 and num1 [0] == '-' or '-' not in num1:
    #     num1 = int(num1)
    #     num1 = int(num1)