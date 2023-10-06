from tkinter import *
import string
import random


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabet = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_alphabets + capital_alphabet + numbers + special_characters
    pl_label = int(l_box.get())

    if choice.get()==1:
        p_field.insert(0,random.sample(small_alphabets,pl_label))
    if choice.get()==2:
        p_field.insert(0,random.sample(small_alphabets+capital_alphabet,pl_label))
    if choice.get()==3:
        p_field.insert(0,random.sample(all,pl_label))

    # password=random.sample(all,pl_label)
    # p_field.insert(0,password)


root = Tk()
root.config(bg='Black')
root.geometry('380x390')
choice = IntVar()
Font = ('arial', 13, 'bold')

# password Label
p_label = Label(root, text='  Password Generator  ', fg='White', bg='Black',font=('times new roman',25,'bold'))
p_label.grid(pady=8,padx=15)
# weak radio button
w_button = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
w_button.grid(pady=8)
# medium radio button
m_button = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
m_button.grid(pady=8)
# strong radio button
s_button = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
s_button.grid(pady=8)
# password length label
pl_label = Label(root, text='  Password Length  ', fg='White', bg='Black',font=Font)
pl_label.grid()
# Spin Box
l_box = Spinbox(root, from_=5, to=18, width=8, font=Font)
l_box.grid(pady=8)
# generate Button
g_button = Button(root, text='Generate', font=Font,command=generator)
g_button.grid(pady=10)
# password Field
p_field = Entry(root, width=30, bd=2)
p_field.grid(pady=20)


root.mainloop()
