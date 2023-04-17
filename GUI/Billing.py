from tkinter import *
from tkinter import ttk
from domain.customer import customer
from domain.MeterReading import user_data,amount
from Billing_Payments import total, Household_payment,Administrative_offices_payment,Business_payment,Manufacturing_industries_payment
from Bill_Caculate import late_fee
from GUI.register import random_number
window = Tk()
window.title("Bill")
window.geometry("360x480")
window.resizable(False,False)

# Create a style
style = ttk.Style(window)
# Import the tcl file
theme_path = "assets/forest-dark.tcl"
# Load the theme file
window.tk.call("source", theme_path)

# Set the theme with the theme_use method
style.theme_use("forest-dark")

def get_total():
    if customer.get_type() == "HouseHold":
        Household_payment()
    elif customer.get_type() == "Administrative_offices":
        Administrative_offices_payment()
    elif customer.get_type() == "Business":
        Business_payment()
    elif customer.get_type() == "Manufacturing_industries":
        Manufacturing_industries_payment()
    else:
        return False

MyLabel = Label(window,text="Billing Payment",bg= "#313131",font=("Helvetica", 20, "bold"))
MyLabel.place(relx = 0.005, rely = 0.01,relheight=0.10,relwidth=0.99)

MyLabel1 = Label(window,text="Name :",bg="#313131",font=("Helvetica", 12))
MyLabel1.place(relx = 0.08, rely= 0.15)

MyLabel2 = Label(window,text="Customer Code :",bg="#313131",font=("Helvetica", 12))
MyLabel2.place(relx = 0.08, rely= 0.25)

MyLabel3 = Label(window,text="Electric Consumption :",bg="#313131",font=("Helvetica", 12))
MyLabel3.place(relx = 0.08, rely= 0.35)

MyLabel4 = Label(window,text= "ID Card :",bg="#313131",font=("Helvetica", 12))
MyLabel4.place(relx = 0.08, rely= 0.45)

MyLabel5 = Label(window, text="Address :",bg="#313131",font=("Helvetica", 12))
MyLabel5.place(relx = 0.08, rely= 0.55)

MyLabel13 = Label(window, text="Type :",bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel13.place(relx = 0.08, rely= 0.65)

MyLabel15 = Label(window, text= "Price :",bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel15.place(relx = 0.08, rely= 0.75)

MyLabel17 = Label(window, text= "Late Fee :",bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel17.place(relx = 0.08, rely= 0.85)

MyLabel6 = Label(window, text="Total cost :",bg="#313131",font=("Helvetica",18,"italic"))
MyLabel6.place(relx = 0.02, rely= 0.94)

MyLabel7 = Label(window, text= customer.get_name(),bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel7.place(relx = 0.3, rely= 0.15)

MyLabel8 = Label(window, text=f"CH{str(random_number)}",bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel8.place(relx = 0.5, rely= 0.25)

MyLabel9 = Label(window, text= user_data,bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel9.place(relx = 0.6, rely= 0.35)

MyLabel10 = Label(window, text= customer.get_id(),bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel10.place(relx = 0.35, rely= 0.45)

MyLabel11 = Label(window, text= customer.get_address(),bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel11.place(relx = 0.3, rely= 0.55)

MyLabel14 = Label(window, text= customer.get_type(),bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel14.place(relx = 0.3, rely= 0.65)

MyLabel16 = Label(window, text= amount,bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel16.place(relx = 0.3, rely= 0.75)

MyLabel18 = Label(window, text= late_fee,bg="#313131",font=("Helvetica", 12, "italic"))
MyLabel18.place(relx = 0.3, rely= 0.85)

MyLabel12 = Label(window, text=total,bg="#313131",font=("Helvetica", 18, "italic"))
MyLabel12.place(relx = 0.4, rely= 0.94)
get_total()
window.mainloop()


