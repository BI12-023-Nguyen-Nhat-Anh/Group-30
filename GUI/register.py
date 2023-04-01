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

    
    myFrame = Frame(window, bg="#fff", borderwidth=2, relief="solid")
    myFrame.place(relx=0.02, rely=0.42, height=250, relwidth=0.26)

    hanoi_btn = Button(myFrame, text="Ha Noi", font=('Bold', 20), fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                   command=lambda: MyEntry2.insert(0, hanoi_btn["text"]))
    hanoi_btn.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.2)

    # update the button command to close the tab
    MyButton.config(command=Close_tab)

def onClick_District():
    def Close_tab():
        myFrame1.destroy()
        MyButton1.config(image=my_img)
        MyButton1.config(command=onClick_District)

    myFrame1 = Frame(window, bg="#fff",borderwidth=2, relief="solid")
    myFrame1.place(relx=0.35, rely=0.42, height=250, relwidth=0.26)

    # create a scrollbar for the frame
    scrollbar = Scrollbar(myFrame1)
    scrollbar.pack(side=RIGHT, fill=Y)

    # create a canvas to hold the buttons and attach the scrollbar to it
    canvas = Canvas(myFrame1, yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    # create a new frame inside the canvas to hold the buttons
    inner_frame = Frame(canvas, bg="#fff")
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    bactuliem_btn = Button(inner_frame, text="Bac Tu Liem", font=('Bold', 20), fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                           command=lambda: MyEntry3.insert(END, "Bac Tu Liem"))
    bactuliem_btn.pack(fill=X, padx=50, pady=5)

    badinh_btn = Button(inner_frame, text="Ba Dinh", font=('Bold', 20), fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                        command=lambda: MyEntry3.insert(END, "Ba Dinh"))
    badinh_btn.pack(fill=X, padx=50, pady=5)

    caugiay_btn = Button(inner_frame, text="Cau Giay", font=('Bold', 20), fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                         command=lambda: MyEntry3.insert(END, "Cau Giay"))
    caugiay_btn.pack(fill=X, padx=50, pady=5)

    dongda_btn = Button(inner_frame, text="Dong Da", font=('Bold', 20), fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                        command=lambda: MyEntry3.insert(END, "Dong Da"))
    dongda_btn.pack(fill=X, padx=50, pady=5)

    haibatrung_btn = Button(inner_frame, text="Hai Ba Trung", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                            command=lambda: MyEntry3.insert(END, "Hai Ba Trung"))
    haibatrung_btn.pack(fill=X, padx=50, pady=5)

    hoankiem_btn = Button(inner_frame, text="Hoan Kiem", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry3.insert(END, "Hoan Kiem"))
    hoankiem_btn.pack(fill=X, padx=50, pady=5)

    hadong_btn = Button(inner_frame, text="Ha Dong", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry3.insert(END, "Ha Dong"))
    hadong_btn.pack(fill = X, padx= 50, pady=5)

    hoangmai_btn =  Button(inner_frame, text="Hoang Mai", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry3.insert(END, "Hoang Mai"))
    hoangmai_btn.pack(fill=X, padx = 50,pady= 5)

    longbien_btn =  Button(inner_frame, text="Long Bien", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry3.insert(END, "Long Bien"))
    longbien_btn.pack(fill=X, padx = 50,pady= 5)

    thanhxuan_btn = Button(inner_frame, text="Thanh Xuan", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry3.insert(END, "Thanh Xuan"))
    thanhxuan_btn.pack(fill=X, padx = 50,pady= 5)

    tayho_btn = Button(inner_frame, text="Tay Ho", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry3.insert(END, "Tay Ho"))
    tayho_btn.pack(fill=X, padx = 50,pady= 5)

    namtuliem_btn = Button(inner_frame, text="Nam Tu Liem", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry3.insert(END, "Nam Tu Liem"))
    namtuliem_btn.pack(fill=X, padx = 50,pady= 5)

    # update the canvas scroll region
    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # update the button command to close the tab
    MyButton1.config(command=Close_tab)

def onClick_Ward():
    def Close_tab():
        myFrame2.destroy()
        MyButton2.config(image=my_img)
        MyButton2.config(command=onClick_Ward)

    myFrame2 = Frame(window, bg="#fff",borderwidth=2, relief="solid")
    myFrame2.place(relx=0.68, rely=0.42, height=250, relwidth=0.26)

    # create a scrollbar for the frame
    scrollbar1 = Scrollbar(myFrame2)
    scrollbar1.pack(side=RIGHT, fill=Y)

    # create a canvas to hold the buttons and attach the scrollbar to it
    canvas1 = Canvas(myFrame2, yscrollcommand=scrollbar1.set)
    canvas1.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar1.config(command=canvas1.yview)

    # create a new frame inside the canvas to hold the buttons
    inner_frame1 = Frame(canvas1, bg="#fff")
    canvas1.create_window((0, 0), window=inner_frame1, anchor='nw')

    dichvong_btn = Button(inner_frame1, text="Dich Vong", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry4.insert(END, "Dich Vong"))
    dichvong_btn.pack(fill=X, padx = 50,pady= 5)

    dichvonghau_btn =  Button(inner_frame1, text="Dich Vong Hau", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry4.insert(END, "Dich Vong Hau"))
    dichvonghau_btn.pack(fill=X, padx = 50,pady= 5)

    maidich_btn = Button(inner_frame1, text="Mai Dich", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry4.insert(END, "Mai Dich"))
    maidich_btn.pack(fill=X, padx = 50,pady= 5)

    nghiado_btn = Button(inner_frame1, text="Nghia Do", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry4.insert(END, "Nghia Do"))
    nghiado_btn.pack(fill=X, padx = 50,pady= 5)

    nghiatan_btn = Button(inner_frame1, text="Nghia Tan", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry4.insert(END, "Nghia Tan"))
    nghiatan_btn.pack(fill=X, padx = 50,pady= 5)

    quanhoa_btn = Button(inner_frame1, text="Quan Hoa", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry4.insert(END, "Quan Hoa"))
    quanhoa_btn.pack(fill=X, padx = 50,pady= 5)

    trunghoa_btn = Button(inner_frame1, text="Trung Hoa", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry4.insert(END, "Trung Hoa"))
    trunghoa_btn.pack(fill=X, padx = 50,pady= 5)

    yenhoa_btn = Button(inner_frame1, text="YenHoa", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry4.insert(END, "Yen Hoa"))
    yenhoa_btn.pack(fill=X, padx = 50,pady= 5)

    # update the canvas scroll region
    inner_frame1.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox("all"))
    # update the button command to close the tab
    MyButton2.config(command=Close_tab)

def onClick_Intended():
    def Close_tab():
        myFrame3.destroy()
        MyButton3.config(image=my_img)
        MyButton3.config(command=onClick_Intended)

    myFrame3 = Frame(window, bg="#fff",borderwidth=2, relief="solid")
    myFrame3.place(relx=0.02, rely=0.8, height=100, relwidth=0.40)

    # create a scrollbar for the frame
    scrollbar = Scrollbar(myFrame3)
    scrollbar.pack(side=RIGHT, fill=Y)

    # create a canvas to hold the buttons and attach the scrollbar to it
    canvas = Canvas(myFrame3, yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    # create a new frame inside the canvas to hold the buttons
    inner_frame = Frame(canvas, bg="#fff")
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    household_btn = Button(inner_frame, text="HouseHold", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry7.insert(END, "HouseHold"))
    household_btn.pack(fill=X, padx = 50,pady= 5)

    administrativeoffices_btn = Button(inner_frame, text="Administrative Offices", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry7.insert(END, "Administrative Offices"))
    administrativeoffices_btn.pack(fill=X, padx = 50,pady= 5)

    business_btn = Button(inner_frame, text="Business", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry7.insert(END, "Business"))
    business_btn.pack(fill=X, padx = 50,pady= 5)

    manufacturingindustries_btn = Button(inner_frame, text="Manufacturing Industries", font=('Bold', 20),fg='black', bg="#fff", bd=0,activebackground="#fff",activeforeground="#fff",
                          command=lambda: MyEntry7.insert(END, "Manufacturing Industries"))
    manufacturingindustries_btn.pack(fill=X, padx = 50,pady= 5)

    # update the canvas scroll region
    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    # update the button to close the tab
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