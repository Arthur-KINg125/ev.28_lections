# zip(iterables) - она соединяет каждый элемент иртерируемых объектов между собой в тип данных tuple и возварщает итератор

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = dict(zip(ls2, ls1))
# print(res)

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [10, 20, 30]

# res = list(zip(ls1, ls2, ls3))
# print(res)

# #  zip - для создания словарей
# d_keys = ['hostname', 'locations', 'vendor', 'model', 'IP']
# data = {
#     'oktobr':['bish_okt', 'Gorkaya 212', 'Vefa', 'Cisco', '10.255.0.12'],
#     'cvrdl':['bish_svrdl', 'Gorkaya 212', 'Vefa', 'Cisco', '10.255.10.12'],
#     '1may':['bish_1may', 'Gorkaya 212', 'Vefa', 'Cisco', '10.25.105.12']
# }
# bishkek_data = {}

# for k in data:
#     bishkek_data[k] = dict(zip(d_keys, data[k]))

# print(bishkek_data)

#====================================================================
# all(), any()

# all (iterable) - Возвращает True, если все элементы итерируемого объекта истина, иначе False.

# ls = [5, 6, 7]
# print(all(ls))

# ip = '10.255.0.155'

# ip1 = '10.255.0y.202'

# res = all(x.isdigit() for x in ip1.split('.'))
# print(res)

# any - Возвращает Тру, если хотябы один элемент истина

# ls = [1, 3, [1,2], 0]
# print(any(ls))

# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']
# command = input('Vvedite command: ')

# if any(x in command for x in ignore):
#     raise Exception('Block you!')
# print('Ok!')


# # ------------------------------------------
# from random import choices
# from string import ascii_letters, digits, punctuation
# from itertools import repeat

# symbols = '_()+-@!#%'
# q_pass = int(input('Vvedite kol-vo paroley: '))

# res = [
#     f(choices(ascii_letters, k=15), choices(digits, k=6), choices(symbols, k=2))
#     for f in repeat(lambda x, y, z: ''.join(set((x+y+z))), q_pass)
# ]
# print(res)
# print(f'Quantity of password: {len(res)}')

# from statistics import mean

# print(f'Average len of passwords: {mean(len(x) for x in res)}')


