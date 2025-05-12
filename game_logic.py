from board import Board

class MemoryGame:
    def __init__(self, theme):
        self.board = Board(theme)

    def play_turn(self, idx1, idx2):
        card1 = self.board.reveal_card(idx1)
        card2 = self.board.reveal_card(idx2)
        self.board.display()
        if card1.name != card2.name:
            print("¡No coinciden!")
            self.board.hide_cards(idx1, idx2)
        else:
            print("¡Pareja encontrada!")

    def is_finished(self):
        return self.board.is_complete()
