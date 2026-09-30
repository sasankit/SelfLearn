# Started at 18:18 on 26.09.2026

# import math as m
# print(m.ceil(2.9))
# print(m.floor(2.9))



# is_hot  = True
# is_cold = True

# if is_hot:
#     print("It's a hot day, drink plenty of water")
# elif is_cold:
#     print("Its a cold day, wear warm clothes")
# else:
#     print("Its a lovely day, enjoy")


 #Exercise:  price of house is 1million, if the buyer has good credit , they put down only 10% else 20%

# good_credit = False
# cost = 1000000

# if good_credit:
#     downpayment = int(cost * 0.10)
#     print(f"Your downpayment is {downpayment} $")
# else:
#     downpayment = int(cost * 0.20)
#     print("Your downpayment is {} $".format(downpayment))


#Comparison Operators

# temp = 16
# if temp >= 30:
#     print("its a hot day")
# elif temp >=15 and temp <= 29:
#     print("its a good day")
# else:
#     print("its a cold day")

#Exercise: if name is less than 3 characters long, name must be atleast 3 characters otherwise if its more than 50 characters long, then name can be max of 50 characters, otherwise name looks good

# min = 3
# max = 50
# name = input("Enter your name: ")
# if len(name) < min:
#     print (f"Name should be atleast 3 characters")
# elif len(name) > max:
#     print("Name should be max of 50 characters")
# else:
#     print("Name looks good")

#Exercise: Weight Converter, if user give weight in Kg,convert it to Lb, ask user first and then give the output

# user_input = float(input("Enter your weight: "))
# option = input("Press (K) for Kg or (L) for Lbs: ").lower()

# if option == "k":
#     convert = round(user_input * 2.20,1)
#     print(f"Your weight is {convert} pound. ")
# elif option == "l":
#     convert = round(user_input / 2.20,1)
#     print(f"Your weight is {convert} Kg ")
# else:
#     print("Invalid Input !!!")


# While Loop: Runs until you add a condition to stop.

# i = 1
# while i < 5:
#     print(i)
#     i += 1
# print("done")


#Exercise: Build a guess game, you have 3 chances if you guessed it right, you win else you lose:

# secret_num = 8
# total_chance = 3
# start = 1

# while start <= total_chance:
#     guess = int(input("Guess the number: "))
#     start += 1    

#     if guess == secret_num:
#         print("Congratulations, you guessed it right, you win") 
#         break
# else:
#     print("Try again !!!")


#Exercise: Build a car game:
# when Help is entered, we give this output, 
# Start - to start the car
# stop: to stop the car
# quit - to exit

# is_started = False

# print("Type 'help' for options !!! ")

# while True:
#     user_input = input("Enter to begin, press help for more info.. ").lower()

#     if user_input == "help" or user_input == "h":
#         print(
#             """
#             Start - to start the car
#             Stop - to stop the car
#             quit - to quit the game
#             """
#             )
#     elif user_input == "start" or user_input == "s":
#         if is_started:
#             print("Car has already Started !!!")
#         else: 
#             is_started = True
#             print("Car started...ready to go")

#     elif user_input == "stop":
#         if not is_started:
#             print("Car is already Stopped...") 
#         else:
#             is_started = False
#             print("Car stopped...")

#     elif user_input == "quit" or user_input == "q":
#         print("Exiting game..")
#         break
# else:
#     print("I dont understand, press 'help' for options")   
    
#Explanation:Game Launches: is_started = False (Car is off).
# Player types "start":Program checks: 
# Is is_started True? -> No, it's False.
# It goes to the else block: changes is_started = True and prints "Car started... ready to go!".

# Player types "start" again:
# Program checks: Is is_started True? -> Yes, it's True.
# It prints: "Car is already started!" (preventing duplicate starts).

# Player types "stop":
# Program checks: Is not is_started True? -> Since is_started is currently True, not is_started evaluates to False.

# Because the if condition is False, it drops into the else block: changes is_started = False and prints "Car stopped.".
# Player types "stop" again:
# Program checks: Is not is_started True? $\rightarrow$ Since is_started is now False, not False evaluates to True.
# It enters the if block and prints: "Car is already stopped!".


# is_started = False

# while True:
#     user = input("press start to begin...").lower()

#     if user == "start":
#         if is_started:
#             print("car has already started")
#         else:
#             is_started = True
#             print("car has started")

#     elif user == "stop":
#         if is_started:
#             is_started = False
#             print("car has stopped")
#         else:
#             print("Car has already stopped")
#     elif user == "quit":
#         print("exit")
#         break
# else:
#     print("Invalid")






#***********************************
#For Loop

# item = [1,2,3]
# for i in item:
#     print(i)

# for i in range(5,10): #using range function 
#     print(i)

# total = 0
# prices = [10,20,30]
# for price in prices:
#     total += price
# print(total)

# Nested Loops

# for x in range(4):
#     for y in range(3):
#         print(f"{x}, {y}")

#Exercise: print the following
# *****
# **
# *****
# **
# **

num = [5,2,5,2,2]
# for i in num:
#     print(i * "*")

# for i in num:
#     output = ""
#     for j in range(i):
#         output += "x"
#     print(output)


