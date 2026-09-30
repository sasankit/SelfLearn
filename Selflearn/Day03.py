# List, Tuple and Sets

# courses = ["Math","Comp","History"]
# print(courses)
# print(courses[0])

# #for last item
# print(courses[-1])

# #index error: when there is no item for that index
# print(courses[5])
# output: IndexError: list index out of range

#List Methods
#Functions inside an object is called method

# Append method
# add item to our list

# courses.append("Art")
# print(courses)

# #Insert 
# # to add item with the index

# courses.insert(0,"Science") #this will come to the first
# print(courses)

#Extend - to add multiple value to our list

# courses_1 = ["courses1"]
# courses.extend(courses_1)
# print(courses)

# #remove - remove an item
# courses.remove('Math')
# print(courses)

# #pop - this will remove as well but will remove the last value

# courses.pop()
# print(courses)
# courses.sort()
# num = [1,5,6,4,8]
# sorted_num = num.sort(reverse=True)
# print(courses)
# print(num)
# print(type(sorted_num))

#Find the index of certain item, use index method
# print(courses.index('Math'))

#Exercise:
# From the list find the largest number

# numbers = [3,6,2,8,4,10]
# max_num = 0

# for i in numbers:
#     if i > max_num:
#         max_num = i
# print(max_num)

# # one step further:
# # ask input from user, store in a list, give the largest number from their input

# num_store = []

# for i in range(5):
#     num = int(input("Enter 5 numbers: "))
#     num_store.append(num)

# maximum = num_store[0]

# for number in num_store:
#     if number > maximum:
#         maximum = number
# print(maximum)


# WAP to remove duplicates from a list

# items = ["mango","apple","banana","apple"]
# print(unique_items)
# dups = []
# for item in items:
#     if item not in dups:
#             dups.append(item)

# print(dups) 
# items = ["mango","apple","banana","apple"]
# unique_items = list(dict.fromkeys(items)) #dict.fromkeys() is used to remove duplicates and its fast.

# a = [1,2,3]
# b = a # b is an instance of a, whatevery you update in b is also gets updated in a
# print(b)
# b.append(4)
# print(a)


#Tuple - Ordered and immutable (cannot be changed)

# tuple = (1,2,5,6)
# tuple1 = tuple

# tuple[0] = 5
# print(tuple)

# Lists are mutable.
# courses1 = courses
# print(courses1)
# courses1[2] = "Science"
# print(courses1)

#Unpacking, # storing value to a variable
# Can be used with Lists and Tuple

# a, b, c = [1,2,3]
# print(a)
# print(b)
# print(c)

#Sets - Unordered and no duplicates allowed

# courses1 = {"History" ,"Comp","Math","History"}

# courses2 = {"History" ,"Comp","Math","History", "Physics"}

# #intersection : common item in 2 set, 
# # difference : difference in one set vs other,
# # union : combine 2 sets

# print(courses1.intersection(courses2))
# print(courses1.difference(courses2))
# print(courses1.union(courses2))

#Dictionaries:
# Key Value Pairs


# WAP to give you the character when you type a number
# if input is 1234. output should be one two three four

# phone = {

# "1":"one",
# "2": "two",
# "3": "three",
# "4": "four"
# }

# # userinput = input("Enter your phone: ")
# # output = ""
# # for i in userinput:
# #     output += phone.get(i,"!") + " "

# # print(output)


# # Emoji Converter

# emoji = {
# ":)" : "😊",
# ":D" : "😁",
# "<3" : "❤️"

# }

# msg = input("Enter your message: ")
# response = ""
# separate = msg.split()
# for item in separate:
#     response += emoji.get(item,item) + " "
# print(response)
    

# ch = "mississippi"
# count = {}
# for i in ch:
#   count[i] = count.get(i,0) + 1
# repeat = max(count, key=count.get)
# print(count)
# print(repeat)    

# original = {"a": 1, "b": 2, "c": 1}
# inverted = {}

# for key, value in original.items():
#   print(key, value)


# #without using .items()
#   for key in original:
#     value = original[key]
#     print(key,value)

# Reverse string
# name = input("Enter your name: ")

# reverse_name = ""
# for names in name:
#     reverse_name = names + reverse_name
# print(reverse_name)