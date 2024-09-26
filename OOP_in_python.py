# class Car:
#     color = "Yellow"
#     brand = "Ferrari"

# car1 = Car()
# print(f"Car's color is : {car1.color}")
# print(f"Brand I love is: {car1.brand}")

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("shrawan", 97)
# print(s1.name, s1.marks)

# s2 = Student("karan", 98)
# print(s2.name, s2.marks)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def cal_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hello ", self.name, "your average marks is: ", sum/3)

# s1 = Student("Leo Messi", [78,89,99])
# s1.cal_avg()



# class Bachelor:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     #we can use static method like this without using self
#     @staticmethod    #Decorator
#     def greet():
#         print("hello")
#     # Now it wont show any error if we do not use self.

#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(f"Hello {self.name}, your average marks is ", sum/3)

# s1 = Bachelor("shrawan", [78,34,65])
# s1.avg_marks()
# s1.greet()


#-------------------------------------------------------------------------------------------------------------------


# Simple example of Inheritance:
# class PremierLeague:
#     @staticmethod
#     def start():
#         print("Premier League has now started")
    
#     @staticmethod
#     def end():
#         print("Premier League has now ended Successfully")


# class Game(PremierLeague):
#     def __init__(self, clubname):
#         self.clubname = clubname

# class Players(Game):                    #Example of Multi level inheritance
#     def __init__(self, namee, JNumber):
#         self.namee = namee
#         self.JNumber = JNumber

# player1 = Players("shrawan", "10")
# player1.start()
# player1.end()
# print(player1.namee, player1.JNumber)


#Multiple Inheritance Example:

# class A:
#     varA = "Welcome to Class A"

# class B:
#     varB = "Welcome to Class B"

# class C(A, B):
#     varC = "Welcome to Class C"

# var1 = C()
# print(var1.varC)
# print(var1.varB)
# print(var1.varA)

#Example how super() method is used: it is used to access method of the parent class.

# class Car:
#     def __init__(self, type):
#         self.type =type

#     @staticmethod
#     def start():
#         print("Car has started...")

#     @staticmethod
#     def stop():
#         print("Car has stopped...")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         super().start()
#         self.name = name
        


# car1 = ToyotaCar("shrawan", "electric")
# print(car1.type)


#Example for class method
# class Person:
#     name = "annonymous"

#     @classmethod        #Decorator
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("shrawan jaiswal")
# print(p1.name)
# print(p1.name)


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = (phy + chem + math)/3

    @property     #this decorator will take the latest values of the subject if updated later on.
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
    

stu1 = Student(98, 78, 88)
print(stu1.percentage)

stu1.phy =72     #if we donot use property decorator here then the value we updated here won't get updated to calculate %
print(stu1.percentage)

stu1.math = 45
print(stu1.percentage)

