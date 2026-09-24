# List, Tuple and Sets

courses = ["Math","Comp","History"]
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

#Tuple - Ordered and immutable (cannot be changed)

# tuple = (1,2,5,6)
# tuple1 = tuple

# tuple[0] = (5)
# print(tuple)

# Lists are mutable.
# courses1 = courses
# print(courses1)
# courses1[2] = "Science"
# print(courses1)


#Sets - Unordered and no duplicates allowed

courses1 = {"History" ,"Comp","Math","History"}

courses2 = {"History" ,"Comp","Math","History", "Physics"}

#intersection : common item in 2 set, 
# difference : difference in one set vs other,
# union : combine 2 sets

print(courses1.intersection(courses2))
print(courses1.difference(courses2))
print(courses1.union(courses2))