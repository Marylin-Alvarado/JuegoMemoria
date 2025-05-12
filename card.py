from PIL import Image, ImageTk
import tkinter as tk

class Card:
    def __init__(self, master, image_path, command):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.image = self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)
        self.button = tk.Button(master, image=self.photo, command=command)
        self.is_flipped = False
        self.is_matched = False

    def flip(self):
        if not self.is_flipped and not self.is_matched:
            self.button.config(image=self.photo)
            self.is_flipped = True

    def hide(self):
        if not self.is_matched:
            self.button.config(image=self.back_image)
            self.is_flipped = False

    def match(self):
        self.is_matched = True
