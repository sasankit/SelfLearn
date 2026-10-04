# Classes are the blueprint to create the objects

class Robot: #class name should always be capital
    def __init__(self, name, color, weight): #initializing a constructor self should always be the first parameter
        self.name = name #best practice is to match the parameter and the attribute name
        self.color = color
        self.weight = weight

    def introduce(self): #methods inside class, methods.
        print("Hello, I am {}, I am of {} color and I weigh {} kg".format(self.name,self.color,self.weight)) #what this introduce function does



#we are creating variable for the robot class
r1 = Robot("Tom","red",30) #pass the name, color , weight, positional argument

r1.introduce() #calling the function with r1 variable.


class Person:
    def __init__(self, n, p, i):
        self.n = n
        self.p = p
        self.i = i

    def standup(self):
        self.is_sitting = False
        print(f"{self.n} stood up")

    def sitdown(self):
        self.is_sitting = True
        print("{} sat down".format(self.n))


p1 = Person("Alice","talkative",False) #Creating an object p1 with the class Person
p2 = Person("Tina","aggresive", True) #Creating an object p2 with the class Person


p1.robot_owned = r1 #defining new attribute to class Person.

p1.sitdown() #calling the sitdown method
p1.robot_owned.introduce() #calling the introduce method from class Robot
p2.standup() #calling the standup method for object p2



class Phone:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def feature(self):
        print(f"your model is {self.model} and the color is {self.color}")


phone1 = Phone("Samsung","S26 Ultra", "Blue")

Phone.feature(phone1)


