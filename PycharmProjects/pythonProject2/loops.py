# when we want to execute set of statements multiple times then we used loop.
# while loop-this loop is used when we want to repeat statements or block repeatedly until given condition true or satisfied.




# for i in range(0,100):
#     print(i)
# list1=[1,3,5,6,7,8,9,10]
# for i in list1:
#     print(i)

#
# for i in range(0,20,2):
#     print(i)
#
# tuple=(1,3,6,8,'priya',9.0)
# for i in tuple:
#     print(i)
"""
#  nested for Loop
list1=[2,4,5,6,8]
list2=['a','b','c','b']
for i in list1:
    print(i)
    for a in list2:
        print(a)



# while loop-execute until the given condition get true
name=""
while name!="priya":
    name=input("enter your name:")
print("Thanks for confirmation")
"""
"""
# nested if
if condition1:
    statement 1
    if condition 2:
        statement 2
    else:
        statement
elif condition 4:
    statement 4
else:
    statement
    """

"""
num=int(input("Enter number:"))
if num%2==0:
    if num%3==0:
        print("divisible by 3 & 2")
    else:print("divisible by 2 not by 3")

else:
    if num%3==0:
        print("divisible by 3 not by 2")

    else:
        print("not divisible by 2 & 3")
        
        


height=int(input("enter you height:"))
if height>5:
    print("you can ride")
    age=int(input("enter your age :"))
    if age<18:
        print("pay 100rs ")
    else:
        print("pay 300rs")
else:
    print("can't ride")
    

username=int(input("enter username :"))
if username=="admin":
    print("Valid Username")
    pass=int(input("enter password"))
    if pass==1234:
        print("Sucessfully login")
else:
 print("Try again")
else:
print("sign in")

"""
# calculator
opr = input("Please Enter an operator [+,-,*,/]: ")

if opr in ['+', '-', '*', '/']:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if opr == '+':
        sum = num1 + num2
        print("Sum of", num1, 'and', num2, '=', sum)
    elif opr == '-':
        if num1 > num2:
            difference = num1 - num2
        else:
            difference = num2 - num1
        print("The difference between", num1, 'and', num2, '=', difference)
    elif opr == '*':
        multi = num1 * num2
        print("Multiplication of ", num1, 'and', num2, '=', multi)
    elif opr == '/':
        if num1 == 0 or num2 == 0:
            print("Numbers must be positive")
        else:
            division = num1 / num2
            print("Division of", num1, 'by', num2, '=', division)
else:
    print("Invalid operator")








