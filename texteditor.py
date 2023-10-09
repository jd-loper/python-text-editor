import tkinter as tk
from tkinter import Text, Button, Menubutton, Menu, OptionMenu
from tkinter import filedialog, font as tkfont

root = tk.Tk()
root.title("ApplePy Text Editor")


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    with open(savelocation, "w+") as file1:
        file1.write(t)


button = Button(root, text="Save", command=saveas)
button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

fonts = list(tkfont.families())
font_var = tk.StringVar(root)
font_var.set("SF Mono")
font_dropdown = OptionMenu(root, font_var, *fonts)
font_dropdown.grid(row=0, column=1, padx=5, pady=5)


def update_font(*args):
    text.config(font=(font_var.get(), 13))


font_var.trace("w", update_font)

text = Text(root)
text.grid(row=1, column=0, columnspan=2, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

root.mainloop()
