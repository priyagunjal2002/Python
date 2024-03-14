"""
#separate all lower case letter,uppercase letter,special case character and number from given string
#my_string="ASdfesD@#HBDHB&^GUV%^*H45fdvnhwT4w5e54uuU"
my_string = "ASdfesD@#HBDHB&^GUV%^*H45fdvnhwT4w5e54uuU"

lowercase_letters = ''
uppercase_letters = ''
special_characters = ''
numbers = ''

# Iterate through each character in the string
for char in my_string:
    if char.islower():
        lowercase_letters += char
    elif char.isupper():
        uppercase_letters += char
    elif not char.isalnum():
        special_characters += char
    elif char.isdigit():
        numbers += char

# Print the results
print("Lowercase letters:", lowercase_letters)
print("Uppercase letters:", uppercase_letters)
print("Special characters:", special_characters)
print("Numbers:", numbers)

"""
#python program to add two numbers

num1=int(input("Enter first number ="))
num2=int(input("Enter second number ="))
sum=num1+num2
print(sum)

"""
#write a python script to concatenate following dict to craete a new one
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict=dict1|dict2|dict3
print(dict)

#python program to print hello world ,a value inside variable a number.
# var_1="Hello World"
# print(var_1)
# 


# print are you from given string
my_string="hello ram where are you going"
print(my_string[16:-6])"""

# write a python program to count the number of characters in a string
from collections import Counter
string="python programming"
char_frequency=Counter(string)
for char,count in char_frequency.items():
    print(char_frequency)

