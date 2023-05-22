def add(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2 

def subtract(num1: int | float, num2: int | float) -> int | float:
    return num1 - num2

def multiply(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2 

def divide(num1: int | float, num2: int | float) -> int | float:
    try:
        return num1 / num2 
    except ZeroDivisionError:
        return 'Na nol\' nel\'za delit\''

def calculator(num1: int | float, num2: int | float):
    """"Nasha function Vypolnyaet arifmeticheskuyu operator"""
    operator = input("Vvedite operator(+, -, *, /)")
    if operator == '+': return add(num1, num2)
    elif operator == '-': return subtract(num1, num2)
    elif operator == '*': return multiply(num1, num2)
    elif operator == '/': return divide(num1, num2)
    else: return "Vy vveli fign\'yu"

def main():
    num1 = input('Vvedite chislo')
    num2 = input('Vvedite chislo')
    try:
        num1 = float(num1) if '.' in num1 else int(num1) 
        num2 = float(num2) if '.' in num2 else int(num2)
    except ValueError:
        print('Ne pravilno')
        main()
        return

    while True:
        result = calculator(num1, num2)
        if type(result) == str:
            print(f'Rezul\'tat: {result}')
        else:
            print(result)
            break
          
    question = input('Hotite prodolzhit\'').lower().strip()
    if question == 'yes':
        main()
    else:
        print('Spasibo za ispol\'zovanie ')

main()