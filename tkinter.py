from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
from chempy import Substance
from chempy import Equilibrium
from chempy import balance_stoichiometry

def click():
    var = Substance.from_formula(entry.get())
    label.config(text="Your formula: " + var.unicode_name + '\n' + 'Mass: ' + '%.3f' % var.mass)

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
