from tkinter import *
from tkinter import messagebox  
 
tk = Tk()
tk.title("Calculator")
tk.geometry("400x400")
Label(tk,text="Calculator",font="Times 12 bold").pack()


sayi1 = Entry(tk, width=25)
sayi1.pack()
sayi2 = Entry(tk, width=25)
sayi2.pack()


def add():
    messagebox.showinfo("Result", int(sayi1.get())+int(sayi2.get()))
    sayi1.delete(0,END)
    sayi2.delete(0,END)
def subtract():
    messagebox.showinfo("Result", int(sayi1.get())-int(sayi2.get()))
    sayi1.delete(0,END)
    sayi2.delete(0,END)
def multiply():
    messagebox.showinfo("Result", int(sayi1.get())*int(sayi2.get()))
    sayi1.delete(0,END)
    sayi2.delete(0,END)
def divide():
    messagebox.showinfo("Result", int(sayi1.get())/int(sayi2.get()))
    sayi1.delete(0,END)
    sayi2.delete(0,END)

btn_add = Button(tk,
            text="+",
            padx="20",pady="5",
            command=add)
btn_add.pack()
 
btn_subtract = Button(tk,
            text="-",
            padx="20",pady="5",
            command=subtract)
btn_subtract.pack()

btn_multiply = Button(tk,
            text="*",
            padx="20",pady="5",
            command=multiply)
btn_multiply.pack()
 
btn_divide = Button(tk,
            text="/",
            padx="20",pady="5",
            command=divide)
btn_divide.pack()


tk.mainloop()
