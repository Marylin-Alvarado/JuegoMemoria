from game_logic import MemoryGame  # ✅ Esto sí funcionará


def main():
    theme = ["🌸", "🌼", "🌻", "🌹"]  # Puedes cambiar a animales 🐶, 🐱, etc.
    game = MemoryGame(theme)

    while not game.is_finished():
        game.board.display()
        idx1 = int(input("Elige la primera carta: "))
        idx2 = int(input("Elige la segunda carta: "))
        game.play_turn(idx1, idx2)

    print("¡Has encontrado todas las parejas!")

if __name__ == "__main__":
    main()
