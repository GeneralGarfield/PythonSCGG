import tkinter as Tk

window = Tk.Tk()

greeting = Tk.Label(text="This Button Does Nothing",
                    width= 30,
                    height= 10,
                    bg="Black",
                    fg= "white")

Button = Tk.Button(
    text= "This Does nothing",
    width= 30,
    height= 5 ,
    bg = "red",
    fg = "white",
)
greeting.pack()

Button.pack()


window.mainloop()

