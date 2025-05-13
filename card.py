from PIL import Image, ImageTk
import tkinter as tk

class Card:
    def __init__(self, master, image_path, command):
        self.image_path = image_path
        self.image = Image.open(image_path).resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)

        self.button = tk.Button(master, command=command, relief="ridge", borderwidth=3, bg="#f0f0f0", activebackground="#d0f0d0")
        self.back_photo = None
        self.is_flipped = False
        self.is_matched = False

    def set_back_image(self, back_photo):
        self.back_photo = back_photo

    def show_back(self):
        self.button.config(image=self.back_photo)

    def flip(self):
        if not self.is_flipped and not self.is_matched:
            self.button.config(image=self.photo)
            self.is_flipped = True

    def hide(self):
        if not self.is_matched:
            self.button.config(image=self.back_photo)
            self.is_flipped = False

    def match(self):
        self.is_matched = True
        self.button.config(state=tk.DISABLED)
