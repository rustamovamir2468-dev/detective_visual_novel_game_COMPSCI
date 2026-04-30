# main.py
# =============================================================
# This is the main entry point for the game.
# It initializes everything and contains the main game loop.
# Authors: 5752530
# =============================================================

from core.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()