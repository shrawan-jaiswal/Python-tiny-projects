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


# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = (phy + chem + math)/3

#     @property     #this decorator will take the latest values of the subject if updated later on.
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"
    

# stu1 = Student(98, 78, 88)
# print(stu1.percentage)

# stu1.phy =72     #if we donot use property decorator here then the value we updated here won't get updated to calculate %
# print(stu1.percentage)

# stu1.math = 45
# print(stu1.percentage)


# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumadd(self):
#         print(self.real, "i + ", self.img, "j")

#     def showNumsub(self):
#         print(self.real, "i - ", self.img, "j")

#     def __add__(self, cmplx ):         #Example of dunder function for addition
#         newReal = self.real + cmplx.real
#         newImg = self.img + cmplx.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, cmplx ):       #Example of dunder function for substraction
#         newReal = self.real - cmplx.real
#         newImg = self.img - cmplx.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(5, 9)
# num2 = Complex(3, 4)
# num1.showNumadd()
# num2.showNumsub()
# num3 = num1 + num2
# print("Addition")
# num3.showNumadd()

# num4 = num1 - num2
# print("substraction")
# num4.showNumsub()


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 *(22/7)* self.radius
    
# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())


# class Employee:
#     name = "Shrawan Jaiyswal"
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role: ", self.role)
#         print("dept: ", self.dept)
#         print("salary: ", self.salary)


# e1 = Employee("CyberSecurity Analyst", "IT department", "$20000")
# print(Employee.name)
# print(e1.showDetails())

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "Engineering and IT", "$1200") #here we used super method to access methods of the parent class.

# eng = Engineer("Elon Musk", 50)
# eng.showDetails()


# class Order:
#     def __init__(self, item, price):
#         self.item = item 
#         self.price = price

#     def __gt__(self,dndrfn):
#         return self.price > dndrfn.price
    
# odr1 = Order('chip', 20)
# odr2 = Order('tea', 150)

# print(odr1 > odr2)

# Example of Encapsulation:
# class Car:
#     def __init__(self, brand, model):
#         self._brand = brand
#         self.__model = model

# car1 = Car("Tesla", "Model 3")
# print(car1._brand)
# print(car1.__model)


#Example of Polymorphism

# class Bird:
#     def sound(self):
#         print("Bird chirps")

# class Dog:
#     def sound(self):
#         print("Dog barks")

# def make_sound(animal):
#         animal.sound()

# bird = Bird()
# dog = Dog()

# make_sound(bird)
# make_sound(dog)


# class Barcelona:
#     def jersey(self):
#         print("Jersey number at Barca is 10")

# class Psg:
#     def jersey(self):
#         print("Jersey number at PSG is 30")

# def sel_jersey(jerseey):
#     jerseey.jersey()

# barca = Barcelona()
# psg = Psg()

# barca.jersey()
# psg.jersey()


#simple example of method overriding.
# class Parent:
#     def display(self):
#         print("This is parent class")

# class Child(Parent):
#     def display(self):
#         print("This is child class")   #Override the parent method


# overRide = Child()
# overRide.display()

#Simple example of method overloading
# class Math:
#     def add(self, a, b, c = None):
#         if c is not None:
#             return a + b + c
#         else:
#             return a + b
        
# math = Math()
# print(math.add(3,7))
# print(math.add(3,7,9))


    


