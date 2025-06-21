from tkinter import *
root=Tk()
global f_num
e= Entry(root)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(number):
    nums=e.get()
    e.delete(0,END)
    e.insert(0,nums+number)
def clear():
    e.delete(0,END)
def add():
    global f_num
    global math
    math = "add"
    f_num=int(e.get())
    e.delete(0,END)
def sub():
    global f_num
    global math
    math = "sub"
    f_num=int(e.get())
    e.delete(0,END)
def div():
    global f_num
    global math
    math="div"
    f_num = int(e.get())
    e.delete(0, END)
def mul():
    global f_num
    global math
    math = "mul"
    f_num = int(e.get())
    e.delete(0, END)
def equal():
    global f_num
    s_num=int(e.get())
    e.delete(0,END)
    global math
    if math=="add":
        num=s_num+f_num
    elif math=="div":
        num=f_num/s_num
    elif math == "sub":
        num = f_num - s_num
    elif math=="mul":
        num=f_num*s_num
    f_num=num
    e.insert(0,str(num))
def number_button():
    button1 =Button(root,text="1",padx=10,pady=5,command=lambda:click("1"))
    button2 = Button(root,text="2", padx=10, pady=5,command=lambda:click("2"))
    button3 = Button(root,text="3", padx=10, pady=5,command=lambda:click("3"))
    button4 = Button(root,text="4", padx=10, pady=5,command=lambda:click("4"))
    button5 = Button(root,text="5", padx=10, pady=5,command=lambda:click("5"))
    button6 = Button(root,text="6", padx=10, pady=5,command=lambda:click("6"))
    button7 = Button(root,text="7", padx=10, pady=5,command=lambda:click("7"))
    button8 = Button(root,text="8", padx=10, pady=5,command=lambda:click("8"))
    button9 = Button(root,text="9", padx=10, pady=5,command=lambda:click("9"))
    button0 = Button(root,text="0", padx=10, pady=5,command=lambda:click("0"))
    button_add = Button(root,text="+", padx=9, pady=5,command=add)
    button_clear = Button(root,text="clear", padx=24, pady=5, command=clear)
    button_equal = Button(root,text="=", padx=32, pady=5,command=equal)
    button_sub = Button(root,text="-", padx=10, pady=5,command=sub)
    button_mul = Button(root,text="*", padx=10, pady=5,command=mul)
    button_div = Button(root,text="/", padx=10, pady=5,command=div)

    button7.grid(row=1,column=0)
    button8.grid(row=1, column=1)
    button9.grid(row=1, column=2)
    button6.grid(row=2, column=2)
    button5.grid(row=2, column=1)
    button4.grid(row=2, column=0)
    button3.grid(row=3, column=2)
    button2.grid(row=3, column=1)
    button1.grid(row=3, column=0)
    button0.grid(row=4, column=0)
    button_add.grid(row=5,column=0)
    button_clear.grid(row=4, column=1,columnspan=2)
    button_equal.grid(row=5, column=1,columnspan=2)
    button_sub.grid(row=6,column=0)
    button_mul.grid(row=6,column=1)
    button_div.grid(row=6,column=2)

number_button()
root.mainloop()