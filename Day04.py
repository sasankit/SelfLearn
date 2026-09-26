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

secret_num = 8
total_chance = 3
start = 1

while start <= total_chance:
    guess = int(input("Guess the number: "))
    start += 1    

    if guess == secret_num:
        print("Congratulations, you guessed it right, you win") 
        break
else:
    print("Try again !!!")
    
