import tkinter as tk
from tkinter import ttk
import openpyxl
import os
from Database import ElectricityConsumption

# Initialize the ElectricityConsumption class
consumption_file = "ElectricityConsumption.xlsx"
meter_reading_file = "MeterReading.xlsx"
ec = ElectricityConsumption(consumption_file, meter_reading_file)

# Set up the main window
root = tk.Tk()
root.title('Electricity Consumption')
root.option_add("*tearOff", False)
root.pack_propagate(False)
root.geometry("1280x720")
root.resizable(0, 0)

# Create a style
style = ttk.Style(root)
# Import the tcl file
root.tk.call("source", "forest-dark.tcl")
# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=0, columnspan=10, padx=(10, 20),
           pady=(10, 10), sticky="nsew")
paned.pack_propagate(False)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# tree frame
treeFrame = ttk.Frame(pane_1)
treeFrame.grid(row=0, column=0, padx=5, pady=5)

# scroll ball
treeScrolly = ttk.Scrollbar(treeFrame)
treeScrolly.pack(side="right", fill="y")

# contents
cols = ("ConsumptionID", "CustomerID", "Month", "Year", "ConsumptionAmount")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScrolly.set, columns=cols, height=13)

treeview.column("ConsumptionID", width=120, anchor="center")
treeview.column("CustomerID", width=120, anchor="center")
treeview.column("Month", width=120, anchor="center")
treeview.column("Year", width=120, anchor="center")
treeview.column("ConsumptionAmount", width=180, anchor="center")

for col_name in cols:
    treeview.heading(col_name, text=col_name)

treeview.pack(fill="both", expand=True)
treeScrolly.config(command=treeview.yview)

def load_data():
    consumption_data = ec.search_consumption_by_customer_id("ID")
    for value_tuple in consumption_data:
        treeview.insert("", tk.END, values=value_tuple)

# Load the data into the treeview
load_data()

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

root.mainloop()
