from tkinter import *
from tkinter import messagebox
root = Tk()
root. title( 'Denomination Counter')
root.configure(bg='light blue')
root. geometry ('650x400' )
label = Label(root, image=image, bg='light blue')
label. place(x=180, y=20)
label1 = Label(root, text="Hey User! Welcome to Denomination Counter Application.", bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)
def msg():
    MsgBox = messagebox.showinfo(
"Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()
button1 = Button(root,text="Let's get started!",command=msg,bg= 'brown',fg='white' )
button1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top. title( "Denominations Calculator")
    top.configure(bg='light grey')
    top. geometry("600x350+50+50")
    label = Label (top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')
    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500",bg='light grey')
    l3 = Label(top, text="100", bg='light grey')
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator( ):
      try:
        global amount
        amount = int(entry-get())
        note2000 = amount // 2000
        amount = 2000
        note500 = amount // 500
        amount %= 500
        note100 = amount // 100
        t1. delete(0, END)
        t2. delete(0, END)
        t3. delete(0, END)
        t1. insert(END, str(note2000))
        t2. insert(END, str(note500) ) 
        t3. insert(END, str(note100) )
        