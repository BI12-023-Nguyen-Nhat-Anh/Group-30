import tkinter as tk
import openpyxl
from tkinter import ttk

root = tk.Tk()
root.title('Customer list')
root.option_add("*tearOff", False)
root.pack_propagate(False)
root.geometry("1440x720")
root.resizable(0, 0)
# Create a style
style = ttk.Style(root)
# Import the tcl file
root.tk.call("source", "forest-dark.tcl")
# Set the theme with the theme_use method
style.theme_use("forest-dark")


"""
=================TREEVIEW======================================
===============================================================
"""
# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=0, columnspan=10, padx=(10, 20),
           pady=(25, 5), sticky="nsew")


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
cols = ("Customer Code", "Name", "Electricity usage address", "Phone Number",
        "Identity number", "Tax Code", "Type", "Status")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScrolly.set, columns=cols, height=13)

treeview.column("Customer Code", width=120, anchor="center")
treeview.column("Name", width=140)
treeview.column("Electricity usage address", width=330)
treeview.column("Phone Number", width=120, anchor="center")
treeview.column("Identity number", width=120, anchor="center")
treeview.column("Tax Code", width=120, anchor="center")
treeview.column("Type", width=160)
treeview.column("Status", width=70, anchor="center")

treeview.pack(fill="both", expand=True)
treeScrolly.config(command=treeview.yview)


def load_data():
    path = "data/data_customer.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook["filtered_data"]

    list_values = list(sheet.values)
    print(list_values)
    for col_name in list_values[0]:
        if col_name in cols:
            treeview.heading(col_name, text=col_name)

    for value_tuple in list_values[1:]:
        treeview.insert("", tk.END, values=value_tuple)


"""
=================Search and filter======================================
===============================================================
"""
# search & filter
search_frame = ttk.LabelFrame(
    root, text="Search and filter", padding=(20, 10))
search_frame.grid(row=1, column=0, padx=(20, 10),
                  pady=(20, 10), columnspan=1, sticky="nsew")
search_frame.columnconfigure(index=0, weight=1)

# ID
id_entry = ttk.Entry(search_frame)
id_entry.insert(0, "ID")
# focusIn: click on entry and the default text disappears
id_entry.bind("<FocusIn>", lambda e: id_entry.delete(0, "end"))
id_entry.bind("<FocusOut>", lambda e: id_entry.insert(
    0, "ID") if not id_entry.get() else None)
id_entry.grid(row=1, column=0, pady=10, sticky="ew")


# Name
name_entry = ttk.Entry(search_frame)
name_entry.insert(0, "Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete(0, "end"))
name_entry.bind("<FocusOut>", lambda e: name_entry.insert(
    0, "Name") if not name_entry.get() else None)
name_entry.grid(row=2, column=0, pady=10, sticky="ew")

root.bind("<FocusOut>", lambda e: id_entry.insert(
    0, "ID") if not id_entry.get() else None)
root.bind("<Leave>", lambda e: name_entry.insert(
    0, "Name") if not name_entry.get() else None)

# Type
type_list = ["Manufacturing industry",
             "Administrative office", "Business", "Household"]
type_combo = ttk.Combobox(search_frame, state="readonly", values=type_list)
type_combo.set("Type")
# right-click to clear the option
type_combo.bind("<Button-3>", lambda event: clear_selection_type(event))


def clear_selection_type(event):
    type_combo.selection_clear()
    type_combo.set("Type")


type_combo.grid(row=3, column=0, pady=10, sticky="ew")

# Status
status_list = ["Active", "Inactive"]
status_combo = ttk.Combobox(search_frame, state="readonly", values=status_list)
status_combo.set("Status")
status_combo.bind("<Button-3>", lambda event: clear_selection_status(event))


def clear_selection_status(event):
    status_combo.selection_clear()
    status_combo.set("Status")


status_combo.grid(row=4, column=0, pady=10, sticky="ew")


# Search button
search_button = ttk.Button(search_frame, text="Search", style="Accent.TButton")
search_button.grid(row=5, column=0, pady=15, sticky="nsew")
search_button.bind("<Button-1>", lambda event: search(event))


def search(event):
    # Get the values from the search inputs
    id_value = id_entry.get()
    name_value = name_entry.get()
    type_value = type_combo.get()
    status_value = status_combo.get()

    # Clear the treeview
    treeview.delete(*treeview.get_children())

    # Filter the data based on the search inputs
    path = "data/data_customer.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook["filtered_data"]
    list_values = list(sheet.values)
    filtered_data = []
    for value_tuple in list_values[1:]:
        if (id_value == "ID" or id_value in value_tuple) and (name_value == "Name" or name_value in value_tuple) and (type_value == "Type" or type_value in value_tuple) and (status_value == "Status" or status_value in value_tuple):
            filtered_data.append(value_tuple)

    # Update the treeview with the filtered data
    for value_tuple in filtered_data:
        treeview.insert("", tk.END, values=value_tuple)


# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

load_data()
root.mainloop()
