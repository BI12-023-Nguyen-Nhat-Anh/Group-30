from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from main import list_user
from GUI.login import phone, password
from domain.customer import customer
from assets.set_logo import logo
from themes.theme import theme
import pandas as pd
import re
import random



window = Tk()
window.title("Electric")
window.geometry("1080x720")
window.resizable(False,False)
logo(window)
theme(window)
global random_number
random_number = random.randint(1000, 9999)



def delete_showerror():
    delete = messagebox.showerror("Error!","Your email is not correct! Try again.")
    if delete == "ok":
        delete.destroy()

def get_identity():
    for custom in list_user:
        if(custom.get_phone()==phone):
            if(custom.get_password()==password):
                MyLabel15.config(text= custom.get_id_card())

def formula_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
        return delete_showerror()


    
myFrame = Frame(window, width=9999, height=9999, )
myFrame.pack(fill=BOTH, expand=True)

Mylabel = Label(window, text="REGISTER FOR ELECTRIC PURCHASE", height=1, font=('bold', 25), border=10, fg="#fff")
Mylabel.place(relx=0.28, rely=0.01)

Mylabel2 = Label(window, text="Personal information", font=50, border=10, fg="#fff")
Mylabel2.place(relx=0.01, rely=0.05)

Mylabel3 = Label(window, text="Full Name (Right click to delete text)", width=27, fg="#fff")
Mylabel3.place(relx=0.02, rely=0.1)

Mylabel4 = Label(window, text="Email (Right click to delete text)", width=25, fg="#fff")
Mylabel4.place(relx=0.5, rely=0.1)

Mylabel5 = Label(window, text="Electricity supply information", font=140, border=10, fg="#fff")
Mylabel5.place(relx=0.01, rely=0.25)

Mylabel6 = Label(window, text="Province/City (Right click to delete text)", width=29, fg="#fff")
Mylabel6.place(relx=0.019, rely=0.32)

Mylabel7 = Label(window, text="District (Right click to delete text)", width=28, fg="#fff")
Mylabel7.place(relx=0.335, rely=0.32)

Mylabel8 = Label(window, text="Ward/ Commune (Right click to delete text)", width=32, fg="#fff")
Mylabel8.place(relx=0.68, rely=0.32)

Mylabel9 = Label(window, text="Electricity usage address (Right click to delete text)", width=37, fg="#fff")
Mylabel9.place(relx=0.02, rely=0.50)

Mylabel10 = Label(window, text="Residential adress (Right click to delete text)", width=32, fg="#fff")
Mylabel10.place(relx=0.51, rely=0.5)

Mylabel11 = Label(window, text="Intended use (Right click to delete text)", width=32, fg="#fff")
Mylabel11.place(relx=0.01, rely=0.7)

Mylabel12 = Label(window, text="Tax identification numbers (Right click to delete text)", width=40, fg="#fff")
Mylabel12.place(relx=0.51, rely=0.7)

Mylabel13 = Label(window, text= "Identify card: ",width=13, fg = "#fff",font=('Bold',15))
Mylabel13.place(relx= 0.69,rely=0.95)

MyLabel15 = Label(window, text = "",fg = "#fff",font=(15))
MyLabel15.place(relx=0.81, rely=0.94, relwidth=0.15, relheight=0.06)
get_identity()

MyEntry = Entry(window, borderwidth=5, font=25)
MyEntry.bind("<Button-3>", lambda e: MyEntry.delete(0, END))
MyEntry.place(relx=0.02, rely=0.13, relwidth=0.45, relheight=0.06)

MyEntry1 = Entry(window, borderwidth=5, font=25)
MyEntry1.bind("<Button-3>", lambda e: MyEntry1.delete(0, END))
MyEntry1.place(relx=0.5, rely=0.13, relwidth=0.45, relheight=0.06)


MyEntry2 = Entry(window, borderwidth=5, font=25)
MyEntry2.bind("<Button-3>", lambda e: MyEntry2.delete(0, END))
MyEntry2.place(relx=0.02, rely=0.35, relwidth=0.3, relheight=0.06)

MyEntry3 = Entry(window, borderwidth=5, font=25)
MyEntry3.bind("<Button-3>", lambda e: MyEntry3.delete(0, END))
MyEntry3.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.06)

MyEntry4 = Entry(window, borderwidth=5, font=25)
MyEntry4.bind("<Button-3>", lambda e: MyEntry4.delete(0, END))
MyEntry4.place(relx=0.68, rely=0.35, relwidth=0.3, relheight=0.06)

MyEntry5 = Entry(window, borderwidth=5, font=25)
MyEntry5.bind("<Button-3>", lambda e: MyEntry5.delete(0, END))
MyEntry5.place(relx=0.02, rely=0.53, relwidth=0.45, relheight=0.06)

MyEntry6 = Entry(window, borderwidth=5, font=25)
MyEntry6.bind("<Button-3>", lambda e: MyEntry6.delete(0, END))
MyEntry6.place(relx=0.51, rely=0.53, relwidth=0.45, relheight=0.06)

MyEntry7 = Entry(window, borderwidth=5, font=25)
MyEntry7.bind("<Button-3>", lambda e: MyEntry7.delete(0, END))
MyEntry7.place(relx=0.02, rely=0.73, relwidth=0.45, relheight=0.06)


MyEntry8 = Entry(window, borderwidth=5, font=25)
MyEntry8.bind("<Button-3>", lambda e: MyEntry8.delete(0, END))
MyEntry8.place(relx=0.515, rely=0.73, relwidth=0.45, relheight=0.06)


def Save_Data():
    df = pd.read_excel('data/data_customer.xlsx', sheet_name='data_customer')

    df1 = pd.read_excel('data/data_customer.xlsx', sheet_name='filtered_data')

    writer = pd.ExcelWriter('data/data_customer.xlsx', engine='openpyxl')
   
    #Take the data from user input
    name = MyEntry.get()
    email = MyEntry1.get()
    province = MyEntry2.get()
    district = MyEntry3.get()
    ward = MyEntry4.get()
    electricity_usage = MyEntry5.get()
    residental_adress = MyEntry6.get()
    intended_use = MyEntry7.get()
    tax = MyEntry8.get()
    for custom in list_user:
        if(custom.get_phone()==phone):
            if(custom.get_password()==password):
                ident = custom.get_id_card()
    
    # Take the information to customer file
    get_customer = customer(ident,name,email,residental_adress,intended_use,tax)
    
    
    if intended_use == "Household":
        
        name = MyEntry.get()
        email = MyEntry1.get()
        province = MyEntry2.get()
        district = MyEntry3.get()
        ward = MyEntry4.get()
        electricity_usage = MyEntry5.get()
        residental_adress = MyEntry6.get()
        intended_use = MyEntry7.get()
        
        for custom in list_user:
            if(custom.get_phone()==phone):
                if(custom.get_password()==password):
                    ident = custom.get_id_card()
        ident = get_customer.get_id()
        name_cus = get_customer.get_name()
        address = get_customer.get_address()
        type_cus = get_customer.get_type()
        tax_cus = get_customer.get_tax()
        mail = get_customer.get_mail()


        
        if (name == "") or (email == "") or (province == "") or (district == "") or (ward == "") or (residental_adress == "") or (intended_use == ""):
            messagebox.showerror("Error!","You need to fill in all the blank!")
        else:
            if formula_email(email) == False:
                formula_email(email)
            else:
                new_data = {'Customer Code': f'CH00120300{str(random_number)}','Name':name_cus,'Electricity usage address': electricity_usage,'Residential address': address,'Phone Number': str(phone),'Email': mail,'Identity number': str(ident),'Tax Code':'None','Type': type_cus, 'Status': "Active"}
                df_new = pd.DataFrame(new_data,index=[0])
                updated_df = pd.concat([df,df_new], ignore_index=True)
                updated_df.to_excel(writer, sheet_name='data_customer', index=False)

                new_data_1 = {'Customer Code': f'CH00120300{str(random_number)}','Name': name_cus,'Electricity usage address': electricity_usage,'Phone Number': str(phone),'Identity number': str(ident),'Tax Code': 'None','Type': type_cus, 'Status': "Active"}
                df1_new = pd.DataFrame(new_data_1,index=[0])
                updated_df_1 = pd.concat([df1,df1_new], ignore_index=True)
                updated_df_1.to_excel(writer, sheet_name='filtered_data', index=False)
                window.destroy()
    else:
        
        name = MyEntry.get()
        email = MyEntry1.get()
        province = MyEntry2.get()
        district = MyEntry3.get()
        ward = MyEntry4.get()
        electricity_usage = MyEntry5.get()
        residental_adress = MyEntry6.get()
        intended_use = MyEntry7.get()
        tax = MyEntry8.get()
        for custom in list_user:
            if(custom.get_phone()==phone):
                if(custom.get_password()==password):
                    ident = custom.get_id_card()
        ident = get_customer.get_id()
        name_cus = get_customer.get_name()
        address = get_customer.get_address()
        type_cus = get_customer.get_type()
        tax_cus = get_customer.get_tax()
        mail = get_customer.get_mail()
        
        
        if (name == "") or (email == "") or (province == "") or (district == "") or (ward == "") or (residental_adress == "") or (intended_use == "") or (tax == ""):
            messagebox.showerror("Error!","You need to fill in all the blank!")
        else:
            
            if formula_email(email) == False:
                formula_email(email)
            else:
                new_data = {'Customer Code': f'CH00120300{str(random_number)}','Name':name_cus,'Electricity usage address': electricity_usage,'Residential address': address,'Phone Number': str(phone),'Email': mail,'Identity number': str(ident),'Tax Code':tax,'Type': type_cus, 'Status': "Active"}
                df_new = pd.DataFrame(new_data,index=[0])
                updated_df = pd.concat([df,df_new], ignore_index=True)
                updated_df.to_excel(writer, sheet_name='data_customer', index=False)

                new_data_1 = {'Customer Code': f'CH00120300{str(random_number)}','Name': name_cus,'Electricity usage address': electricity_usage,'Phone Number': str(phone),'Identity number': str(ident),'Tax Code': tax,'Type': type_cus, 'Status': "Active"}
                df1_new = pd.DataFrame(new_data_1,index=[0])
                updated_df_1 = pd.concat([df1,df1_new], ignore_index=True)
                updated_df_1.to_excel(writer, sheet_name='filtered_data', index=False)
                window.destroy()
    writer.book.save('data/data_customer.xlsx')
    import domain.MeterReading
    
    
def Clear_Data():
    MyEntry.delete(0,END)
    MyEntry1.delete(0,END)
    MyEntry2.delete(0,END)
    MyEntry3.delete(0,END)
    MyEntry4.delete(0,END)
    MyEntry5.delete(0,END)
    MyEntry6.delete(0,END)
    MyEntry7.delete(0,END)
    MyEntry8.delete(0,END)

def onClick_Province():
    def Close_tab():
        listbox.destroy()
        myFrame.destroy()
        MyButton.config(image=my_img)
        MyButton.config(command=onClick_Province)

    def on_select(event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            value = widget.get(selection)
            MyEntry2.delete(0, END)
            MyEntry2.insert(0, value)
            myFrame.destroy()
            listbox.destroy()
    myFrame = Frame(window, bg="#fff", borderwidth=2, relief="solid")
    myFrame.place(relx=0.02, rely=0.42, height=30, relwidth=0.26)

    listbox = Listbox(myFrame,font=(20))
    listbox.place(width=277,height=25)
    
    
    listbox.insert(END, "Hanoi")
    

    listbox.bind("<<ListboxSelect>>", on_select)

    # update the button command to close the tab
    MyButton.config(command=Close_tab)

def onClick_District():
    def Close_tab():
        listbox.destroy()
        myFrame1.destroy()
        MyButton1.config(image=my_img)
        MyButton1.config(command=onClick_District)

    def on_select(event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            value = widget.get(selection)
            MyEntry3.delete(0, END)
            MyEntry3.insert(0, value)
            listbox.destroy()
            myFrame1.destroy()
        
    myFrame1 = Frame(window, bg="#fff",borderwidth=2, relief="solid")
    myFrame1.place(relx=0.35, rely=0.42, height=250, relwidth=0.26)

    listbox = Listbox(myFrame1,font=(20))
    listbox.place(width=277,height=246)
    

    listbox.insert(END, "Bac Tu Liem")
    listbox.insert(END, "Ba Dinh")
    listbox.insert(END, "Cau Giay")
    listbox.insert(END, "Dong Da")
    listbox.insert(END, "Hai Ba Trung")
    listbox.insert(END, "Hoan Kiem")
    listbox.insert(END, "Ha Dong")
    listbox.insert(END, "Hoang Mai")
    listbox.insert(END, "Long Bien")
    listbox.insert(END, "Thanh Xuan")
    listbox.insert(END, "Tay Ho")
    listbox.insert(END, "Nam Tu Liem")
    
    listbox.bind("<<ListboxSelect>>", on_select)
    # update the button command to close the tab
    MyButton1.config(command=Close_tab)

def onClick_Ward():
    def Close_tab():
        listbox.destroy()
        myFrame2.destroy()
        MyButton2.config(image=my_img)
        MyButton2.config(command=onClick_Ward)

    def on_select(event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            value = widget.get(selection)
            MyEntry4.delete(0, END)
            MyEntry4.insert(0, value)
            listbox.destroy()
            myFrame2.destroy()
        
    myFrame2 = Frame(window, bg="#fff",borderwidth=2, relief="solid")
    myFrame2.place(relx=0.68, rely=0.42, height=250, relwidth=0.26)

    listbox = Listbox(myFrame2,font=(20))
    listbox.place(width=277,height=246)
    
    
    listbox.insert(END, "Dich Vong")
    listbox.insert(END, "Dich Vong Hau")
    listbox.insert(END, "Mai Dich")
    listbox.insert(END, "Nghia Do")
    listbox.insert(END, "Nghia Tan")
    listbox.insert(END, "Quan Hoa")
    listbox.insert(END, "Trung Hoa")
    listbox.insert(END, "Yen Hoa")
    listbox.insert(END, "Long Bien")
    listbox.insert(END, "Thanh Xuan")
    listbox.insert(END, "Tay Ho")
    listbox.insert(END, "Nam Tu Liem")
    listbox.insert(END, "Cong Vi")
    listbox.insert(END, "Dien Bien")
    listbox.insert(END, "Doi Can")
    listbox.insert(END, "Co Nhue")
    listbox.insert(END, "Duc Thang")
    listbox.insert(END, "Phu Diem")
    listbox.insert(END, "Minh Khai")
    listbox.insert(END, "Cat Linh")
    listbox.insert(END, "Kham Thien")
    listbox.insert(END, "Lang Ha")
    listbox.insert(END, "Bien Giang")
    listbox.insert(END, "Dong Mai")
    
    listbox.bind("<<ListboxSelect>>", on_select)
    # update the button command to close the tab
    MyButton2.config(command=Close_tab)

def onClick_Intended():
    def Close_tab():
        myFrame3.destroy()
        MyButton3.config(image=my_img)
        MyButton3.config(command=onClick_Intended)

        
    def on_select(event):
       
       if listbox.curselection() != ():
            selection = listbox.get(listbox.curselection())
            MyEntry7.delete(0,END)
            MyEntry7.insert(0,selection)
            listbox.destroy()
            myFrame3.destroy()
            global MyLabel14
            
            if selection == "Household":
                 
                MyLabel14 = Label(window, text="You cannot type here",bg="#313131")
                MyLabel14.place(relx=0.515, rely=0.73, relwidth=0.45, relheight=0.06)
                MyEntry7.delete(0,END)
                MyEntry7.insert(0,selection)
                 
            elif selection == "Administrative office":
                
                if Mylabel4.winfo_exists():
                    MyLabel14.destroy()
                    selection = listbox.get(listbox.curselection())
                    MyEntry7.delete(0,END)
                    MyEntry7.insert(0,selection)
                    
                else:
                    selection = listbox.get(listbox.curselection())
                    MyEntry7.delete(0,END)
                    MyEntry7.insert(0,selection)
                
            elif selection == "Business":
                
                if Mylabel4.winfo_exists():
                    MyLabel14.destroy()
                    selection = listbox.get(listbox.curselection())
                    MyEntry7.delete(0,END)
                    MyEntry7.insert(0,selection)
                    
                else:
                    selection = listbox.get(listbox.curselection())
                    MyEntry7.delete(0,END)
                    MyEntry7.insert(0,selection)
                
                
            elif selection == "Manufacturing industry":
                
                if Mylabel4.winfo_exists():
                    MyLabel14.destroy()
                    selection = listbox.get(listbox.curselection())
                    MyEntry7.delete(0,END)
                    MyEntry7.insert(0,selection)
                    
                else:
                    selection = listbox.get(listbox.curselection())
                    MyEntry7.delete(0,END)
                    MyEntry7.insert(0,selection)
                
                
            else:
                return False
                

    myFrame3 = Frame(window, bg="#fff",borderwidth=2, relief="solid")
    myFrame3.place(relx=0.02, rely=0.8, height=100, relwidth=0.40)

    listbox = Listbox(myFrame3,font=(20))
    listbox.place(width=428, height=96)
    
    
    listbox.insert(END, "Household")
    listbox.insert(END, "Administrative office")
    listbox.insert(END, "Business")
    listbox.insert(END, "Manufacturing industry")
    
    
    listbox.bind("<<ListboxSelect>>", on_select)
    MyButton3.config(command=Close_tab)

my_img = ImageTk.PhotoImage(Image.open("assets/Arrow_7.png"))

MyButton = Button(image=my_img, fg="#313131", bd=0, activebackground="#313131", activeforeground="#313131",
command=onClick_Province)
MyButton.place(relx=0.276, rely=0.36, relwidth=0.04, relheight=0.036)

MyButton1 = Button(image=my_img, fg="#313131", bd=0, activebackground="#313131", activeforeground="#313131",
command=onClick_District)
MyButton1.place(relx=0.605, rely=0.36, relwidth=0.04, relheight=0.036)

MyButton2 = Button(image=my_img, fg="#313131", bd=0, activebackground="#313131", activeforeground="#313131",
command=onClick_Ward)
MyButton2.place(relx=0.935, rely=0.36, relwidth=0.04, relheight=0.036)

MyButton3 = Button(image=my_img, fg="#313131", bd=0, activebackground="#313131", activeforeground="#313131",
command=onClick_Intended)
MyButton3.place(relx=0.425, rely=0.74, relwidth=0.04, relheight=0.036)

MyButton4 = Button(window, text="Save",fg="#fff", activebackground="#313131", activeforeground="#313131",command=Save_Data)
MyButton4.place(relx= 0.35,rely= 0.9, relwidth= 0.1, relheight= 0.05)

MyButton5 = Button(window, text="Clear",fg="#fff", activebackground="#313131", activeforeground="#313131",command=Clear_Data)
MyButton5.place(relx= 0.50,rely= 0.9, relwidth= 0.1, relheight= 0.05)


window.mainloop()