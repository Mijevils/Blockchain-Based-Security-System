import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
from hash import Encrypt
import threading
from Config import Config
from solidity import Connect
import time
from datetime import *
from tkinter import messagebox
import sys

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
        self.connect = Connect()
        self.protectedfiles = self.config.getProtecteds()  # stores all directories that are protected, reads off config
        self.root.protocol("WM_DELETE_WINDOW", self.onClose)
        self.hash = self.encrypt.makeHash(self.protectedfiles)
        self.timenext = datetime.now() + timedelta(seconds=5)  # change based on how long to wait until next update

    def homePage(self):
        """
        Description: Constructs the GUI for the program page.
        Input: Self
        Output: Tkinter window containing the GUI
        """
        for widget in self.root.winfo_children():
            widget.destroy()  # wipe home window

        frame = tk.Frame(master=self.root, bg=self.basecolour)
        frame.pack(pady=0, padx=0, fill="both", expand=True)
        left_frame = tk.Frame(master=frame, bg="white", width=150)
        left_frame.pack(side="left", fill="y")
        left_frame.pack_propagate(0)
        top_frame = tk.Frame(master=frame, bg="white", height=75)
        top_frame.pack(side="top", fill="x", anchor="nw")
        frame.grid_columnconfigure(0, weight=1)  # Allow the left_frame to resize proportionally
        frame.grid_rowconfigure(0, weight=1)

        ##### LABELS #####
        label = tk.Label(master=top_frame, text="Protection program", font=("Roboto", 24), bg="white")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        status = tk.Label(master=frame, text="Your device is protected!", font=("Roboto", 24), bg=self.basecolour)
        status.pack(pady=12, padx=10)

        ##### IMAGES #####
        image = Image.open('resources\images\profile.png').resize((100, 100), Image.Resampling.LANCZOS)
        prof = ImageTk.PhotoImage(image)
        profile = tk.Button(master=left_frame, image=prof, borderwidth=0, height=100, width=100, command=self.profile)
        profile.pack(pady=10)

        logo_image = Image.open("resources\images\logo.png").resize((100, 100), Image.Resampling.LANCZOS)
        prep = ImageTk.PhotoImage(logo_image)
        logo = tk.Label(master=top_frame, image=prep, borderwidth=0, height=100, width=100)
        logo.pack(side=RIGHT)

        ##### Side Labels #####
        uphist = tk.Label(master=left_frame, text="Upload History:", font=("Roboto", 12), bg="white")
        uphist.pack(pady=10)
        self.timeUpload()
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

        #### HOME BUTTON ####
        home = Image.open('resources\images\home.png').convert("RGBA").resize((100, 100), Image.Resampling.LANCZOS)
        ready = ImageTk.PhotoImage(home)
        back = tk.Button(master=user_frame, image=ready, borderwidth=0, height=100, width=100, command=self.homePage)
        back.image = ready
        back.pack(side="left", anchor='nw', pady=10, padx=0)

        #### LABELS ####
        label = tk.Label(master=user_frame, text="Your profile", font=("Roboto", 24), bg=self.basecolour)
        label.pack(side="top", pady=12, padx=10)
        surv = tk.Label(master=user_frame, text="Files under surveillance:", font=("Roboto", 24), bg=self.basecolour)
        surv.pack(pady=50, padx=10)
        self.text = tk.Text(master=user_frame, wrap=tk.WORD, width=40, height=5, bg=self.basecolour, font="Roboto", borderwidth=0, highlightthickness=0)
        self.text.pack(pady=20, padx=10)
        for item in self.protectedfiles:  # fill text with protected files.
            self.text.insert(tk.END, f"{item}\n")
        self.text.config(state=tk.DISABLED)  # Disable keyboard editing when code is live

        #### BUTTONS ####
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
        """
        Description: Clears the register of protected files, both the array and config file
        Input: None, just self
        Output: None
        """
        self.config.clearConfig()
        self.protectedfiles.clear()

        # clear text
        self.text.config(state=tk.NORMAL)
        self.text.delete('1.0', tk.END)


    def onClose(self):
        """
        Description: Allows program to withdraw but run anyway
        Input: None, just self
        Output: Window appears to close
        """
        self.root.withdraw()

    def timeUpload(self):
        """
        Description: Function to print "hello" to the console.
        Input: None, just self.
        Output: None, but uploads hashes to the eth node every x minutes.
        """
        if self.timenext.strftime('%Y-%m-%d %H:%M') == datetime.now().strftime('%Y-%m-%d %H:%M'):
            self.timenext = self.timenext + timedelta(seconds=5)

            hash = self.encrypt.makeHash(self.protectedfiles)
            if hash != self.hash:
                # hash = self.connect.getHash()
                self.ChangePopup()
                #### Pause everything until user clicks accept or something
                self.hash = hash
                # if user clicks no try and retrieve the file that changed?
            print(hash)
            self.connect.deployContract(hash)  # npx node has to be active for this to work !!
        self.root.after(10000, self.timeUpload)  # time in milliseconds

    def ChangePopup(self):
        answer = messagebox.askyesno("Change in files",
                                     "There has been a change in the protected files. If this was not you, or you didn't trigger it in any way (installing a program may have changed these files) we recommend reaching out to a professional. Do you wish to stop the program until this issue is resolved?",
                                     icon='warning')
        if answer:
            messagebox.showinfo("Response", "Shutting down.")
            sys.exit(1)
        else:
            messagebox.showinfo("Response", "Resuming upload.")
        # popupRoot = Toplevel(self.root)
        # button = tk.Label(popupRoot, text="Warning", command=self.halt)
        # button.pack(pady=20)
        # popupText = tk.Text(master=popupRoot, wrap=tk.WORD, width=40, height=5, bg="white", font="Roboto", borderwidth=0, highlightthickness=0)
        # popupText.insert(tk.END, "There has been a change in the protected files. If this was not you, or you didn't trigger it in any way (installing a program may have changed these files) we recommend reaching out to a professional.")
        # popupText.pack()
        # popupRoot.geometry('390x50+700+500')

    def run(self):
        self.root.mainloop()


a = GUI()
a.homePage()
