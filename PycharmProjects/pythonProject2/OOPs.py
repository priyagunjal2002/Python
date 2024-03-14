"""class student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self. marks = marks

    def talk(self):
        print("name is:", self.name)
        print("rollno is:", self.rollno)
        print("marks:", self.marks)
#Creating an instance of the student class
s = student("Riya", 2, 80)
s1 = student("Ritesh", 5, 84)
# calling the talk method
s.talk()
s1.talk()"""
import code

"""
#self  variable:
self is the default variable which is always pointing
to current Object.

by using self we can access instance Variable and
instance methods of object.

Notes:
1. self should be first parameter inside construtor
def__init__(self)
2.self should be first para. inside instance methods
def talk(self):

## Consturctor Concept
- constructor is a special method in python
- the name of  constructor should be __init__(self)
- constructor will be executed  automatically at time of
object creation
- the main purpose of constructor is to declare and initialize
instance variables
-per objcet constructor will be executed only once,
- constructor can take atleast one argu.
- constructor is optional & if we are not providing
any constructor then python will provide default constructor."""

"""
class Student:
    def __init__(self, name, rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("student name :{}\nrollno:{}\nmarks:{}".format(self.name, self.rollno,self.marks))

s1=Student("Priya",3,85)
s1.display()
s2=Student("Snehal",6,86)
s2.display()"""

"""
Methods:
1. name of the methods can be any name 
2. method will be executed if we call that method
3. per object , method can be called any number of times
4. inside method we can write business logic.


Constructor
1.Constructor name should be always __ init__
2. construtor will be executed automatically a the time 
of object creation
3.per objcet constructor will be executed only once.


types Of Varibles:
instance 
static
local variables."""

"""
class student:
    def __init__(self):
        self.name="Arya"
        self.age=13
        self.marks=75
    def talk(self):
        print("Name Is : ", self.name)
        print("Age Is : ", self.age)
        print("marks Is : ", self.marks)

arya = student()
arya.talk()"""
"""
# Type of variable
1.instance (Object level)
2.static(Class level)
3.local(method level)

Instance :if the value of a variable is varied from
object to object then such type of of variable are called


1.inside constructor by using self variable.
2. inside instance methos by using self variable.
3.Outside of the class by using object refernce variable.

1.inside constructor by using self variable:

 we can declare instance variable inside a constructor
by using self keyword"""

"""
#Ex:
class Employee:
    def __init__(self):
        self.eno=100
        self.ename="Nikita"
        self.esal=25000
# creayte instance
e= Employee()

# printing Attributes
print(e.__dict__)"""
"""
#2.inside instance method by using self variable.

class Test:
    def __init__(self):
        self.a=20
        self.b=50
    def m1(self):
        self.c =30
## Instance of the Test class
t=Test()

t.m1()

print(t.__dict__)"""
"""
#3.Outside of the class by using object refernce
# variable.

class Test:
    def __init__(self):
        self.a=20
        self.b=50
    def m1(self):
        self.c =30
## Instance of the Test class
t=Test()
# call the instance
t.m1()

# add new Attribute  d
t.d=60

print(t.__dict__)"""
"""
# How to access Instance Variables:
class Test:
    def __init__(self):
        self.a = 20
        self.b = 50

    def display(self):
        print(self.a)
        print(self.b)

t=Test()
t.display()
print(t.a,t.b)"""
"""
#delete instance variable from the object
syntax: with in the class
del self.variableName
2.outside of class we can delete instance

class Test:
    def __init__(self):
        self.a=20
        self.b=30
        self.c=40
        self.d=50
t1 =Test()
t2= Test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)"""

"""
class Test:
    def __init__(self):
        self.a=20
        self.b=30
t2=Test()
t1=Test()
t2.a=888
t2.b=899

print("t1: ",t1.a,t1.b)
print("t2: ",t2.a,t2.b)"""

# -------------------------------------------------------------------------------------
"""
## Static  Variable :
if the value of a variable is not varied  from object to object such type of variable we
have to declare with in the class ditrectly but ouside of method.such type of variable are
called as Static   variables.

- we can access statics variable either by class name or by object reference.
-But recommended to use class name
 """

"""
Instance variable vs static variables
Note
In the case of instance variable for every object a separate copy wii be created , but
in the case of static variable for total class only one copy will be created and shared by 
every object of  that class.


class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
print('t1:',t1.x,t1.y)
Test.x=888
t1.y=999
print('t1:',t1.x,t1.y)
"""
"""
# Various paces to declare staic variable
1.inside constructor by using class name
2.inside instance method  by using class name
3.inside classmethod by using either class name or class variable
4.inside staticmethod by using class name
5. In general we can declare with in the class directly but from out side of
any method.



class Test:
    a=20
    def __init__(self):
        Test.b=20
    def m1(self):
        Test.c=40
    @classmethod
    def m2(cls):
        cls.d1=30
        Test.d2=300
    @staticmethod
    def m3():
        Test.e=60
print(Test.__dict__)

t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
t.m2()
print(Test.__dict__)
t.m3()
print(Test.__dict__)
Test.f=60
print(Test.__dict__)
"""
"""
class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

# craete an instance of the Test class
t=Test()

# access class Attribute 'a' directly
print(Test.a)

#access instance attribute 'a'
print(t.a)

#call instance methode m1
t.m1()

#call instance methode m2
t.m2()

#call instance methode m3
t.m3()
"""
"""
class Test:
    a=20
    @classmethod
    def m1(cls):
        cls.a=200
    @staticmethod
    def m2():
        Test.a=300
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)
"""
"""
### you can change static variable using either self Or 
Object refernce variables

class Test:
    a=50
    def m1(self):
        self.a=200
t1=Test()
t1.m1()
print(Test.a)
print(t1.a)
"""
"""
## delete static variable of a class

#Syntax: del className.variableName"""
"""
class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a

    def m1(self):
        Test.c=30
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=40
        del Test.c
    @staticmethod
    def m3():
        del Test.d
        Test.e=50
print(Test.__dict__)

# create an instance of the test class
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
t.m2()
print(Test.__dict__)
t.m3()
print(Test.__dict__)



class Test:
    pass

"""

"""
import sys

class Customer:
    '''Customer class with bank operation'''
    bankname = 'SBIBANK'

    def __init__(self, name, balance=500.0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        print('Balance after deposit: ', self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient Funds..")
            sys.exit()
        self.balance = self.balance - amt
        print("Balance after withdraw: ", self.balance)

print("Welcome to", Customer.bankname)

while True:
    name = input("Enter your Name : ")
    if name.isalpha():
        break
    else:
        print("Invalid Name.Please enter a valid name with Only alphabets.")



c = Customer(name)

while True:
    print("\nd- Deposite \nw -Withdraw \ne - Exit")
    option = input("Choose your option : ")

    if option.lower() == 'd':
        amt = float(input("Enter amout to Deposit: "))
        c.deposit(amt)

    elif option.lower() == 'w':
        amt= float(input("Enter amout to Withdraw: "))
        c.withdraw(amt)

    elif option.lower() == 'e':
        print(f"Thanks for Banking ,{c.name}! Have a great day!")
        sys.exit()

    else:
        print("Invalid option. pls choose a valid option")

"""

"""
#Local variable:
class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        self.b=200
        print(self.b) # Now a is accessible though 'self'

t= Test()
t.m1()
t.m2()
"""
# -------------------------------------------------
"""
Types Of methods:
1.Instance methods
2.class method 
3.static method

- Inside method implementation if we are using instance variable 
then such type of methods are called as instance methods.

Inside instance method declaration we have to pass
self variable.

def m1(self):
    by using self variable inside method we can able to 
    access instance variables.within the class we can call instance method by usingh self
    variable &from outside of the class.

we can call  by using object refernce

"""
"""### 
-The first arguments to the instance method is always self ,which 
is the refernce variable to current object
- self --> refernce variable to the current object.
- cls - refernce variable to the current Class.
"""
"""
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hi',self.name)
        print("your marks are: ", self.marks)

    def calculate_grade(self):
        if self.marks>=60:
            print("you got first grade")
        elif self.marks>=50:
            print("you got second grade")
        elif self.marks >= 35:
            print("you got Thirdd grade")
        else:
            print("you are fail !")

n= int(input("Enter number of students: "))
for i in range (n):
    name= input("Enter Name: ")
    marks =float(input("Enter Marks : "))
    s= student(name,marks)
    s.display()
    s.calculate_grade()
    print()
"""
"""
lst=[i*j for i in range(3) for j in range(4)]
print(lst)
#(0,1,2)*(0,1,2,3)=0,0,0,0,0,1,2,3,0,2,4,6
"""
"""
#setter & getter method:
- Setter method can be used to set values to the
instance variables. setter method also known as mutator method

syntax:
def setVariable(self, variable):
    self.variable= variable

#Ex:
def setName(self, name):
    self.name= name


## getter
- can be used to get values of the instance variable.
- it can also called as accessor method.

syntax:
def getVariable(self):
    return self.variable
#Ex:
def getName(self):
    return self.name
"""
"""
class student:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n=int(input("Enter number of students : "))
# create a list to store students object
student_list=[]
for i in range(n):
    s=student()
    name=input("Enter Name : ")
    s.setName(name)
    marks= float(input("Enter Marks : "))
    s.setMarks(marks)
    student_list.append(s)

## For Display student info
for s in student_list :
    print("Hi", s.getName())
    print("your Marks are : ", s.getMarks())
    print()
"""
"""
# class method
- inside method implementation if we are using only 
static varible, then such type of method we should decalre as 
class method.
-we can call classmethod by using classname
or object refernce variable.
-@classmethod
"""
"""
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{}walks with {}legs..".format(name,cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')

"""
"""
# Static Methods:
- inside these mthod we won't use any instance or class variable
here we won't provide self or cls arguments at the time of declaration

- we can declare static method explicitly by using @staticmethod
decorator
"""
"""
class maths:
    @staticmethod
    def add (x,y):
        print("The sum of : ",x+y)

    @staticmethod
    def product(x,y):
        print("The product is: ", x*y)

    @staticmethod
    def  avg(x,y):
        print("The Avg of: ", (x+y)/2)

maths.add(20,30)
maths.product(20, 30)
maths.avg(20,30)


Note:
In general we can use only instance & static method. 
Inside static method we can access class level variable by using class name
--class method are most rarely used method in python.
--Passing members of once class to another class:
    we can access members of one class inside another class.
"""
"""
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):
        print("Employee Number : ", self.eno)
        print("Employee Name: ", self.ename)
        print("Employee Salary : ", self.esal)

class Test:
    @staticmethod
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()
# create an instance of the Employee class
e= Employee(101,'Anjum',25000)
# call the modify method from Test class
Test.modify(e)


def check_same_entries(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


list1 = [int(input(f"Enter element {i + 1} of list 1: ")) for i in range(5)]
list2 = [int(input(f"Enter element {i + 1} of list 2: ")) for i in range(5)]
if check_same_entries(list1, list2):
    print("Both lists have the same values/entries.")
else:
    print("Both lists do not have the same values/entries.")


To handle the cleAN UP TASKS, PYTHON  provides a mechanism called
a Destructor. __del__
that gets invoked automatically when abn object is about to be destroyed.
In the destructor you can include code to release resources, close files,
or perfrom any necessary clean superbefore the object is removed from memory


- when an object goes out of scope 
-the refernce counter of the object reaches 0.

# craete destructor using __del__()method

def __del__(self):
    # Body of a destructor
 """
"""
#Ex:
class student:
    #COnstructor
    def __init__(self,name):
        print("inside Constructor")
        self.name=name
        print("object Initilize")

    def show(self):
        print("HEllo, my name is", self.name)

    # Destructor
    def __del__(self):
        print("inside destrutor")
        print("Object destroyed")

#create object

s1 =student("Priya")
s1.show()

# delete object
del s1
"""
### Inheritance In python
"""
The Process of inheriting the propeties of the parent 
class into a child class is called inheritance.

the existing class is called base class or parent
class and then new class is called a subclass or child
class or derived class.


The main purpose of inheritance is the reusability of 
code beacause we can use the existing class to create a new class
insted of creating it from scratch.



type Of inheritance

-single 
-multiple
-multilevel
-Hierarchical
-Hybrid


- Single interitance:
 a child class inherits from a signle-parent class
Here is one chile class & one Prent class 

"""
"""
#BAse class/Parent class
class Vehicle:
    def Vehicle_info(self):
        print("inside vehicle class")
#child class
class car(Vehicle):
    def car_info(self):
        print("Inside car class")
# create object of car
car=car()

# access vehicle info using car object

car.car_info()
car.Vehicle_info()


# multiple Inheritance
One child class can inherit from multiple parent class.
one child class & multiple parent class.
"""
# Ex:
# parent class1
"""
class Person:
    def Person_info(self,name, age):
        print("Inside Person class")
        print("Name : ",name, 'age: ', age)

#parent class2
class Company:
    def Company_info(self,comapay_name,Location):
        print("Inside Company Class")
        print("company Name is :", comapay_name, 'Location: ', Location)

# child class
class Employee(Person,Company):
    def Employee_info(self,sal,position):
        print("Inside Employee class")
        print('Salary :', sal, 'Position: ', position)

s1= Employee()
s1.Person_info("Pooja",25)
s1.Company_info("Tcs","pune")
s1.Employee_info(50000,"UIX")

"""

### Multi-level Inheritance

# a class inherits a child class or deriverd class.
# Note: When a child become a parent class for Another child class.
# Ex:
"""
class Parent:
    def m1(self):
        print("this is m1 for parent class")

# child class
class childA(Parent):
    def m2(self):
        print("this is m2 for child class1")

# child class2
class childB(childA):
    def m3(self):
        print("this is m3 for child class2")

obj= childB()
obj.m1()
obj.m2()
obj.m3()


# parent class
class Vehicle:
    def Vehicle_info(self):
        print("inside vehicle class")
#child 1 class
class car(Vehicle):
    def car_info(self):
        print("Inside car class")

class sportscar(car):
    def sportscar_info(self):
        print("Inside Soprtscar class")

# create object of car
s_car=sportscar()


# access vehicle info using car object
s_car.Vehicle_info()
s_car.car_info()
s_car.sportscar_info()
"""
"""
# Hierarchical Inheritance
#- more than one child class is derived from a single parent class
#- we can say one parent class & multiple child class.



class Vehicle:
    def Vehicle_info(self):
        print("inside vehicle class")
# child 1 class
class car(Vehicle):
    def car_info(self,name):
        print("Inside car class",name)


class sportscar(Vehicle):
    def sportscar_info(self,name):
        print("Inside Soprtscar class",name)

Obj1=car()
Obj1.Vehicle_info()
Obj1.car_info("Lamborghini")

Obj2=sportscar()
Obj2.Vehicle_info()
Obj2.sportscar_info("Huracan")



#inheritance in python
the process of inheriting the properties of the parent class into
    child class is called inheritance

the main purpose of inheritance is  the reusability of code
because we can use  the existing class to create a new class insted
of creating it from scratch

types
-single 
- multiple
-multilevel
-Hierarchical
-Hybrid

-parents class (Base class) or existing class
-child class(subclass /new class /derived class)



- a child class inherits from a single parents class 
1child class
    |
1 parent class


#Ex:

# base class
class father:
    def father_info(self):
        print("inside father class")

# child class
class son(father):
    def son_info(self):
        print("Inside Son class")

# creating Object
son= son()

#access fathers info using son object
son.father_info()
son.son_info()
"""

# ----------------------------------------------------------------------------------------------
""""

python Destructor to destory the object

- python has a garbage collector that handle memory management automatically.
-for Ex: it clean up the memory when an object goes out of scope
- to handle the clean up task  python provide a mechanism called destructor
__del__

- when an object goes out of scope
- the refernce counter of the object reaches 0.



syntax:
def __del__(self):
    # body of a destructor

Ex:

class student:
    # constructor
    def __init__(self,name):
        print("Inside Constructor")
        self.name=name
        print("Object initializesd")

    def display(self):
        print("hello , my name is: ", self.name)

    # destructor
    def __del__(self):
        print("Inside Destructor")
        print("Object Destroyed")

# create obejct
Object= student("Innara")
Object.display()

#delete Object
del Object


class vehicle:
    def __init__(self,speed):
       if speed>120:
             raise Exception("Not Allowed")
       self.speed =speed

    def __del__(self):
        print("Release resources")

# create object

car = vehicle(240)

del car

# parent class

class person:
    def person_info(self,name, age):
       print("name: ", name,"age :",age)

class company:
    def Company_info(self,company_name, location):
        print("company: ", company_name, "loacation:", location)

class Employee(person,company):
    def Emp_info(self,e_Id,designation):
        print("id: ", e_Id, "designation:", designation)

obj=Employee()
obj.person_info("sakshi",21 )
obj.Company_info("TCS","pune")
obj.Emp_info(101,"data analyst")




# Hybird Inheritance :

when Inheritance is consists of multiple  types or combination of
diff. inheritance is called hybrid inheritance

class vehicle:
    def vehicle_info(self):
        print("vehicle class is parent class of car, bike class")

class car(vehicle):
    def car_info(self):
        print("car class is subclass of vehicle class")

class bike(vehicle):
    def bike_info(self):
        print("bike class is child of vehicle")

##
class Sportscar(car,vehicle):
    def Sportscar_info(self):
        print("Sportscar class is child class of car class")

class Sportsbike(bike,vehicle):
    def Sportsbike_info(self):
        print(" sportsbike class is child class of bike class")
# create Object

v = Sportscar()
v.vehicle_info()
v.car_info()
v.Sportscar_info()


v= Sportsbike()
v.vehicle_info()
v.bike_info()
v.Sportsbike_info()


# Super( ) function :

## The Super function returns a temporary object of the
parent class that allows us to call a parents class method
inside a child class method.

- we can use the super() function in both single& multiple
inheritance
- it supports code reusability as there is no need to
write the entrie function.
- not required to remember or specify the parent class
    name to acess its method



#Ex:

class parent:
    def show_message(self):
        print("message from parent class")

class child(parent):
    def show_message(self):
        super().show_message()
        print("Message from child class")

child_obj =child()
child_obj.show_message()


#issubclass() function: if a class is a subclass of another class.
syntax:
issubclass(class,classinfo)

class -the class that you want to check if it is a subclass
classinfo -the class or a tuple of classes to check if the 1st 
parameter is a subclass of any.

#EX:
class parent:
    pass
class Child(parent):
    pass

# check if chid is a subclass of parent
result= issubclass(Child,parent)

print(result)

# Method Overriding:
when a derived class(subclass) provides a specific implementation
for a method that is already defined in its base class(superclass.True)
the overridden method in the subclass should have the same name
and signature as the method in the supperclass.

-when a child class method has the same parameters,&retrurn type as a method in its
superclass, then the method in the child is said to override the method in the parent class.

Note:
Method of overridening is a fundamental concept in oops & allows for polymorphism , where
Object of diff. classes can be treated as object of common base class.

1.create a parent class containing the method you wish to override
2. define a child class that inherits from the parent class.
3.In the child class, creayte a method with exact same signature
(same name, parameter,and return type)as the method in the
parent class.
4.provide a new implementation for the child class.



class Animal:
    def make_sound(self):
        print("Genric animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# creating instance for subclass
dog_instance=Dog()
cat_instance=Cat()

# calling the Overridden method
dog_instance.make_sound()
cat_instance.make_sound()



class Employee:
    def __init__(self,name , salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        return f"{self.name} earns{self.salary}"

class SalariedEmployee(Employee):
    def __init__(self, name , salary , bonus):
        super().__init__(name,salary)
        self.bonus= bonus

    def get_total_earning(self):
        return self.salary+self.bonus

    def get_details(self):
        details=super().get_details()
        return f"{details}, receive a bonus of Rs.{self.bonus}"

employee=SalariedEmployee("Monika",50000,10000)
print(employee.get_details())
# creating a instance of Employee with default value
print(Employee().get_details())
"""
"""
diff.between method of overloading & Overriding
method Overloading:define multiple method with the same name but diff.parameter
-used to create more cosise and readable code.
- help improve code organization & reduce the need for multiple function name
-Not supported nativley in python but can be simulated using default agruments or other
means

##Overriding:
-occurs between a parent class & its child class.
- Promotes polymorphism & inheritance in oops
- Replaces a method in a child
-class with specific implementation
overwriting the method in the superclass.
- Determines the method to execute dynamically at runtime based on the objects type

"""
"""
**What is the role of MRO(method resolution order) in python-**
-it defines the sequence in which base classes are explored when executing the method.
-MRO is specially useful in python due to its supports multiple inheritance.
-MRO follows an order bottom to top and left to right.
-this means that method are 1st searched for in the class of object ,then in the immediate superclass 
and if there are multiple superclass they are searched from left to right based on the order.
-complex inheritance
-conflict resolution


class A:
    def info(self):
        print("Inside A")

class B(A):
    def info(self):
        print("In class B")

class C(B,A):
     def info(self):
         print("Inside Class C")

c=C()
c.info()
print(C.mro())

"""

"""
#MRO in multiple inheritance---
class A:
    def method(self):
        print("A().method called")

class B:
    def method(self):
        print("B().method called")

class C(B,A):
    pass
c=C()
c.method()
print(C.mro())


suppose A and B both are inherit from C and method()is called an object of class C  that is not 
 defined in C.

 
"""

"""
# MRO
class A:
    def display(self):
        print("display message on a screen")

class B:
    def display(self):
        print("display message in class B")

class C(B,A):
    pass


c=C()
c.display()
print(C.mro())

"""

"""
polymorphism-
        the ability to use single type entity,such as method,operators,object to present
        different types in various scenarios.like 1 person but different behaviour 
        different places,which is nothing but polymorphism.
        
-poly means many and morphs means form.
-types of polymorphism
-Duck type philosophy of python


-operator overloading
-method overloading
-constructor overloading

overriding-
-method overriding
-constructor overrriding


# duck type philosophy-
at the runtime if it walks like duck and talk like a duck it must be duck.
python follows this principle this is called duck type philosophy.
-that concept in python that focus on an object behaviour rather than type.
-it allow you to call method on object without checking their specific type
 assuming they support the required behaviour.
 
 ***Advantages of duck typing***
 -promotes flexibility and code reusability by focusing on behaviour rather than type.
 -simplifies code and make it more adaptable to different object type.
 

In python we cannot specify the type explicitly.based on provided value at runtime the type 
will be consider.hence python is dynamically typed programming language.


def f1(obj):
    obj.talk()

# what is the type of obj?we cannot decide at the beggining at runtime  
# we can pass any type  then how we can decide the type

"""

"""

class Duck:
    def talk(self):
        print("quack...quack")

class Dog:
    def talk(self):
        print("Bow...Bow")

class cat:
    def talk(self):
        print("meow...meow")

class Goat:
    def talk(self):
        print("Myaaahhh...")




def f1(obj):
    obj.talk()
I=[Duck(),cat(),Dog()]
for obj in I:
    f1(obj)

"""

"""
class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")
class fish:
    def swim(self):
        print("fish swim in sea")

for obj in Bird(),Airplane(),fish():
    obj.fly()
    
    """



"""

class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swim in sea")

for obj in [Bird(), Airplane(), Fish()]:
    if hasattr(obj, 'fly'):
        obj.fly()
    elif hasattr(obj, 'swim'):
        obj.swim()

"""

"""opeartor overlaoding-
we can use the same operator for multiple purpose
which is nothing but operator overloading.
python support operator overloading

print(10+20)
print("Priya"+"Gunjal")

"""

"""
# we can overload + operator to work with book object 
# also 
+ ------->object.__add__(self,other)
- --------->object.__sub__(self,other)
* ---------->object.__sub__(self,other)
/ ---------->object.__div__(self,other)
// ---------->object.__floordiv__(self,other)
% ----------->object.__mod__(self,other)
** -------------->object.__pow__(self,other)

class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)

# print(b1+b2)

"""

"""

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __gt__(self, other):
        return self.marks>other.marks

    def __le__(self, other):
     return self.marks<=other.marks
s1=Student("Neha",98)
s2=Student("Priya",87)
print(s1>s2)
print(s1<=s2)
print(s1>=s2)

"""

"""method overloading-
if two methods having same name but different  argument the those method
is called as method overloading.

m1(int a)
m1(double d)

but in python method overloading is not possible.
if we are trying to declare multiple methods with the samne name & different 
no of argument then python is always consider only last method.


class Test:
    def m1(self):
        print("no-arg-method")

    def m1(self,a):
        print("one -arg-method")

    def m1(self,a,b):
        print("two-arg-method")

t=Test()
t.m1(10,20)

"""

"""
# how we can handle method overloading requirements in python
-most of the times,if method with variables of arguments required
    then we can handle with default argument or with variable number agr.method

"""
"""
class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of 3 no:",a+b+c)

        elif a!=None and b!=None:
            print("the sum of 2 no :",a+b)

        else:
            print("please provide two or three arguments")
t=Test()
t.sum(10)
t.sum(10,20)
t.sum(10,20,30)

"""

"""

# with variable number of agr method
class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total+=x
        print("the sum:",total)
t=Test()
t.sum(10,20)

"""

"""constructor overloading-
                      constructor overloading is not possible in python.
if we defined multiple constructor then the last constructor will be consider. 

class Test:
    def __init__(self):
        print("no-arg constructor")

    def __init__(self,a):
         print("One-arg constructor")
    def __init__(self,a,b):
        print("Two-arg Constructor")

t=Test(10,20)

"""


"""
# method overriding-
         if child class not satisfied with parent class implementation then child class 
         is redefined that method in the child based on its requirements.
         this concept is called overriding.
---overridden concept applicable for both method and constructor


class P:
    def property(self):
        print("gold+land+cash+power")

    def marry(self):
        print("Manasi")
        
class C(P):
    def marry(self):
        print("Neha")

c=C()
c.marry()
c.property()

"""


"""

# to call parent class constructor by using super()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def display(self):
        print("Employee Name:",self.name)
        print("Employee age :",self.age)
        print("Employee salary :",self.esal)
        print("Employee No:",self.eno)

e=Employee("Priya",21,101,21000)
e1=Employee("manasi",22,102,23000)
print(e.display())
print(e1.display())


"""


"""Encapsulation--
wrapping a data and methods into a single unit is called
encapsulation.
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

# Creating an instance of the Car class
my_car=Car("Toyota", "Camry", 2020)

# Accessing the attributes using getter methods
print(my_car.get_make())  # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_year())





class Student:
    def __init__(self,name="Priya",marks=80):
        self.name=name
        self.marks=marks
s1=Student()
s2=Student("Neha",89)

print("Name:{} marks:{}".format(s1.name,s1.marks))
print("Name :{} marks:{}".format(s2.name,s2.marks))

"""

"""
# protected members

class Super:
    def __init__(self):
          self._value1=100      #protected member
          self.__value2=200      #private member

    def display(self):
        print(self._value1)
        print(self.__value2)

class sub(Super):
    def show(self):
        print(self._value1)
        print(self.__value2)

obj=Super()
obj.display()

"""

"""Abstraction --hididng an unnecessary data and only showing an essential data"""
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def payment(self,amount):
        pass

    def print_slip(self,amount):
        print("Purchase of rs",amount)


class creditcardpayment(payment):
    def test(self,amount,):
        print("credit card payment of Rs",amount)
class paypalpayment(payment):
    def payment(self,amount):
        print("paypal payment in Rs.",amount)
 

obj=creditcardpayment()
obj.payment(500)
obj.print_slip(500)
print(isinstance(obj,payment))

obj=paypalpayment()
obj.payment(600)
obj.print_slip(600)



"""grabage collection
import gc
print(gc.isenabled())

gc.enable()
gc.disable()

"""

"""


from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def payment(self, amount):
        pass

    def print_slip(self, amount):
        print("Purchase of Rs", amount)


class CreditCardPayment(Payment):
    def payment(self, amount):
        print("Credit card payment of Rs", amount)


class PaypalPayment(Payment):
    def payment(self, amount):
        print("Paypal payment in Rs.", amount)


obj = CreditCardPayment()
obj.payment(500)
obj.print_slip(500)
print(isinstance(obj, Payment))

obj = PaypalPayment()
obj.payment(600)
obj.print_slip(600)

"""


