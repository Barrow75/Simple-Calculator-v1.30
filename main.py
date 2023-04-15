# Calculator 1v3.0
# System Update: User input multiple numbers

# Import all names and functions from the tkinter module (*)
from tkinter import *

# opening the code in a new window (UI) with the title Calculator
root = Tk()
root.title("Calculator")
# Where the input and output will be displayed when clicking a button
enter = Entry(root, width=35, borderwidth=5)
enter.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Called when a number button is clicked/ overall deletes and updates the current number being displayed on screen when
# that number is being pressed
def button_click(number):
    # gets current text and then stores it as a variable
    current = enter.get()
    # clears number so another number can be entered after operator is pressed
    enter.delete(0, END)
    # inserts new number that is pressed right after it stores the previous number is stored
    enter.insert(0, str(current) + str(number))


# function is used to clear the input field.
def button_clear():
    enter.delete(0, END)


# function is called when the add (+) button is pressed
def button_add():
    # gets the first number and display it
    first_number = enter.get()
    # the globals make this accessible to anywhere in the program
    # f_number will be stored before (+) operation
    global f_number
    # get the type of math operation that will be performed
    global math
    # indicates addition will be used
    math = "addition"
    # converts the first number to an integer and stores it as a global variable
    f_number = int(first_number)
    # Number is cleared so another number can be entered
    enter.delete(0, END)


# called when the equal (=) button is pressed

def button_Equal():
    # gets the second number and then deletes it when the operator is pressed
    second_number = enter.get()
    enter.delete(0, END)
    # performs the requested operator on the numbers that are selected
    if math == "addition":
        enter.insert(0, f_number + int(second_number))
    if math == "subtraction":
        enter.insert(0, f_number - int(second_number))
    if math == "multiplication":
        enter.insert(0, f_number * int(second_number))
    if math == "division":
        enter.insert(0, f_number / int(second_number))


# function is called when the subtract (-) button is pressed
def button_Subtract():
    first_number = enter.get()
    global f_number
    global math
    math = "subtraction"
    f_number = int(first_number)
    enter.delete(0, END)


# function is called when the multiply (*) button is pressed
def button_Multiply():
    first_number = enter.get()
    global f_number
    global math
    math = "multiplication"
    f_number = int(first_number)
    enter.delete(0, END)


# function is called when the divide (/) button is pressed
def button_Divide():
    first_number = enter.get()
    global f_number
    global math
    math = "division"
    f_number = int(first_number)
    enter.delete(0, END)


# creates the buttons on the calculator
# padx and pady are the width and height of each button
# command button is used specify what happens when a button is clicked
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonAdd = Button(root, text="+", padx=39, pady=20, command=button_add)
buttonEqual = Button(root, text="=", padx=91, pady=20, command=button_Equal)
buttonClear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

buttonSubtract = Button(root, text="-", padx=41, pady=20, command=button_Subtract)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=button_Multiply)
buttonDivide = Button(root, text="/", padx=41, pady=20, command=button_Divide)

# specify the location of where the button will be placed
# sticky="nswe" = aligns the buttons
button1.grid(row=3, column=0, sticky="nsew")
button2.grid(row=3, column=1, sticky="nsew")
button3.grid(row=3, column=2, sticky="nsew")

button4.grid(row=2, column=0, sticky="nsew")
button5.grid(row=2, column=1, sticky="nsew")
button6.grid(row=2, column=2, sticky="nsew")

button7.grid(row=1, column=0, sticky="nsew")
button8.grid(row=1, column=1, sticky="nsew")
button9.grid(row=1, column=2, sticky="nsew")

button0.grid(row=4, column=0, sticky="nsew")

buttonAdd.grid(row=5, column=0, sticky="nsew")
buttonEqual.grid(row=5, column=1, columnspan=2, sticky="nsew")
buttonClear.grid(row=4, column=1, columnspan=2, sticky="nsew")

buttonSubtract.grid(row=6, column=0, sticky="nsew")
buttonMultiply.grid(row=6, column=1, sticky="nsew")
buttonDivide.grid(row=6, column=2, sticky="nsew")

# closes the mainloop of the tkinter window
root.mainloop()
