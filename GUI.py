import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
from hash import Encrypt
import threading
from Config import Config


class GUI():
    """
    Class to implement the program's GUI
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600")  # size of GUI window
        self.basecolour = "#a5e07e"  # shade of green used in the background of GUI
        self.encrypt = Encrypt()
        self.config = Config()
        self.protectedfiles = self.config.getProtecteds()  # stores all directories that are protected, reads off config

    def homePage(self):
        """
        Description: Constructs the GUI for the program page.
        Input: Self
        Output: Tkinter window containing the GUI
        """
        frame = tk.Frame(master=self.root, bg=self.basecolour)
        frame.pack(pady=0, padx=0, fill="both", expand=True)

        left_frame = tk.Frame(master=frame, bg="white", width=100)
        left_frame.pack(side="left", fill="y")
        top_frame = tk.Frame(master=frame, bg="white", height=75)
        top_frame.pack(side="top", fill="x", anchor="nw")

        ##### LABELS #####
        label = tk.Label(master=top_frame, text="Protection program", font=("Roboto", 24), bg="white")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        status = tk.Label(master=frame, text="Your device is protected!", font=("Roboto", 24), bg=self.basecolour)
        status.pack(pady=12, padx=10)

        ##### IMAGES #####
        image = Image.open('profile.png').resize((100, 100), Image.Resampling.LANCZOS)
        prof = ImageTk.PhotoImage(image)
        profile = tk.Button(master=left_frame, image=prof, borderwidth=0, height=100, width=100, command=self.profile)
        profile.pack(pady=10)

        logo_image = Image.open("logo.png").resize((100, 100), Image.Resampling.LANCZOS)
        prep = ImageTk.PhotoImage(logo_image)
        logo = tk.Label(master=top_frame, image=prep, borderwidth=0, height=100, width=100)
        logo.pack(side=RIGHT)

        ##### Side Labels #####
        files = tk.Label(master=left_frame, text="Files in custody:", font=("Roboto", 12), bg="white")
        files.pack(pady=10, padx=10)
        uphist = tk.Label(master=left_frame, text="Upload History:", font=("Roboto", 12), bg="white")
        uphist.pack(pady=200)

        self.root.mainloop()

    def profile(self):
        """
        Description: Function to be triggered when user clicks profile button. In the profile menu, one should be able
        to see and change what files are under surveillance.
        Input: None, triggered on click.
        Output: User taken to user page.
        """
        for widget in self.root.winfo_children():
            widget.destroy()  # wipe home window

        user_frame = tk.Frame(master=self.root, bg=self.basecolour)
        user_frame.pack(pady=0, padx=0, fill="both", expand=True)
        label = tk.Label(master=user_frame, text="Your profile", font=("Roboto", 24), bg=self.basecolour)
        label.pack(pady=12, padx=10)
        surv = tk.Label(master=user_frame, text="Files under surveillance:", font=("Roboto", 24), bg=self.basecolour)
        surv.pack(pady=50, padx=10)
        self.text = tk.Text(master=user_frame, wrap=tk.WORD, width=40, height=5, bg=self.basecolour, font="Roboto", borderwidth=0, highlightthickness=0)
        self.text.pack(pady=20, padx=10)
        for item in self.protectedfiles:  # fill text with protected files.
            self.text.insert(tk.END, f"{item}\n")
        self.text.config(state=tk.DISABLED)  # Disable keyboard editing when code is live
        change = tk.Button(master=user_frame, text="Change protected directories", font=("Roboto", 12), command=self.browse)
        change.pack(padx=5, pady=15)
        clear = tk.Button(master=user_frame, text="Stop protecting files", font=("Roboto", 12), command=self.clearfile)
        clear.pack(padx=5, pady=20)
        calc = tk.Button(master=user_frame, text="Calculate superhash", font=("Roboto", 12), command=lambda: self.encrypt.makeHash(self.protectedfiles))
        calc.pack(padx=5, pady=20)


    def browse(self):
        """
        Description: Allows the user to select what files to protect upon a button is triggered
        Input: Self
        Output: None, but populates protected files array
        """
        path = filedialog.askdirectory(  # askopenfilenames for files, currently only directories
            initialdir="/",
            title="Select a File or Directory",
            #filetypes=(
            #    ("Text files", "*.txt*"),
            #    ("All files", "*.*"),
            #    ("Directory", "*")  # Allow selection of directories
        )

        # if path:  # checks it exists
        if os.path.isdir(path):  # checks it is a directory
            print(f"Selected directory: {path}")
            for root, dirs, files in os.walk(path):
                for file in files:
                    # Construct the full file path
                    file_path = os.path.join(root, file)
                    if file_path not in self.protectedfiles:  # avoid the addition of duplicates to protected files.
                        self.protectedfiles.append(file_path)
                        self.config.writeConfig(file_path)

            # clear text
            self.text.config(state=tk.NORMAL)
            self.text.delete('1.0', tk.END)

            # Fill text with protected file names
            for item in self.protectedfiles:
                self.text.insert(tk.END, f"{item}\n")

            # Disable editing after updating
            self.text.config(state=tk.DISABLED)

        # else:  # if not a directory then a file
        #    print(f"Selected file: {path}")
        #    self.protectedfiles.append(path)
        else:  # doesn't exist
            print("No file or directory selected.")
        print(self.protectedfiles)


    def clearfile(self):
        self.config.clearConfig()
        self.protectedfiles.clear()

        # clear text
        self.text.config(state=tk.NORMAL)
        self.text.delete('1.0', tk.END)


    def run(self):
        self.root.mainloop()


a = GUI()
a.homePage()