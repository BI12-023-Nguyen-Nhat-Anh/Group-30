from tkinter import *
from tkinter.font import Font
import openpyxl

root = Tk()
root.title('Customer list')

# adjust size
root.geometry("1280x719")
# tells the root to not let the widgets inside it determine its size.
root.pack_propagate(False)
root.resizable(0, 0)  # makes the root window fixed in size.

# set the background image
img = PhotoImage(file="assets/Bill.png")

# create a canvas on top of the label to make it clickable
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.place(x=0, y=0)

# display the image on the canvas
canvas.create_image(0, 0, image=img, anchor="nw")

# add a rectangle to the canvas to define the clickable region
rect_dashboard = canvas.create_rectangle(16, 62, 158, 93, fill="", outline="")
canvas.tag_bind(rect_dashboard, "<Button-1>",
                lambda event: switch_window_dashboard())

rect_cus = canvas.create_rectangle(16, 102, 158, 133, fill="", outline="")
canvas.tag_bind(rect_cus, "<Button-1>", lambda event: switch_window_customer())


def switch_window_dashboard():
    root.destroy()
    import dashboard


def switch_window_customer():
    root.destroy()
    import customer


root.mainloop()
