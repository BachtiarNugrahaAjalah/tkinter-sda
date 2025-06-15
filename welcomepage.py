from tkinter import Tk, Canvas, Button
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv
from crud import CryptoCRUDApp
from compe import versus_app
class Introduction:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("PROJECT AKHIR SEMESTER")
        self.root.resizable(False, False)
        
        # Background
        bg_image = Image.open('Background/BgIntro.png')
        self.background_photo = ImageTk.PhotoImage(bg_image)

        # Card Photo
        self.fiki = ImageTk.PhotoImage(Image.open('Foto/CardFiki.png').resize((140, 140)))
        self.Bachtiar = ImageTk.PhotoImage(Image.open('Foto/CardBach.png').resize((140, 140)))
        self.Riki = ImageTk.PhotoImage(Image.open('Foto/CardRiki.png').resize((140, 140)))
        self.Raffa = ImageTk.PhotoImage(Image.open('Foto/CardRaffa.png').resize((140, 140)))

        # Stage Photo
        self.stageFiki = ImageTk.PhotoImage(Image.open('Foto/Fiki.png').resize((490,490)))
        self.stageBach = ImageTk.PhotoImage(Image.open('Foto/Bachtiar.png').resize((500,500)))
        self.stageRiki = ImageTk.PhotoImage(Image.open('Foto/Riki.png').resize((390,390)))
        self.stageRaffa = ImageTk.PhotoImage(Image.open('Foto/Raffa.png').resize((490,490)))

        # Canvas Setup
        self.mycanvas = Canvas(self.root, width=1280, height=720)
        self.mycanvas.pack(fill='both', expand=True)
        self.mycanvas.create_image(0, 0, image=self.background_photo, anchor='nw')

        # Card
        self.Fiki = self.mycanvas.create_image(280, 160, image=self.fiki)
        self.Bach = self.mycanvas.create_image(515, 160, image=self.Bachtiar)
        self.Rizki = self.mycanvas.create_image(750, 160, image=self.Riki)
        self.Rappa = self.mycanvas.create_image(999, 160, image=self.Raffa)

        # Stage
        self.stage_awal = self.mycanvas.create_image(670, 400, image=self.stageFiki)

        # Bind
        self.mycanvas.tag_bind(self.Fiki, '<Button-1>', self.stageKI)
        self.mycanvas.tag_bind(self.Bach, '<Button-1>', self.stageBA)
        self.mycanvas.tag_bind(self.Rizki, '<Button-1>', self.stageRI)
        self.mycanvas.tag_bind(self.Rappa, '<Button-1>', self.stageRA)

        # Buttons
        self.btn_crud = Button(self.root, text="CRUD", font=('Arial', 20, 'bold'), bg='purple', command=self.load_crud)
        self.btn_crud.place(x=1050, y=600)
        self.btn_vs = Button(self.root, text="VS", font=('Arial', 20, 'bold'), bg='purple', command=self.load_vs)
        self.btn_vs.place(x=950, y=600)
        
        self.btn_back = Button(self.root, text="BACK", font=('Arial', 12, 'bold'), bg='purple', command=self.load_welcome)
        self.btn_back.place(x=50, y=650)

    def load_crud(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        CryptoCRUDApp(self.root)

    def load_vs(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        versus_app(self.root)
    
    def load_welcome(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Welcome(self.root)

    # Stage Switching
    def stageKI(self, e):
        self.mycanvas.itemconfig(self.stage_awal, image=self.stageFiki)
        self.mycanvas.coords(self.stage_awal, 670, 400)

    def stageBA(self, e):
        self.mycanvas.itemconfig(self.stage_awal, image=self.stageBach)
        self.mycanvas.coords(self.stage_awal, 650, 400)

    def stageRI(self, e):
        self.mycanvas.itemconfig(self.stage_awal, image=self.stageRiki)
        self.mycanvas.coords(self.stage_awal, 650, 450)

    def stageRA(self, e):
        self.mycanvas.itemconfig(self.stage_awal, image=self.stageRaffa)
        self.mycanvas.coords(self.stage_awal, 650, 435)

class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("PROJECT AKHIR SEMESTER")
        self.root.resizable(False, False)

        self.load_assets()
        self.setup_ui()
    
    def load_intro(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Introduction(self.root)

    def load_assets(self):
        # Load background
        bg_image_raw = Image.open("Background/Bgp.png").resize((1280, 720))
        self.bg_photo = ImageTk.PhotoImage(bg_image_raw)

        # Load ghost icon (placeholder)
        ghost_image_raw = Image.open("Background/Bgp.png").resize((50, 50))
        self.ghost_photo = ImageTk.PhotoImage(ghost_image_raw)

    def load_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About This Application")
        about_window.geometry("500x400")
        about_window.resizable(False, False)

        tk.Label(about_window, text="Tentang Aplikasi Ini", font=("Arial", 16, "bold")).pack(pady=10)

        scrollbar = tk.Scrollbar(about_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box = tk.Text(about_window, wrap='word', yscrollcommand=scrollbar.set, font=("Arial", 12))
        text_box.pack(expand=True, fill='both', padx=10, pady=10)

        explanation = """
Aplikasi ini dibuat menggunakan Python dan library Tkinter untuk membuat GUI.
Fitur utama dari aplikasi ini meliputi:
- Fitur CRUD (Create, Read, Update, Delete)
- Interaksi pengguna menggunakan tombol dan input field
- Pengolahan data secara real-time
- Sistem skor dan timer
- Gambar dan desain antarmuka interaktif

Tujuan aplikasi ini adalah untuk mempermudah pengguna dalam mengelola data dan menampilkan antarmuka yang ramah pengguna.
    """
        text_box.insert(tk.END, explanation)
        text_box.config(state='disabled')  # Agar tidak bisa diedit

        scrollbar.config(command=text_box.yview)
        
    def setup_ui(self):
        # Background label
        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Outline frame
        self.background = tk.PhotoImage(file="BackgroundElement/latar.png")
        self.outline_frame = tk.Frame(self.root, width=810, height=410, bg="black", highlightbackground="white", highlightthickness=2)
        self.label = tk.Label(self.outline_frame, image=self.background, borderwidth=0, highlightthickness=0)
        self.label.place(x=0, y=0, width=self.background.width(), height=self.background.height())
        self.outline_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.add_ghosts()
        self.add_title()
        self.add_progress_bar()
        self.add_buttons()

    def add_ghosts(self):
        for i in range(3):
            ghost_label = tk.Label(self.outline_frame, image=self.ghost_photo, bg="black")
            ghost_label.place(x=320 + i * 60, y=45)

    def add_title(self):
        title_label = tk.Label(self.outline_frame, text="WELCOME TO OUR PROJECT", font=("Press Start 2P", 18, "bold"), fg="white", bg="black")
        title_label.place(relx=0.5, y=150, anchor="center")

    def add_progress_bar(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TProgressbar", foreground="#9b59b6", background="#9b59b6")

        progress_bar = ttk.Progressbar(self.outline_frame, style="TProgressbar", orient="horizontal", length=400, mode="determinate")
        progress_bar.place(relx=0.5, y=240, anchor="center")
        progress_bar['value'] = 60  # 60%

    def add_buttons(self):
        play_btn = tk.Button(self.outline_frame, text="START", width=12, height=1, bg="#e74c3c", fg="white", activebackground="#c0392b", command=self.load_intro)
        play_btn.place(relx=0.25, y=340, anchor="center")

        menu_btn = tk.Button(self.outline_frame, text="ABOUT", width=12, height=1, bg="#f1c40f", fg="black", activebackground="#f39c12", command=self.load_about)
        menu_btn.place(relx=0.5, y=340, anchor="center")

        exit_btn = tk.Button(self.outline_frame, text="EXIT", width=12, height=1, bg="#3498db", fg="white", activebackground="#2980b9", command=self.root.destroy)
        exit_btn.place(relx=0.75, y=340, anchor="center")
