# pause_menu.py - File that draws the pause menu overlay
# Author(s): 5752530
# ====================================================
# Draws a semi-transparent overlay with two options: Resume (returns to the game) and Quit (closes the game).
# Triggered by pressing Escape during gameplay.
# ====================================================
import pygame
import sys
from settings import *

class PauseMenu:

    def __init__(self, screen):
        self.screen       = screen
        self.font_title   = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        self.font_button  = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)
        self.hovered      = None  # Index of the button currently being hovered over.

        # --- Button dimensions ---
        self.button_width  = 300
        self.button_height = 50
        self.button_gap    = 20

        # --- The two buttons: 0 = Resume, 1 = Quit ---
        self.options = ["Resume", "Quit"]

        # Add sound effect of clicking for the pause menu - 5744357
        self.click_sfx = pygame.mixer.Sound(CLICK_SFX_PATH)
        self.click_sfx.set_volume(0.35)

    def draw(self, palette): # Draws the semi-transparent overlay and the menu buttons.
        self._draw_overlay()
        self._draw_title(palette)
        for i, option in enumerate(self.options):
            rect = self._get_rect(i)
            self._draw_button(rect, option, i, palette)

    def handle_event(self, event, gsm): # Handles mouse movement and clicks.
        # gsm — the GameStateManager, so Resume can switch state back.
        if event.type == pygame.MOUSEMOTION:
            self.hovered = None
            for i in range(len(self.options)):
                if self._get_rect(i).collidepoint(event.pos):
                    self.hovered = i

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(len(self.options)):
                if self._get_rect(i).collidepoint(event.pos):
                    
                    # Play clicking sound
                    self.click_sfx.play()
                    
                    if i == 0:              # Resume button.
                        gsm.revert()        # Revert goes back to whatever state we paused from.
                    elif i == 1:            # Quit button.
                        pygame.quit()
                        sys.exit()

    def _draw_overlay(self): # Draws a semi-transparent dark rectangle over the whole screen.
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)  # SRCALPHA enables transparency.
        overlay.fill((0, 0, 0, 160))        # Black with 160 out of 255 opacity.
        self.screen.blit(overlay, (0, 0))

    def _draw_title(self, palette): # Draws the "PAUSED" title near the top centre of the overlay.
        title_surface = self.font_title.render("PAUSED", True, WHITE)
        x = (SCREEN_WIDTH  - title_surface.get_width())  // 2
        y = (SCREEN_HEIGHT // 2) - 120
        self.screen.blit(title_surface, (x, y))
    
    def _get_rect(self, index): # Calculates the rectangle for a button at a given index.
        x = (SCREEN_WIDTH  - self.button_width)  // 2
        y = (SCREEN_HEIGHT // 2) - 20 + index * (self.button_height + self.button_gap)
        return pygame.Rect(x, y, self.button_width, self.button_height)

    def _draw_button(self, rect, text, index, palette): # Draws a single button, highlighted if hovered.
        colour = palette["accent"] if self.hovered == index else palette["ui"]
        pygame.draw.rect(self.screen, colour, rect, border_radius=8)
        pygame.draw.rect(self.screen, WHITE,  rect, 2, border_radius=8)

        text_surface = self.font_button.render(text, True, WHITE)
        text_x = rect.centerx - text_surface.get_width()  // 2
        text_y = rect.centery - text_surface.get_height() // 2
        self.screen.blit(text_surface, (text_x, text_y))
