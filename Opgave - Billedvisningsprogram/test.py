# Import Module
from tkinter import *
from PIL import Image, ImageTk
import os

# Create Tkinter Object
root = Tk()

# Read the Image
dirlist = os.listdir(
        'C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data')
print(dirlist)
image = Image.open(f'C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{dirlist[-1]}')

# Resize the image using resize() method
resize_image = image.resize((20, 20))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

# Execute Tkinter
root.mainloop()