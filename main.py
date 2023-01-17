import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import os
# ^ ^ ^ ^ ^ Import ^ ^ ^ ^ ^


# Laver en klasse som hedder "BilledeContainer" til at indeholde alle de billeder vi skal bruge samt metode til at vise dem.
class BilledKig(ttk.Frame):
    dirlist = os.listdir(
        'C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data')
    print(dirlist)
    print(len(dirlist))

    curr_img_num = 0

    def __init__(self, beholder):
        super().__init__(beholder)  # Her kalder vi superklassen, som er "ttk.Frame".
        # Som argument sendes vores "App" klasse, som agerer som en beholder

        # Test label
        test_label = ttk.Label(beholder, text="Hello World")
        test_label.grid(row=0, column=0, sticky="nsew")

        naeste_knap = ttk.Button(beholder, text="Neaste", command=lambda: self.vis_neaste_billede(self.dirlist, beholder))  # Opret knap
        naeste_knap.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)  # Placer knap
        naeste_knap.focus()

        forrige_knap = ttk.Button(beholder, text="Forrige", command=lambda: self.vis_forrige_billede(self.dirlist, beholder))  # Opret knap
        forrige_knap.grid(column=2, row=2, sticky=tk.EW, padx=5, pady=5)  # Placer knap

        billede = Image.open(
            f"C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{self.dirlist[0]}")
        billede = billede.resize((300, 300))
        self.curr_img = ImageTk.PhotoImage(billede)

        self.billede_label = ttk.Label(beholder, image=self.curr_img, text="test")
        self.billede_label.grid(column=3, row=5, sticky=tk.EW, padx=5, pady=5)

    def vis_neaste_billede(self, dirlist, owner):  # Funktion til visning af naeste billede
        try:
            self.curr_img_num += 1

            billede = Image.open(f"C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{dirlist[self.curr_img_num]}")
            self.curr_img = ImageTk.PhotoImage(billede)

            self.billede_label = ttk.Label(owner, image=self.curr_img)
            self.billede_label.grid(column=3, row=5, sticky=tk.EW, padx=5, pady=5)

        except IndexError:
            self.curr_img_num = -1
            self.vis_neaste_billede(dirlist, owner)

        except PermissionError:
            self.vis_neaste_billede(dirlist, owner)

    def vis_forrige_billede(self, dirlist, owner):  # Funktion til visning af forrige billede
        try:
            if self.curr_img_num != 0:
                self.curr_img_num -= 1
            else:
                self.curr_img_num = len(dirlist) - 1

            billede = Image.open(f"C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{dirlist[self.curr_img_num]}")
            self.curr_img = ImageTk.PhotoImage(billede)

            self.billede_label = ttk.Label(owner, image=self.curr_img)
            self.billede_label.grid(column=3, row=5, sticky=tk.EW, padx=5, pady=5)

        except PermissionError:
            self.vis_forrige_billede(dirlist, owner)


# Laver en App klasse som indeholder vores root vindue.
class App(tk.Tk):
    def __init__(self):
        super().__init__()  # Arv fra tkinter
        self.title("Hello World")  # Titel på main vindue
        self.geometry("800x600")  # Demensioner på vindue
        self.resizable(False, False)  # Lås demensioner


if __name__ == "__main__":
    app = App()
    BilledKig(app)
    app.mainloop()  # Kør mainloop
