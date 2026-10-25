import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as font
import os
from docx2pdf import convert

root = tk.Tk()
root.title("DOCX to PDF")

def add_file():
    file_path = filedialog.askopenfilename(title="Select DOCX", filetypes=[("Word documents", "*.docx")])
    if not file_path:
        return
    try:
        word2pdf(file_path)
    except Exception as exc:
        messagebox.showerror("Conversion failed", str(exc))
        return
    messagebox.showinfo("Conversion complete", "PDF saved beside the source document.")

def word2pdf(file_path):
    # docx2pdf.convert performs the conversion and returns None.
    convert(file_path)

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
