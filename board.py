from card import Card
import random

class Board:
    def __init__(self, theme):
        if theme == "flores":
            symbols = ["🌹", "🌻", "🌷", "🌼", "🌸", "🌺"]
        else:
            symbols = ["🐶", "🐱", "🐰", "🦊", "🐵", "🐸"]

        self.cards = [Card(symbol) for symbol in symbols for _ in range(2)]
        random.shuffle(self.cards)

    def display(self):
        for idx, card in enumerate(self.cards):
            print(f"[{idx}] {card}", end=' ')
        print()

    def reveal_card(self, index):
        self.cards[index].reveal()
        return self.cards[index]

    def hide_cards(self, idx1, idx2):
        self.cards[idx1].hide()
        self.cards[idx2].hide()

    def is_complete(self):
        return all(card.revealed for card in self.cards)
