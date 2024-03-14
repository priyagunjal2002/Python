"""
# list comprehension
result=[i*j for i in range(3) for j in range(4)]
print(result)

# check file exists in python before opening it using function os.path.exists
import os
if os.path.exists("SOFT SKILLS.txt"):
    print("File exists")
else:
    print("file does not exists")
"""

# what is the difference between binary and text mode when opening files
"""binary mode is used in  opening file of unstructured data and text file is nothing but the textual data"""

# diff.between read() and realine()
"""readline is used to read the particular line and read is used for read the char.."""

# how do you append text to an existing file in python?
"""using 'a' for appending file and 'a+' for appending ,reading and writing in the file"""
f=open("online python.txt","a+")
print(f.write("python is dynamically scripting language\n it is used in game development."))
print(f.write("Python used PVM ie.python virtual machine"))
print("file name :",f.mode)
print(f.writable())
print(f.readable())
print(f.close())