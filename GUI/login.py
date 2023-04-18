import tkinter as tk
import os
from tkinter import messagebox
from PIL import Image, ImageTk
from main import list_user
from main import admin_data
from domain.user import user
from assets.set_logo import logo

def back_button(root):
    root.destroy()
    login()

# check_login function takes input from user then compare with the data 
def check_login(phone_input, password_input):
    global phone, password
    phone=phone_input.get()
    password=password_input.get()
    if(phone!='') and (password!=''):
        for custom in list_user:
            if(custom.get_phone()==phone):
                if(custom.get_password()==password):
                    root.destroy()
                    import GUI.register
                    return custom.get_id_card()
        if(admin_data.get_id()==phone):
            if(admin_data.get_password()==password):
                root.destroy()
                import GUI.customer
                return True
    messagebox.showerror("Invalid","Please try again!")
    root.destroy()
    login()

# check_reset function takes input from the user to update the new password for user
def check_reset(id_card, password_input, confirm_password):
    global id, password, con_password
    id=id_card.get()
    password=password_input.get()
    con_password=confirm_password.get()
    if(con_password==password) and (id!=""):
        for custom in list_user:
            if(id==custom.get_id_card()):
                custom.add_password(con_password)
                with open("data/user.txt","w") as f:
                    f.write(f"{admin_data.get_id()},{admin_data.get_password()}\n")
                    for custom in list_user:
                        print(f"{custom.get_id_card()},{custom.get_phone()},{custom.get_password()}")
                        f.write(f"{custom.get_id_card()},{custom.get_phone()},{custom.get_password()}\n")
                f.close()
        root_reset.destroy()
        login()

def check_user(phone_input, id_card, password_input, confirm_password):
    global phone, id, password, confirm 
    phone=phone_input.get()
    id=id_card.get()
    password=password_input.get()
    confirm=confirm_password.get()
    if(phone!="") and (id!="") and (password!="") and (confirm!=""):
        if(password==confirm):
            tk.Label(text="Wrong id template", fg="white", bg="white").place(x=225,y=86)
            with open("data/user.txt","a+") as f:
                f.write(f"{id},{phone},{password}\n")
            f.close()
            k=user(id,phone,password)
            list_user.append(k)
            root_register.destroy()
            login()

# Compare_password function to warn user when password and confirm password do not match
def compare_password(password_input, confirm_password, x,y):
    if(password_input.get()==confirm_password.get()):
        tk.Label(text="Password doesn't match", fg="white", bg="white").place(x=x, y=y)
    else:
        tk.Label(text="Password doesn't match", fg="red", bg="white").place(x=x, y=y)

# check_phone_number function ensures that when a user enters a phone number containing only 10 digits from 0 to 9
def check_phone_number(input):
    if input.isdigit() and len(phone_input.get())<10:
        return True
    elif input=="":
        return True
    else:
        return False
    
def check_identity(input):
    if input.isdigit() and len(id_card.get())<12:
        return True
    elif input=="":
        return True
    else:
        return False

# show_password function shows the user's password otherwise only *, show function will show how to display for user input
def show_password(password_input):
    global password_visible
    password_visible = not password_visible
    if password_visible:
        password_input.config(show="")
    else:
        password_input.config(show="*")

def new_user():
    root.destroy()
    global root_register
    root_register=tk.Tk()
    logo(root_register)
    root_register.geometry("1000x562")
    root_register.title("Register")
    root_register.resizable(False, False)
    img=Image.open("assets/sign_up.png")
    img=img.resize((1000,562))
    background=ImageTk.PhotoImage(img)
    tk.Label(image=background).pack()
    
    identity_card=root_register.register(check_identity)
    global id_card
    id_card = tk.Entry(root_register, validate="key", validatecommand=(identity_card, '%S'), font="assets/Space_Mono/SpaceMono-Regular 13", borderwidth=0, background="white",width=30)
    id_card.place(x=115, y=113)

    number_input = root_register.register(check_phone_number)
    global phone_input
    phone_input = tk.Entry(root_register, validate="key", validatecommand=(number_input, '%S'), font="assets/Space_Mono/SpaceMono-Regular 13", borderwidth=0, background="white",width=30)
    phone_input.place(x=115, y=200)

    password_input = tk.Entry(root_register, font="assets/Space_Mono/SpaceMono-Regular.ttf 13", borderwidth=0, background="white",width=30, show="*")
    password_input.place(x=115, y=285)

    global password_visible
    password_visible = False
    show_password_button = tk.Button(root_register, text="Show", command=lambda: show_password(password_input), borderwidth=0, background="white", activebackground="white")
    show_password_button.place(x=342, y=285)
    
    confirm_password = tk.Entry(root_register, font="assets/Space_Mono/SpaceMono-Regular.ttf 13", borderwidth=0 , background="white",width=30, show="*")
    confirm_password.place(x=115, y=373)

    password_visible = False
    show_password_button = tk.Button(root_register, text="Show", command=lambda: show_password(confirm_password), borderwidth=0, background="white", activebackground="white")
    show_password_button.place(x=342, y=373)

    password_input.bind('<KeyRelease>', lambda event: compare_password(password_input, confirm_password, 270, 345))    
    confirm_password.bind('<KeyRelease>', lambda event: compare_password(password_input, confirm_password, 270, 345))

    img = Image.open("assets/submit.png")
    img = img.resize((321,50))
    submit = ImageTk.PhotoImage(img)
    submit_button = tk.Button(image=submit, background="white", activebackground="white", borderwidth=0, command=lambda: check_user(phone_input, id_card, password_input, confirm_password))
    submit_button.place(x=88, y=427, in_=root_register)

    back=tk.Button(text="Back",command=lambda: back_button(root_register), background="white", border=0,activebackground="white").place(x=10, y=30)
    root_register.mainloop()

def reset():
    root.destroy()  # when run form reset, form login will straightway close to open form reset
    global root_reset
    root_reset=tk.Tk()
    logo(root_reset)
    root_reset.geometry("438x574")
    root_reset.resizable(False, False)
    root_reset.config(bg="white")
    root_reset.title("Reset your password")

    tk.Label(root_reset, text="Reset password", font="assets/Space_Mono/SpaceMono-Regular.ttf 30", bg="white", fg="#645CBB").place(x=70,y=64)

    box=tk.Canvas(root_reset, width=321, height=55, highlightbackground="black", background="white")
    box.create_rectangle(150,150,250,250)
    box.place(x=58,y=180)    
    tk.Label(root_reset,text="Identity card number", bg="white").place(x=70,y=183)

    identity_card=root_reset.register(check_identity)
    global id_card
    id_card = tk.Entry(root_reset, validate="key", validatecommand=(identity_card, '%S'), font="assets/Space_Mono/SpaceMono-Regular 13", borderwidth=0, background="white",width=30)
    id_card.place(x=73, y=207)

    box=tk.Canvas(root_reset, width=321, height=55, highlightbackground="black", background="white")
    box.create_rectangle(150,150,250,250)
    box.place(x=58,y=287)
    tk.Label(root_reset,text="New password", bg="white").place(x=70,y=290)
    password_input = tk.Entry(root_reset, font="assets/Space_Mono/SpaceMono-Regular.ttf 13", borderwidth=0, background="white",width=30, show="*")
    password_input.place(x=73, y=314)
    
    global password_visible
    password_visible = False
    show_password_button = tk.Button(root_reset, text="Show", command=lambda: show_password(password_input), borderwidth=0, background="white", activebackground="white")
    show_password_button.place(x=342, y=314)
    
    box=tk.Canvas(root_reset, width=321, height=55, highlightbackground="black", background="white")
    box.create_rectangle(150,150,250,250)
    box.place(x=58,y=390)
    tk.Label(root_reset,text="Confirm password", bg="white").place(x=70,y=395)
    confirm_password = tk.Entry(root_reset, font="assets/Space_Mono/SpaceMono-Regular.ttf 13", borderwidth=0 , background="white",width=30, show="*")
    confirm_password.place(x=73, y=420)

    # bind function to forcus on new event in this stutation is when user input password_input and confirm_password, compare_password function will compare in real time
    password_input.bind('<KeyRelease>', lambda event: compare_password(password_input, confirm_password, 235, 395))    
    confirm_password.bind('<KeyRelease>', lambda event: compare_password(password_input, confirm_password, 235, 395))

    password_visible = False
    show_password_button = tk.Button(root_reset, text="Show", command=lambda: show_password(confirm_password), borderwidth=0, background="white", activebackground="white")
    show_password_button.place(x=342, y=417)

    # to have a beautiful button I use an image named update.png as a button
    sign_up = Image.open("assets/update.png")
    sign_up = sign_up.resize((321,50))
    sign_up_button = ImageTk.PhotoImage(sign_up)
    update_button = tk.Button(image=sign_up_button, text="Update", background="white", activebackground="white", borderwidth=0, command=lambda: check_reset(id_card, password_input, confirm_password))
    update_button.place(x=60, y=480, in_=root_reset)

    back=tk.Button(text="Back",command=lambda: back_button(root_reset), background="white", border=0,activebackground="white").place(x=10, y=30)
    root_reset.mainloop()

def login():
    global root
    root=tk.Tk()
    logo(root)
    root.geometry("438x574")
    root.resizable(False, False)
    root.config(bg="white")
    root.title("Login")

    tk.Label(root, text="Login", font="assets/Space_Mono/SpaceMono-Regular.ttf 30", bg="white", fg="#645CBB").place(x=169,y=64)
    box=tk.Canvas(root, width=321, height=55, highlightbackground="black", background="white")
    box.create_rectangle(150,150,250,250)
    box.place(x=58,y=180)

    tk.Label(root,text="Phone number", bg="white").place(x=70,y=183)
    number_input = root.register(check_phone_number)
    global phone_input
    phone_input = tk.Entry(root, validate="key", validatecommand=(number_input, '%S'), font="assets/Space_Mono/SpaceMono-Regular 13", borderwidth=0, background="white",width=30)
    phone_input.place(x=73, y=207)

    # to have a beautiful box input, I created a rectangle then I created an input box with boderwith=0 to invisible in front of the user
    box=tk.Canvas(root, width=321, height=55, highlightbackground="black", background="white")
    box.create_rectangle(150,150,250,250)
    box.place(x=58,y=287)

    tk.Label(root,text="Password", bg="white").place(x=70,y=290)

    password_input = tk.Entry(root, font="Arial 13", borderwidth=0, background="white",width=30, show="*")
    password_input.place(x=73, y=314)

    global password_visible
    password_visible = False
    show_password_button = tk.Button(root, text="Show", command=lambda: show_password(password_input), borderwidth=0, background="white", activebackground="white")
    show_password_button.place(x=340, y=314)

    # when user click forget button, user will run reset function
    forget = tk.Button(root, text="Forgot password?", borderwidth=0, command=lambda: reset(), background="white", fg="#645CBB", activebackground="white", activeforeground="light blue")
    forget.place(x=165, y=360)  

    tk.Label(root,text="Don't have an account ?", background="white").place(x=100,y=400)
    tk.Button(root,text="Create one", borderwidth=0, command=lambda: new_user(), activebackground="white", background="white", fg="#645CBB", activeforeground="light blue").place(x=240,y=400)

    # to have a beautiful button I use an image named submit.png as a button
    log_in = Image.open("assets/submit.png")
    log_in = log_in.resize((321,50))
    log_in_button = ImageTk.PhotoImage(log_in)
    submit_button = tk.Button(image=log_in_button, background="white", activebackground="white", borderwidth=0, command=lambda: check_login(phone_input, password_input))
    submit_button.place(x=59, y=430, in_=root)

    root.mainloop()
login()
