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
    var = Substance.from_formula(entry_a.get())
    answer_a.config(text="Your formula: " + var.unicode_name + '\n' + 'Mass: ' + '%.3f' % var.mass)

'''
Function for calculating coefficients in the equation.
The entered equation is divided into input and output data
using the split function.
Using the balance_stoichiometry function from the champy package,
coefficients are selected in the equation.
Dictionaries are used for their output.
'''    
    
def clicked():
    ex,prod=entry_b.get().split('=')
    ex,prod=balance_stoichiometry(set(ex.split('+')),set(prod.split('+')))
    answer_b.config(text='Коэффициенты: '+str(dict(ex))+str(dict(prod)))
    
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        root.destroy()
    
root = Tk()
root.title("Chemical calculator")
root["bg"]="plum2"
root.iconbitmap("chem.ico")
root.protocol("WM_DELETE_WINDOW", on_closing)

frame_a = Frame(root, borderwidth=10, relief=GROOVE, bg = "plum2")
frame_a.pack()

frame_b = Frame(root, borderwidth=10, relief=GROOVE, bg = "plum2")
frame_b.pack()

label_a = Label(frame_a, text = "Введите формулу вещества: ", bg="plum2", font=("Courier", 12, "italic"))
label_a.pack()

label_b = Label(frame_b, text = "Введите уравнение: ", bg="plum2", font=("Courier", 12, "italic"))
label_b.pack()

entry_a = Entry(frame_a, width = 50)
entry_a.pack()

entry_b = Entry(frame_b, width = 50)
entry_b.pack()

button = Button(frame_a, text='Посчитать', command=click, bg='#CA9BD5', font=("Courier", 12, "italic"))
button.pack()

answer_1 = Label(frame_a, text = "Ответ: ", bg="plum2", font=("Courier", 12, "italic"))
answer_1.pack()

answer_a = Label(frame_a, bg="plum2", font=("Courier", 12, "italic"))
answer_a.pack()

button2 = Button(frame_b, text='Уравнять реакцию', command=clicked, bg='#CA9BD5', font=("Courier", 12, "italic"))
button2.pack()

answer_2 = Label(frame_b, text = "Ответ: ", bg="plum2", font=("Courier", 12, "italic"))
answer_2.pack()

answer_b = Label(frame_b, bg="plum2", font=("Courier", 12, "italic"))
answer_b.pack()

button3 = Button(text = 'Click and quit', command = on_closing, bg="plum2", font=("Courier", 12, "italic"))
button3.pack()

root.mainloop()
