from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):

#     @abstractmethod
#     def voice(self):
#         ...

#     @abstractproperty
#     def legs(self):
#         ...

# class Dog(AbstractAnimal):
#     ...

# # obj = Dog() # Error

# class Dog(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('гав-гав')

# obj = Dog() # Type Error
# obj.voice()
# print(obj.legs)

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        ...

class Square(Shape):
    def __init__(self, length):
        super().__init__('Square')
        self.length = length
    
    def area(self):
        return self.length ** 2
    
obj = Square(12)
print(obj.area())
print(obj.name)


