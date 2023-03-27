import tkinter as tk
import threading
from PIL import Image, ImageTk

# Compare_password function to warn user when password and confirm password do not match
def compare_password(password_input, confirm_password):
    if(password_input.get()==confirm_password.get()):
        tk.Label(root_reset, text="Password doesn't match", fg="white", bg="white").place(x=235, y=395)
    else:
        tk.Label(root_reset, text="Password doesn't match", fg="red", bg="white").place(x=235, y=395)

# check_number function ensures that when a user enters a phone number containing only 10 digits from 0 to 9
def check_number(input):
    if input.isdigit() and len(phone_input.get())<10:
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

# check_login function takes input from user then compare with the data 
def check_login(username_input, password_input):
    global user_name, password
    user_name=username_input.get()
    password=password_input.get()
    if(user_name!='') and (password!=''):
        print(user_name)
        print(password)

# check_reset function takes input from the user to update the new password for user
def check_reset(phone_input, password_input, confirm_password):
    global phone, password, con_password
    phone=phone_input.get()
    password=password_input.get()
    con_password=confirm_password.get()
    if(con_password==password) and (phone_input.get()!=""):
        print(phone)
        print(password)
        root_reset.destroy()
        login()

def reset():
    root.destroy()  # when run form reset, form login will straightway close to open form reset
    global root_reset
    root_reset=tk.Tk()
    root_reset.geometry("438x574")
    root_reset.resizable(False, False)
    root_reset.config(bg="white")
    root_reset.title("Reset your password")

    tk.Label(root_reset, text="Reset password", font="assets/Space_Mono/SpaceMono-Regular.ttf 30", bg="white", fg="#645CBB").place(x=70,y=64)

    box=tk.Canvas(root_reset, width=321, height=55, highlightbackground="black", background="white")
    box.create_rectangle(150,150,250,250)
    box.place(x=58,y=180)    
    tk.Label(root_reset,text="Phone number", bg="white").place(x=70,y=183)
    number_input = root_reset.register(check_number)
    global phone_input
    phone_input = tk.Entry(root_reset, validate="key", validatecommand=(number_input, '%S'), font="assets/Space_Mono/SpaceMono-Regular 13", borderwidth=0, background="white",width=30)
    phone_input.place(x=73, y=207)

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
    password_input.bind('<KeyRelease>', lambda event: compare_password(password_input, confirm_password))    
    confirm_password.bind('<KeyRelease>', lambda event: compare_password(password_input, confirm_password))

    password_visible = False
    show_password_button = tk.Button(root_reset, text="Show", command=lambda: show_password(confirm_password), borderwidth=0, background="white", activebackground="white")
    show_password_button.place(x=342, y=417)

    # to have a beautiful button I use an image named update.png as a button
    sign_up = Image.open("assets/update.png")
    sign_up = sign_up.resize((321,50))
    sign_up_button = ImageTk.PhotoImage(sign_up)
    update_button = tk.Button(image=sign_up_button, text="Update", background="white", activebackground="white", borderwidth=0, command=lambda: check_reset(phone_input, password_input, confirm_password))
    update_button.place(x=60, y=480, in_=root_reset)

    root_reset.mainloop()

def login():
    global root
    root=tk.Tk()
    root.geometry("438x574")
    root.resizable(False, False)
    root.config(bg="white")
    root.title("Login")

    tk.Label(root, text="Login", font="assets/Space_Mono/SpaceMono-Regular.ttf 30", bg="white", fg="#645CBB").place(x=169,y=64)
    box=tk.Canvas(root, width=321, height=55, highlightbackground="black", background="white")
    box.create_rectangle(150,150,250,250)
    box.place(x=58,y=180)

    tk.Label(root,text="Phone number/Username", bg="white").place(x=70,y=183)

    username_input = tk.Entry(root, font="assets/Space_Mono/SpaceMono-Regular.ttf 13", borderwidth=0, background="white",width=30)
    username_input.place(x=73, y=207)

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
    tk.Button(root,text="Create one", borderwidth=0, activebackground="white", background="white", fg="#645CBB", activeforeground="light blue").place(x=240,y=400)

    # to have a beautiful button I use an image named submit.png as a button
    log_in = Image.open("assets/submit.png")
    log_in = log_in.resize((321,50))
    log_in_button = ImageTk.PhotoImage(log_in)
    submit_button = tk.Button(image=log_in_button, background="white", activebackground="white", borderwidth=0, command=lambda: check_login(username_input, password_input))
    submit_button.place(x=59, y=430, in_=root)

    root.mainloop()
login()