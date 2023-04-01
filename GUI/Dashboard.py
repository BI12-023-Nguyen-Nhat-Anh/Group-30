from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Dashboard')

# adjust size
root.geometry("1440x769")
# tells the root to not let the widgets inside it determine its size.
root.pack_propagate(False)
root.resizable(0, 0)  # makes the root window fixed in size.
# set the background image
img = PhotoImage(file="assets/Dashboard.png")
label = Label(root, image=img)
label.place(x=0, y=0)


root.mainloop()
