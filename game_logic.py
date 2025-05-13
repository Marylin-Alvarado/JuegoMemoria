import tkinter as tk
import random
from card import Card
from PIL import Image, ImageTk
import os
import time

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.level = 1
        self.locked = False
        self.start_time = 0
        self.time_limit = 60
        self.game_over = False
        self.bg_color = "#f0f8ff"  # azul claro
        self.master.configure(bg=self.bg_color)
        self.start_game()

    def start_game(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.cards = []
        self.first_card = None
        self.locked = False
        self.start_time = time.time()
        self.game_over = False

        self.load_images()
        self.create_board()

        self.label = tk.Label(self.master, text=f"\U0001F33C Nivel {self.level}", font=("Arial", 16, "bold"), bg=self.bg_color)
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        self.timer_label = tk.Label(self.master, text="Tiempo restante: 60s", font=("Arial", 12), bg=self.bg_color)
        self.timer_label.grid(row=0, column=3, sticky="e", padx=10)
        self.update_timer()

    def update_timer(self):
        if self.game_over:
            return

        elapsed = int(time.time() - self.start_time)
        remaining = self.time_limit - elapsed

        if remaining <= 10:
            self.timer_label.config(fg="red")
        else:
            self.timer_label.config(fg="black")

        if remaining >= 0:
            self.timer_label.config(text=f"Tiempo restante: {remaining}s")
            self.master.after(1000, self.update_timer)
        else:
            self.game_over = True
            self.time_out()

    def load_images(self):
        assets_path = os.path.join(os.getcwd(), 'assets')
        all_images = [
            os.path.join(assets_path, file)
            for file in os.listdir(assets_path)
            if file != 'reverso.png'
        ]

        base_pairs = 6
        increment_per_level = 2
        num_pairs = min(len(all_images), base_pairs + (self.level - 1) * increment_per_level)

        selected_images = random.sample(all_images, num_pairs)
        self.images = selected_images * 2
        random.shuffle(self.images)

        back_path = os.path.join(assets_path, 'reverso.png')
        self.back_image = Image.open(back_path).resize((100, 100))
        self.back_photo = ImageTk.PhotoImage(self.back_image)

    def create_board(self):
        cols = 4
        for index, image_path in enumerate(self.images):
            card = Card(self.master, image_path, lambda c=index: self.on_card_click(c))
            row = (index // cols) + 1
            col = index % cols
            card.button.grid(row=row, column=col, padx=5, pady=5)
            card.set_back_image(self.back_photo)
            card.show_back()
            self.cards.append(card)

    def on_card_click(self, index):
        if self.locked or self.game_over:
            return
        card = self.cards[index]
        if card.is_flipped or card.is_matched:
            return
        card.flip()
        if not self.first_card:
            self.first_card = card
        else:
            self.locked = True
            self.master.after(1000, self.check_match, card)

    def check_match(self, second_card):
        if not self.first_card:
            self.locked = False
            return
        if self.first_card.image_path == second_card.image_path:
            self.first_card.match()
            second_card.match()
        else:
            self.first_card.hide()
            second_card.hide()
        self.first_card = None
        self.locked = False
        if all(card.is_matched for card in self.cards):
            self.game_over = True
            self.master.after(500, self.show_level_complete)

    def show_level_complete(self):
        tiempo = int(time.time() - self.start_time)
        popup = tk.Toplevel(self.master)
        popup.title("\u2728 \u00a1Bien hecho!")
        popup.configure(bg="#d0f0c0")  # Verde claro

        msg = f"\U0001F604 \u00a1Nivel {self.level} superado!\nTiempo: {tiempo} segundos"
        tk.Label(popup, text=msg, font=("Arial", 14), bg="#d0f0c0").pack(padx=20, pady=10)

        tk.Button(popup, text="Siguiente nivel \u25B6\uFE0F", command=lambda: self.advance_level(popup)).pack(pady=10)

    def advance_level(self, popup):
        popup.destroy()
        self.level += 1
        self.start_game()

    def time_out(self):
        popup = tk.Toplevel(self.master)
        popup.title("\u23F3 Tiempo agotado")
        popup.configure(bg="#ffe4e1")  # Rosa claro

        tk.Label(popup, text=f"\u26A0\uFE0F Se te acabó el tiempo en el nivel {self.level}.", font=("Arial", 13), bg="#ffe4e1").pack(padx=20, pady=10)
        tk.Button(popup, text="Reintentar nivel \u21BA", command=lambda: self.retry_level(popup)).pack(pady=10)

    def retry_level(self, popup):
        popup.destroy()
        self.start_game()
