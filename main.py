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

    def __init__(self, owner):
        super().__init__(owner)  # Her kalder vi superklassen, som er "ttk.Frame".
        # Som argument sendes vores "App" klasse, som agerer som en beholder

        # Test label
        test_label = ttk.Label(owner, text="Hello World")
        test_label.grid(row=0, column=0, sticky="nsew")

        naeste_knap = ttk.Button(owner, text="Neaste", command=lambda: self.vis_neaste_billede(self.dirlist, owner))  # Opret knap
        naeste_knap.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)  # Placer knap
        naeste_knap.focus()

        forrige_knap = ttk.Button(owner, text="Forrige", command=lambda: self.vis_forrige_billede(self.dirlist, owner))  # Opret knap
        forrige_knap.grid(column=2, row=2, sticky=tk.EW, padx=5, pady=5)  # Placer knap

        billede = Image.open(
            f"C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{self.dirlist[0]}")
        billede = billede.resize((780, 500))
        self.curr_img = ImageTk.PhotoImage(billede)

        self.billede_label = ttk.Label(owner, image=self.curr_img)
        self.billede_label.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5, columnspan=5, rowspan=5)

    def vis_neaste_billede(self, dirlist, owner):  # Funktion til visning af naeste billede
        try:
            self.curr_img_num += 1

            billede = Image.open(f"C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{dirlist[self.curr_img_num]}")  # path
            img = ImageTk.PhotoImage(billede)  # convert image object to tkinter image
            # ImageTk.getimage(img)  # get info about image (e.g. size)

            # Work in progress
            resize_width = False
            resize_height = False
            if img.width() <= 780: pass  # If width less than window
            elif img.height() <= 500: pass  # If length less than window
            else: img = ImageTk.PhotoImage(billede.resize((780, 500)))  # If dimensions are larger: resize
            # TODO: Dynamic resizing (function)

            print('Width:', img.width(), ' Height', img.height())

            self.curr_img = img
            self.billede_label = ttk.Label(owner, image=self.curr_img)
            self.billede_label.grid(column=0, row=5, sticky=tk.NSEW, padx=5, pady=5, columnspan=5, rowspan=5)

            # test size change
            # owner.geometry('1200x800')

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
            img = ImageTk.PhotoImage(billede)

            self.curr_img = img
            self.billede_label = ttk.Label(owner, image=self.curr_img)
            self.billede_label.grid(column=3, row=5, sticky=tk.EW, padx=5, pady=5)

        except PermissionError:
            self.vis_forrige_billede(dirlist, owner)

    @staticmethod
    def resize_image(picture):
        if picture.width() <= 780:
            pass  # If width less than window
        elif picture.height() <= 500:
            pass  # If length less than window
        else:
            img = ImageTk.PhotoImage(picture.resize((780, 500)))  # If dimensions are larger: resize
        return picture.width(), picture.height()


# Laver en App klasse som indeholder vores root vindue.
class App(tk.Tk):
    def __init__(self):
        super().__init__()  # Arv fra tkinter
        self.title("Hello World")  # Titel på main vindue
        self.geometry("800x600")  # Demensioner på vindue
        self.resizable(False, False)  # Lås demensioner

    def update(self) -> None:
        self.geometry(self.test2)


if __name__ == "__main__":
    app = App()
    BilledKig(app)
    app.mainloop()  # Kør mainloop
