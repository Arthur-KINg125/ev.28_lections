# # Множественное наследование - это когда класс наследуется от двух или более классов

# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing')

#     def ride(self):
#         print('We\'re riding on the ground')


# class Plane:
#     def play_music_at_station(self):
#         print('Listening Ed Sheeran!')

# #     def fly(self):
# #         print('We\'re flying!')



# # class FutureAuto(Auto, Plane):
# #     pass 

# # obj = FutureAuto()
# # obj.ride()
# # obj.fly()
# # obj.play_music_at_station()
 
# #-------------------------------------
# Проблема ромба - когда поиск шел в родительский класс прежде чем искать у соседнего общего потомка (рещена с помощю MRO)
# MRO - механизм для корректного поиска родительских методов. Был создан для решения проблемы ромба, которая появилась после введения object в пайтон. Поиск идет таким образом что если у родительских классов есть общий предок, то идет поиск в ширину


# class Zero:
#     def say(self):
#         print('class Zero')

# class First(Zero):
# #     def say(self):
# #         print('class First')

# # class Second(Zero):
# #     def say(self):
# #         print('class Second')

# # class MyClass(First, Second):
# #     def say(self):
# #         super().say()
# #         print('class MyClass')

# # obj = MyClass()
# # obj.say()

# # print(MyClass.mro())


# class Z:
#     pass

# class Y:
#     pass

# class A(Z):
#     pass

# class B(Y):
#     pass

# class X(A, B): # 1
#     pass

# print(X.mro())


# Проблема перекрестного наследования 

# class Y:
#     pass

# class X:
#     pass

# class A(X, Y):
#     pass

# class B(Y, X):
#     pass

# class MyMro(type):
#     def mro(cls) -> list[type]:
#         return [cls, A, B, X, Y, object]
    
# class MyClass(A, B):
#     pass


# print(MyClass.mro())

