from tkinter import *
from tkinter import ttk

from Views import *
from tkinter import messagebox

#colors used here 
Co0="#ffffff"
Co1= "#000000"
Co2="#4456F0"

window= Tk()
window.title(" ")
window.geometry('490x500')
window.configure(background=Co0)
window.resizable(width=FALSE,height=FALSE)

#Frame
Frame_up=Frame(window , width=650,height=50,bg=Co2)
Frame_up.grid(row=0,column=0,padx=0,pady=1)

Frame_down=Frame(window , width=650,height=150,bg=Co0)
Frame_down.grid(row=1,column=0,padx=0,pady=1)

Frame_table=Frame(window , width=500,height=100,bg=Co0,relief="flat")
Frame_table.grid(row=2,column=0,padx=10,pady=1,columnspan=2,sticky=NW)

#Function
def show():
    global tree
    list_header=['Name','Phone','Email','Address']
    demo_list=view()

    tree= ttk.Treeview(Frame_table,selectmode='extended',columns=list_header,show="headings")

    vsb = ttk.Scrollbar(Frame_table,orient="vertical",command=tree.yview)
    hsb = ttk.Scrollbar(Frame_table,orient="horizontal",command=tree.xview)

    tree.configure(yscrollcommand=vsb.set , xscrollcommand=hsb.set)

    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')

    #Tree head
    tree.heading(0,text='Name',anchor=NW)
    tree.heading(1,text='Phone',anchor=NW)
    tree.heading(2,text='Email',anchor=NW)
    tree.heading(3,text='Address',anchor=NW)

    #tree columns
    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=90, anchor='nw')
    tree.column(2, width=150, anchor='nw')
    tree.column(3, width=100, anchor='nw')

    for item in demo_list:
        tree.insert('','end',values=item)

show()

def insert():
    Name = e_name.get()
    Phone = e_Ph.get()
    Email = e_email.get()
    Address = e_address.get()

    data = [Name, Phone, Email, Address]

    if Name == '' or Phone == '' or Email == '' or Address == '':
        messagebox.showwarning('data', 'Please fill in all fields')

    else:
        add(data)
        messagebox.showinfo('data', 'data added successfully')

        e_name.delete(0, 'end')
        e_Ph.delete(0, 'end')
        e_email.delete(0, 'end')
        e_address.delete(0, 'end')

        show()

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Name = str(tree_list[0])
        Phone = str(tree_list[1])
        Email = str(tree_list[2])
        Address = str(tree_list[3])

        e_name.insert(0, Name)
        e_Ph.insert(0, Phone)
        e_email.insert(0, Email)
        e_address.insert(0, Address)

        def confirm():
            new_Name = e_name.get()
            new_Phone = e_Ph.get()
            new_Email = e_email.get()
            new_Address = e_address.get()

            data = [new_Phone, new_Name, new_Phone, new_Email, new_Address]

            update(data)

            messagebox.showinfo('Success', 'data updated successfully')

            e_name.delete(0, 'end')
            e_Ph.delete(0, 'end')
            e_email.delete(0, 'end')
            e_address.delete(0, 'end')

            for widget in Frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()

        b_confirm =  Button(Frame_down, text="Confirm", width=10, height=1, bg=Co2, fg = Co0, font=('Ivy 8 bold'), command=confirm)
        b_confirm.place(x = 290, y = 110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')


def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_Phone = str(tree_list[2])

        remove(tree_Phone)

        messagebox.showinfo('Success', 'Data has been deleted successfully')

        for widget in Frame_table.winfo_children():
            widget.destroy()
        show()

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')


def to_search():
    Phone = e_search.get()

    data = search(Phone)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values = item)

    e_search.delete(0, 'end')

#frame_up widget
app_name=Label(Frame_up,text="Contact Book",fg=Co0,height=1,bg=Co2,font='Verdana 17 bold')
app_name.place(x=5,y=5)

#frame_down widgets,l=label,e=entry,b=button
l_name=Label(Frame_down,text="Name",width=20,height=1,bg=Co0,anchor=NW)
l_name.place(x=10,y=20)
e_name=Entry(Frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_name.place(x=80,y=20)

l_Ph=Label(Frame_down,text="Phone",width=20,height=1,bg=Co0,anchor=NW)
l_Ph.place(x=10,y=50)
e_Ph=Entry(Frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_Ph.place(x=80,y=50)

l_email=Label(Frame_down,text="Email",width=20,height=1,bg=Co0,anchor=NW)
l_email.place(x=10,y=80)
e_email=Entry(Frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_email.place(x=80,y=80)

l_addess=Label(Frame_down,text="Address",width=20,height=1,bg=Co0,anchor=NW)
l_addess.place(x=10,y=110)
e_address=Entry(Frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_address.place(x=80,y=110)

b_search=Button(Frame_down,text="Search",bg=Co2,fg=Co0,command=to_search)
b_search.place(x=290,y=20)
e_search=Entry(Frame_down,width=18,justify='left',highlightthickness=1,relief="solid")
e_search.place(x=350,y=20)

b_view=Button(Frame_down,text="View",bg=Co2,fg=Co0,width=8,command=show)
b_view.place(x=290,y=50)

b_add=Button(Frame_down,text="Add",bg=Co2,fg=Co0,width=8,command=insert)
b_add.place(x=390,y=50)

b_update=Button(Frame_down,text="Update",bg=Co2,fg=Co0,width=8,command=to_update)
b_update.place(x=390,y=80)

b_delete=Button(Frame_down,text="Delete",bg=Co2,fg=Co0,width=8,command=to_remove)
b_delete.place(x=390,y=110)

window.mainloop()