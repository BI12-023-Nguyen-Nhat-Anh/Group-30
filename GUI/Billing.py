import tkinter as tk
from tkinter import ttk
import openpyxl
from Database import Billing

def search_data():
    billing_id = billing_id_entry.get()
    customer_id = customer_id_entry.get()

    if billing_id != "BillingID":
        results = billing.search_billing(billing_id)
    elif customer_id != "CustomerID":
        results = billing.search_billing_by_customer_id(customer_id)
    else:
        results = []

    reset_treeview()

    for row in results:
        treeview.insert("", "end", values=row)


def reset_treeview():
    for row in treeview.get_children():
        treeview.delete(row)

    for row in billing.search_billing_by_customer_id("*"):
        treeview.insert("", "end", values=row)


def on_treeview_select(event):
    pass  # Add any action to be performed when selecting a row in the treeview

billing = Billing("Billing.xlsx", "Consumption.xlsx", "Customer.xlsx")

root = tk.Tk()
root.title('Billing list')
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
cols = ("BillingID", "CustomerID", "ConsumptionID", "BillingDeadline", "Month", "Year", "BillingAmount",
        "LateFee", "TotalBill", "Status")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScrolly.set, columns=cols, height=13)

treeview.column("BillingID", width=120, anchor="center")
treeview.column("CustomerID", width=120, anchor="center")
treeview.column("ConsumptionID", width=120, anchor="center")
treeview.column("BillingDeadline", width=120, anchor="center")
treeview.column("Month", width=120, anchor="center")
treeview.column("Year", width=120, anchor="center")
treeview.column("BillingAmount", width=120, anchor="center")
treeview.column("LateFee", width=120, anchor="center")
treeview.column("TotalBill", width=120, anchor="center")
treeview.column("Status", width=120, anchor="center")
treeview.bind('<Button-1>', lambda event: on_treeview_select(event))

treeview.pack(fill="both", expand=True)
treeScrolly.config(command=treeview.yview)

# Search & filter
search_frame = ttk.LabelFrame(
    root, text="Search and filter", padding=(20, 10))
search_frame.grid(row=1, column=0, padx=(15, 10),
                  pady=(10, 10), columnspan=2, sticky="nsew")
search_frame.columnconfigure(index=0, weight=1)
search_frame.pack_propagate(False)

# BillingID
billing_id_entry = ttk.Entry(search_frame)
billing_id_entry.insert(0, "BillingID")
billing_id_entry.bind("<Double-Button-1>",
                      lambda e: billing_id_entry.delete(0, "end"))
billing_id_entry.bind("<Button-3>", lambda e: billing_id_entry.insert(
    0, "BillingID") if not billing_id_entry.get() else None)
billing_id_entry.grid(row=1, column=0, columnspan=2, padx=(5, 5), pady=(5, 5))

# CustomerID
customer_id_entry = ttk.Entry(search_frame)
customer_id_entry.insert(0, "CustomerID")
customer_id_entry.bind("<Double-Button-1>",
                       lambda e: customer_id_entry.delete(0, "end"))
customer_id_entry.bind("<Button-3>", lambda e: customer_id_entry.insert(
    0, "CustomerID") if not customer_id_entry.get() else None)
customer_id_entry.grid(row=1, column=2, columnspan=2, padx=(5, 5), pady=(5, 5))

# Search Button
search_button = ttk.Button(search_frame, text="Search", command=search_data)
search_button.grid(row=1, column=4, padx=(5, 5), pady=(5, 5))

# Reset Button
reset_button = ttk.Button(
    search_frame, text="Reset", command=reset_treeview)
reset_button.grid(row=1, column=5, padx=(5, 5), pady=(5, 5))

# Populate the treeview
reset_treeview()

root.mainloop()

