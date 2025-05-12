class Card:
    def __init__(self, name):
        self.name = name
        self.revealed = False

    def reveal(self):
        self.revealed = True

    def hide(self):
        self.revealed = False

    def __repr__(self):
        return self.name if self.revealed else "🂠"

    def __str__(self):
        return self.name
