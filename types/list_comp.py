# list comprehenshions - генераторы списков

# list comprehensions - упрощенный подход к созданию списков, который задействует в себе цикл for
# , а также конструкция if для определения того, что в итоге попадает в нащ список

# list -> 0 - 200 -> % 2 == 0

# ls = []
# for x in range(0, 201):
#     if x % 2 == 0:
#         ls.append(x)

# ls = [x for x in range(0, 201) if x % 2 != 0]
# print(ls)

# lst: 0 - 300 -> num% 2 == 0, num % 3 == 0
# ls = []
# for x in range(0, 301):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
#         print(ls)

# ls = [i for i in range(0, 301)if i % 2 == 0 and i % 3 == 0]
# print(ls)

# list: 0 - 100 -> x % 2 == 0: x 2, i % 3 == 0: x ** 3

# ls = []
# for x in range eeeeeeeeeeeee

# ls = []
# for x in range(0, 101):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     elif x % 3 == 0:

# print(ls)
# print(5 if input() == 'yes' else 7)
# ls = [x for x in range(0,101) if x % 2 == 0 or x % 3 == 0]
# print(ls)

#................................................
# newlist - [experssion for item in itarable <if congiyiom == True> 

# ls = [str(i * 2) for i in range(0,11)]
# print(ls)

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# # result = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# res = []
# for x in ls:
#     for item in x:
#         res.append(item)

# print(res)

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# res = [item for x in ls for item in x]
# print(res)
# ----------------------------------------------------------

# from datetime import datetime

# start = datetime.now()
# ls = [x for x in range(0,1_000_000_000)]
# # ls = []
# # for x in range(0, 100_000_000):
# #     ls.append(x)
# finish = datetime.now()
# print(finish - start)

# set compehensions
# set_ ={x for  x in range(1, 100)}
# print(set_, type(set_))
# set1 = [1,2,3,4, 'a', True]
# print(set1)

#---------------------------------------
# dict comprehenshions
# dict = {
#     key:Value,
#     key:value
# }

# dict_ = {x: x ** 2 for x in range(0, 16)}
# print(dict_)

# names = ['John', 'Tirion', 'Eygan', 'Sansa', 'Ramsi']
# dict_ = {x: len(x) for x in names }
# print(dict_)

# ------------------------------------------

# new_dict = {}
# for k, v in dict1.items():
#     for inner_key, inner_value in v.items():
#         if max(v.values()) == inner_value:
#             new_dict[k] = inner_key
# print(dict1)
# print(new_dict)

# res = {key: inner_key for key, value in dict1.items() for inner_key, inner_value in value.items() if inner_value == max(value.values())}
# print(res)

dict1 = {
    'Soke': {'history': 99, 'fizik': 95, 'math': 94},
    'Omoke': {'history': 84, 'math': 75, 'fizik': 68},
    'John': {'history': 100, 'math': 90, 'math': 87}, 
}

res = {}

for k, v in dict1.items():
    for key_inner, value_inner in v.items():
        max(v.values()) == value_inner

print(value_inner)

