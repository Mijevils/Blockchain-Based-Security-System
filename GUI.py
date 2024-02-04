import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("900x600")
basecolour = "#a5e07e"
root.configure(bg=basecolour)

def login():
    print("Test")

frame = tk.Frame(master=root, bg=basecolour)
frame.pack(pady=0, padx=0, fill="both", expand=True)

left_frame = tk.Frame(master=frame, bg="white", width=100)
left_frame.pack(side="left", fill="y")
top_frame = tk.Frame(master=frame, bg="white", height=75)
top_frame.pack(side="top", fill="x", anchor="nw")

label = tk.Label(master=top_frame, text="Protection program", font=("Roboto", 24), bg="white")
label.pack(pady=12, padx=10)

status = tk.Label(master=frame, text="Your device is protected!", font=("Roboto", 24), bg=basecolour)
status.pack(pady=12, padx=10)

image = Image.open('profile.png')
image = image.resize((100, 100), Image.ANTIALIAS)
prof = ImageTk.PhotoImage(image)
profile = tk.Button(master=left_frame, image=prof, borderwidth=0, height=100, width=100)
profile.pack(pady=10)

#entry1 = tk.Entry(master=frame)
#entry1.insert(0, "Username")  # Set default text as a placeholder
#entry1.pack(pady=12, padx=10)

#entry2 = tk.Entry(master=frame, show="*")
#entry2.insert(0, "Password")  # Set default text as a placeholder
#entry2.pack(pady=12, padx=10)

#button = tk.Button(master=frame, text="Login", command=login)
#button.pack(pady=12, padx=10)

#checkbox_var = tk.BooleanVar()
#checkbox = tk.Checkbutton(master=frame, text="Remember me", variable=checkbox_var)
#checkbox.pack(pady=12, padx=10)

root.mainloop()
