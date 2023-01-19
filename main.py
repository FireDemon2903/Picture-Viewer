import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import os
# ^ ^ ^ ^ ^ Import ^ ^ ^ ^ ^


# Lav klassen "BilledKig" til widgets som skal vises til brugeren
class BilledKig(ttk.Frame):
    dirlist = os.listdir('.\\tis')
    print(dirlist)
    print(len(dirlist))

    curr_img_num = 0

    def __init__(self, owner):
        super().__init__(owner)  # Her kalder vi superklassen, som er "ttk.Frame".
        # Som argument sendes vores "App" klasse, som agerer som en beholder/vores 'root'

        # Test label
        test_label = ttk.Label(owner, text="Hello World")
        test_label.grid(row=0, column=0, sticky="nsew")

        naeste_knap = ttk.Button(owner, text="Neaste", command=lambda: self.vis_neaste_billede(self.dirlist, owner))  # Opret knap
        naeste_knap.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)  # Placer knap
        naeste_knap.focus()

        forrige_knap = ttk.Button(owner, text="Forrige", command=lambda: self.vis_forrige_billede(self.dirlist, owner))  # Opret knap
        forrige_knap.grid(column=2, row=2, sticky=tk.EW, padx=5, pady=5)  # Placer knap

        billede = Image.open(
            f".\\tis\\{self.dirlist[0]}")
        billede = billede.resize((780, 500))
        self.curr_img = ImageTk.PhotoImage(billede)

        self.billede_label = ttk.Label(owner, image=self.curr_img)
        self.billede_label.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5, columnspan=5, rowspan=5)

    def vis_neaste_billede(self, dirlist, owner):  # Funktion til visning af naeste billede
        try:
            self.curr_img_num += 1

            billede = Image.open(f".\\tis\\{dirlist[self.curr_img_num]}")  # path
            
            img_dim = self.resize_image(ImageTk.PhotoImage(billede))  # Skaf billedets demensioner. Hvis det ikke passer ind i beholderen, gør det mindre
            img = ImageTk.PhotoImage(billede.resize(img_dim))  # Gør billedet mindre, hvis det ikke passer

            self.curr_img = img  # Set nyt billede til at blive vist
            self.billede_label = ttk.Label(owner, image=self.curr_img)  # Lav label til billedet
            self.billede_label.grid(column=0, row=5, sticky=tk.NSEW, padx=5, pady=5, columnspan=5, rowspan=5)  # Formater

            # test size change:
            # owner.geometry('1200x800')
            # size change works, but isn't implemented (yet?)

        except IndexError:
            self.curr_img_num = -1
            self.vis_neaste_billede(dirlist, owner)

        except PermissionError:  # Hvis der er andre mapper i dirlist, ignorer dem og gå videre til naeste
            self.vis_neaste_billede(dirlist, owner)

    def vis_forrige_billede(self, dirlist, owner):  # Funktion til visning af forrige billede
        try:
            if self.curr_img_num != 0:
                self.curr_img_num -= 1
            else:
                self.curr_img_num = len(dirlist) - 1


            billede = Image.open(f".\\tis\\{dirlist[self.curr_img_num]}")  # Path
            img_dim = self.resize_image(ImageTk.PhotoImage(billede))  # Skaf billedets demensioner. Hvis det ikke passer ind i beholderen, gør det mindre
            img = ImageTk.PhotoImage(billede.resize(img_dim))  # Gør billedet mindre, hvis det ikke passer
            
            self.curr_img = img  # Set nyt billede til at blive vist
            self.billede_label = ttk.Label(owner, image=self.curr_img)  # Lav label til billedet
            self.billede_label.grid(column=0, row=5, sticky=tk.NSEW, padx=5, pady=5, columnspan=5, rowspan=5)  # Formater

        except PermissionError:  # Hvis der er andre mapper i dirlist, ignorer dem og gå videre til naeste
            self.vis_forrige_billede(dirlist, owner)

    def zoom_billede(self):  # TODO
        pass

    @staticmethod
    def resize_image(image):  # Staticmethod, som returnerer et billedes demensioner, efter et check om den kan være i beholderen
        img_width, img_height = image.width(), image.height()  # Get image dimensions
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
    BilledKig(app)  # Instansiér BilledKig(), med app som arg(beholder)
    app.mainloop()  # Kør mainloop
