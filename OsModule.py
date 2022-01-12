#The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system. 

import os

print(os.getcwd()) #get current directory

#change directory
#os.chdir("C:\\Users\\Anjali\\Desktop")
#print(os.getcwd())

#make a new directory & remove it
os.mkdir("C:\\Users\\Anjali\\Desktop\Python1")
os.rmdir("C:\\Users\\Anjali\\Desktop\Python1")

#remove a file
#os.remove("Scripting\\main.py")

#join path 
print(os.path.join("C:\\Users\\Anjali\\Desktop\\Python\\Scripting","C:\\Users\\Anjali\\Desktop\\Python\\Scripting\\OsModule.py"))

#slpit path into directory name and file name
print(os.path.split("C:\\Users\\Anjali\\Desktop\\Python\\Scripting\\OsModule.py"))

#check if a path exists
print(os.path.exists("C:\\Users\\Anjali\\Desktop\\Python\\Scripting\\OsModule.py"))