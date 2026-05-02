# core/game.py
# =============================================================
# LOGIC TEAM: The main Game class.
# This opens the pygame window and runs the master game loop.
# Every frame: handle input -> update logic -> draw to screen.
# Authors: 5752530
# =============================================================

import pygame
import sys

from settings import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE, WHITE, BLACK, DARK_GRAY)
from core.game_state import GameStateManager, State

class Game:
    """The top-level Game class. Creates the window, owns the GSM, and runs the main loop"""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.gsm = GameStateManager()

        self.font = pygame.font.SysFont("Arial", 24) # Placeholder font

# --- Main game loop ---

    def run(self):
        """Start and keep running the game until the player quits."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

# --- Event handling ---
    """Read all input events (keyboard, mouse, etc.) and respond to them."""

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.gsm.is_state(State.SCENE):
                        self.gsm.change_state(State.PAUSED)
                    elif self.gsm.is_state(State.PAUSED):
                        self.gsm.revert()

# --- Update logic ---
    """Update all game logic (movement, interactions, etc.) based on the current state."""

    def update(self):
        if self.gsm.is_state(State.MAIN_MENU):
            pass # main_menu.py

        elif self.gsm.is_state(State.SCENE):
            pass # scene_manager.py

        elif self.gsm.is_state(State.DIALOGUE):
            pass # dialogue_manager.py

        elif self.gsm.is_state(State.CUTSCENE):
            pass # cutscene_manager.py

        elif self.gsm.is_state(State.BULLETIN_BOARD):
            pass # bulletin_board.py

        elif self.gsm.is_state(State.DEDUCTION):
            pass # deduction_manager.py

        elif self.gsm.is_state(State.GAME_OVER):
            pass # game_over.py

# --- Drawing ---
    """Draw everything to the screen based on the current state."""

    def draw(self):
        self.screen.fill(BLACK)

        if self.gsm.is_state(State.MAIN_MENU):
            self._draw_placeholder("MAIN MENU - press Enter to start")

        elif self.gsm.is_state(State.SCENE):
            self._draw_placeholder("SCENE - press ESC to pause")

        elif self.gsm.is_state(State.DIALOGUE):
            self._draw_placeholder("DIALOGUE STATE")

        elif self.gsm.is_state(State.PAUSED):
            self._draw_placeholder("PAUSED - press ESC to resume")
            
        elif self.gsm.is_state(State.BULLETIN_BOARD):
            self._draw_placeholder("BULLETIN BOARD")

        elif self.gsm.is_state(State.DEDUCTION):
            self._draw_placeholder("DEDUCTION")

        elif self.gsm.is_state(State.GAME_OVER):
            self._draw_placeholder("GAME OVER")

        pygame.display.flip()

# --- Helper ---
    """Draws a simple placeholder message in the center of the screen for each state, until we implement the actual screens."""
    def _draw_placeholder(self, message: str):
        text_surface = self.font.render(message, True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)