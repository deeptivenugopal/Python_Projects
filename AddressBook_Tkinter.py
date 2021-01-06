#Creating Address Book using Tkinter GUI
'''
These are the step to build a contact book python project:

Importing module
Initializing window
Define buttons
Define functions
'''

#1. Importing module

from tkinter import*
from tkinter import messagebox 

#2. Initializing window
root = Tk()

#Use x for size of the rectangle and not *. Do onot use spaces
root.geometry('400x400')

root.config(bg = 'SlateGray3')

root.title('Address Book')

root.resizable(0,0)


contactlist = [['Deepti Venugopal', '121'],
    ['Mike Daemon', '2323245'],
    ['David Parker', '12121212'],
    ['James Kong', '98989898'],
    ['Mandy Dave', '5656566']]

#Data types in tkinter, holds strings
Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
select.pack(side=LEFT,fill=BOTH, expand=1)

#Define Functions
'''
Selected() function used to return selected value
Addcontact() function used to add new contact
EDIT() function will edit existing contact
DELETE() function will delete selected contact
VIEW() function will view selected contact
EXIT() used to destroy mainloop
RESET() will set the name and number field to empty string
Select_set() will sort the manage the contactlist and also used in other functions
'''

def Selected():
    #print(select.curselection()[0])        
    return int(select.curselection()[0])

def AddContact():
    if Name.get() == '' and Number.get()== '':
        messagebox.showerror("Error","Contact Details is Blank")
        return        
    contactlist.append([Name.get(),Number.get()])
    Select_set()

def EDIT():
    if not select.curselection() == ():
        contactlist[Selected()] = [Name.get(), Number.get()]
        Select_set()
    else:
        messagebox.showerror("Error","No contact selected")
        return

def DELETE():
    if not select.curselection() == ():
        del contactlist[Selected()]
        Select_set()
    else:
        messagebox.showerror("Error","No contact selected")
        return

def VIEW():
    if not select.curselection() == ():
        NAME, PHONE = contactlist[Selected()]
        Name.set(NAME)
        Number.set(PHONE)
    else:
        messagebox.showerror("Error","No contact selected")
        return

def EXIT():
    root.destroy()

def RESET():
    Name.set('')
    Number.set('')

def Select_set():
    contactlist.sort()
    select.delete(0,END)
    for name, phone in contactlist:
        select.insert(END,name)
Select_set()

#4. Define buttons and labels

Label(root, text='NAME', font='arial 12 bold', bg='SlateGray3').place(x=30, y=20)

Entry(root, textvariable = Name).place(x=100, y=20)

Label(root, text='PHONE', font='arial 12 bold', bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable = Number). place(x=130, y=70)

Button(root, text='ADD', font='arial 12 bold', bg='SlateGray4',command=AddContact).place(x=50, y=110)
Button(root, text='EDIT', font='arial 12 bold', bg='SlateGray4',command=EDIT).place(x=50, y=260)

Button(root, text='DELETE', font='arial 12 bold', bg='SlateGray4',command=DELETE).place(x=50, y=210)
Button(root, text='VIEW', font='arial 12 bold', bg='SlateGray4',command=VIEW).place(x=50, y=160)

Button(root, text='EXIT', font='arial 12 bold', bg='tomato',command=EXIT).place(x=300, y=320)
Button(root, text='RESET', font='arial 12 bold', bg='SlateGray4',command=RESET).place(x=50, y=310)

root.mainloop()


