from tkinter import *
from PIL import ImageTk, Image

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

Mylabel3 = Label(window, text="Full Name", width=12, bg="#fff")
Mylabel3.place(relx=0.01, rely=0.1)

Mylabel4 = Label(window, text="Identify card name", width=15, bg="#fff")
Mylabel4.place(relx=0.5, rely=0.1)

Mylabel5 = Label(window, text="Electricity supply information", font=140, border=10, bg="#fff")
Mylabel5.place(relx=0.01, rely=0.25)

Mylabel6 = Label(window, text="Province/City", width=12, bg="#fff")
Mylabel6.place(relx=0.015, rely=0.32)

Mylabel7 = Label(window, text="District", width=12, bg="#fff")
Mylabel7.place(relx=0.335, rely=0.32)

Mylabel8 = Label(window, text="Ward/ Commune", width=13, bg="#fff")
Mylabel8.place(relx=0.68, rely=0.32)

Mylabel9 = Label(window, text="Electricity usage address", width=18, bg="#fff")
Mylabel9.place(relx=0.02, rely=0.50)

Mylabel10 = Label(window, text="Residential adress", width=15, bg="#fff")
Mylabel10.place(relx=0.5, rely=0.5)

Mylabel11 = Label(window, text="Intended use", width=13, bg="#fff")
Mylabel11.place(relx=0.01, rely=0.7)

Mylabel12 = Label(window, text="Tax identification numbers", width=25, bg="#fff")
Mylabel12.place(relx=0.5, rely=0.7)

MyEntry = Entry(window, borderwidth=5, font=25)
MyEntry.place(relx=0.02, rely=0.13, relwidth=0.45, relheight=0.06)

MyEntry1 = Entry(window, borderwidth=5, font=25)
MyEntry1.place(relx=0.5, rely=0.13, relwidth=0.45, relheight=0.06)

MyEntry2 = Entry(window, borderwidth=5, font=25)
MyEntry2.place(relx=0.02, rely=0.35, relwidth=0.3, relheight=0.06)

MyEntry3 = Entry(window, borderwidth=5, font=25)
MyEntry3.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.06)

MyEntry4 = Entry(window, borderwidth=5, font=25)
MyEntry4.place(relx=0.68, rely=0.35, relwidth=0.3, relheight=0.06)

MyEntry5 = Entry(window, borderwidth=5, font=25)
MyEntry5.place(relx=0.02, rely=0.53, relwidth=0.45, relheight=0.06)

MyEntry6 = Entry(window, borderwidth=5, font=25)
MyEntry6.place(relx=0.51, rely=0.53, relwidth=0.45, relheight=0.06)

MyEntry7 = Entry(window, borderwidth=5, font=25)
MyEntry7.place(relx=0.02, rely=0.73, relwidth=0.45, relheight=0.06)

MyEntry8 = Entry(window, borderwidth=5, font=25)
MyEntry8.place(relx=0.515, rely=0.73, relwidth=0.45, relheight=0.06)


def onClick_Province():
    def Close_tab():
        myFrame.destroy()
        MyButton.config(image=my_img)
        MyButton.config(command=onClick_Province)

    myFrame = Frame(window, bg="#fff", borderwidth=20)
    myFrame.config( highlightbackground="black")
    myFrame.place(relx=0.02, rely=0.42, height=250, relwidth=0.26)

    hanoi_btn = Button(myFrame, text="Hanoi", font=('Bold', 20), fg='black', bg="#fff", bd=0,
                   command=lambda: MyEntry2.insert(0, hanoi_btn["text"]))
    hanoi_btn.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.2)

    # update the button command to close the tab
    MyButton.config(command=Close_tab)

def onClick_District():
    def Close_tab():
        myFrame1.destroy()
        MyButton1.config(image=my_img)
        MyButton1.config(command=onClick_District)

    myFrame1 = Frame(window, bg="black")
    myFrame1.place(relx=0.35, rely=0.42, height=250, relwidth=0.26)

    # create a scrollbar for the frame
    scrollbar = Scrollbar(myFrame1)
    scrollbar.pack(side=RIGHT, fill=Y)

    # create a canvas to hold the buttons and attach the scrollbar to it
    canvas = Canvas(myFrame1, yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    # create a new frame inside the canvas to hold the buttons
    inner_frame = Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    bactuliem_btn = Button(inner_frame, text="BacTuLiem", font=('Bold', 20), fg='white', bg="black", bd=0,
                           command=lambda: MyEntry3.insert(END, "BacTuLiem"))
    bactuliem_btn.pack(fill=X, padx=50, pady=5)

    badinh_btn = Button(inner_frame, text="BaDinh", font=('Bold', 20), fg='white', bg="black", bd=0,
                        command=lambda: MyEntry3.insert(END, "BaDinh"))
    badinh_btn.pack(fill=X, padx=50, pady=5)

    caugiay_btn = Button(inner_frame, text="CauGiay", font=('Bold', 20), fg='white', bg="black", bd=0,
                         command=lambda: MyEntry3.insert(END, "CauGiay"))
    caugiay_btn.pack(fill=X, padx=50, pady=5)

    dongda_btn = Button(inner_frame, text="DongDa", font=('Bold', 20), fg='white', bg="black", bd=0,
                        command=lambda: MyEntry3.insert(END, "DongDa"))
    dongda_btn.pack(fill=X, padx=50, pady=5)

    haibatrung_btn = Button(inner_frame, text="HaiBaTrung", font=('Bold', 20), fg='white', bg="black", bd=0,
                            command=lambda: MyEntry3.insert(END, "HaiBaTrung"))
    haibatrung_btn.pack(fill=X, padx=50, pady=5)

    hoankien_btn = Button(inner_frame, text="HoanKiem", font=('Bold', 20), fg='white', bg="black", bd=0,
                          command=lambda: MyEntry3.insert(END, "HoanKiem"))
    hoankien_btn.pack(fill=X, padx=50, pady=5)

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

    myFrame2 = Frame(window, bg="black")
    myFrame2.place(relx=0.68, rely=0.42, height=250, relwidth=0.26)

    # update the button command to close the tab
    MyButton2.config(command=Close_tab)

def onClick_Intended():
    def Close_tab():
        myFrame3.destroy()
        MyButton3.config(image=my_img)
        MyButton3.config(command=onClick_Intended)

    myFrame3 = Frame(window, bg="black")
    myFrame3.place(relx=0.02, rely=0.8, height=250, relwidth=0.40)

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

window.mainloop()