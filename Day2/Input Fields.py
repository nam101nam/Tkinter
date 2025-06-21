from tkinter import *
root= Tk("Chuong Trinh")
e = Entry(root,width=50,fg="blue",borderwidth=5)
e.insert(0,"Nhap ten cua ban: ")
e.pack()
def enter_your_name():
    hello="Hello "+e.get()
    label=Label(root,text=hello)
    label.pack()
button=Button(root,text="Enter your name",command=enter_your_name)
button.pack()
root.mainloop()