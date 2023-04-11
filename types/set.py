# Set() - Множества
# 'Это изменяемый, неупорядочный, итерируемый, неиндексируемый тип данных'

# Множества хранят в себе неизменяемые  типы данных

# a = ['febw']
# print(hash(a))

# # 1 -> set()
# a = set([1, 2, 3, 4])
# print(a)

# a = set({1:2, 3:4})
# print(a)
# set2 = {1, 2, 4}
# print(set2)

# set1 = {1,2,2,2,2,2,3}
# print(set1)

# frozenset - неизменяемое множество
# a = frozenset([1, 2, 3, 4, 5])
# a.add(7)
# print(a)


# set1 = {0,}
# print(type(set1))

# set1 = {1, 0, True, False}
# print(set1)

# a = 0 
# print(bool(a))

# Методы SET


# add -> для добавления 

# set1 ={1, 2, 3}
# set1.add(4)
# print(set1)
# set1.add((1,2,3,4,5))
# set1.add((1,2,3,4,5))
# print(set1)

# update - он может добавлять но не повторяя имеющееся добавляет все итрируемые 

# set1.update({3 : '1', 4:'5'})
# # print(set1)
# set1.update('string', {1, 2, 3, 4, 5, 6, 7})
# print(set1)

# set1.update([1,2,3,4,5,6])
# print(set1)

# Удаление в set 
# clear - очищает все множества 
# remove(element) - удаляет элемент если его нету нету выдает ошибку
# discard - Если элемента нету ничего не происходит
# pop () - удаляет из set (FIFO) first in first out

# set1 = {1,2,3,4,5}
# set1.remove(2)
# set1.clear()
# set1.discard(5)
# print(set1.pop())
# print(set1)

# # difference - выводит отличия
# set1 = {1,2,3,4}
# set2  = {2,3,5,7}
# print(set1.difference(set2))
# print(set2.difference(set1))

# a = set1.symmetric_difference(set2)
# print(a)
# print(set1^set2)

# print(set1.intersection(set2))
# print(set1 & set2)

# print(set1.union(set2))
# print(set1 | set2)


# set1 =  {1,2,3,4,5}
# set2 = {4,5,6,7}
# print(set1.difference(set2))

# num = list(input())
# print(len(num) == len(set(num)))


# tuple - неизменяемый, индексируемый, итрируемый, упорядочный тип данных.
# index(element) - возвращает индекс этого элемента в кортеж
# литералы() 
# a = (True, 'a', 1, 1, 2, 1)
# print(a, type(a)) 
# b = tuple()
# print(a.index(True))
# # count(element) - возвращает число вхождений этого элемента в кортеж 
# # print(a.count(1))
