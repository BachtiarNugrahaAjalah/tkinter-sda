import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, Button
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

class CryptoCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Data Kripto")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.data_kripto = load_data()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.build_ui()

    def build_ui(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="ID CoinGecko(API) (Contoh: bitcoin, ethereum, dll):").pack()
        entry_id = tk.Entry(self.main_frame)
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
            self.build_ui()

        def hapus_terakhir():
            if self.data_kripto:
                self.data_kripto.pop()
                save_data(self.data_kripto)
                self.build_ui()

        tk.Button(self.main_frame, text="Tambah Koin", command=tambah_data).pack(pady=5)
        tk.Button(self.main_frame, text="Hapus Terakhir", command=hapus_terakhir).pack()
        tk.Button(self.main_frame, text="Next")

        canvas_frame = tk.Frame(self.main_frame)
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
                nama = f"{coin['nama']} ({market['symbol'].upper()})"
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

    def edit_data(self, index):
        coin = self.data_kripto[index]
        nama_baru = simpledialog.askstring("Edit Nama", "Nama baru:", initialvalue=coin['nama'])
        if nama_baru:
            self.data_kripto[index]['nama'] = nama_baru
            save_data(self.data_kripto)
            self.build_ui()
    
    def button(self):
        self.btn_next = Button(self.root, text="NEXT", font=('Arial', 12, 'bold'), bg='purple', command=self.load_main)
        self.btn_next.place(x=1150, y=650)
        
        self.btn_back = Button(self.root, text="BACK", font=('Arial', 12, 'bold'), bg='purple')
        self.btn_back.place(x=50, y=650)

            
# root = tk.Tk()
# app = CryptoCRUDApp(root)
# root.mainloop()