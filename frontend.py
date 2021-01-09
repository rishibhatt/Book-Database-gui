from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=li.curselection()[0]
    selected_tuple = li.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    li.delete(0,END)
    for row in backend.view():
        li.insert(END,row)
def search_command():
    li.delete(0,END)
    for row in backend.search(title_var.get(),author_var.get(),year_var.get(),isbn_var.get()):
        li.insert(END,row)
def add_command():
    li.delete(0,END)
    backend.insert(title_var.get(),author_var.get(),year_var.get(),isbn_var.get())
    li.insert(END,(title_var.get(),author_var.get(),year_var.get(),isbn_var.get()))


def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_var.get(),author_var.get(),year_var.get(),isbn_var.get())

def close_command():
    window.destroy()

window = Tk()

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)
title_var = StringVar()
e1 = Entry(window,textvariable=title_var)
e1.grid(row=0,column=1)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)
author_var = StringVar()
e2 = Entry(window,textvariable=author_var)
e2.grid(row=0,column=3)


l3 = Label(window,text="Year")
l3.grid(row=1,column=0)
year_var = StringVar()
e3 = Entry(window,textvariable=year_var)
e3.grid(row=1,column=1)


l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)
isbn_var = StringVar()
e4 = Entry(window,textvariable=isbn_var)
e4.grid(row=1,column=3)


li=Listbox(window,width=30)
li.grid(row=2,column=0,rowspan=6,columnspan=4)

li.bind('<<ListboxSelect>>',get_selected_row)

sb = Scrollbar(window)
sb.grid(row=2,column=4,rowspan=6)

li.configure(yscrollcommand=sb.set)
sb.configure(command=li.yview)

b1=Button(window,text="View All",width=12,command= view_command)
b1.grid(row=2,column=5)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=5,)

b3=Button(window,text="Add Entry",width=12,command = add_command)
b3.grid(row=4,column=5)

b4=Button(window,text="Update selected",width=12,command= update_command)
b4.grid(row=5,column=5)

b5=Button(window,text="Delete selected",width=12,command = delete_command)
b5.grid(row=6,column=5)

b6=Button(window,text="Close",width=12,command = close_command)
b6.grid(row=7,column=5)

window.mainloop()
