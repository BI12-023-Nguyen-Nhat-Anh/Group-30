from tkinter import ttk


def theme(root):
    
    style = ttk.Style(root)
    # Import the tcl file
    root.tk.call("source", "themes/forest-dark.tcl")
    # Set the theme with the theme_use method
    style.theme_use("forest-dark")