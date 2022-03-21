# link to the code for displaying an image:
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

import tkinter as tk
from tkinter import *
##from PIL import ImageTk, Image 

# main window
window = tk.Tk()
canvas = tk.Canvas(window, width = 900, height = 600)
canvas.pack()

img = PhotoImage(file="lab4_morsecode.png") 

panel = tk.Label(window, image = img)
canvas.create_image(300,20, anchor=NW, image=img)

# just some labeling
label1 = tk.Label(master=window, text="Latest letter: ", bg="white")
label1.place(x=50, y=100)

label2 = tk.Label(master=window, text="History: ", bg="white")
label2.place(x=50, y=200)

label3 = tk.Label(master=window, text="Current Input: ", bg="white")
label3.place(x=50, y=300)

# sadly does not show a button
##fr_buttons = tk.Frame(canvas)
##btn = tk.Button(window, text="button?")
##btn.grid(row=0, column=0, sticky="nsew")

# uncomment me to see a button
##btn = tk.Button(master=canvas, text="boop")
##btn.grid(row=50, column=50, sticky="nsew")





#mainloop()  
