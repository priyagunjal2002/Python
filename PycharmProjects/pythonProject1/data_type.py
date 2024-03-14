"""data type specifies the which type of value the variable has stored.
1)Numeric-int,float.complex
2)Boolean-True,False
3)Text-string
4)dict-key value pair
5)sequence type-list,tuple
6)set


list-to store multiple values in a single variable.it is mutable

m1=12
m2=13
m3="python"
l1=[m1,m2,m3]
print(l1)

# tuple-it is immutable
tuple=(12,45,89)
print(tuple)


# dict-key value pair
marks={"name":"priya","age":21,"course":"Data Science"}
print(marks)

marks=[34,88,99,87]
print(marks,type(marks))
"""
# take input from user add two no
"""
num1=input("Enter first no")
num2=input("enter second no")
sum=int(num1) + int(num2)
print(sum)

num1=int(input("enter 1st no.="))
num2=int(input("enter 2nd no.="))
sum=num1+num2
print(sum)
"""

# convert a string to an integer
# str="1234"
# print(int(str))


# python program to calculate the avg of 3 no enter by users

num1=int(input("Enter first number = "))
num2=int(input("Enter second number ="))
num3=int(input("Enter third number = "))
sum=num1+num2+num3
avg=sum/3
print(avg)






