from PIL import Image, ImageTk

def logo(root):
    # Upload logo from folder assets
    img = Image.open('assets/logo.png')

    # Convert photos to PhotoImage format
    icon = ImageTk.PhotoImage(img)

    # Set app icon with png image
    root.iconphoto(True, icon)