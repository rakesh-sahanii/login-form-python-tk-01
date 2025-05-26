import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Login Form")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#121212")

def show():
    username = "usernamE"
    password = "123456"
    image_path = "assets/image.jpg"

    if entry1.get() == username and entry2.get() == password:
        img = Image.open(image_path)
        img = img.resize((300, 200))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

mainframe = tk.Frame(root, bg="#121212")
mainframe.pack()

headingLabel = tk.Label(mainframe, text="Login Form".upper(), font=("Arial, 30"), bg="#121212", pady="40", fg="#ffffff")
headingLabel.grid(row=0, column=0, columnspan=2)

label1 = tk.Label(mainframe, text="Username: ", font=("Arial, 16"), bg="#121212", fg="#ffffff")
label1.grid(row=1, column=0)

entry1 = tk.Entry(mainframe, font=("Arial, 16"))
entry1.grid(row=1, column=1, columnspan=2)

label2 = tk.Label(mainframe, text="Password: ", font=("Arial, 16"), bg="#121212", fg="#ffffff")
label2.grid(row=2, column=0)

entry2 = tk.Entry(mainframe, font=("Arial, 16"), show="*")
entry2.grid(row=2, column=1)

button1 = tk.Button(mainframe, text="Login", bg="red", fg="#ffffff", font=("Arial, 16"), padx="20", command=show)
button1.grid(row=3, column=0, columnspan=2, pady=(20, 0))

image_label = tk.Label(mainframe, bg="#121212")
image_label.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
