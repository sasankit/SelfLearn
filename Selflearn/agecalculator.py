# import datetime


# def agecalculator():
#         while True:
#             try:
#                 birthyear = int(input("Enter your birth year: "))
#                 currentyear = datetime.date.today().year
#                 agecalc = currentyear - birthyear
#                 return agecalc
#             except ValueError:
#                 print("Enter only year like 1999, 2000 !!!")
#             finally:
#                 print("Thank you !!!")


# age = agecalculator()
# print(age)


# Using tkinter to create a window app

import datetime
import tkinter as tk

def calculate_age():
    try:
        birthyear = int(entry.get())
        currentyear = datetime.date.today().year
        age = currentyear - birthyear
        result_label.config(text=f"Your age is: {age}")
    except ValueError:
        result_label.config(text="Please enter a valid year like 1999 or 2000")

# Window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("300x200")

# Input label
label = tk.Label(window, text="Enter your birth year:")
label.pack()

# Input box
entry = tk.Entry(window)
entry.pack()

# Button
button = tk.Button(window, text="Calculate Age", command=calculate_age)
button.pack()

# Result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the app
window.mainloop()






