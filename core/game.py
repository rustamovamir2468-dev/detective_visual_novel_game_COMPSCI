# game.py - File that opens window and runs the game loop.
# Author(s): 5752530
# ====================================================
# This is the main file that runs the game.
# Opens the window, runs the loop, and coordinates between the different systems.
# ====================================================

import pygame
import sys # Only needed for sys,exit() to close the game when the player clicks the X button on the window.
from settings import * # Import all the constants from settings.py.
from core.game_state import GameStateManager, State

# --- The main game class ---
class Game:
    def __init__(self):
        pygame.init()
        self.screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock   = pygame.time.Clock() # Controls game loop timing (FPS).
        self.gsm     = GameStateManager()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events() # Checks for player input and other events.
            self.update() # Updates the game state
            self.draw() # Draws the current state of the game to the screen.
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get(): # Returns list of all events that happened since last frame
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.gsm.is_state(State.PAUSED):
                        self.gsm.revert()
                    elif not self.gsm.is_state(State.MAIN_MENU):
                        self.gsm.change_state(State.PAUSED)

    def update(self): # REPLACE EACH PASS WITH THE APPROPRIATE FUNCTION CALLS TO UPDATE THE GAME STATE.
        if self.gsm.is_state(State.MAIN_MENU):
            pass
        elif self.gsm.is_state(State.SCENE):
            pass
        elif self.gsm.is_state(State.DIALOGUE):
            pass
        elif self.gsm.is_state(State.PAUSED):
            pass
        elif self.gsm.is_state(State.BULLETIN_BOARD):
            pass
        elif self.gsm.is_state(State.DEDUCTION):
            pass
        elif self.gsm.is_state(State.GAME_OVER):
            pass

    def draw(self): # DRAW THE APPROPRIATE THINGS FOR EACH STATE, FOR NOW JUST PLACEHOLDERS.
        self.screen.fill(BLACK) # Clear the screen with a black background before drawing anything.

        if self.gsm.is_state(State.MAIN_MENU):
            self._draw_placeholder("MAIN MENU")
        elif self.gsm.is_state(State.SCENE):
            self._draw_placeholder("SCENE")
        elif self.gsm.is_state(State.DIALOGUE):
            self._draw_placeholder("DIALOGUE")
        elif self.gsm.is_state(State.PAUSED):
            self._draw_placeholder("PAUSED")
        elif self.gsm.is_state(State.BULLETIN_BOARD):
            self._draw_placeholder("BULLETIN BOARD")
        elif self.gsm.is_state(State.DEDUCTION):
            self._draw_placeholder("DEDUCTION")
        elif self.gsm.is_state(State.GAME_OVER):
            self._draw_placeholder("GAME OVER")

        pygame.display.flip() # Update the full screen with this frame, because we are using double buffering (the default in Pygame).

    def _draw_placeholder(self, label: str):
        font    = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        surface = font.render(label, True, WHITE) # True for anti-aliasing, WHITE for colour.
        x = (SCREEN_WIDTH  - surface.get_width())  // 2
        y = (SCREEN_HEIGHT - surface.get_height()) // 2
        self.screen.blit(surface, (x, y)) # Blit means to draw the surface onto the screen at the specified coordinates.

# --- Start the game when this file is run directly ---
if __name__ == "__main__":
    game = Game()
    game.run()