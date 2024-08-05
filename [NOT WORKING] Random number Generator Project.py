# This is going to be a Python GUI that just counts. Should be pretty easy.
# NOTE THIS SCRIPT WILL NOT RUN, THERE IS A WORKING VERSION OF THIS FILE IN THE GITHUB. WILL KEEP THIS UP TO REMEMBER SOME OF MY WORK.


import tkinter as tk
import random 

window = tk.Tk()

window.geometry("1920x1020")

greeting = tk.Label(text= "random Number Generator",
                    width= 1020,
                    height= 5,
                    bg="white")

greeting.pack()

def DPtext():
        global entry1
        string = tk.Entry.get()
        tk.Label.configure(text=string)

def DPtext2():
    global entry2
    string = tk.Entry.get()
    tk.Label.configure(text=string)


entry1= tk.Entry(window,
                width= 100)
entry1.focus_set()
entry1.pack()

entry2= tk.Entry(window,
                width= 100)
entry2.focus_set()
entry2.pack()

ok_button = tk.Button(window, text="Okay", width=20,)
ok_button.pack(pady=20)


def num(entry1, entry2):
    X = entry1 - entry2
    return X


def randomnumber():
    nl = num(random.randint(10,20), random.randint(55,64))

result_label = tk.Label(window, text="", font="Courier 22 bold")

result_label.pack(pady=20)



def updated_Label():
    try:
        entry1_value = int(entry1.get())
        entry2_value = int(entry2.get())
    except ValueError:
        result_label.config(text="Please enter valid integers")
        return


label = tk.Label(window,
                 text="",
                 font= "Courier 22 bold",
                 command= updated_Label
)

label.pack()   

window.mainloop()




