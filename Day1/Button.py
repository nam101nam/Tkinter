from tkinter import *
i=1
root=Tk("Chuong Trinh")
def click_button():
    global i
    label=Label(root,text=i).pack()
    i+=1
button=Button(root,text="Nhan di!",command=click_button)
button.pack()
root.mainloop()