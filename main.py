import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
import csv
from io import BytesIO
import requests

File_CSV = 'data_kripto.csv'
foto_koin = []


def load_data():
    data = []
    try:
        with open(File_CSV, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data


def save_data(data):
    with open(File_CSV, 'w', newline='') as file:
        fieldnames = ['id', 'nama']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def get_crypto(ids):
    if not ids:
        return []
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': ','.join(ids)
    }
    try:
        response = requests.get(url, params=params)
        return response.json()
    except:
        return []


class our_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi TKinter Kelompok 5 (keknya)")
        self.x = (root.winfo_screenwidth() - 1280) // 2
        self.y = (root.winfo_screenheight() - 770) // 2
        self.root.geometry(f"1280x720+{self.x}+{self.y}")
        self.root.resizable(False, False)
        self.data_kripto = load_data()

        #font
        self.font = ("Beekman Square", 24, "bold")
        self.button_font = ("Pixelify sans", 14, "bold")

        #image
        image = Image.open("pictures/bg.png").resize((1280, 720))
        self.photo = ImageTk.PhotoImage(image)
        image1 = Image.open("pictures/perkenalan.png").resize((1280, 720))
        self.photo1 = ImageTk.PhotoImage(image1)

        #background
        self.bg_label = tk.Label(self.root, image=self.photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self.root, text="UAP SDA KEL 5", font=self.font, bg="#000000", fg="white").place(relx=0.5, y=40, anchor="n")
        tk.Button(self.root, text="Anggota", width=10, font=self.button_font, bg="yellow", fg="black", bd=5, relief="ridge", command=self.Start_perkenalan).place(relx=0.5, rely=0.5, x=-240, anchor="center")
        tk.Button(self.root, text="Start", width=10, font=self.button_font, bg="blue", fg="white", bd=5, relief="ridge", command=self.CRUD_root).place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(self.root, text="Keluar", width=10, font=self.button_font, bg="red", fg="white", bd=5, relief="ridge", command=self.ask_exit).place(relx=0.5, rely=0.5, x=240, anchor="center")

    def ask_exit(self):
        if messagebox.askyesno("Keluar", "Apakah kamu yakin ingin keluar?"):
            self.root.destroy()

    def back_home(self, now, back):
        now.destroy()
        back.deiconify()

    def buat_button_back(self, now, back):
        tk.Button(now, text="Kembali", font=self.button_font, bg="red", fg="white", bd=5, command=lambda: self.back_home(now, back)).place(relx=0.5, rely=0.5, x=550, y=320, anchor="center")

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
        crud_window.title("Program Inti")
        crud_window.geometry(f"1280x720+{self.x}+{self.y}")
        crud_window.resizable(False, False)

        tk.Label(crud_window, text="ID CoinGecko(API) (Contoh: bitcoin, ethereum, dll):").pack()
        entry_id = tk.Entry(crud_window)
        entry_id.pack()

        def tambah_data():
            coin_id = entry_id.get().strip().lower()
            if not coin_id:
                return messagebox.showwarning("Peringatan", "ID CoinGecko tidak boleh kosong.")
            info = get_crypto([coin_id])
            if not info:
                return messagebox.showerror("Error", "Koin tidak ditemukan di CoinGecko!")
            name = info[0]['name']
            self.data_kripto.append({'id': coin_id, 'nama': name})
            save_data(self.data_kripto)
            crud_window.destroy()
            self.CRUD_root()

        def hapus_terakhir():
            if self.data_kripto:
                self.data_kripto.pop()
                save_data(self.data_kripto)
                crud_window.destroy()
                self.CRUD_root()

        tk.Button(crud_window, text="Tambah Koin", command=tambah_data).pack(pady=5)
        tk.Button(crud_window, text="Hapus Terakhir", command=hapus_terakhir).pack()

        canvas_frame = tk.Frame(crud_window)
        canvas_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(canvas_frame)
        scrollbar.pack(side="right", fill="y")

        canvas = tk.Canvas(canvas_frame, bg="white", yscrollcommand=scrollbar.set)
        list_frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=list_frame, anchor="nw")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=canvas.yview)

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        list_frame.bind("<Configure>", on_frame_configure)

        ids = [coin['id'] for coin in self.data_kripto]
        market_data = get_crypto(ids)
        market_map = {coin['id']: coin for coin in market_data}

        for i, coin in enumerate(self.data_kripto):
            frame = tk.Frame(list_frame, bg="white")
            frame.pack(fill="x", pady=2)

            market = market_map.get(coin['id'])
            if market:
                image_url = market['image']
                nama = f"{market['name']} ({market['symbol'].upper()})"
                harga = f"${market['current_price']:,.2f}"
                perubahan = market['price_change_percentage_24h']
                warna = "green" if perubahan >= 0 else "red"
                persen = f"{perubahan:+.2f}%"
            else:
                image_url = None
                nama = f"{coin['nama']} ({coin['id']})"
                harga = "N/A"
                persen = ""
                warna = "black"

            try:
                if image_url:
                    img_data = requests.get(image_url).content
                    img = Image.open(BytesIO(img_data)).resize((24, 24))
                else:
                    img = Image.new("RGB", (24, 24), color="gray")
            except:
                img = Image.new("RGB", (24, 24), color="gray")

            photo = ImageTk.PhotoImage(img)
            foto_koin.append(photo)

            tk.Label(frame, image=photo, bg="white").pack(side="left", padx=5)
            teks = tk.Label(frame, text=f"{nama}\n{harga}   {persen}",
                            justify="left", anchor="w", bg="white", fg=warna,
                            font=("Segoe UI", 10))
            teks.pack(side="left", padx=10)
            teks.bind("<Button-1>", lambda e, idx=i: self.edit_data(idx))

        self.buat_button_back(crud_window, self.root)

    def edit_data(self, index):
        coin = self.data_kripto[index]
        nama_baru = simpledialog.askstring("Edit Nama", "Nama baru:", initialvalue=coin['nama'])
        if nama_baru:
            self.data_kripto[index]['nama'] = nama_baru
            save_data(self.data_kripto)
            self.CRUD_root()


