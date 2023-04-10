from PIL import Image, ImageTk

def logo(root):
    # Tải ảnh đầu vào từ tệp tin, ví dụ ảnh png
    img = Image.open('assets/logo.png')

    # Chuyển đổi ảnh sang định dạng PhotoImage
    icon = ImageTk.PhotoImage(img)

    # Thiết lập biểu tượng của ứng dụng bằng ảnh png
    root.call('wm', 'iconphoto', root._w, icon)