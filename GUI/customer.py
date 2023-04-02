from tkinter import *
from tkinter.font import Font
import openpyxl

window = Tk()
window.title('Customer list')

# adjust size
window.geometry("1280x719")
# tells the root to not let the widgets inside it determine its size.
window.pack_propagate(False)
window.resizable(0, 0)  # makes the root window fixed in size.

# set the background image
img = PhotoImage(file="assets/customer.png")

# create a canvas on top of the label to make it clickable
canvas = Canvas(window, width=img.width(), height=img.height())
canvas.place(x=0, y=0)

# display the image on the canvas
canvas.create_image(0, 0, image=img, anchor="nw")

# add a rectangle to the canvas to define the clickable region
rect_dashboard = canvas.create_rectangle(16, 62, 158, 93, fill="", outline="")
canvas.tag_bind(rect_dashboard, "<Button-1>",
                lambda event: switch_window_dashboard())

rect_bill = canvas.create_rectangle(16, 136, 158, 167, fill="", outline="")
canvas.tag_bind(rect_bill, "<Button-1>", lambda event: switch_window_bill())


def switch_window_dashboard():
    window.destroy()
    import GUI.dashboard


def switch_window_bill():
    window.destroy()
    import GUI.bill


window.mainloop()
