from tkinter import *
from tkinter import messagebox

def click():
    answer_a.config(text="Hi!")

def clicked():
    answer_b.config(text="Hello!")

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        window.destroy()
        window.protocol("WM_DELETE_WINDOW", on_closing)  

window = Tk()
window.title("Chemical Calculator")
window["bg"]="plum2"
window.iconbitmap("chem.ico")

frame_a = Frame(window, borderwidth=10, relief=GROOVE,bg="plum2")
frame_a.pack()

frame_b = Frame(window, borderwidth=10, relief=GROOVE,bg="plum2")
frame_b.pack()

label_a = Label(frame_a,text="Введите формулу вещества:",bg='plum2',font=("Courier", 12, "italic"))
label_a.pack()

label_b = Label(frame_b,text="Введите уравнение:",bg='plum2',font=("Courier", 12, "italic"))
label_b.pack()

entry_a = Entry(frame_a, width = 50)
entry_a.pack()

entry_b = Entry(frame_b, width = 50)
entry_b.pack()


button = Button(frame_a, text='Посчитать', command=click,bg='#CA9BD5',font=("Courier", 12, "italic")) 
button.pack()

answer_a = Label(frame_a,text="Ответ: ",bg='plum2',font=("Courier", 12, "italic") )
answer_a.pack()

button2 = Button(frame_b, text='Уравнять реакцию', command=clicked,bg='#CA9BD5',font=("Courier", 12, "italic"))
button2.pack()

answer_b = Label(frame_b,text="Ответ: ",bg='plum2',font=("Courier", 12, "italic") )
answer_b.pack()

button3 = Button(text = "Click and quit", command = on_closing, bg='#CA9BD5', font=("Courier", 12, "italic"))
button3.pack()

window.mainloop()
