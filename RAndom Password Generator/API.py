from tkinter import *
from tkinter import ttk
import string
import random
from tkinter import messagebox

root = Tk()
root.geometry("300x400")
root.resizable(False, False)
root.title("Simple Passord Generator")
root.config(bg="Beige") #YellowGreen

#---------------------------------Function Code----------------------------------------

#All the functions

def enter(e):
    gen_button['bg'] = "Orange"
    gen_button['fg'] = "Black"
    
def leave(e):
    gen_button['bg'] = "Grey"
    gen_button['fg'] = "Black"
    
def password_generation():
    try:
        password_length = Length_pass.get()
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        
        password_store = []
        
        password_store.extend(letters)
        password_store.extend(digits)
        password_store.extend(symbols)
        
        random.shuffle(password_store)
        
        Password.set("".join(password_store[0:password_length]))
    except:
        messagebox.askretrycancel("NO MATCH FOUND" , "TRY AGAIN")
    
# ------------------------Graphical User interface Code-------------------------------- 

# Title of API
title_name = Label(root, text="Password Generator", bg="White", fg="Black", font=("Stencil" , 16), borderwidth=5, relief=RIDGE, padx=5 ,pady=5)
title_name.pack(side=TOP)
title_name.place(x=25, y=10)

# Description Frame
desc_frame = Frame(root , bg = "white" , borderwidth=8 , relief=FLAT)
# desc_frame.pack()
desc_frame.place(x=25 , y=100 , width=250 , height=125)

# Password lenght
pass_len = Label(desc_frame , text="Password Length:-" , bg="White" , font=("Consolas" , 10 , "bold"))
# pass_len.pack()
pass_len.grid(row=0 , column=0 , pady=15)

Length_pass = IntVar()
pass_entry = Entry(desc_frame , textvariable = Length_pass , width=15 , relief=SUNKEN , borderwidth=5)
pass_entry.grid(row=0 , column=1 , padx=10 , pady=5 , sticky=W)
#sticky=w is used to make the entry box not go out of bound

#Frame for generate button
frame2 = Frame(desc_frame , bg="WHITE")
# frame2.grid(row=1 , column=1 , padx=20 , pady=30)
frame2.place(x=0 , y=50)

#passwod generate button
gen_button = Button(frame2 , text="GENERATE" , width=15 , bg="Orange" , fg="Black" , cursor = "hand2" , command=password_generation)
gen_button.pack(side="right" , padx=70 , pady=20)
gen_button.bind("<Enter>" , enter)
gen_button.bind("<Leave>" , leave)

#Frame for Passwords
pass_frame = Frame(root , bg = "White" , )
pass_frame.place(x=25 , y=250 , width=250 , height=100 )

#Password will be generated
pass_label = Label(pass_frame , text="Password" , bg="White" , font=("Consolas" , 12 , "bold"))
pass_label.place(x=90 , y=20)

Password = StringVar()
gen_pass = Entry(pass_frame , textvariable = Password , borderwidth=5 , width=18 , bg="White" , fg = "Blue" , font=("Consolas" , 10 , "bold"))
gen_pass.place(x=58 , y=50)



root.mainloop()
