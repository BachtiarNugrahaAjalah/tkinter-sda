import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class our_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi TKinter Seadanya")
        self.root.geometry("1000x1000")
        self.root.resizable(True,True)

if __name__ == "__main__":
    root = tk.Tk()
    app = our_app(root)
    root.mainloop()