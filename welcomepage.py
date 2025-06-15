import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from intro import Introduction

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

        menu_btn = tk.Button(self.outline_frame, text="ABOUT", width=12, height=1, bg="#f1c40f", fg="black", activebackground="#f39c12")
        menu_btn.place(relx=0.5, y=340, anchor="center")

        exit_btn = tk.Button(self.outline_frame, text="EXIT", width=12, height=1, bg="#3498db", fg="white", activebackground="#2980b9", command=self.root.destroy)
        exit_btn.place(relx=0.75, y=340, anchor="center")

