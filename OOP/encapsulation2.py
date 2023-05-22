# # Анатация свойств(@property(getter, setter))

# class Person:
#     __name = 'John'
#     __age = 22
#     __code = '996'
#     __number = '555666777'
#     __full_number = __code + __number

#     @property
#     def name(self):
#         '''The name property(getter)'''
#         print(self.__name)
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             print('Invalid value for name!')
#         else:
#             print('Setter', value)
#             self.__name = value

#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value not in range(0, 150):
#             print('Invalid Values')
#         else:
#             self.__age = value 
#     @property
#     def number(self):
#         name = input('Vvedite svoye imya: ')
#         if self.__name.lower().strip() == name:
#             print('Invalid name!')
#         else:
#             print(self.__full_number)

#     @number.setter
#     def number(self, value: dict):
#         '''Value muxt be dict, first pair code , second pair number'''
#         if value['code'] != '+996':
#             print('Number changed from Kyrgyzstan number!')
#         elif len(value['number']) != 9:
#             print('Number changed from Kyrgyzstan number!')
#         self.__code = ['code']
#         self.__number = value['number']
#         self.__full_number = self.__code + self.__number



# obj = Person()
# obj.name
# obj.name = 'Jamie'
# obj.name
# obj.age
# obj.age = 30
# obj.age
# obj.number
# obj.number = {'code': '+7', 'number': '777999888'}
# obj.number


# -------------------------------------------------
# read - write - delete (radius)

# class Circle:
#     def __init__(self, radius) -> None:
#         self._radius = radius

#     def _get_radius(self):
#         print('getter, _get_radius')
#         return self._radius
    
#     def _set_radius(self, value):
#         print('setter, _set_radius')
#         if not isinstance(value, (int, float)):
#             raise ValueError('radius must b ean int or float objject!')
#         self._radius = value

#     def _del_radius(self):
#         print('deleted')
#         answer = input('Are you sure to delete radius yes/no?')
#         if answer.lower().strip() == 'yes':
#             del self._radius
#             print('Deleted')
#         else:
#             print('Not deleted!')

#     radius = property(fget=_get_radius, fset=_set_radius, fdel=_del_radius, doc='The radius property')

# obj = Circle(5)
# print(obj.radius)
# obj.radius = 7.5
# print(obj.radius)
# del obj.radius
# print(obj.radius)

#-------------------------
# read - only

# class CoordinateWriteError(Exception):
#     pass


# class Point:
#     def __inti__(self, x, y) -> None:
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         print(self.__x)

#     @property
#     def y(self):
#         print(self.__y)

#     @x.setter
#     def x(self, value):
#         raise CoordinateWriteError('x coordinate is read-only field!')
    
#     @y.setter
#     def x(self, value):
#         raise CoordinateWriteError('y coordinate is read-only field!')
    





# ------------------
# write - only
# import hashlib
# import os

# class User:
#     def __init__(self, username, password) -> None:
#         self.username = username
#         self.password = password

#     @property
#     def password(self):
#         raise ArithmeticError('password field is write-only!')

#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise ValueError('invalid value for password')
#         salt = os.urandom(32)
#         self._hashed_password = hashlib.pbkdf2_hmac('sha256', value.encode('utf-8'), salt, 100_000)

# john = User ('John Snow', 'secretkey')
# # print(john.password)
# john.password = 'johnthebest'
# print(john._hashed_password)
