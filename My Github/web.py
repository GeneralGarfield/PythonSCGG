import tkinter as tk
import webbrowser as web
from PIL import Image,ImageTk
import os

#Creates the window
window = tk.Tk()
window.geometry("720x480")

# Links the directory to the folder
directory_path = os.path.dirname(__file__)
file_path = os.path.join(directory_path, 'GarfieldCharacter.png')

#Creates the Label
Banner = tk.Label(text= "This is my Github page please Check it out!",
                  bg= "white",
                  width= 1080,
                  height= 5
)
Banner.pack()


# Creates the functions for the website and for the picture to load up

def website():
    web.open("https://github.com/GeneralGarfield/PythonSCGG/")
    
def picture():
    picture = Image.open(file_path)
    image = ImageTk.PhotoImage(picture)
    image_label = tk.Label(window, image=image)
    image_label.image = image
    image_label.pack()
    

    
button_to_google = tk.Button(text= "Github",
                             command= website)
button_to_google.pack()



picture()

window.mainloop()
