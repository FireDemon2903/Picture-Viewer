import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import os
# ^ ^ ^ ^ ^ Import ^ ^ ^ ^ ^
# TODO: Fix billede load, så den opdaterer billedets demensioner (scale) efter resize_image funktionen
# TODO: Fix billede panning med mus
# TODO: Lås knapper og tset_label i frame over billedet, så de ikke flytter sig når der bliver zoomet
# TODO: Fjern hard-coded filepaths
# TODO: Profit :)


# Lav klassen "BilledKig" til widgets som skal vises til brugeren
class BilledKig(ttk.Frame):
    curr_img_num = 0

    def __init__(self, owner_root, dirlist):
        super().__init__(owner_root)  # Her kalder vi superklassen, som er "ttk.Frame".
        # Som argument sendes vores "App" klasse, som agerer som en beholder
        self.dirlist = dirlist

        # Test label
        self.test_label = ttk.Label(self, text="Hello World", anchor=tk.CENTER)
        self.test_label.grid(row=0, column=1, sticky=tk.EW, columnspan=2)

        self.naeste_knap = ttk.Button(self, text="Neaste", command=lambda: self.vis_neaste_billede(owner_root))  # Opret knap
        self.naeste_knap.grid(column=2, row=1, sticky=tk.EW, padx=5, pady=5)  # Placer knap

        self.forrige_knap = ttk.Button(self, text="Forrige", command=lambda: self.vis_forrige_billede(owner_root))  # Opret knap
        self.forrige_knap.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)  # Placer knap

        self.img = Image.open(f"C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{self.dirlist[0]}")
        dim = self.resize_image_check(self.img)
        self.img_tk = ImageTk.PhotoImage(self.img.resize(dim))

        self.billede_label = ttk.Label(self, image=self.img_tk)
        self.billede_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5, columnspan=5, rowspan=5)

        owner_root.bind("<MouseWheel>", self.zoom)
        self.x, self.y = 0, 0
        self.scale = 1.0

        owner_root.bind("w", lambda event: self.vis_forrige_billede(owner_root))
        owner_root.bind("e", lambda event: self.vis_neaste_billede(owner_root))
        owner_root.bind("r", lambda event: self.update_billede())
        # Eksempel: self.frame.bind("<Return>", lambda event, a=10, b=20, c=30: self.rand_func(a, b, c))

        # test size change
        # owner.geometry('1200x800')
        # size change works, but isn't implemented (yet?)

    def vis_neaste_billede(self, owner):  # Funktion til visning af naeste billede
        try:
            self.curr_img_num += 1  # Increment index number (next picture)
            self.update_billede()
            self.naeste_knap.focus()

        except IndexError:
            self.curr_img_num = -1
            self.vis_neaste_billede(owner)

        except PermissionError:
            self.vis_neaste_billede(owner)

    def vis_forrige_billede(self, owner):  # Funktion til visning af forrige billede
        try:
            if self.curr_img_num != 0:
                self.curr_img_num -= 1
            else:
                self.curr_img_num = len(self.dirlist) - 1

            self.update_billede()
            self.forrige_knap.focus()

        except PermissionError:  # Hvis der er andre mapper i mappen, ignorer dem og gå videre
            self.vis_forrige_billede(owner)

    def zoom(self, event):
        if event.delta > 0:
            self.scale += 0.1
        else:
            self.scale -= 0.1

        # Create a new image with the zoomed size
        self.img_tk = ImageTk.PhotoImage(self.img.resize((int(self.img.width * self.scale), int(self.img.height * self.scale))))
        self.billede_label.config(image=self.img_tk)

    def update_billede(self):
        self.img = Image.open(f"C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{self.dirlist[self.curr_img_num]}")
        dim = self.resize_image_check(self.img)

        self.img_tk = ImageTk.PhotoImage(self.img.resize(dim))
        self.billede_label.config(image=self.img_tk)

        self.x, self.y = 0, 0
        self.scale = 1

    @staticmethod
    def resize_image_check(image):  # Staticmethod, som returnerer et billedes demensioner, efter et check om den kan være i beholderen
        img_width, img_height = image.width, image.height  # Get image dimensions
        max_width, max_height = 780, 500  # Assign max width and height

        resize_width = False
        resize_height = False

        if img_width >= max_width: resize_width = True  # If width greater than window
        if img_height >= max_height: resize_height = True  # If length greater than window
        if resize_width: img_width = max_width  # Change width to 780
        if resize_height: img_height = max_height  # Change height to 500

        return img_width, img_height


# Laver en 'App' klasse. Agerer som vores root vindue.
class App(tk.Tk):
    def __init__(self):
        super().__init__()  # Arv fra tkinter
        self.title("Hello World")  # Titel på main vindue
        self.geometry("800x600")  # Demensioner på vindue
        self.resizable(False, False)  # Lås demensioner


if __name__ == "__main__":
    app = App()  # Instansiér App()
    img_folder = os.listdir('C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data')
    BilledKig(app, img_folder).pack()  # Instansiér BilledKig(), med app og dirlist som args
    app.mainloop()  # Kør mainloop
