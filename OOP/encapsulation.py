# Инкапсуляция:
# 1. Языковая конструкция, которая помогает связать данные с методами для их обработки и управления(связь между методами данными и методами, которые управляют ими) (класс - капсула)
# 2. Механизм сокрытия, при помощи, которого можно ограничить доступ одного компонента программы от другого.


# Инкапсуляция как связь

# class Phone:
#     number = '+996700700700'

#     def print_number(self):
#         print(f'МОй номер: {Phone.number}')
#         print(f'МОй номер: {self.number}')

# # my_phone = Phone()
# # my_phone.print_number()

# # Инкапсуляция как механизм сокрытия
# # 3 уровня сокрытия данных в питоне
# #   1. Публичный(public) - number, print_number
# #   2. Защищенный(Protected_) - _number
# #   3. Приватный(protected__) - __number

# # class Car:
# #     _country = 'Germany'
    
# #     def __init__(self) -> None:
# #         self.marka = 'Mercedes-Benz' # public
# #         self._model = 'W140' # protected
# #         self.__color = 'gray'

# # obj = Car()
# # print(dir(obj))
# # print(obj._Car__color)
# # print(obj._country)
# # print(obj._model)



# class Phone:
#     username = 'John'
#     caller = 'Jamie'
#     count_of_calls = 0

#     def answer_call(self):
#         print(f'{self.caller} звонит вам!')
#         question = input('Взять трубку? (yes/no) ')
#         if question.lower().strip() == 'yes':
#             print('Привет!')
#         else:
#             print('Сбросили трубку!')

#     def increment_call_counter(self):
#         self.count_of_calls += 1
        
#     def end_call(self):
#         self.increment_call_counter()
#         print('Aloo!')
#         print(f'Количество звонков от {self.caller}: {self.count_of_calls}')

# john = Phone()
# print(john.username)
# john.answer_call()
# john.end_call()


# ------------------------------------------------



# class Person:
#     def init(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old!')

# obj = Person('John', 18)
# obj.display_info()
# obj.nationality = 'Kyrgyz'
# print(obj.nationality)
# obj.age = -18
# obj.name = 55
# obj.display_info()

#--------------------------------------
# getter and setter
# Они нужны, чтобы избежать прямого обращения к сокрытым атрибутам
# при этом можно добавить валидацию(проверки) данных, которые будут установлены в атрибут.

class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f'My name is {self.__name} and I\'m {self.__age} years old!')

# Getter
    def name(self):
        return self.__name

# setter
    def set_name(self, name):
        if not isinstance(name, str):
            print('Name must be str') 
        else:
            self.__name = name

# Getter
    def age(self):
        return self.__age

# setter
    def set_age(self, age):
        if not isinstance(age, int) or not 0 <= age < 150:
            print('Invalid value for age') 
        else:
            self.__age = age

obj = Person('John', 24)
print(obj.name())
obj.set_age(-18)
obj.display_info()
obj.set_name('Raychel')
obj.display_info()
print(obj.age())


