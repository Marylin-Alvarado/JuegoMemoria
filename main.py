import tkinter as tk
from game_logic import MemoryGame

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
