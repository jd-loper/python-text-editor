import tkinter as tk
from tkinter import Text, Button, Menubutton, Menu, OptionMenu
from tkinter import filedialog, font as tkfont

root = tk.Tk()
root.title("ApplePy Text Editor")

text = Text(root)
text.grid()


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


button = Button(root, text="Save", command=saveas)
button.grid()

# Font chooser
fonts = list(tkfont.families())
font_var = tk.StringVar(root)
font_var.set("SF Mono")  # default value
font_dropdown = OptionMenu(root, font_var, *fonts)
font_dropdown.grid()


def update_font(*args):
    text.config(font=(font_var.get(), 12))  # assuming font size 12


font_var.trace("w", update_font)

root.mainloop()
