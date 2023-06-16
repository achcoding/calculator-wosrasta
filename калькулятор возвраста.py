from tkinter import *

window = Tk()
window.title("Калькулятор возвраста")
window.geometry('400x200')
lbl = Label(window, text='Введите свой возвраст', font=("Arial", 16))
lbl.pack()
lbl2 = Label(window, text='Ваш возвраст', font=("Arial", 16))
lbl2.place(x=150, y = 100)
r1 = Entry(width=25)
r1.pack()
p1 = Entry(width=15)
p1.place(x=150, y=150)

def rost(h):
    h = h
    return h
def green():
    p1.delete(0, END)
    result = rost(r1.get())
    p1.insert(0, result)
btn = Button(window, command=green, text="=")
btn.place(x=160, y=70)
input()
