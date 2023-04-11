num1 = float(input('Введите число: '))
operation = input('Введите операцию (+, -, *, /, %, **, //): ')
num2 = float(input('Введите число: '))
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
elif operation == '%':
    print(num1 % num2)
elif operation == '**':
    print(num1 ** num2)
elif operation == '//':
    print(num1 // num2)
else:
    print('Данной операции нет в системе.')

    