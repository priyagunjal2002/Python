"""
In any programming language there are 2 types
of errors are possible-
1.syntax error
2.runtime error

Exceptional handling concept applicable for runtime errors.

an unwanted and unexpected event that disturbs normal flow of program
is called exception.



print(10/0)
print(10/("ten"))
x=int(input("Enter number:"))
print(x)


# try-->


print("stmt-1")
try:
    print(10/2)
except ZeroDivisionError:
    print("please enter valid no:")
print("stmt-3")


"""


"""
# single try b;lock weith multiple except block
try:
 x=int(input("Enter first number:"))
 y=int(input("Enter second Number :"))
 print(x/y)

except ZeroDivisionError:
 print("cant divide with zero")

except ValueError:
 print("please provide int value only")


"""

"""
# single try block with single except block to handle multiple exception in a single except block

try:
    x=int(input("Enter first number :"))
    y=int(input("Enter second Number :"))
    print(x/y)

except(ZeroDivisionError,ValueError) as msg:
    print("please provide valid numbers and problem is :",msg)


"""


"""

# default exception

try:
    x=int(input("Entet First number :"))
    y=int(input("Enter second number :"))
    print(x/y)

except(ZeroDivisionError) as msg:
    print("Enter valid number",msg)

except:
    print("Default exception ")


"""

"""
# finally block-clear -executed at last

try:
    x=int(input("Entet First number :"))
    y=int(input("Enter second number :"))
    print(x/y)

except(ZeroDivisionError) as msg:
    print("Enter valid number",msg)

except:
    print("Default exception ")

finally:
    print("stmt-1")
    print("stmt-2")
    print("stmt-3")


"""


# nested try-except-finally

try:
    print("outer try block")

    try:
        print("Inner try block")
        x=int(input("Enter first number :"))
        y=int(input("Enter second number :"))
        print(x/y)

    except ZeroDivisionError:
        print("Inner except block")

    finally:
        print("Inner finally block")

except:
    print("Outer except block")
    print("please enter int value only")

finally:
    print("outer finally block")
