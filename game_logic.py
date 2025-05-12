import tkinter as tk
import random
from card import Card
from PIL import Image, ImageTk
import os

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de Memoria: Flores y Animales")
        self.cards = []
        self.first_card = None
        self.load_images()
        self.create_board()

    def load_images(self):
        self.images = []
        assets_path = os.path.join(os.getcwd(), 'assets')
        for file in os.listdir(assets_path):
            if file != 'reverso.png':
                self.images.append(os.path.join(assets_path, file))
        self.images *= 2  # Duplicar imágenes para pares
        random.shuffle(self.images)
        self.back_image = Image.open(os.path.join(assets_path, 'reverso.png'))
        self.back_image = self.back_image.resize((100, 100))
        self.back_photo = ImageTk.PhotoImage(self.back_image)

    def create_board(self):
        for index, image_path in enumerate(self.images):
            card = Card(self.master, image_path, lambda c=index: self.on_card_click(c))
            card.button.grid(row=index // 4, column=index % 4)
            card.back_image = self.back_photo
            card.button.config(image=self.back_photo)
            self.cards.append(card)

    def on_card_click(self, index):
        card = self.cards[index]
        if card.is_flipped or card.is_matched:
            return
        card.flip()
        if not self.first_card:
            self.first_card = card
        else:
            self.master.after(1000, self.check_match, card)

    def check_match(self, second_card):
        if self.first_card.image_path == second_card.image_path:
            self.first_card.match()
            second_card.match()
        else:
            self.first_card.hide()
            second_card.hide()
        self.first_card = None
