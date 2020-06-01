nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []
# for n in nums:
# my_list.append(n*n)
# print(my_list)

#my_list = [n*n for n in nums]
# print(my_list)S

# using a map and lambda

#my_list = map(lambda n: n*n, nums)
# print(my_lmy)

#my_list = []
# for n in nums:
#    if n % 2 == 0:
#        my_list.append(n)
# print(my_list)

#my_list = [n for n in nums if n % 2 == 0]

# print(my_list)


#my_list = filter(lambda n: n % 2 == 0, nums)
# print(list(my_list))

#my_list = []
# for letter in 'abcd':
#   for number in range(4):
#       my_list.append((letter, number))
# print(my_list)


#my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
#print(my_list, my_list)

names = ['bruce', 'clark', 'peter', 'logan', 'wade']
heros = ['batman', 'superman', 'spiderman', 'wolverine', 'deadpool']

#my_dicr = {}
# for name, hero in zip(names, heros):
#   my_dicr[name] = hero
# print(my_dicr)

#my_dict = {name: hero for name, hero in zip(names, heros) if name != 'peter'}
# print(my_dict)
#sets in python
#nums = [1, 1, 2, 1, 3, 4, 3, 4, 3, 4, 5, 5, 6, 7, 6, 8, 9, 9, 5, 4]
#my_set = set()
# for n in nums:
#    my_set.add(n)
# print(my_set)

#my_set = {n for n in nums}

# print(my_set)

# Generator Expession


# def gen_function(nums):
#   for n in nums:
#       yield n


#my_gen = gen_function(nums)

# for i in my_gen:
# print(i)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
