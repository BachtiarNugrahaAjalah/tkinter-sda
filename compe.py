import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv

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

        self.ao_team = []
        self.aka_team = []

        with open("dataBase/daftar_tim.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                self.ao_team.append(row[0])
                self.aka_team.append(row[1])
        
        self.red_team_name = "Aka"
        self.blue_team_name = "Ao"
        self.divisionn = ["Championship", "Exhibition"]

        #frame
        self.frame_atas = tk.Frame(root, bg="black", width=1280, height=80)
        self.frame_atas.pack(side="top", fill="both", expand=False)
        self.frame_atas_kiri = tk.Frame(self.frame_atas, bg="black", width=640, height=80)
        self.frame_atas_kiri.bind("<Button-1>", self.remove_focus)
        self.frame_atas_kiri.pack(side="left", fill="both", expand=False)
        self.frame_atas_kanan = tk.Frame(self.frame_atas, bg="black", width=640, height=80)
        self.frame_atas_kanan.bind("<Button-1>", self.remove_focus)
        self.frame_atas_kanan.pack(side="right", fill="both", expand=False)
        
        self.frame_bawah = tk.Frame(root, bg="grey", width=1280, height=50)
        self.frame_bawah_kanan = tk.Frame(self.frame_bawah, bg="dark red", width=640, height=50)
        self.frame_bawah_kiri = tk.Frame(self.frame_bawah, bg="dark blue", width=640, height=50)
        self.frame_bawah_kanan.bind("<Button-1>", self.remove_focus)
        self.frame_bawah_kiri.bind("<Button-1>", self.remove_focus)
        self.frame_bawah_kanan.pack(side="right", fill="both", expand=False)
        self.frame_bawah_kiri.pack(side="left", fill="both", expand=False)
        self.frame_bawah.pack(side="bottom", fill="both", expand=False)

        self.frame_kiri = tk.Frame(root, bg="blue", width=640, height=260)
        self.frame_kiri.bind("<Button-1>", self.remove_focus)
        self.frame_kiri.pack(side="left", fill="both", expand=False)
        
        self.frame_kanan = tk.Frame(root, bg="red", width=640, height=260)
        self.frame_kanan.bind("<Button-1>", self.remove_focus)
        self.frame_kanan.pack(side="right", fill="both", expand=False)
    
        self.frame_judges = tk.Frame(root, bg="#C0C0C0", width=150, height=40)
        self.frame_judges.place(anchor="center", x=640, y=115)

        #image dan label
        self.judges = ttk.Label(self.frame_judges, text="5", font=self.font, justify="center", foreground="white", background="dark blue", border=2, relief="raised", width=2, anchor="center")
        self.judges.pack(side="left")
        self.judges_label = tk.Label(self.frame_judges, text="Judges", font=("Beekman Square", 15, "bold"), fg="black", bg="#C0C0C0")
        self.judges_label.pack(side="left", padx=10)

        bendera_merah = Image.open("pictures/bendera_merah.png").resize((200, 200))
        self.red_flag = ImageTk.PhotoImage(bendera_merah)
        red_flag_label = tk.Label(self.frame_kanan, image=self.red_flag)
        red_flag_label.place(x = 350, y = 70)
        
        bendera_biru = Image.open("pictures/bendera_biru.png").resize((200, 200))
        self.blue_flag = ImageTk.PhotoImage(bendera_biru)
        blue_flag_label = tk.Label(self.frame_kiri, image=self.blue_flag)
        blue_flag_label.place(x = 350, y = 70)
        
        valid = root.register(self.limit_characters)

        self.ao_name_entry = tk.Entry(self.frame_atas, font=("Beekman Square", 10), width=25, justify="left", validate="key", validatecommand=(valid, '%P'))
        self.ao_name_entry.place(anchor="center", x=370, y=20)
        self.aka_name_entry = tk.Entry(self.frame_atas, font=("Beekman Square", 10), width=25, justify="left", validate="key", validatecommand=(valid, '%P'))
        self.aka_name_entry.place(anchor="center", x=910, y=20)
        self.ao_name_entry.insert(0, "Enter Blue Team Name")
        self.ao_name_entry.config(fg="gray")
        self.ao_name_entry.bind("<FocusIn>", self.on_focus_in_ao)
        self.ao_name_entry.bind("<FocusOut>", self.on_focus_out_ao)
        self.aka_name_entry.insert(0, "Enter Red Team Name")
        self.aka_name_entry.config(fg="gray")
        self.aka_name_entry.bind("<FocusIn>", self.on_focus_in_aka)
        self.aka_name_entry.bind("<FocusOut>", self.on_focus_out_aka)
        self.ao_name_entry.bind("<Return>", self.write_name_ao)
        self.aka_name_entry.bind("<Return>", self.write_name_aka)
        
        self.ao_label = tk.Label(self.frame_atas, text="Ao", font=self.font, fg="blue", bg="black")
        self.ao_label.place(anchor="center", x=410, y=60)
        self.aka_label = tk.Label(self.frame_atas, text="Aka", font=self.font, fg="red", bg="black")
        self.aka_label.place(anchor="center", x=870, y=60)

        self.frame_dif = tk.Frame(self.frame_atas, bg="black", width=200, height=30).place(anchor="center", x=640, y=15)
        self.label_dificult = tk.Label(self.frame_dif, text="Division : ", font=("Beekman Square", 16), fg="white", bg="black").place(anchor="center", x=585, y=15)

        self.blue_score = 0 
        self.label_blue_score = tk.Label(self.frame_kiri, text="0", font=("Arial", 170), fg="white", bg="blue") 
        self.label_blue_score.place(anchor="e", x=215,y=170) 
        self.red_score = 0 
        self.label_red_score = tk.Label(self.frame_kanan, text="0", font=("Arial", 170), fg="white", bg="red") 
        self.label_red_score.place(anchor="e", x=215,y=170) 

        self.blue_score_buttons_frame = tk.Frame(self.frame_kiri)
        self.blue_score_buttons_frame.config(bg="blue") 
        self.blue_score_buttons_frame.place(anchor="center", x = 150, y = 300) 

        self.red_score_buttons_frame = tk.Frame(self.frame_kanan)
        self.red_score_buttons_frame.config(bg="red") 
        self.red_score_buttons_frame.place(anchor="center", x = 150, y = 300) 

        self.label_timer_kiri = tk.Label(self.frame_kiri, text=f"0:00", font=("Beekman Square", 92), fg="white", bg="dark blue")
        self.label_timer_kiri.place(anchor="center", x=350, y=500)
        
        self.label_timer_kanan = tk.Label(self.frame_kanan, text=f"0:00", font=("Beekman Square", 92), fg="white", bg="dark red")
        self.label_timer_kanan.place(anchor="center", x=350, y=500)
        
        # button
        self.selection_division = ttk.Combobox(self.frame_dif, font=("Beekman Square", 16), width=10, justify="center", state="readonly")
        self.selection_division.place(anchor="center", x=700, y=15)
        self.selection_division.set("Division")
        self.selection_division.config(foreground="gray")
        self.selection_division['values'] = self.divisionn
        self.selection_division.bind("<<ComboBoxSelected>>", self.autorhize)
        self.selection_division.bind("<FocusOut>", self.combox_focusout)
        
        self.frame_cb_team_kiri = tk.Frame(self.frame_kiri, background="black", width=250, height=25)
        self.frame_cb_team_kiri.place(anchor="center", x=400, y=24)
        self.team_selection_ao = ttk.Combobox(self.frame_cb_team_kiri, font=("Beekman Square",10), width=20, justify="left", state="readonly")
        self.team_selection_ao.pack(side="left")
        self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
        self.team_selection_ao.config(foreground="gray")
        self.team_selection_ao['values'] = self.ao_team.copy()
        self.team_selection_ao.bind("<<ComboboxSelected>>", self.autorhize)
        
        self.frame_cb_team_kanan = tk.Frame(self.frame_kanan, background="black", width=250, height=25)
        self.frame_cb_team_kanan.place(anchor="center", x=240, y=24)
        self.team_selection_aka = ttk.Combobox(self.frame_cb_team_kanan, font=("Beekman Square",10), width=20, justify="left", state="readonly")
        self.team_selection_aka.pack(side="left")
        self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
        self.team_selection_aka.config(foreground="gray")
        self.team_selection_aka['values'] = self.aka_team.copy()
        self.team_selection_aka.bind("<<ComboboxSelected>>", self.autorhize)

        self.exit_button = tk.Button(self.frame_atas, text="Exit", font=self.button_font, fg="white", bg="red", width=4, height=1, cursor="hand2", command=self.execute)
        self.exit_button.place(anchor="center", x=1240, y=50)

        self.done_button = tk.Button(self.frame_bawah, text="Done", font=self.button_font, fg="white", bg="green", width=10, height=1, state="disabled", command=self.done_action)
        self.done_button.place(anchor="center", x=640, y=25) 

        self.blue_penalty_button = tk.Button(self.frame_bawah_kiri, text="Kikken", font=("Beekman Square", 12, "bold"), fg="white", bg="dark blue", width=10, state="disabled", command=self.blue_kikken)
        self.blue_penalty_button.place(anchor="center", x=470, y=25)
        self.blue_disqualify_button = tk.Button(self.frame_bawah_kiri, text="Shikkaku", font=("Beekman Square", 12, "bold"), fg="white", bg="dark blue", width=10, state="disabled", command=self.blue_shikkaku)
        self.blue_disqualify_button.place(anchor="center", x=290, y=25)
        
        self.red_penalty_button = tk.Button(self.frame_bawah_kanan, text="Kikken", font=("Beekman Square", 12, "bold"), fg="white", bg="dark red", width=10, state="disabled", command=self.red_kikken)
        self.red_penalty_button.place(anchor="center", x=170, y=25)
        self.red_disqualify_button = tk.Button(self.frame_bawah_kanan, text="Shikkaku", font=("Beekman Square", 12, "bold"), fg="white", bg="dark red", width=10, state="disabled", command=self.red_shikkaku)
        self.red_disqualify_button.place(anchor="center", x=350, y=25)

        self.blue_score_buttons_plus = tk.Button(self.blue_score_buttons_frame, text="-1", font=("Arial", 16), fg="white", bg="green", width=4, command=self.kurang_blue).grid(row=0, column=1, padx=20)
        self.blue_score_buttons_min = tk.Button(self.blue_score_buttons_frame, text="+1", font=("Arial", 16), fg="white", bg="blue", width=4, command=self.tambah_blue).grid(row=0, column=0, padx=20)

        self.red_score_buttons_min = tk.Button(self.red_score_buttons_frame, text="-1", font=("Arial", 16), fg="white", bg="green", width=4, command=self.kurang_red).grid(row=0, column=1, padx=20)
        self.red_score_buttons_plus = tk.Button(self.red_score_buttons_frame, text="+1", font=("Arial", 16), fg="white", bg="blue", width=4, command=self.tambah_red).grid(row=0, column=0, padx=20)

        self.reset_button = tk.Button(self.frame_bawah_kanan, text="Reset", font=self.button_font, fg="white", bg="dark green", command=self.reset_timer)
        self.reset_button.place(anchor="center", x=560, y=25)

        self.timer_button = tk.Button(self.frame_kiri, text="Start", font=self.button_font, fg="white", bg="green", state="disabled", command=self.toggle)
        self.timer_button.place(anchor="center", x=150, y=500)

        self.status_stopwatch = True
        self.show_or_hide_stopwatch_button = tk.Button(self.frame_bawah_kiri, text="Show/Hide\nStopwatch", font=self.button_font, command=self.status_stopwatch_on_button, fg="white", bg="dark green", bd=2, relief="ridge", width=10, height=2)
        self.show_or_hide_stopwatch_button.place(anchor="center", x=80, y=25)

        self.running = False
        self.paused = False
        self.timer = 0
        self.minutes = 0
        self.seconds = 0
        self.round = 0
        self.match = 0
        self.nilai_maks = 5
        self.total = 0
        
        self.winner_team = None
        self.winner_name = None
        self.winner_score = None
        
        self.losser_team = None
        self.losser_name = None
        self.losser_score = None

        self.first_point = False
        self.who_first = None

        self.status_player_blue = "Clear"
        self.status_player_red = "Clear"
        
    def reset(self):
        self.team_selection_aka.config(foreground="gray")
        self.team_selection_ao.config(foreground="gray")
        self.winner_team = None
        self.winner_name = None
        self.winner_score = None
        
        self.losser_team = None
        self.losser_name = None
        self.losser_score = None
    
    #functions
    def autorhize(self, event):
        event.widget.config(foreground="black")
        if self.selection_division.get() != "Division" and self.team_selection_ao.get() != f"Pilih team {self.blue_team_name}" and self.team_selection_aka.get() != f"Pilih team {self.red_team_name}":
            self.timer_button.config(state="normal")
            self.done_button.config(state="normal")
            self.red_disqualify_button.config(state="normal")
            self.red_penalty_button.config(state="normal")
            self.blue_disqualify_button.config(state="normal")
            self.blue_penalty_button.config(state="normal")
        else:
            self.timer_button.config(state="disabled")
            self.done_button.config(state="disabled")
            self.red_disqualify_button.config(state="disabled")
            self.red_penalty_button.config(state="disabled")
            self.blue_disqualify_button.config(state="disabled")
            self.blue_penalty_button.config(state="disabled")

    def remove_focus(self, event):
        event.widget.focus_set()

    def combox_focusout(self, event):
        if event.widget.get() == "Division" or event.widget.get() == f"Pilih team {self.blue_team_name}" or event.widget.get() == f"Pilih team {self.red_team_name}" :
            event.widget.config(foreground="gray")
        else:
            event.widget.config(foreground="black")
        
    def write_name_ao(self, event):
        value = event.widget.get()
        if value != "":
            self.ao_label.config(text=value)
            self.blue_team_name = value
            event.widget.config(state="disabled")
            if self.team_selection_ao.get() == "Pilih team Ao":
                self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
            return "break"
    
    def write_name_aka(self, event):
        value = event.widget.get()
        if value != "":
            self.aka_label.config(text=value)
            self.red_team_name = value
            event.widget.config(state="disabled")
            if self.team_selection_aka.get() == "Pilih team Aka":
                self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
            return "break"

    def on_focus_in_ao(self, event):
        event.widget.config(state="normal")
        event.widget.config(fg="black")
        if event.widget.get() == "Enter Blue Team Name":   
           event.widget.delete(0, tk.END)
    
    def on_focus_in_aka(self, event):
        event.widget.config(state="normal")
        event.widget.config(fg="black")
        if event.widget.get() == "Enter Red Team Name":   
           event.widget.delete(0, tk.END)

    def on_focus_out_ao(self, event):
        if event.widget.get() == "":
            event.widget.insert(0, "Enter Blue Team Name")
            event.widget.config(fg="gray")

    def on_focus_out_aka(self, event):
        if event.widget.get() == "":
            event.widget.insert(0, "Enter Red Team Name")
            event.widget.config(fg="gray")

    def limit_characters(self, value):
        if value == "Enter Blue Team Name" or value == "Enter Red Team Name":
            return True
        return len(value) <= 14
        
    def reset_timer(self):
        self.running = False
        self.paused = False
        self.timer = 0
        self.minutes = 0
        self.seconds = 0
        self.label_timer_kiri.config(text="0:00")
        self.label_timer_kanan.config(text="0:00")
        self.timer_button.config(text="Start")
        self.red_score = 0
        self.blue_score = 0
        self.label_red_score.config(text="0")
        self.label_blue_score.config(text="0")
        self.blue_score_buttons_frame.place(anchor="center", x = 150, y = 300)
        self.red_score_buttons_frame.place(anchor="center", x = 150, y = 300)
        self.label_blue_score.config(font=("Arial", 170), fg="white", bg="blue")
        self.label_red_score.config(font=("Arial", 170), fg="white", bg="red")
        self.label_blue_score.place(anchor="e", x=215,y=170)
        self.label_red_score.place(anchor="e", x=215,y=170)

    def update(self):
        if self.running and not self.paused:
            self.timer += 1
            self.minutes = (self.timer % 3600) // 60
            self.seconds = self.timer % 60
            self.label_timer_kiri.config(text=f"{self.minutes}:{self.seconds:02d}")
            self.label_timer_kanan.config(text=f"{self.minutes}:{self.seconds:02d}")
            self.frame_kiri.after(1000, self.update)
            if self.timer >= 180:
                self.reset_timer()
                messagebox.showinfo("Waktu Habis", "Waktu telah habis!")
                self.done_action()

    def toggle(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.update()
            self.timer_button.config(text="Pause")
        elif not self.paused:
            self.paused = True
            self.timer_button.config(text="Resume")
        else:
            self.paused = False
            self.update()
            self.timer_button.config(text="Pause")

    def done_action(self):
        self.selection_division.config(state="disabled")
        self.round += 1
        if self.round == 1:
            if self.red_score > self.blue_score:
                self.winner_team = self.aka_name_entry.get()
                self.winner_name = self.team_selection_aka.get()
                self.winner_score = self.red_score
                self.losser_team = self.ao_name_entry.get()
                self.losser_name = self.team_selection_ao.get()
                self.losser_score = self.blue_score
                self.ao_team.remove(self.losser_name)
                self.aka_team.remove(self.winner_name)
                self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                self.team_selection_ao['values'] = self.ao_team
                self.team_selection_aka['values'] = self.aka_team
                self.reset_timer()
                self.timer_button.config(state="disabled")
                self.done_button.config(state="disabled")
                self.red_disqualify_button.config(state="disabled")
                self.red_penalty_button.config(state="disabled")
                self.blue_disqualify_button.config(state="disabled")
                self.blue_penalty_button.config(state="disabled")

                with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])
                
                self.reset()

            elif self.blue_score > self.red_score:
                self.winner_team = self.ao_name_entry.get()
                self.winner_name = self.team_selection_ao.get()
                self.winner_score = self.blue_score
                self.losser_team = self.aka_name_entry.get()
                self.losser_name = self.team_selection_aka.get()
                self.losser_score = self.red_score
                self.aka_team.remove(self.losser_name)
                self.ao_team.remove(self.winner_name)
                self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                self.team_selection_aka['values'] = self.aka_team
                self.team_selection_ao['values'] = self.ao_team
                self.reset_timer()
                self.timer_button.config(state="disabled")
                self.done_button.config(state="disabled")
                self.red_disqualify_button.config(state="disabled")
                self.red_penalty_button.config(state="disabled")
                self.blue_disqualify_button.config(state="disabled")
                self.blue_penalty_button.config(state="disabled")

                with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])
                
                self.reset()

            elif self.red_score == self.blue_score:
                if self.who_first == self.ao_name_entry.get():
                    self.winner_team = self.ao_name_entry.get()
                    self.winner_name = self.team_selection_ao.get()
                    self.winner_score = self.blue_score
                    self.losser_team = self.aka_name_entry.get()
                    self.losser_name = self.team_selection_aka.get()
                    self.losser_score = self.red_score
                    self.aka_team.remove(self.losser_name)
                    self.ao_team.remove(self.winner_name)
                    self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                    self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                    self.team_selection_aka['values'] = self.aka_team
                    self.team_selection_ao['values'] = self.ao_team
                    self.reset_timer()
                    self.timer_button.config(state="disabled")
                    self.done_button.config(state="disabled")
                    self.red_disqualify_button.config(state="disabled")
                    self.red_penalty_button.config(state="disabled")
                    self.blue_disqualify_button.config(state="disabled")
                    self.blue_penalty_button.config(state="disabled")

                    with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])

                    self.reset()
                    
                elif self.who_first == self.aka_name_entry.get():
                    self.winner_team = self.aka_name_entry.get()
                    self.winner_name = self.team_selection_aka.get()
                    self.winner_score = self.red_score
                    self.losser_team = self.ao_name_entry.get()
                    self.losser_name = self.team_selection_ao.get()
                    self.losser_score = self.blue_score
                    self.ao_team.remove(self.losser_name)
                    self.aka_team.remove(self.winner_name)
                    self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                    self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                    self.team_selection_ao['values'] = self.ao_team
                    self.team_selection_aka['values'] = self.aka_team
                    self.reset_timer()
                    self.timer_button.config(state="disabled")
                    self.done_button.config(state="disabled")
                    self.red_disqualify_button.config(state="disabled")
                    self.red_penalty_button.config(state="disabled")
                    self.blue_disqualify_button.config(state="disabled")
                    self.blue_penalty_button.config(state="disabled")

                    with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])

                    self.reset()

        elif self.round == 2:
            if self.red_score > self.blue_score:
                self.winner_team = self.aka_name_entry.get()
                self.winner_name = self.team_selection_aka.get()
                self.winner_score = self.red_score
                self.losser_team = self.ao_name_entry.get()
                self.losser_name = self.team_selection_ao.get()
                self.losser_score = self.blue_score
                self.ao_team.remove(self.losser_name)
                self.aka_team.remove(self.winner_name)
                self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                self.team_selection_ao['values'] = self.ao_team
                self.team_selection_aka['values'] = self.aka_team
                self.reset_timer()
                self.timer_button.config(state="disabled")
                self.done_button.config(state="disabled")
                self.red_disqualify_button.config(state="disabled")
                self.red_penalty_button.config(state="disabled")
                self.blue_disqualify_button.config(state="disabled")
                self.blue_penalty_button.config(state="disabled")

                with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])
                
                self.reset()

            elif self.blue_score > self.red_score:
                self.winner_team = self.ao_name_entry.get()
                self.winner_name = self.team_selection_ao.get()
                self.winner_score = self.blue_score
                self.losser_team = self.aka_name_entry.get()
                self.losser_name = self.team_selection_aka.get()
                self.losser_score = self.red_score
                self.aka_team.remove(self.losser_name)
                self.ao_team.remove(self.winner_name)
                self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                self.team_selection_aka['values'] = self.aka_team
                self.team_selection_ao['values'] = self.ao_team
                self.reset_timer()
                self.timer_button.config(state="disabled")
                self.done_button.config(state="disabled")
                self.red_disqualify_button.config(state="disabled")
                self.red_penalty_button.config(state="disabled")
                self.blue_disqualify_button.config(state="disabled")
                self.blue_penalty_button.config(state="disabled")


                with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])
                
                self.reset()

            elif self.red_score == self.blue_score:
                if self.who_first == self.ao_name_entry.get():
                    self.winner_team = self.ao_name_entry.get()
                    self.winner_name = self.team_selection_ao.get()
                    self.winner_score = self.blue_score
                    self.losser_team = self.aka_name_entry.get()
                    self.losser_name = self.team_selection_aka.get()
                    self.losser_score = self.red_score
                    self.aka_team.remove(self.losser_name)
                    self.ao_team.remove(self.winner_name)
                    self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                    self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                    self.team_selection_aka['values'] = self.aka_team
                    self.team_selection_ao['values'] = self.ao_team
                    self.reset_timer()
                    self.timer_button.config(state="disabled")
                    self.done_button.config(state="disabled")
                    self.red_disqualify_button.config(state="disabled")
                    self.red_penalty_button.config(state="disabled")
                    self.blue_disqualify_button.config(state="disabled")
                    self.blue_penalty_button.config(state="disabled")


                    with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])

                    self.reset()
                    
                elif self.who_first == self.aka_name_entry.get():
                    self.winner_team = self.aka_name_entry.get()
                    self.winner_name = self.team_selection_aka.get()
                    self.winner_score = self.red_score
                    self.losser_team = self.ao_name_entry.get()
                    self.losser_name = self.team_selection_ao.get()
                    self.losser_score = self.blue_score
                    self.ao_team.remove(self.losser_name)
                    self.aka_team.remove(self.winner_name)
                    self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                    self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                    self.team_selection_ao['values'] = self.ao_team
                    self.team_selection_aka['values'] = self.aka_team
                    self.reset_timer()
                    self.timer_button.config(state="disabled")
                    self.done_button.config(state="disabled")
                    self.red_disqualify_button.config(state="disabled")
                    self.red_penalty_button.config(state="disabled")
                    self.blue_disqualify_button.config(state="disabled")
                    self.blue_penalty_button.config(state="disabled")
                    

                    with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])

                    self.reset()

        elif self.round == 3:
            self.paused = True
            self.running = False
            result = tk.Toplevel()
            result.title("Result")
            x = (result.winfo_screenwidth() - 853) // 2
            y = (result.winfo_screenheight() - 480) // 2
            result.geometry(f"853x480+{x}+{y}")
            result.resizable(False, False)

            image = Image.open("pictures/bg1.png").resize((853, 480))
            self.photo = ImageTk.PhotoImage(image)

            if self.red_score > self.blue_score:
                self.winner_team = self.aka_name_entry.get()
                self.winner_name = self.team_selection_aka.get()
                self.winner_score = self.red_score
                self.losser_team = self.ao_name_entry.get()
                self.losser_name = self.team_selection_ao.get()
                self.losser_score = self.blue_score
                self.ao_team.remove(self.losser_name)
                self.aka_team.remove(self.winner_name)
                self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                self.team_selection_ao['values'] = self.ao_team
                self.team_selection_aka['values'] = self.aka_team
                self.reset_timer()
                self.timer_button.config(state="disabled")
                self.done_button.config(state="disabled")
                self.red_disqualify_button.config(state="disabled")
                self.red_penalty_button.config(state="disabled")
                self.blue_disqualify_button.config(state="disabled")
                self.blue_penalty_button.config(state="disabled")

                with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])
                
                self.reset()

            elif self.blue_score > self.red_score:
                self.winner_team = self.ao_name_entry.get()
                self.winner_name = self.team_selection_ao.get()
                self.winner_score = self.blue_score
                self.losser_team = self.aka_name_entry.get()
                self.losser_name = self.team_selection_aka.get()
                self.losser_score = self.red_score
                self.aka_team.remove(self.losser_name)
                self.ao_team.remove(self.winner_name)
                self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                self.team_selection_aka['values'] = self.aka_team
                self.team_selection_ao['values'] = self.ao_team
                self.reset_timer()
                self.timer_button.config(state="disabled")
                self.done_button.config(state="disabled")
                self.red_disqualify_button.config(state="disabled")
                self.red_penalty_button.config(state="disabled")
                self.blue_disqualify_button.config(state="disabled")
                self.blue_penalty_button.config(state="disabled")

                with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])
                
                self.reset()

            elif self.red_score == self.blue_score:
                if self.who_first == self.ao_name_entry.get():
                    self.winner_team = self.ao_name_entry.get()
                    self.winner_name = self.team_selection_ao.get()
                    self.winner_score = self.blue_score
                    self.losser_team = self.aka_name_entry.get()
                    self.losser_name = self.team_selection_aka.get()
                    self.losser_score = self.red_score
                    self.aka_team.remove(self.losser_name)
                    self.ao_team.remove(self.winner_name)
                    self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                    self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                    self.team_selection_aka['values'] = self.aka_team
                    self.team_selection_ao['values'] = self.ao_team
                    self.reset_timer()
                    self.timer_button.config(state="disabled")
                    self.done_button.config(state="disabled")
                    self.red_disqualify_button.config(state="disabled")
                    self.red_penalty_button.config(state="disabled")
                    self.blue_disqualify_button.config(state="disabled")
                    self.blue_penalty_button.config(state="disabled")

                    with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])

                    self.reset()
                    
                elif self.who_first == self.aka_name_entry.get():
                    self.winner_team = self.aka_name_entry.get()
                    self.winner_name = self.team_selection_aka.get()
                    self.winner_score = self.red_score
                    self.losser_team = self.ao_name_entry.get()
                    self.losser_name = self.team_selection_ao.get()
                    self.losser_score = self.blue_score
                    self.ao_team.remove(self.losser_name)
                    self.aka_team.remove(self.winner_name)
                    self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
                    self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
                    self.team_selection_ao['values'] = self.ao_team
                    self.team_selection_aka['values'] = self.aka_team
                    self.reset_timer()
                    self.timer_button.config(state="disabled")
                    self.done_button.config(state="disabled")
                    self.red_disqualify_button.config(state="disabled")
                    self.red_penalty_button.config(state="disabled")
                    self.blue_disqualify_button.config(state="disabled")
                    self.blue_penalty_button.config(state="disabled")

                    with open("dataBase/hasil_pertandingan.csv", "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([self.winner_team,self.winner_name,self.winner_score,self.losser_team,self.losser_name,self.losser_score])

                    self.reset()

            def ok_button_on_result():
                result.destroy()
                self.reset_timer()
                self.reset()

            def text_in_result():
                daftar_winner = []
                daftar_losser = []
                daftar_nama_winner = []
                daftar_nama_losser = []
                daftar_skor_winner = []
                daftar_skor_losser = []

                with open("dataBase/hasil_pertandingan.csv", "r") as file:
                    reader = csv.reader(file)
                    header = next(reader)
                    for row in reader:
                        if row:
                            daftar_winner.append(row[0])
                            daftar_nama_winner.append(row[1])
                            daftar_skor_winner.append(row[2])
                            daftar_losser.append(row[3])
                            daftar_nama_losser.append(row[4])
                            daftar_skor_losser.append(row[5])

                title_result_text = f"{self.selection_division.get()} Match Result (Match {int(self.match)+1})\n\n"
                paragraph_winner_round1 = f"""
Round 1\n
Winner Team: {daftar_winner[0 + int(self.match)*3]}\nWinner Name: {daftar_nama_winner[0 + int(self.match)*3]}\nWinner Score: {daftar_skor_winner[0 + int(self.match)*3]}\n
Losser Team: {daftar_losser[0 + int(self.match)*3]}\nLosser Name: {daftar_nama_losser[0 + int(self.match)*3]}\nLosser Score: {daftar_skor_losser[0 + int(self.match)*3]}
"""
                paragraph_winner_round2 = f"""
Round 2\n
Winner Team: {daftar_winner[1 + int(self.match)*3]}\nWinner Name: {daftar_nama_winner[1 + int(self.match)*3]}\nWinner Score: {daftar_skor_winner[1 + int(self.match)*3]}\n
Losser Team: {daftar_losser[1 + int(self.match)*3]}\nLosser Name: {daftar_nama_losser[1 + int(self.match)*3]}\nLosser Score: {daftar_skor_losser[1 + int(self.match)*3]}
"""
                paragraph_winner_round3 = f"""
Round 3\n
Winner Team: {daftar_winner[2 + int(self.match)*3]}\nWinner Name: {daftar_nama_winner[2 + int(self.match)*3]}\nWinner Score: {daftar_skor_winner[2 + int(self.match)*3]}\n
Losser Team: {daftar_losser[2 + int(self.match)*3]}\nLosser Name: {daftar_nama_losser[2 + int(self.match)*3]}\nLosser Score: {daftar_skor_losser[2 + int(self.match)*3]}
"""
                
                canvas = tk.Canvas(result, width=853, height=480)
                canvas.pack()
                canvas.create_image(0, 0, image=self.photo, anchor="nw")
                canvas.create_text(426, 50, text=title_result_text, fill="white", font=("Beekman Square", 16, "bold"))
                canvas.create_text(126, 240, text=paragraph_winner_round1, fill="white", font=("Beekman Square", 16, "bold"))
                canvas.create_text(426, 240, text=paragraph_winner_round2, fill="white", font=("Beekman Square", 16, "bold"))
                canvas.create_text(726, 240, text=paragraph_winner_round3, fill="white", font=("Beekman Square", 16, "bold"))

            text_in_result()

            self.team_selection_aka['values'] = self.aka_team.copy()
            self.team_selection_ao['values'] = self.ao_team.copy()
            self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
            self.team_selection_aka.config(foreground="gray")
            self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
            self.team_selection_ao.config(foreground="gray")
            self.ao_name_entry.delete(0, tk.END)
            self.ao_name_entry.insert(0, "Enter Blue Team Name")
            self.ao_name_entry.config(fg="gray")
            self.ao_name_entry.config(state="normal")
            self.aka_name_entry.delete(0, tk.END)
            self.aka_name_entry.insert(0, "Enter Red Team Name")
            self.aka_name_entry.config(fg="gray")
            self.aka_name_entry.config(state="normal")
            self.ao_label.config(text="Ao")
            self.aka_label.config(text="Aka")
            self.red_team_name = "Aka"
            self.blue_team_name = "Ao"
            self.selection_division.set("Division")
            self.selection_division.config(foreground="gray")
            self.selection_division.config(state="normal")
            self.round = 0
            self.match += 1
            tk.Button(result, text="OK", font=("Beekman Square", 12, "bold"), fg="white", bg="red", command=ok_button_on_result).place(anchor="center", relx=0.5, rely=0.8, x=290, y=45)

    def tambah_blue(self):
        if not self.first_point:
            self.first_point = True
            self.who_first = self.ao_name_entry.get()
        if self.total != self.nilai_maks: 
            self.blue_score += 1
            self.total += 1
        self.label_blue_score.config(text=str(self.blue_score)) 
    
    def tambah_red(self):
        if not self.first_point:
            self.first_point = True
            self.who_first = self.aka_name_entry.get()
        if self.total != self.nilai_maks:
            self.red_score += 1
            self.total += 1
        self.label_red_score.config(text=str(self.red_score)) 
        
    def kurang_blue(self):
        if self.total <= self.nilai_maks:
            self.blue_score = max(0, self.blue_score - 1)
            self.total = max(0, self.total - 1)
        self.label_blue_score.config(text=str(self.blue_score))

    def kurang_red(self):
        if self.total <= self.nilai_maks:
            self.total = max(0, self.total - 1)
            self.red_score = max(0, self.red_score - 1) 
        self.label_red_score.config(text=str(self.red_score)) 

    def blue_kikken(self):
        self.blue_score = 0
        self.red_score = 5
        self.round += 1
        self.done_action()
            
    def red_kikken(self):
        self.round += 1
        self.red_score = 0
        self.blue_score = 5
        self.done_action()
    
    def blue_shikkaku(self):
        messagebox.showinfo("Menang", f"Team {self.red_team_name} menang karena\nTeam {self.blue_team_name} menyerah")
        self.reset()
        self.reset_timer()
        self.ao_name_entry.delete(0, tk.END)
        self.ao_name_entry.insert(0, "Enter Blue Team Name")
        self.ao_name_entry.config(fg="gray")
        self.ao_name_entry.config(state="normal")
        self.aka_name_entry.delete(0, tk.END)
        self.aka_name_entry.insert(0, "Enter Red Team Name")
        self.aka_name_entry.config(fg="gray")
        self.aka_name_entry.config(state="normal")
        self.team_selection_aka['values'] = self.aka_team.copy()
        self.team_selection_ao['values'] = self.ao_team.copy()
        self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
        self.team_selection_aka.config(foreground="gray")
        self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
        self.team_selection_ao.config(foreground="gray")
        self.ao_label.config(text="Ao")
        self.aka_label.config(text="Aka")
        self.red_team_name = "Aka"
        self.blue_team_name = "Ao"
        self.selection_division.set("Division")
        self.selection_division.config(foreground="gray")
        self.selection_division.config(state="normal")
        self.round = 0
        self.match += 1
        root.quit()
            
    def red_shikkaku(self):
        messagebox.showinfo("Menang", f"Team {self.red_team_name} menang karena\nTeam {self.blue_team_name} menyerah")
        self.reset()
        self.reset_timer()
        self.team_selection_aka['values'] = self.aka_team.copy()
        self.team_selection_ao['values'] = self.ao_team.copy()
        self.team_selection_aka.set(f"Pilih team {self.red_team_name}")
        self.team_selection_aka.config(foreground="gray")
        self.team_selection_ao.set(f"Pilih team {self.blue_team_name}")
        self.team_selection_ao.config(foreground="gray")
        self.ao_name_entry.delete(0, tk.END)
        self.ao_name_entry.insert(0, "Enter Blue Team Name")
        self.ao_name_entry.config(fg="gray")
        self.ao_name_entry.config(state="normal")
        self.aka_name_entry.delete(0, tk.END)
        self.aka_name_entry.insert(0, "Enter Red Team Name")
        self.aka_name_entry.config(fg="gray")
        self.aka_name_entry.config(state="normal")
        self.ao_label.config(text="Ao")
        self.aka_label.config(text="Aka")
        self.red_team_name = "Aka"
        self.blue_team_name = "Ao"
        self.selection_division.set("Division")
        self.selection_division.config(foreground="gray")
        self.selection_division.config(state="normal")
        self.round = 0
        self.match += 1
        root.quit()

    def status_stopwatch_on_button(self):
        self.status_stopwatch = not self.status_stopwatch
        if self.status_stopwatch:
            self.label_timer_kiri.place(anchor="center", x=350, y=500)
            self.label_timer_kanan.place(anchor="center", x=350, y=500)
            self.timer_button.place(anchor="center", x=150, y=500)
        else:
            self.label_timer_kiri.place_forget()
            self.label_timer_kanan.place_forget()
            self.timer_button.place_forget()

    def execute(self):
        self.root.quit()
        with open("dataBase/hasil_pertandingan.csv", newline="") as file:
                reader = csv.reader(file)
                header = next(reader)
        with open("dataBase/hasil_pertandingan.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
 
root = tk.Tk()
vers = versus_app(root)
root.mainloop()