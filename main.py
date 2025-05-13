import tkinter as tk
from game_logic import MemoryGame

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    root.resizable(False, False)
    game = MemoryGame(root)
    root.mainloop()
