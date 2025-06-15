from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk
import tkinter as tk
from main import CryptoCRUDApp

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
        self.btn_next = Button(self.root, text="NEXT", font=('Arial', 12, 'bold'), bg='purple', command=self.load_main)
        self.btn_next.place(x=1150, y=650)
        
        self.btn_back = Button(self.root, text="BACK", font=('Arial', 12, 'bold'), bg='purple')
        self.btn_back.place(x=50, y=650)

    def load_main(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        CryptoCRUDApp(self.root)

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