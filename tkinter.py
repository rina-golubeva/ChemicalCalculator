from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

from chempy import Substance
from chempy import Equilibrium
from chempy import balance_stoichiometry

'''
Function for calculating the molar mass of a substance.
For a substance entered from the keyboard via the mass method
from the champy package, the mass value is calculated.
The substance itself is processed using the Substance function.from_formula,
its output is carried out through the unicode_name method.
'''

def click():
    var = Substance.from_formula(entry.get())
    label.config(text="Your formula: " + var.unicode_name + '\n' + 'Mass: ' + '%.3f' % var.mass)

'''
Function for calculating coefficients in the equation.
The entered equation is divided into input and output data
using the split function.
Using the balance_stoichiometry function from the champy package,
coefficients are selected in the equation.
Dictionaries are used for their output.
'''    
    
def clicked():
    ex,prod=entry.get().split('=')
    ex,prod=balance_stoichiometry(set(ex.split('+')),set(prod.split('+')))
    label.config(text='Коэффициенты: '+str(dict(ex))+str(dict(prod)))   
    
root = Tk()

root.title("Chemical calculator")

frame = Frame(root, borderwidth=10, relief=GROOVE)
frame.pack()

entry = Entry(frame, width = 50)
entry.pack()

label = Label(frame)
label.pack()

button = Button(frame, text='Посчитать', command=click)
button.pack()

button2 = Button(frame, text='Уравнять реакцию', command=clicked)
button2.pack()

root.mainloop()
