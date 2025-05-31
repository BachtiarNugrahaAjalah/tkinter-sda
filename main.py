import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class our_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi TKinter Kelompok 5 (keknya)")
        self.root.geometry("1200x650")
        self.root.resizable(False,False)

        #font
        self.font = ("Monserrat", 24, "bold")
        self.button_font = ("Cooper Black", 14)

        #image
        image = Image.open("bg.png").resize((1200, 650))
        self.photo = ImageTk.PhotoImage(image)
        image1 = Image.open("perkenalan.png").resize((1200, 650))
        self.photo1 = ImageTk.PhotoImage(image1)

        #background
        self.bg_label = tk.Label(self.root, image=self.photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
     
        tk.Label(self.root, text="UAP SDA KEL 5", font=self.font, bg="#000000", fg="white").place(relx=0.5, y=40, anchor="n")
        tk.Button(self.root, text="Start", width=15, font=self.button_font, bg="blue", fg="white", bd=10, relief="ridge", padx=10, pady=5, highlightthickness=0, command=self.Start_perkenalan).place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(self.root, text="Exit", width=10, font=self.button_font, bg="red", fg="white", bd=10, relief="ridge", padx=10, pady=5, highlightthickness=0, command=self.ask_exit).place(relx=0.5, rely=0.5, y=90, anchor="center")

    def ask_exit(self):
        Keluar = messagebox.askyesno("Keluar", "Apakah kamu yakin ingin keluar?")
        if Keluar:
            self.root.destroy()

    def Start_perkenalan(self):
        self.root.withdraw()
        perkenalan_root = tk.Toplevel()
        perkenalan_root.title("Perkenalan")
        perkenalan_root.geometry("1220x650")
        bg_label = tk.Label(perkenalan_root, image=self.photo1)
        bg_label.image = self.photo1
        bg_label.place(x=0, y=0)

        tk.Label(perkenalan_root, text="Foto Perkenalan", font=self.font, fg="white", bg="#0f3460").pack(pady=80)

        def start_program():
            perkenalan_root.destroy()
            self.CRUD_root()

        tk.Button(perkenalan_root, text="Program Inti", width=10, font=self.button_font, bg="blue", fg="white", bd=10, relief="ridge", padx=10, pady=5, highlightthickness=0, command=start_program).pack(pady=10)

    def CRUD_root(self):
        crud_window = tk.Toplevel()
        crud_window.title("Program inti")
        crud_window.geometry("1200x650")
        bg_label = tk.Label(crud_window, image=self.photo1)
        bg_label.image = self.photo1
        bg_label.place(x=0, y=0)

        tk.Label(crud_window, text="CRUD", font=self.font, fg="white", bg="#1a1a2e").place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(crud_window, text="Keluar", width=10, font=self.button_font, bg="red", fg="white", padx=10, pady=5, command=exit).place(relx=0.5, rely=0.5, y = 100, anchor="center")

    def exit_root(self):
        self.root.destroy()
