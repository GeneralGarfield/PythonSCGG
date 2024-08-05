# FUN FACT: This whole script is not that diffrent from my last one 
# Only some lines were change

# Imports libraries
import tkinter as tk
import socket
from tkinter import messagebox


# Sets the window's dimensions & starts the GUI
window = tk.Tk()

window.geometry("280x280")

# This is the tool finds your local IP address
def IPaddress():
    ip = str(socket.gethostbyname(socket.gethostname()))
    return ip

# Heres whats shows up when clicked
def text():
    msg=messagebox.showinfo("IP Address",IPaddress())


# Intro Text
Hugetext = tk.Label(text= "Click to find your local IP",
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
