# Make a scientific calculator with the use of a GUI
import math
from tkinter import *

# Declares variable
expression = ""


# Imports all of the functions and components of Tkinter
def press(digit):
    # Allows for a global expression variable
    global expression
    # The string gets concatenated
    expression = expression + str(digit)

    # Using the method 'set' to update the equation
    equation.set(expression)


# Function to run the final calculation
def equatepress():
    try:

        global expression

        # Evaluates the final expression and turns it into a string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable using an empty string
        expression = ""

        # in case of an error
    except:

        equation.set(" error ")
        expression = ""

# Defines the square root command
def root():
    global expression
    expression = math.sqrt(float(expression))
    equation.set(expression)
    expression = ""


# Defines the sine rule to be used on the calculator
def sin():
    global expression
    expression = math.sin(float(expression))
    equation.set(expression)
    expression = ""


# Defines the tan rule to be used on the calculator
def tan():
    global expression
    expression = math.tan(float(expression))
    equation.set(expression)
    expression = ""


def cos():
    global expression
    expression = math.cos(float(expression))
    equation.set(expression)
    expression = ""


# Delete contents of entry field
def delete():
    global expression
    expression = ""
    equation.set("")


# Creating the gui window :)
if __name__ == "__main__":
    # Making the window
    gui = Tk()

    # Set the background color of the gui
    gui.configure(background="grey")

    # Creating the title of the gui
    gui.title("Simple Calculator")

    # Changing the size of the window
    gui.geometry("157x345")

    # StringVar is the variable class used for the calculations
    equation = StringVar()

    # Creating the area for calculations(expression)
    expression_area = Entry(gui, textvariable=equation, bg="#000000", fg='white')

    # Using the grid method to place objects
    expression_area.grid(columnspan=10, ipadx=20)

    # Creating the buttons
    # Placing them within the grid
    button1 = Button(gui, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=2, width=6)
    button1.grid(row=4, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=2, width=6)
    button2.grid(row=4, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=2, width=6)
    button3.grid(row=4, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=2, width=6)
    button4.grid(row=6, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=2, width=6)
    button5.grid(row=6, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=2, width=6)
    button6.grid(row=6, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=2, width=6)
    button7.grid(row=8, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=2, width=6)
    button8.grid(row=8, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=2, width=6)
    button9.grid(row=8, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=2, width=6)
    button0.grid(row=10, column=1)

    addition = Button(gui, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=2, width=6)
    addition.grid(row=10, column=0)

    subtract = Button(gui, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=2, width=6)
    subtract.grid(row=10, column=2)

    multiplication = Button(gui, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=2, width=6)
    multiplication.grid(row=11, column=1)

    division = Button(gui, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=2, width=6)
    division.grid(row=11, column=0)

    Decimals = Button(gui, text=' . ', fg='black', bg='white', command=lambda: press("."), height=2, width=6)
    Decimals.grid(row=13, column=0)

    equals = Button(gui, text=' = ', fg='black', bg='white', command=equatepress, height=2, width=6)
    equals.grid(row=11, column=2)

    Delete = Button(gui, text=' del ', fg='black', bg='white', command=delete, height=2, width=6)
    Delete.grid(row=14, column=0)

    Sin = Button(gui, text="sin", fg='black', bg='white', command=sin, height=2, width=6)
    Sin.grid(row=12, column=0)

    Tan = Button(gui, text="tan", fg='black', bg='white', command=tan, height=2, width=6)
    Tan.grid(row=12, column=1)

    Cos = Button(gui, text="cos", fg='black', bg='white', command=cos, height=2, width=6)
    Cos.grid(row=12, column=2)

    Root = Button(gui, text="√", fg='black', bg='white', command=root, height=2, width=6)
    Root.grid(row=13, column=2)

    Power = Button(gui, text="^", fg='black', bg='white', command=lambda: press("**"), height=2, width=6)
    Power.grid(row=13, column=1)

    # Starts the gui
    gui.mainloop()






