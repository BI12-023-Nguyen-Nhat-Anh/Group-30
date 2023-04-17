import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import openpyxl
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# Initialize root window
root = tk.Tk()
root.title("Billing Chart")
root.geometry("1280x960")
root.resizable(False, False)
root.withdraw()  # Hide root window initially

# Configure custom theme
style = ttk.Style(root)
theme_path = "assets/forest-dark.tcl"
root.tk.call("source", theme_path)
style.theme_use("forest-dark")

# Load customer data from Excel file
def load_data():
    file_path = "data/Billing.xlsx"
    df = pd.read_excel(file_path)
    return df

data = load_data()

filtered_data = None

# Get Customer ID
def get_customer_id():
    global customer_id
    customer_id_win = tk.Toplevel(root)
    customer_id_win.title("Enter Customer ID")
    customer_id_win.resizable(False, False)

    ttk.Label(customer_id_win, text="Enter Customer ID:").pack(padx=5, pady=(5, 0), anchor="w")
    customer_id_entry = ttk.Entry(customer_id_win)
    customer_id_entry.pack(padx=5, pady=(0, 5), anchor="w")

    def submit():
        global customer_id
        customer_id = customer_id_entry.get()

        if customer_id not in data["CustomerID"].unique():
            messagebox.showerror("Error", "Customer ID not found.")
        else:
            customer_id_win.destroy()
            main_app()

    ttk.Button(customer_id_win, text="Submit", command=submit).pack(padx=5, pady=5, anchor="w")
    customer_id_win.mainloop()

# Main application
def main_app():
    root.deiconify()
    global filtered_data
    # Filter data based on customer ID
    filtered_data = data[data["CustomerID"] == customer_id].sort_values(["Year", "Month"])

    # Create frames
    chart_pane = ttk.Frame(root, width=1200, height=600)
    chart_pane.grid(row=0, column=0, columnspan=2, sticky="nsew")

    details_pane = ttk.Frame(root, width=600, height=150)
    details_pane.grid(row=1, column=0, sticky="nsew")

    export_pane = ttk.Frame(root, width=600, height=150)
    export_pane.grid(row=1, column=1, sticky="nsew")

    # Configure grid weights
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # Chart type variable
    chart_type = tk.StringVar()
    chart_type.set("BillingAmount")

    # Plot chart function
    def plot_chart():
        # Clear existing chart
        ax.clear()

        # Modified function to generate command for checkbuttons
        def create_toggle_line_visibility_fn(checkbutton_var, line):
            def toggle_line_visibility():
                line.set_visible(checkbutton_var.get())
                canvas.draw()

            return toggle_line_visibility

        lines = []  # Store line objects for the custom legend
        for year in filtered_data["Year"].unique()[-3:]:
            year_data = filtered_data[filtered_data["Year"] == year]
            months = year_data["Month"].tolist()
            values = year_data[chart_type.get()].tolist()
            line, = ax.plot(months, values, label=str(year), marker='o', picker=5)  # Added ',' after line to unpack the tuple
            lines.append(line)

        # Create custom legend with checkbuttons
        legend_items = []
        for line in lines:
            checkbutton_var = tk.BooleanVar()
            checkbutton_var.set(True)
            toggle_fn = create_toggle_line_visibility_fn(checkbutton_var, line)  # Generate the command function
            checkbutton = ttk.Checkbutton(canvas.get_tk_widget(), text=line.get_label(), variable=checkbutton_var,  # Use canvas.get_tk_widget()
                                        command=toggle_fn)  # Use the generated function as command
            legend_items.append((line, [checkbutton]))

        legend = ax.legend(handles=[item[0] for item in legend_items], loc='upper left', bbox_to_anchor=(1, 1))

        # Place checkbuttons in the correct position
        for idx, (_, widgets) in enumerate(legend_items):
            widget = widgets[0]
            x = (legend.get_window_extent(renderer=canvas.get_renderer()).xmax + 200)  # Use the legend's window extent to calculate the x position
            y_offset = 20  # Adjust the vertical distance between checkbuttons
            y = legend.get_window_extent(renderer=canvas.get_renderer()).ymin + idx * y_offset  # Calculate the y position for each checkbutton based on the legend's ymin and the y_offset
            widget.place(x=x, y=y)  # Place the checkbuttons in the canvas widget


        # Customize chart
        ax.set_xlabel("Month")
        ax.set_ylabel(chart_type.get())
        ax.set_title(f"{chart_type.get()} Chart")
        ax.set_xticks(range(1, 13))
        if chart_type.get() == "BillingAmount":
            ax.set_ylim(0, max(filtered_data["BillingAmount"]) * 1.2)
        else:
            ax.set_ylim(0, max(filtered_data["TotalBill"]) * 1.2)
        ax.grid()
        canvas.draw()


    # Create chart
    fig = Figure(figsize=(10, 6), dpi=100)
    ax = fig.add_subplot(111)  # Changed variable name from plt to ax
    canvas = FigureCanvasTkAgg(fig, master=chart_pane)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Create a function to handle clicks on chart data points
    def on_pick(event):
        ind = event.ind[0]
        selected_data = filtered_data.iloc[ind]
        details_tab_text.delete(1.0, tk.END)
        details = f"BillingID: {selected_data['BillingID']}\n" \
                  f"CustomerID: {selected_data['CustomerID']}\n" \
                  f"ConsumptionID: {selected_data['ConsumptionID']}\n" \
                  f"BillingDeadline: {selected_data['BillingDeadline']}\n" \
                  f"BillingAmount: {selected_data['BillingAmount']}\n" \
                  f"LateFee: {selected_data['LateFee']}\n" \
                  f"TotalBill: {selected_data['TotalBill']}\n" \
                  f"Status: {selected_data['Status']}"
        details_tab_text.insert(tk.END, details)

    # Connect the pick function to the chart
    canvas.mpl_connect('pick_event', on_pick)

    # Chart type combobox
    chart_type_combobox = ttk.Combobox(details_pane, textvariable=chart_type, state="readonly", values=["BillingAmount", "TotalBill"])
    chart_type_combobox.pack(padx=5, pady=5, anchor="w")
    chart_type_combobox.bind("<<ComboboxSelected>>", lambda _: plot_chart())

    # Details tab
    notebook = ttk.Notebook(details_pane)
    details_tab = ttk.Frame(notebook)
    notebook.add(details_tab, text="Details")
    notebook.pack(fill=tk.BOTH, expand=True)

    details_tab_text = tk.Text(details_tab, wrap=tk.WORD)
    details_tab_text.pack(fill=tk.BOTH, expand=True)

    # Export chart to png
    def export_chart():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            fig.savefig(file_path)

    export_button = ttk.Button(export_pane, text="Export Chart", command=export_chart)
    export_button.pack(padx=5, pady=5, anchor="w")

    # Plot initial chart
    plot_chart()

    # Center the window on the screen and start the tkinter main event loop
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2
    root.geometry(f"+{x}+{y}")
    root.mainloop()

get_customer_id()