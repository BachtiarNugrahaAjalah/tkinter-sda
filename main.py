import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class our_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi TKinter Kelompok 5 (keknya)")
        self.x = (root.winfo_screenwidth() - 1280) // 2
        self.y = (root.winfo_screenheight() - 720) // 2
        self.root.geometry(f"1280x720+{self.x}+{self.y}")
        self.root.resizable(False,False)

        #font
        self.font = ("Monserrat", 24, "bold")
        self.button_font = ("Monserrat", 14, "bold")

        #image
        image = Image.open("bg.png").resize((1280, 720))
        self.photo = ImageTk.PhotoImage(image)
        image1 = Image.open("perkenalan.png").resize((1280, 720))
        self.photo1 = ImageTk.PhotoImage(image1)

        #background
        self.bg_label = tk.Label(self.root, image=self.photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
     
        tk.Label(self.root, text="UAP SDA KEL 5", font=self.font, bg="#000000", fg="white").place(relx=0.5, y=40, anchor="n")
        tk.Button(self.root, text="Anggota", width=10, font=self.button_font, bg="yellow", fg="black", bd=5, relief="ridge", padx=10, pady=5, highlightthickness=0, command=self.Start_perkenalan).place(relx=0.5, rely=0.5, x = -240, anchor="center")
        tk.Button(self.root, text="Start", width=10, font=self.button_font, bg="blue", fg="white", bd=5, relief="ridge", padx=10, pady=5, highlightthickness=0, command=self.CRUD_root).place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(self.root, text="Exit", width=10, font=self.button_font, bg="red", fg="white", bd=5, relief="ridge", padx=10, pady=5, highlightthickness=0, command=self.ask_exit).place(relx=0.5, rely=0.5, x = 240, anchor="center")

        
    def ask_exit(self):
        Keluar = messagebox.askyesno("Keluar", "Apakah kamu yakin ingin keluar?")
        if Keluar:
            self.root.destroy()

    def back_home(self, now, back):
        now.destroy()
        back.deiconify()

    def bttn_back(self, now, back):
        kmbl = tk.Button(now, text="Kembali", width=10, font=self.button_font, bg="red", fg="white", bd=5, relief="ridge", padx=10, pady=5, highlightthickness=0, command=lambda: self.back_home(now, back)).place(relx=0.5, rely=0.5,x = 550, y = 320, anchor="center")
        return kmbl
    
    def buat_button_back(self, now, back):
        back_button = self.bttn_back(now, back)
        back_button.pack(pady=0.5)

    def Start_perkenalan(self):
        self.root.withdraw()
        perkenalan_root = tk.Toplevel()
        perkenalan_root.title("Perkenalan")
        perkenalan_root.geometry(f"1280x720+{self.x}+{self.y}")
        perkenalan_root.resizable(False, False)
        bg_label = tk.Label(perkenalan_root, image=self.photo1)
        bg_label.image = self.photo1
        bg_label.place(x=0, y=0)

        tk.Label(perkenalan_root, text="Foto Perkenalan", font=self.font, fg="white", bg="#1a1a2e").pack(pady=80)
        self.buat_button_back(perkenalan_root, self.root)

    def CRUD_root(self):
        self.root.withdraw()
        crud_window = tk.Toplevel()
        crud_window.title("Program inti")
        crud_window.geometry(f"1280x720+{self.x}+{self.y}")
        crud_window.resizable(False, False)
        bg_label = tk.Label(crud_window, image=self.photo1)
        bg_label.image = self.photo1
        bg_label.place(x=0, y=0)

        tk.Label(crud_window, text="CRUD", font=self.font, fg="white", bg="#1a1a2e").place(relx=0.5, rely=0.5, anchor="center")
        self.buat_button_back(crud_window, self.root)
