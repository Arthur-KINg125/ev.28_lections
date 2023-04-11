# Операторы сравнения
# Условные операторы и логические операторы

# операторы сравнения
# <, >, ==(равно), !=(не равно), <=, >=

# 1 < 7 - True
# 7 > 9 - False

# Условные операторы
# if
# elif
# else

# if <condition>:
#     <body if> # сработает если в conditoin  if придет true
# [elif] <condition>:
#     <body elif>
# [elif] <condition>:
# [else]:
#     <body else> # сработает если во всех выше стоящих условиях пришло false

# string = input('Enter smt: ')

# if string.lower() == 'hello':
#     print('Hello, it\'s me. I was wondering if after all these years you\'d like to meet')
# elif string.lower() == 'Dusha pepla':
#     print('NOOOOOO')
# elif string.lower() == 'abra-kadabra':
#     print('SIm Salamon Kadabra')
# else:
#     print('What are you talking about, can you write it again,')


# print('Registration Form:')
# email = input('Enter your email: ')
# password = input('Enter your password: ')
# if len(password) < 8:
#     raise ValueError('Password is too short!\nNeed to be 8 symbols or more!')
# elif password.isdigit():
#     raise ValueError('Password is invalid!\nPassword must contain symbols too!')
# elif password.isalpha():
#     raise ValueError('Password is invalid!\nPassword must contain symbols too!')

# password2 = input('Enter password confirmation: ')

# if password != password2:
#     raise ValueError('Passwords did not match!')

# print(f'Successfully registeres! Hello Mr/Mrs {email}!')

# age = input('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')

# if age < 18:
#     print(f'Access Denied! Come again after {18 - age} year')
# else:
#     print('You can pass! Welcome to Kazakhstan')

# and - лошические и 
# or - лог или
# not - лог отрицание

# money = 1_000_001
# status = 'premium'

# if money < 1_000_000 and status == 'premium':
#     print('You\'re president of our club!')
# elif money > 1_000_000 or status == 'premium':
#     print('You\'re ministr of our club')
# else: 
#     print('You\'re honorable member of the club')

# str1 = 'hello world'
# print(str1)
# symbol = input('Enter the symbol: ')

# if symbol not in str1:
#     print(f'The symbol: {symbol} does not exists!')
# else:
#     print(f'The symbol: {symbol} exists')


# if symbol in str1:
#     print(f'The symbol: {symbol} exists')
# else:
#     print(f'The symbol: {symbol} does not exists)

# разрешаем доступ если он юзер гита или гугла и его возраст 21 или у него есть деньги(10000)

# user = 'John'
# is_google_use = True
# is_github_use = True
# age = 19
# user_coins = 9000

# if (is_github_use or is_google_use) and (age > 21 or user_coins > 10000):
#     print(f'You can enter the system Mr/Mrs {user}!')
# else: 
#     print('Sorry, you couldn\'t enter!')

# mark = int(input('Vvedite lyuboe chislo, bruh.... '))

# if mark > 90 or mark == 90:
#     print('Отлично, Ваша оценка 5!')
# elif mark > 80 or mark == 80:
#     print('NOrmana, vse horosho')
# elif mark > 70 or mark == 70:
#     print('Nuuu, hotyaby ne dva')
# elif mark > 60 or mark == 60:
#     print('School system is shit, i don\'t care.')
# else:
#     print('Loh, v sleduyushiy raz povezet')