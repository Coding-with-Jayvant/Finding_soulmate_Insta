#insta feature finding Soulmate 
#just 
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import random
import string

def fun(user_inp):
    str2 = user_inp,'&',random.choice(string.ascii_uppercase)
    tk.messagebox.showinfo("your soulmate:",str2)

root = tk.Tk()
root.withdraw()
user_inp = simpledialog.askstring(title="Find your soulmate", prompt="ENter your name:")  
fun(user_inp)
