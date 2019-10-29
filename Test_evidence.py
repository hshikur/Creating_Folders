import os
import sys
from tkinter import *

#def component_name(): 
#    Device_component_name = e1.get()
#    folder=Label(master)
#    folder.grid(row=0,column=1)     
#creatFolder()

def createFolder():
    try:
        if not os.path.exists(e1):
            os.makedirs(e1)
    except OSError:
        print ('Error: Creating get(). ' +  get())
#        
#def createFolder():
#        if not os.path.exists(e1):
#            os.makedirs(e1)
#        if not os.path.exists(os.path.join(e1, e2):
#            os.makedirs(e2)
# Example
#createFolder('./data/')

#folders = ['folder 01', 'folder 02', 'folder 03']
#root_path = '/tmp'

#def createe():
#     root_path = '/tmp'
#     folders = ['folder 01', 'folder 02', 'folder 03']

#for folder in folders:
#    os.mkdir(os.path.join(root_path, folder))

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
button1=Button(master,text="Create Folders",command=createFolder)
button1.place(x=110, y=110)
 
mainloop() 

