# range function
# built in range()-it is mainly used in for loops
"""
syntax-
range(start,stop,stopwise)
range starts at 0 and increment by 1.


for num in range(5):
    print(num)


# how to used start and stop argument
for num in range(0,7):
    print(num)

# Negative integers
for num in range(-5,2):
    print(num)


# if we want to passed float values
for num in range(int(1.12,2.0)):
    print(num)--------.it gives error


# start,stop and step
for i in range(-12,-2,3):
    print(i)


# create a list using range() functiom
list=list(range(0,10))
print(len(list))


my_list=['python','java','c','cpp']
# my_list_length=len(my_list)

# for i in range(my_list_length):
#     print("hello python")

for i in range (len(my_list)):
        print("hello")




# python function
def add():
    print("WElCOME ")
# call function
add()
print("python programming")

# when the function add() is called ,the program control transfer to the functiom
# all the code inside the function is executed
# the control of the program jumps to the statement after the function call.



def greet(name):
    print("hello",name)
greet("Priya")


# function to add number
def add_num(num1,num2):
 sum=num1+num2
 print("sum of",num1,'and',num2,'=',sum)
add_num(12,56)


# return statement
def power_number(num):
    result=num*num*num
    return result
num=int(input("enter number:"))
power=print(power_number(num))




# program to check given no is even or odd
def evenodd(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")
evenodd(56)
evenodd(23)



# write a python function that takes a number as parameter and checks wheteher is prime number or not.
#

def is_prime(n):
    if n<2:
     return False
    for i in range(2,n):
     if(n%i==0):

        return False
    return True
n=int(input("enter Number:"))
if is_prime(n):
 print("Given no is prime number")
else:
 print("No is not a prime number")


#  1 to 100
# number divible by 3----fizz
# number divisible by 5-----buzz
# number divisible by 3 & 5---fizz buzz
for num in range(1,100):
    if num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    elif num%3==0 and num%5==0:
        print("fizz buzz")
    else:
        print(num)



def wish(name):
    print("hello",name,"good morning")
wish("Priya")
"


def add(x, y):
    return x + y

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the add function with user input
result = add(num1, num2)

# Displaying the result
print("The sum is", result)

# error in below code

def sum_sub(a,b):
    return a +b
    return a-b
    return sum_sub()
a=int(input("enter vlue of a :"))
b=int(input("Enter value of b :"))
sum_sub=sum_sub(a,b)
print("the sum is",)
print("the substraction is :")
sum_sub()




def sum(*n):
    total=0
    for n1 in n:
     total=total+n1
    print("The sum is:",total)
sum()
sum(10,20)
sum(10,20,30)


def display(**kwargs):
 for k,v in kwargs.items():
  print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rno=100,name="Priti",marks=70,subject="python")



print(type(5 / 2))
print(type(5 // 2))



a = 3
b = 1
print(a, b)
a, b = b, a
print(a, b)



a = [1, 2]
print(a * 3)


example = ["Sunday", "Monday", "Tuesday", "Wednesday"];
del example[2]
print(example)

numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
print(sorted_numbers)


def thrive(n):
   if n % 15 == 0:
       print("thrive", end = “ ”)
    elif n % 3 != 0 and n % 5 != 0:
       print("neither", end = “ ”)
   elif n % 3 == 0:
       print("three", end = “ ”)
   elif n % 5 == 0:
       print("five", end = “ ”)
thrive(35)
thrive(56)
thrive(15)
thrive(39)



def solve(a):
 a = [1, 3, 5]
 a = [2, 4, 6]
 print(a)
 solve(a)
 print(a)


def solve(a, b):
    return b
  if a ==0
    else solve(b % a, a)
print(solve(20, 50))

# print(2 ** 3 + 5 ** 2)

"""

# Types of variables-
"""global-The variables which are declared outside of function is called global variables.these can be accessed in all functions of tnat module. 

a=10
def f1():
 print(a)
def f2():
 print(a)
f1()
f2()
"""

"""local variables-variables declared inside the function .They are available only for the function in which we declared it.

def f1():
 a=10
 print(a)
def f2():
    a=20
    print(a)
f1()
f2()
"""

"""Global keyword:
a=10
def f1():
 global a
a=777
print(a)

def f2():
    print(a)

    f1()
    f2()
    
    """
"""Recursive function-A function that calls itself is called recursive function
formula-factorial(n)=n*factorial(n-1)
def factorial(n):
    if n==0:
        result=1
    else:
     result=n*factorial(n-1)
    return result
print("Factorial of 4 is:",factorial(4))
print("Factorial of 5 is:",factorial(5))

"""

"""Anonymous functions: sometimes we can declare a function without any name ,such type of nameless functions are called anonymous function or lambda functions.
  the main purpose of anonymous function is just for instant use.(ie.for one time usage
  
  normal function-we can define by using def keyword.

def squareIt(n):
    return n*n
"""

"""lambda function-we can define using lambda keyword
   lambda n:n*n 
   syntax of lambda function:
   lambda argument_list:expression
   
   note-by using lambda function we can write very concise code so that reliability of the program will be improved.
   """

"""write a program to create a lambda function to find square of given number
s=lambda n:n*n
print("The square of 4 is :",s(4))
print("The square of 6 is :",s(6))

"""

"""lambda function to find sum of 2 given numbers
s=lambda a,b:a+b
print("Sum of 10,20 is :",s(10,20))
print("Sum 0f 300,200 is :",s(300,200))"""

"""lambda function to find biggest of given values
s=lambda a,b :a if a>b else b
print("The biggest of 23,90 is :",s(23,90))
print("The biggest of 43.8,87.6 is:" ,s(43.8,87.6))"""

""" note-lambda function  internally returns expression value and we are not required to write return satement explicitly

sometimes can pass function as argument to another function.In such cases lambda function are best choice.
we can use lambda function very commonly with filter(),map(),and reduce() function ,bcoz these functions expect function as an argument.
"""

"""filter() function-
we can use filter function to filter values from given sequence 

program to filter the list 

def iseven(x):
 if x % 2==0:
  return True
 else:
  return False
l=[0,5,10,15,20,25]
l1=list(filter(iseven,l))
print(l1)

# with lambda function
l=[0,5,10,15,20,25]
l1=list(filter(lambda x:x%2==0,l))
print(l1)


l=[0,5,10,15,20,25]
l1=list(filter(lambda x:x%2!=0,l))
print(l1)

"""
"""map()function-for every element present in the given squence ,apply some functionality and generate new element with rewquired modification
  syntax :map(function,sequence)
l=[1,2,3,4,5]
def doubleIt(x):
    return 2*x
l1=list(map(doubleIt,l))
print(l1)

# with lambda function
l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print(l1)

l=[1,2,3,4,5]
l1=list(map(lambda x:x**2,l))
l2=list(map(lambda x:x**3,l))
print(l1)
print(l2)

"""
"""we can apply map() function to multiple list also.but make sure that all list should have same length.
syntax:map(lambda x,y:x*y,l1,l2))

l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)
"""
"""reduce function()-
from functools import *
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)
"""
"""ALiasing
def wish(name):
 print("Good morning",name)

greeting=wish
wish("Priya")
greeting("Priya")
del wish
greeting("Psycho")

"""

"""nested function
def outer_func():
    def inner_func():
        print("Hello, World!")
    inner_func()
outer_func()
"""

"""Fuction decorators-decorator is a function which can take a function as argument and extend its functionality.
and return modified functions with extended functionality.
a decorator function is a function that accepts a function as parameter and returns a function.
a decorator takes the result of function,modifies the result and return it.
we use @function_name to specify decorator..used in authorizatioon,authentication.
the main objective of decorator function is we can extend the functionality of existing function without modifies that function.
def wish(name):
    print("hello",name,"Good Morning")
wish("Priya")
"""
"""
# indentation error
def decor(fun):
    def inner():
        print("If:Before enhancing function")
        fun()
        print("If:after enhancing function")
        return inner()
def num():
 print("we will use this function")
print("and will enhance this in decorators")
num()
result_fun=decor(num)
result_fun
"""

"""
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def num():
    return 10

print(num())
"""

"""Generator-is a function which is reponsible to generate a sequence of value
it uses yield keyword to return values.
next() function-this function is used to retirve element from a generator object

def disp(a,b):
    yield a
    yield b

result=disp(10,200)
print(result)
# print(type(result))
# value1=next(result)
# print(value1)
# value2=next(result)
# print(value2)

for value in result:
    print(value)
    

def countdown(num):
    print("start countdown")

    while num>0:
        yield num
        num=num-1

values=countdown(5)
for x in values:
     print(x)
"""
"""
import random
import time

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
subjects = ['Math', 'Science', 'English', 'History', 'Computer Science']

def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        results.append(person)
    return results
    


g=[x*x for x in range(10000000000000000)]
print(next(g))


import mymodule
mymodule.welcome("Priya Gunjal")
"""

"""
import mymodule

a = mymodule.Person["age"]
b = mymodule.Person["country"]
print(a)
print(b)
"""
# help('modules')
"""
import math
values=math.pi
print(values)

import math
sin_val=math.sin(90)
print(sin_val)


import statistics
stat=statistics.median([2,3,4,5,6,7,8])
print(stat)


import statistics
stat=statistics.mean([2,3,4,7,8,8])
print(stat)

import statistics
stat=statistics.mode([2,3,4,7,8,8])
print(stat)


import statistics
stat=statistics.stdev([2,3,4,7,8,8])
print(stat)

"""
import packages
a=packages.welcome("Priya")
print(a)
