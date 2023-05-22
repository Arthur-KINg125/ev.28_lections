# OOП - объектно-ориентированое програмирование

# Класс -> это описание того, как должен выглядить объект, то есть в классе мы описываем какими свойствами(данными) и поведениям(функций) должен обладать объект

# Объект -> это сущность которую мы создаем от класса, у объекта есть собственые состояния свойств(данные)

# Целью создания было связать данные с функциями которые упровляли этими данными

# Cвойствами(атрибутами) - называют обычные переменые внутри класса в которых хранятся данные объекта

# Методы это обычные функций внутри класса, методы описывают поведение объекта

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + " " + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f"Name: {self.name}, age: {self.age}, Job: {self.job}, Citizen: {self.citizen}"

# john = Human("John", "S77S", "King of North", "Northerner")
# billal = Human("Billal", "Lanister", "programmist", "KGZ")

# # print(john, type(john))
# # print(dir(john))
# print(john.show_info())
# john.age = 24
# print(john.show_info())
# john.job = "King of Westeros"
# print(john.show_info())
# print()
# print(billal.show_info())
# billal.age = 23
# print(billal.show_info())
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# class Dog:
#     # Аттрибуты класса 
#     age = 0
#     ushi = True

#     def __init__(self, name, color) -> None:
#         "Инициализатор, именно здесь создаются аттрибуты объекта"
#         # Self - ссылка на объект который только что создался
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f"{self.name} Лает!")

#     def show_info(self):
#         print(f"Name: {self.name}, age: {self.age}, color: {self.color}, ushi: {self.ushi}")

#     def slip(self):
#         print(f"{self.name} Cпит!")

# rex = Dog("Rex", "black")
# pluto = Dog("Pluto", "brow")
# aktosh = Dog("Aktosh", "gray")

# rex.show_info()
# rex.bark()
# pluto.show_info()
# pluto.bark()
# aktosh.show_info()
# aktosh.slip()
# print()
# rex.age = 2
# pluto.age = 5
# aktosh.age = 11
# aktosh.ushi = False

# rex.show_info()
# pluto.show_info()
# aktosh.slip()
# aktosh.show_info()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# class Human:
#     def __init__(self) -> None:
#         print("init worked!")
#         self.raychel = "raychel"
#         self.golod = 100
    
#     def eat(self, meal, doela = True):
#         print(f"{self.raychel} покушала {meal}")
#         if doela:
#             self.golod -= 50
#         else:
#             self.golod -= 25
        


# obj = Human()
# print(obj.raychel, obj.golod)
# obj.eat("burger", doela = False)
# print(obj.raychel, obj.golod)
# obj.eat("Kruasan")
# print(obj.raychel, obj.golod)
