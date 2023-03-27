from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.title("Electric")
window.geometry("1080x720")
myFrame = Frame(window,width=9999,height=9999,bg="#fff").pack()


Mylabel = Label(window, text="REGISTER FOR ELECTRIC PURCHASE", height=1,font=('bold',25),border=10,bg="#fff").place(relx = 0.28, rely = 0.01)
Mylabel2 = Label(window,text="Personal information",font= 50,border=10,bg="#fff").place(relx= 0.01, rely = 0.05)
Mylabel3 = Label(window,text="Full Name",width=12,bg="#fff").place(relx= 0.01, rely = 0.1)
Mylabel4 = Label(window,text="Identify card name",width = 15,bg="#fff").place(relx=0.5,rely=0.1)
Mylabel5 = Label(window,text="Electricity supply information",font= 140,border=10,bg="#fff").place(relx = 0.01,rely = 0.25)
Mylabel6 = Label(window,text="Province/City",width=12,bg="#fff").place(relx = 0.015, rely = 0.32)
Mylabel7 = Label(window,text="District",width=12,bg="#fff").place(relx = 0.335,rely = 0.32)
Mylabel8 = Label(window,text="Ward/ Commune",width=13,bg="#fff").place(relx= 0.68, rely = 0.32)
Mylabel9 = Label(window,text="Electricity usage address",width=18,bg="#fff").place(relx= 0.02, rely = 0.50)
Mylabel10 = Label(window,text="Residential adress",width=15,bg="#fff").place(relx= 0.5, rely = 0.5)
Mylabel11 = Label(window,text="Intended use",width=13,bg="#fff").place(relx= 0.01, rely = 0.7)
Mylabel12 = Label(window,text="Tax identification numbers",width=25,bg="#fff").place(relx= 0.5, rely = 0.7)


MyEntry = Entry(window,borderwidth=5,font=25).place(relx=0.02,rely=0.13,relwidth = 0.45,relheight = 0.06)
MyEntry1 = Entry(window,borderwidth=5,font=25).place(relx=0.5,rely=0.13,relwidth = 0.45,relheight = 0.06)
MyEntry2 = Entry(window,borderwidth=5,font=25).place(relx=0.02,rely=0.35,relwidth = 0.3,relheight = 0.06)
MyEntry3 = Entry(window,borderwidth=5,font=25).place(relx=0.35,rely=0.35,relwidth = 0.3,relheight = 0.06)
MyEntry4 = Entry(window,borderwidth=5,font=25).place(relx=0.68,rely=0.35,relwidth = 0.3,relheight = 0.06)
MyEntry5 = Entry(window,borderwidth=5,font=25).place(relx=0.02,rely=0.53,relwidth = 0.45,relheight = 0.06)
MyEntry6 = Entry(window,borderwidth=5,font=25).place(relx=0.51,rely=0.53,relwidth = 0.45,relheight = 0.06)
MyEntry7 = Entry(window,borderwidth=5,font=25).place(relx=0.02,rely=0.73,relwidth = 0.45,relheight = 0.06)
MyEntry8 = Entry(window,borderwidth=5,font=25).place(relx=0.515,rely=0.73,relwidth = 0.45,relheight = 0.06)

def onClick_Province():
    def Close_tab():
        myLable.destroy()
        my_img = ImageTk.PhotoImage(file="assets/Arrow_Down.png")
        MyButton.config(image = my_img)
        MyButton.config(command = onClick_Province)
    myLable = Label(window, text=" ",borderwidth=5,font=25,bg="black")
    myLable.place(relx=0.02,rely=0.42,relwidth = 0.3,relheight = 0.06)
    MyButton.config(text = 'X')
    MyButton.config(command = Close_tab)

def onClick_District():
    def Close_tab():
        myLable.destroy()
        my_img = ImageTk.PhotoImage(Image.open("assets/Arrow_Down.png"))
        MyButton.config(image = my_img)
        MyButton.config(command = onClick_District)
    myLable = Label(window, text=" ",borderwidth=5,font=25,bg="black")
    myLable.place(relx=0.35,rely=0.42,relwidth = 0.3,relheight = 0.06)
    MyButton1.config(text = 'X')
    MyButton1.config(command = Close_tab)

def onClick_Ward():
    def Close_tab():
        myLable.destroy()
        my_img = ImageTk.PhotoImage(Image.open("assets/Arrow_Down.png"))
        MyButton.config(image = my_img)
        MyButton.config(command = onClick_Ward)
    myLable = Label(window, text=" ",borderwidth=5,font=25,bg="black")
    myLable.place(relx=0.68,rely=0.42,relwidth = 0.3,relheight = 0.06)
    MyButton2.config(text = 'X')
    MyButton2.config(command = Close_tab)

def onClick_Intended():
    def Close_tab():
        myLable.destroy()
        my_img = ImageTk.PhotoImage(Image.open("assets/Arrow_Down.png"))
        MyButton.config(image = my_img)
        MyButton.config(command = onClick_Intended)
    myLable =Label(window, text=" ",borderwidth=5,font=25,bg="black")
    myLable.place(relx=0.02,rely=0.8,relwidth = 0.45,relheight = 0.06)
    MyButton3.config(text = 'X')
    MyButton3.config(command = Close_tab)

my_img = ImageTk.PhotoImage(Image.open("assets/Arrow_Down.png"))
MyButton = Button(image = my_img,bg="#fff",borderwidth=5,activebackground="#158aff",activeforeground="white",command=onClick_Province)
MyButton.place(relx = 0.28,rely = 0.35, relwidth = 0.04, relheight = 0.056)
MyButton1 = Button(image= my_img,bg="#fff",borderwidth=5,activebackground="#158aff",activeforeground="white",command=onClick_District)
MyButton1.place(relx = 0.62,rely = 0.35, relwidth = 0.04, relheight = 0.056)
MyButton2 = Button(image= my_img,bg="#fff",borderwidth=5,activebackground="#158aff",activeforeground="white",command=onClick_Ward)
MyButton2.place(relx = 0.94,rely = 0.35, relwidth = 0.04, relheight = 0.056)
MyButton3 = Button(image= my_img,bg="#fff",borderwidth=5,activebackground="#158aff",activeforeground="white",command=onClick_Intended)
MyButton3.place(relx = 0.43,rely = 0.73, relwidth = 0.04, relheight = 0.056)


window.mainloop()



    

