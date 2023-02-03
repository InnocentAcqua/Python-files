from tkinter import *

window=Tk()
window.title("Calculator")
ent=Entry(window,width=30,borderwidth=5)
ent.grid(column=0,row=0,columnspan=5,pady=10,padx=10)

def click(number):
    current=ent.get()
    ent.delete(0,END)
    ent.insert(0,str(current)+str(number))

def equal():
    try:
        y= str(eval(ent.get()))
        ent.delete(0,END)
        ent.insert(0,y)

    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

def clear():
    ent.delete(0,END)


but_click0 = Button(window, text="0", padx=40, pady=20, command=lambda: click(0))
but_click1 = Button(window, text="1", padx=40, pady=20, command=lambda: click(1))
but_click2 = Button(window, text="2", padx=40, pady=20, command=lambda: click(2))
but_click3 = Button(window, text="3", padx=40, pady=20, command=lambda: click(3))
but_click4 = Button(window, text="4", padx=40, pady=20, command=lambda: click(4))
but_click5 = Button(window, text="5", padx=40, pady=20, command=lambda: click(5))
but_click6 = Button(window, text="6", padx=40, pady=20, command=lambda: click(6))
but_click7 = Button(window, text="7", padx=40, pady=20, command=lambda: click(7))
but_click8 = Button(window, text="8", padx=40, pady=20, command=lambda: click(8))
but_click9 = Button(window, text="9", padx=40, pady=20, command=lambda: click(9))

but_add=Button(window, text="+", padx=40, pady=20, command=lambda: click("+"))
but_subtract=Button(window, text="-", padx=40, pady=20, command=lambda: click("-"))
but_multiply=Button(window, text="*", padx=40, pady=20, command=lambda: click("*"))
but_devide=Button(window, text="/", padx=40, pady=20, command=lambda: click("/"))

but_clear=Button(window, text="C", padx=40, pady=20, command=clear)
but_clear.grid(column=3, row=5)

but_equal=Button(window, text="=", padx=40, pady=20, command=equal)
but_equal.grid(column=1, row=5)

but_click0.grid(column=1, row=1)
but_click1.grid(column=2, row=1)
but_click2.grid(column=3, row=1)
but_click3.grid(column=1, row=2)
but_click4.grid(column=2, row=2)
but_click5.grid(column=3, row=2)
but_click6.grid(column=1, row=3)
but_click7.grid(column=2, row=3)
but_click8.grid(column=3, row=3)
but_click9.grid(column=1, row=4)
but_add.grid(column=2, row=4)
but_subtract.grid(column=3, row=4)
but_multiply.grid(column=1, row=5)
but_devide.grid(column=2, row=5)





window.mainloop()
