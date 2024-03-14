# open
# r= open an exiting  file  for read(read)
# w=open an existing file for write
# a=open an existing file for append operation.
# r+=to read and write data into the file
# w+=to write and read data
# a+=to append and read data from file.

# binary-video,audio,Images(unstructured data)
# document data-.docs,.pdf,.txt
# open file
# f=open("file.txt","w")

# f=open("SOFT SKILLS.txt","w")
# print("File Name :",f.name)
# print("File Name :",f.mode)
# print("Is File Readable: ",f.readable())
# print("Is File Writable: ",f.writable())
# print("Is File Closed : ",f.closed)
# f.close()

# print("Is File Closed : ",f.closed)
# f=open("C:\Users\Amit\OneDrive\Documents\SOFT SKILLS.txt")
# print(f.read("C:\Users\Amit\OneDrive\Documents\SOFT SKILLS.txt"))

# open and read a file....
# f=open("SOFT SKILLS.txt","r")
# char=(f.read())
# print(char)
# print(f.readline(15))

# print(f.readable())

"""
f=open("online python.txt","w")
print(f.write("Python is easy to learn\nit is used for different purpose."))
print(f.write("Python is dynamically scripting language"))
print("file name:",f.name)
print("file name :",f.mode)
print("Is File Readable :",f.readable())
print("Is File Writable :",f.writable())
print(f.close())
"""
"""pickling and unpickling of object-
the process of writing state of object to the file is called pickling and 
the process of reading state of an object from the file is called unpickling.
we can implement pickling and unpickling by using pickle module of python
pickle module  contains dump() function to perform pickling.

pickling is the process through which a python object hierarchy is converted into a byte stream
hierarchy is a tree like structure.unpickling uses load() function..

pickle.dump()-write the pickle representation of the object to the open file object file.
pickle.dumps()-return the pickle representation of the object 
pickle.load()-
pickle.loads()

advantages-
1.saving and loading machine learning models
2.serialization-json,xml,hdf5,pickle(file format)
3.storing application

-serialization formats like JSON,which can not handle tuples and datetime objects
-pickle can serialize almost every common used built -in python data type.
-it also returns the exact state of object which JSON cannot do.
-pickles allows for flexibility when deserializing objects.
-you can easily saves diff.variables into a pickle file and load them bck a different
python session ,recovering your data exactly the way it was without achieving to edit your code.

DISADVANTAGES- OF PICKLE---
-pickle is unsafe because it can execute malicious python callable to construct objects.
-when deserializing an object.,pickle cannot tell the diff.between a malicious 
callable and non malicious one.due to this  user can end up executing arbitrary code during deserialization.
-pickle is a python module &you may struggle to deserialize pickle object when using diff language.
-according to multiple benchmark ,pickle appears to slower & produces large values than format such as JSON and apacheThrift.


import pickle
people={
    "name":"priya",
    "age":21,
    "gender":"female",
    "height":5.6

}
db={}
db[people]=people

"""
# check file exists in os or not
import os
if os.path.exists("SOFT SKILLS.txt"):
    print("File exists")
else:
    print("file does not exists")










