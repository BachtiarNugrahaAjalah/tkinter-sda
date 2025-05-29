import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class our_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi TKinter Seadanya")
        self.root.geometry("1000x1000")
        self.root.resizable(True,True)
        self.font = ("Courier New", 24, "bold")
        self.button_font = ("Cooper Black", 14)
        image = Image.open("bg.png").resize((700, 400))
        self.photo = ImageTk.PhotoImage(image)
        image1 = Image.open("perkenalan.png").resize((700, 400))
        self.photo1 = ImageTk.PhotoImage(image1)
        self.bg_label = tk.Label(self.root, image=self.photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

     
        tk.Label(self.root, text="UAP SDA KEL 5", font=self.font, bg="#000000", fg="white").place(relx=0.5, y=40, anchor="n")
        tk.Button(self.root, text="Start", width=15, font=self.button_font, command=self.Start_perkenalan).place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(self.root, text="Exit", width=10, font=self.button_font, command=self.exit_root).place(relx=0.5, rely=0.5, y=60, anchor="center")


     def Start_perkenalan(self):
        self.root.withdraw()

        perkenalan_root = tk.Toplevel()
        perkenalan_root.title("Perkenalan")
        perkenalan_root.geometry("700x400")
        bg_label = tk.Label(perkenalan_root, image=self.photo1)
        bg_label.image = self.photo1
        bg_label.place(x=0, y=0)

        tk.Label(perkenalan_root, text="Foto Perkenalan", font=self.font, fg="white", bg="#0f3460").pack(pady=80)

        def start_program():
            perkenalan_root.destroy()
            self.CRUD_root()

        tk.Button(perkenalan_root, text="Program Inti", width=10, font=self.button_font, command=start_program).pack(pady=10)

    def CRUD_root(self):
        crud_window = tk.Toplevel()
        crud_window.title("Program inti")
        crud_window.geometry("700x400")
        bg_label = tk.Label(crud_window, image=self.photo1)
        bg_label.image = self.photo1
        bg_label.place(x=0, y=0)

        tk.Label(crud_window, text="CRUD", font=self.font, fg="white", bg="#1a1a2e").place(relx=0.5, rely=0.5, anchor="center")

    def exit_root(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = our_app(root)
    root.mainloop()
