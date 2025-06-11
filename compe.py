import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class versus_app():
    def __init__(self, root):
        self.root = root
        self.root.title("Battle Red Versus Blue")
        self.x = (root.winfo_screenwidth() - 1280) // 2
        self.y = (root.winfo_screenheight() - 770) // 2
        self.root.geometry(f"1280x720+{self.x}+{self.y}")
        self.root.resizable(False,False)

        self.font = ("Beekman Square", 24, "bold")
        self.button_font = ("Pixelify sans", 14, "bold")

        # image1 = Image.open()
        
        self.frame_bawah = tk.Frame(root, bg="grey", width=1280, height=50)
        self.frame_bawah.pack(side="bottom", fill="both", expand=False)

        self.frame_kiri = tk.Frame(root, bg="blue", width=640, height=260)
        self.frame_kiri.pack(side="left", fill="both", expand=False)
        
        self.frame_kanan = tk.Frame(root, bg="red", width=640, height=260)
        self.frame_kanan.pack(side="right", fill="both", expand=False)
    
        bendera_merah = Image.open("pictures/bendera_merah.png").resize((300, 300))
        self.red_flag = ImageTk.PhotoImage(bendera_merah)
        

root = tk.Tk()
vers = versus_app(root)
root.mainloop()