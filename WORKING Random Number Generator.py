import tkinter as tk
import random as random
from tkinter import messagebox

# Sets the window's dimensions & starts the GUI
window = tk.Tk()

window.geometry("480x480")

# This is the tool randomize the numbers numbers
def equation():
    X = random.randint(-100000000,1000000000) 
    Y = random.randint(-100000000,1000000000)
    N1 = X + Y
    return N1

# Heres whats shows up when clicked
def text():
    msg=messagebox.showinfo("Numbers",equation())


# Intro Text
Hugetext = tk.Label(text= "CLICK ON THE BUTTON TO GENERATE A RANDOM NUMBER",
                    width= 1080,
                    height= 10)
Hugetext.pack()

# Heres the Button
button = tk.Button(text= "Click here!",
                   command= text,                  
)
button.pack()


window.mainloop()

#CREDIT TO @2024 GENERALGARFIELD