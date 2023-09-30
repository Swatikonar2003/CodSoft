from tkinter import  *

def click (event):
    global value
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if value.get().isdigit():
            value1=int(value.get())
        else:
            value1= eval(screen.get())
        value.set(value1)
        screen.update()
    elif text == "c":
         value .set("")
         screen .update()
    else:
        value.set(value.get()+text)
        screen.update()


Main_root=Tk()
Main_root.geometry("350x490")
Main_root.title("Calculator")
value=StringVar()
value.set(" ")
# ipad=internal padding
screen=Entry(Main_root,textvariable=value,font=50)
screen.pack(fill=X,ipadx=8,padx=15,pady=15)

# for 1st line
F1=Frame(Main_root,bg="white")
F1.pack()

B1=Button(F1,text="9",font="12", padx=10, pady=10)
B1.pack(side=LEFT, padx=18, pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="8",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="7",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="/",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)

# For 2nd line
F1=Frame(Main_root,bg="white")
F1.pack()

B1=Button(F1,text="6",font="12", padx=10, pady=10)
B1.pack(side=LEFT, padx=18, pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="5",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="4",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="%",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)

# for 3rd line
F1=Frame(Main_root,bg="white")
F1.pack()

B1=Button(F1,text="3",font="12", padx=10, pady=10)
B1.pack(side=LEFT, padx=18, pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="2",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="1",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="*",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)

# For 4th line
F1=Frame(Main_root,bg="white")
F1.pack()

B1=Button(F1,text="0",font="12", padx=10, pady=10)
B1.pack(side=LEFT, padx=18, pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="-",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="+",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)
B1=Button(F1,text="=",font="12 ", padx=10, pady=10)
B1.pack(side=LEFT,padx=18,pady=12)
B1.bind("<Button-1>", click)

# for 5th line
F1=Frame(Main_root,bg="white")
F1.pack()

B1=Button(F1,text="c",font="12", padx=50, pady=10)
B1.pack(side=LEFT, padx=20, pady=12)
B1.bind("<Button-1>", click)
# B1=Button(F1,text="%",font="12 ", padx=10, pady=10)
# B1.pack(side=LEFT,padx=18,pady=12)
# B1.bind("<Button-1>", click)
# B1=Button(F1,text="=",font="12 ", padx=10, pady=10)
# B1.pack(side=LEFT,padx=18,pady=12)
# B1.bind("<Button-1>", click)

Main_root.mainloop()