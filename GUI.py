import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600")
        self.basecolour = "#a5e07e"

    def makeScene(self):
        frame = tk.Frame(master=self.root, bg=self.basecolour)
        frame.pack(pady=0, padx=0, fill="both", expand=True)

        left_frame = tk.Frame(master=frame, bg="white", width=100)
        left_frame.pack(side="left", fill="y")
        top_frame = tk.Frame(master=frame, bg="white", height=75)
        top_frame.pack(side="top", fill="x", anchor="nw")

        label = tk.Label(master=top_frame, text="Protection program", font=("Roboto", 24), bg="white")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        status = tk.Label(master=frame, text="Your device is protected!", font=("Roboto", 24), bg=self.basecolour)
        status.pack(pady=12, padx=10)

        image = Image.open('profile.png').resize((100, 100), Image.ANTIALIAS)
        prof = ImageTk.PhotoImage(image)
        profile = tk.Button(master=left_frame, image=prof, borderwidth=0, height=100, width=100)
        profile.pack(pady=10)

        logo_image = Image.open("logo.png").resize((100, 100), Image.ANTIALIAS)
        prep = ImageTk.PhotoImage(logo_image)
        logo = tk.Label(master=top_frame, image=prep, borderwidth=0, height=100, width=100)
        logo.pack(side=RIGHT)

        files = tk.Label(master=left_frame, text="Files in custody:", font=("Roboto", 12), bg="white")
        files.pack(pady=10, padx=10)
        uphist = tk.Label(master=left_frame, text="Upload History:", font=("Roboto", 12), bg="white")
        uphist.pack(pady=200)

        self.root.mainloop()

a = GUI()
a.makeScene()