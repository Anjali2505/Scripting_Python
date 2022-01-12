#Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.

#To create a tkinter app:
  #Importing the module – tkinter
  #Create the main window (container)
  #Add any number of widgets to the main window
  #Apply the event Trigger on the widgets.

import tkinter
from tkinter import ttk
from tkinter import *

#To create a main window, tkinter offers a method 'Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)'
#root = Tk()
#root.title("First GUI using Python")

#ttk module provides access to the Tk themed widget set
#grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
#ttk.Button(root, text="Hello There!").grid()

#mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
#root.mainloop()

#FRAME

#frame = Frame(root)
#labelText = StringVar()
#label = Label(frame, textvariable=labelText)
#button = Button(frame, text="Hey! I am a button")
#labelText.set("Hey! Wassup")

#pack() method:It organizes the widgets in blocks before placing in the parent widget.
#label.pack()
#button.pack()
#frame.pack()

#adding attributes to frame
#frame = Frame(root)
#Label(frame, text="Hey!").pack()
#Button(frame, text="B1").pack(side=LEFT, fill=Y)
#Button(frame, text="B2").pack(side=RIGHT, fill=X)
#Button(frame, text="B3").pack(side=TOP, fill=Y)
#Button(frame, text="B4").pack(side=LEFT, fill=X)

#frame.pack()
#root.mainloop()

#GRID 

# The sticky option specifies which edge of the cell the widget should stick to.
#Label(root, text="Name").grid(row=0, column=0, sticky=N)
#user input
#Entry(root, width=100).grid(row=0, column=1)
#Button(root, text='Submit').grid(row=0, column=5)

#RADIO BUTTONS
#Label(root, text="Gender").grid(row=1, column=0, sticky=N)
#Radiobutton(root, text="F", value=1).grid(row=1, column=1, sticky=N)
#Radiobutton(root, text="M", value=1).grid(row=1, column=2, sticky=N)

#CHECK BUTTONS
#Label(root, text="Courses").grid(row=2, column=0, sticky=N)
#Checkbutton(root, text="Python").grid(row=3, column=1, sticky=N)
#Checkbutton(root, text="Django").grid(row=4, column=1, sticky=N)
#Checkbutton(root, text="Flask").grid(row=5, column=1, sticky=N)

#root.mainloop()

#Sample Application

def square(event):
  n=int(num1.get())
  res=n*n 
  #deletes previous result before inserting new one
  result.delete(0, "end")
  result.insert(0, res)

root = Tk()
Label(root, text="Find Square of a No").pack()
num1= Entry(root)
num1.pack(side=LEFT)

btn = Button(root, text="Squares to")
#kinter bind is defined as a function for dealing with the functions and methods of Python that are bind to the events that occur during the program execution such as moving the cursor using a mouse, clicking of mouse buttons, clicking of buttons on the keyboard, etc are events that are handled using bind function in Tkinter.
btn.bind("<Button-1>", square)
btn.pack(side=LEFT)

result = Entry(root)
result.pack(side=LEFT)

root.mainloop()










