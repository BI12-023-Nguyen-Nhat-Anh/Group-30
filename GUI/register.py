from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
window = Tk()
window.title("Electric")
window.geometry("1080x720")
window.resizable(False,False)

myFrame = Frame(window, width=9999, height=9999, bg="#fff")
myFrame.pack(fill=BOTH, expand=True)

Mylabel = Label(window, text="REGISTER FOR ELECTRIC PURCHASE", height=1, font=('bold', 25), border=10, bg="#fff")
Mylabel.place(relx=0.28, rely=0.01)

Mylabel2 = Label(window, text="Personal information", font=50, border=10, bg="#fff")
Mylabel2.place(relx=0.01, rely=0.05)

Mylabel3 = Label(window, text="Full Name (Right click to delete text)", width=27, bg="#fff")
Mylabel3.place(relx=0.02, rely=0.1)

Mylabel4 = Label(window, text="Identify card name (Right click to delete text)", width=33, bg="#fff")
Mylabel4.place(relx=0.5, rely=0.1)

Mylabel5 = Label(window, text="Electricity supply information", font=140, border=10, bg="#fff")
Mylabel5.place(relx=0.01, rely=0.25)

Mylabel6 = Label(window, text="Province/City (Right click to delete text)", width=29, bg="#fff")
Mylabel6.place(relx=0.019, rely=0.32)

Mylabel7 = Label(window, text="District (Right click to delete text)", width=28, bg="#fff")
Mylabel7.place(relx=0.335, rely=0.32)

Mylabel8 = Label(window, text="Ward/ Commune (Right click to delete text)", width=32, bg="#fff")
Mylabel8.place(relx=0.68, rely=0.32)

Mylabel9 = Label(window, text="Electricity usage address (Right click to delete text)", width=37, bg="#fff")
Mylabel9.place(relx=0.02, rely=0.50)

Mylabel10 = Label(window, text="Residential adress (Right click to delete text)", width=32, bg="#fff")
Mylabel10.place(relx=0.51, rely=0.5)

Mylabel11 = Label(window, text="Intended use (Right click to delete text)", width=32, bg="#fff")
Mylabel11.place(relx=0.01, rely=0.7)

Mylabel12 = Label(window, text="Tax identification numbers (Right click to delete text)", width=40, bg="#fff")
Mylabel12.place(relx=0.51, rely=0.7)

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
    
    name = MyEntry.get()
    identify = MyEntry1.get()
    province = MyEntry2.get()
    district = MyEntry3.get()
    ward = MyEntry4.get()
    electricity_usage = MyEntry5.get()
    residental_adress = MyEntry6.get()
    intended_use = MyEntry7.get()
    tax = MyEntry8.get()
    if (name == "") or (identify == "") or (province == "") or (district == "") or (ward == "") or (residental_adress == "") or (intended_use == "") or (tax == ""):
        messagebox.showerror("Error!","You need to fill in all the blank!")
    else:

        with open("data_register.txt",'w') as wf:
            write = wf.write(f"[{name}, {identify}]: {province};{district};{ward};{electricity_usage};{residental_adress};{intended_use};{tax}")
            if write == "":
                write.pop()
            
        if (name != "") and (identify != "") and (province != "") and (district != "") and (ward != "") and (residental_adress != "") and (intended_use != "") and (tax != ""):
            with open("register.txt", 'a') as af:
                with open("data_register.txt",'r') as r:
                    read = r.read()
                r.close()
                af.write(str(read)+ "\n")
        os.remove("data_register.txt")
        window.quit()
    
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
        myFrame.destroy()
        MyButton.config(image=my_img)
        MyButton.config(command=onClick_Province)

    def on_select(envet):
        if listbox.curselection() != ():
                
            selected = listbox.get(listbox.curselection())
            MyEntry2.delete(0,END)
            MyEntry2.insert(0,selected)

    myFrame = Frame(window, bg="#fff", borderwidth=2, relief="solid")
    myFrame.place(relx=0.02, rely=0.42, height=250, relwidth=0.26)

    listbox = Listbox(myFrame,font=(20))
    listbox.place(width=277,height=246)
    
    
    listbox.insert(END, "Hanoi")
    

    listbox.bind("<<ListboxSelect>>", on_select)

    # update the button command to close the tab
    MyButton.config(command=Close_tab)

def onClick_District():
    def Close_tab():
        myFrame1.destroy()
        MyButton1.config(image=my_img)
        MyButton1.config(command=onClick_District)

    def on_select(envet):
        if listbox.curselection() != ():
            selected = listbox.get(listbox.curselection())
            MyEntry3.delete(0,END)
            MyEntry3.insert(0,selected)

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
        myFrame2.destroy()
        MyButton2.config(image=my_img)
        MyButton2.config(command=onClick_Ward)

    def on_select(envet):
        if listbox.curselection() != ():
            selected = listbox.get(listbox.curselection())
            MyEntry4.delete(0,END)
            MyEntry4.insert(0,selected)

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
    listbox.insert(END, "YenHoa")
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

    def on_select(envet):
        if listbox.curselection() != ():
            selected = listbox.get(listbox.curselection())
            MyEntry7.delete(0,END)
            MyEntry7.insert(0,selected)

    myFrame3 = Frame(window, bg="#fff",borderwidth=2, relief="solid")
    myFrame3.place(relx=0.02, rely=0.8, height=100, relwidth=0.40)

    listbox = Listbox(myFrame3,font=(20))
    listbox.place(width=428, height=96)
    
    
    listbox.insert(END, "HouseHold")
    listbox.insert(END, "Administrative Offices")
    listbox.insert(END, "Business")
    listbox.insert(END, "Manufacturing Industries")
    
    
    listbox.bind("<<ListboxSelect>>", on_select)
    MyButton3.config(command=Close_tab)

my_img = ImageTk.PhotoImage(Image.open("assets/Arrow_1.png"))

MyButton = Button(image=my_img, bg="#fff", bd=0, activebackground="#fff", activeforeground="white",
command=onClick_Province)
MyButton.place(relx=0.276, rely=0.36, relwidth=0.04, relheight=0.036)

MyButton1 = Button(image=my_img, bg="#fff", bd=0, activebackground="#fff", activeforeground="white",
command=onClick_District)
MyButton1.place(relx=0.605, rely=0.36, relwidth=0.04, relheight=0.036)

MyButton2 = Button(image=my_img, bg="#fff", bd=0, activebackground="#fff", activeforeground="white",
command=onClick_Ward)
MyButton2.place(relx=0.935, rely=0.36, relwidth=0.04, relheight=0.036)

MyButton3 = Button(image=my_img, bg="#fff", bd=0, activebackground="#fff", activeforeground="white",
command=onClick_Intended)
MyButton3.place(relx=0.425, rely=0.74, relwidth=0.04, relheight=0.036)

MyButton4 = Button(window, text="Save",bg="#fff", activebackground="#fff", activeforeground="white",command=Save_Data)
MyButton4.place(relx= 0.35,rely= 0.9, relwidth= 0.1, relheight= 0.05)

MyButton5 = Button(window, text="Clear",bg="#fff", activebackground="#fff", activeforeground="white",command=Clear_Data)
MyButton5.place(relx= 0.50,rely= 0.9, relwidth= 0.1, relheight= 0.05)



window.mainloop()