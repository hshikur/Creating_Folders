
from tkinter import *
master = Tk()
master.geometry("300x300")
master.title("Test Evidence") 
Label(master, text='Component').grid(row=0) 
Label(master, text='Test round').grid(row=1)
Label(master, text='Study name').grid(row=2)  
e1 = Entry(master) 
e2 = Entry(master)
e3 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
button1=Button(master,text="Create Folders")
button1.place(x=110, y=110)
 
mainloop() 

