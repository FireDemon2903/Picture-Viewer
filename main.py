import tkinter as tk
from tkinter import ttk
# from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import os
# ^ ^ ^ ^ ^ Import ^ ^ ^ ^ ^
# TODO: Fix billede load, så den opdaterer billedets demensioner (scale) efter resize_image funktionen
# TODO: Fix billede panning med mus
# TODO: Lås knapper og tset_label i frame over billedet, så de ikke flytter sig når der bliver zoomet
# TODO: Profit :)


class Knapper(ttk.Frame):
    def __init__(self, container, billede):
        super().__init__(container)

        self.naeste_knap = ttk.Button(self, text="Neaste", command=lambda: billede.vis_neaste_billede())  # Opret knap
        self.naeste_knap.grid(column=2, row=1, sticky=tk.EW, padx=5, pady=5)  # Placer knap

        self.forrige_knap = ttk.Button(self, text="Forrige", command=lambda: billede.vis_forrige_billede())  # Opret knap
        self.forrige_knap.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)  # Placer knap

        container.bind("w", lambda event: billede.vis_forrige_billede())
        container.bind("e", lambda event: billede.vis_neaste_billede())
        container.bind("r", lambda event: billede.update_billede())


# Lav klassen "BilledKig" til widgets som skal vises til brugeren
class BilledKig(ttk.Frame):
    curr_img_num = 0

    def __init__(self, container, dirlist):
        super().__init__(container)  # Her kalder vi superklassen, som er "ttk.Frame".
        # Som argument sendes vores "App" klasse, som agerer som en beholder
        self.container = container
        self.dirlist = dirlist

        self.img = Image.open(f"C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data\\{self.dirlist[0]}")
        dim = self.resize_image_check(self.img)
        self.img_tk = ImageTk.PhotoImage(self.img.resize(dim))

        self.billede_label = ttk.Label(self, image=self.img_tk)
        self.billede_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5, columnspan=4)

        self.container.bind("<MouseWheel>", self.zoom)
        self.x, self.y = 0, 0
        self.scale = 1.0

        # Til boarder rundt om frame
        self['borderwidth'] = 1
        self['relief'] = 'ridge'

    def vis_neaste_billede(self):  # Funktion til visning af naeste billede
        try:
            self.curr_img_num += 1  # Increment index number (next picture)
            self.update_billede()

        except IndexError:
            self.curr_img_num = -1
            self.vis_neaste_billede()

        except PermissionError:
            self.vis_neaste_billede()

    def vis_forrige_billede(self):  # Funktion til visning af forrige billede
        try:
            if self.curr_img_num != 0:
                self.curr_img_num -= 1
            else:
                self.curr_img_num = len(self.dirlist) - 1

            self.update_billede()

        except PermissionError:  # Hvis der er andre mapper i mappen, ignorer dem og gå videre
            self.vis_forrige_billede()

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
        self.geometry("1000x600")  # Demensioner på vindue
        self.resizable(False, False)  # Lås demensioner

        self.__create_widgets()

    def __create_widgets(self):

        img_folder = os.listdir(
            'C:\\Users\\Jonathan\\OneDrive - Rybners\\2G\\Programmering - 2G\\Gamejam - Jonathan^2 & Nataniel\\data')

        billede_frame = BilledKig(self, img_folder)  # Instansiér BilledKig(), med app og dirlist som args
        knapper = Knapper(self, billede_frame)

        knapper.pack()
        billede_frame.pack()


if __name__ == "__main__":
    app = App()  # Instansiér App()
    app.mainloop()  # Kør mainloop
