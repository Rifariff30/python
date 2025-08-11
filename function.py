# def greet_user(name,age):
#     print(f"Hello, {name},! Welcome to the program. i know your is {age} year old")

# greet_user("Aisha",20)


# def add(a, b):
#     print(a + b)
# add(2, 3)


# def add(a, b):
#     return a + b
# i = add(3, 6)
# print(i) 
# print(i+3)
# print(i*3)

# higher order function

# def greet_user(name,msg="good morning"):
#      print(f"{msg}, {name}!")
# greet_user("john")

# def add(a,b):
#     """this function add two numbers"""
#     return a + b
# print(add.__doc__)

# add=lambda a,b: a + b
# print(add(3,5))

# map

# numbers=[1,2,3,4,5,6]
# squared=map(lambda x:x**2,numbers)
# print(list(squared))

# filter

# numbers=[1,2,3,4,5,6]
# even_num=filter(lambda x:x%2==0,numbers)
# print(list(even_num))

# reduce

from functools import reduce

numbers = [1, 2, 3, 4]
sum_num = reduce(lambda x, y: x + y, numbers)
print(sum_num)

