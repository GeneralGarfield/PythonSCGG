# Import libraries
import tkinter as tk
from PIL import Image, ImageTk
import os

#THis should make it the same directory
directory_path = os.path.dirname(__file__)
file_path = os.path.join(directory_path, 'DK.png')
# Create the window
window = tk.Tk()
window.geometry("480x480")

# Create the Label
text_label = tk.Label(window, text="Click on the button for a surprise")
text_label.pack()

# Load the Image
def DK():
    picture = Image.open(file_path)
    image = ImageTk.PhotoImage(picture)
    image_label = tk.Label(window, image=image)
    image_label.image = image
    image_label.pack()

# Create the button
def MainButton():
    button = tk.Button(window, text="Click Here!", command=DK)
    button.pack()

# Initialize the button
MainButton()

# Run the Tkinter event loop
window.mainloop()
