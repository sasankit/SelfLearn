#Functions in Python

# BMI Calculator

# def bmi_calculator(name, height_m, weight_kg):
#     bmi = weight_kg / (height_m ** 2)
#     print(f"Your BMI is: {bmi}")
#     if bmi < 25:
#         print(f"Mr/Ms {name}, you are not overweight")
#     else:
#         print(f"Mr/Ms {name}, you are overweight")



# name1 = "abc"
# height_m1 = 1.79
# weight_kg1 = 83

# bmi_calculator(name1,height_m1,weight_kg1)

#Error handling in Python: 
# try , except, finally

# try:
#     num1 = int(input("Enter a number: "))
#     print(1/num1)
# except ZeroDivisionError:
#     print("Enter number above zero")
# except ValueError:
#     print("Enter only number")


# standard practice for positional argument and keyword arguments
# *args and **kwargs

# def student(*args, **kwargs):
#     print(args)
#     print(kwargs)


# student(["hello" , "how are you"], name = "tom")

# courses = ["Math","Science"]
# detail = {
# 'name' : 'Tom',
# 'age' : 20

# }

# student(*courses,**detail)

