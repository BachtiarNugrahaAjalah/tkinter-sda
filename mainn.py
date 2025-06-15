import tkinter as tk
from welcomepage import Welcome
from intro import Introduction
from main import CryptoCRUDApp
from compe import versus_app

root = tk.Tk()
app = Welcome(root)
root.mainloop()