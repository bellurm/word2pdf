import tkinter as tk
from tkinter import filedialog
import tkinter.font as font
import os
from docx2pdf import convert

root = tk.Tk()
root.title("DOCX to PDF")

def add_file():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select File")
    convert(file_path)
    info = tk.Label(frame, text="Converted Successfully!", font=24, bg="green", fg="white")
    info.pack()

def word2pdf(file_path):
    location = r""
    cv = convert(file_path)
    cv.convert(location, start=0, end=None)
    cv.close()

canvas = tk.Canvas(root, height = 500, width = 600)
canvas.pack()

frame = tk.Frame(root, bg="indigo")
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

button = tk.Button(frame, text = "Select File",
        padx = 1000, pady = 50, bg = "dark blue", fg = "white", command = add_file)

button_font = font.Font(size=20)
button["font"] = button_font

button.pack()
root.mainloop()
