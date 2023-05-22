# Принцыпы ООП:
# 1. Наследование
# 2. Инкапуляция 
# 3. Полиморфизм

# 4. Абстракция
# 5. Композиция 
# 6. Агрегация 

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Наследование
# Позволяет принимать родительские методы и атрибуты дочернего классу

# Родительский класс 
# Дочерний класс

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# class Animal:
#     def print_info(self):
#         print("I\'m an Animal")

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# lion = Lion()
# Lion.print_info()
# print(dir(Animal))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# class Animal:
#     def say(self):
#         print(f"This animal name is: {self.name}: {self.golos}")

#     def eat(self):
#         print(f"{self.name} eats: {self.meal}")


# class Lion(Animal):
#     name = "Lion"
#     golos = "roar"
#     meal = "meat"
#     griva = True

#     def info(self):
#         print(f'{self.name} griva: {self.griva}')


# class Dog(Animal):
#     name = "Dog"
#     golos = "bark"
#     meal = "meat"

# class Koala(Animal):
#     name = "Koala"
#     golos = "roar"
#     meal = "efkalift"

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# print()
# julian.say()
# julian.eat()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# class Person:
#     def info(self):
#         print("I\'m person from Bishkek")

# class Student(Person):
#     def info(self):
#         super().info()
#         print("I\'m study at Manas University")
#     # pass


# obj = Student()
# obj.info()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price   

#     def get_info(self):
#         return {"brand": self.brand, "model": self.model, "price": self.price}     


# class Acer(Laptop):
#     def __init__(self, model, price, year, videocard):
#         super().__init__("acer", model, price)
#         self.year = year
#         self.video = videocard

#     def get_info(self):
#         repr = super().get_info()
#         repr["year"] = self.year
#         repr["videocard"] = self.video
#         return repr

# class Apple(Laptop):
#     def __init__(self, model, price, display, year):
#         super().__init__("MacBook", model, price)
#         self.display = display
#         self.year = year

#     def get_info(self):
#         repr = super().get_info()
#         repr["display"] = self.display
#         repr["year"] = self.year
#         return repr

# mac = Apple("Pro", "1500$", 14, 2020)
# print(mac.get_info())

# acer = Acer("Swift", "600$", 2019, "Nvidia")
# print(acer.get_info())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""Тут надо еще раз проверить """
# class Employee:
#     bonus = 1.5

#     def __init__(self, first_name, last_name, salary):
#         self.salary = salary
#         self.name = f"{first_name} {last_name}, Salary: {self.salary}"

#     def give_increase(self):
#         self.salary *= self.bonus

#     def __str__(self) -> str:
#         return self.name


# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language):
#         super().__init__(first_name, last_name, salary)
#         self.lang = language

#     def __str__(self) -> str:
#         return f"{str(super())}, Prog Language: {self.lang}"


# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs=[]):
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs

#     def add_devs(self, developer):
#         self.devs.append(developer)

#     def show_devs(self):
#         return [str(x) for x in self.devs]


# dev1 = Developer("John", "Snow", 1500, "Python")
# dev2 = Developer("Steve", "Jobs", 2000, "C++")
# dev3 = Developer("Lary", "Jobs", 3000, "JS")
# dev4 = Developer("Tirion", "Lanister", 2000, "Js")

# man1 = Manager("Jamie", "Lanister", 4000, [dev2, dev1])
# man2 = Manager("Willam", "Kan", 1500)

# print(f"Manager {man1}, has {man1.show_devs()} developers!")
# print(f"Manager {man2}, has {man2.show_devs()} developers!")

# man1.add_devs(dev3)
# man2.add_devs(dev3)
# man2.add_devs(dev4)

# dev3.give_increase()
# dev4.give_increase()
# man2.give_increase()

# print("After")
# print(f"Manager {man1}, has {man1.show_devs()} developers!")
# print(f"Manager {man2}, has {man2.show_devs()} developers!")
