# main_menu.py - File that draws the title/start screen
# Author(s): 5752530
# ====================================================
# The first screen the player sees when the game launches.
# Displays the game title and a Start button.
# Clicking Start moves the game to the NAME_INPUT state.
# ====================================================
import pygame
from core.game_state import State
from settings import *

class MainMenu:

    def __init__(self, screen):
        self.screen      = screen
        self.font_title  = pygame.font.SysFont("Arial", FONT_SIZE_TITLE)
        self.font_button = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)
        self.hovered     = False  # True when the mouse is over the Start button.

        # --- Start button dimensions ---
        self.button_width  = 300
        self.button_height = 55
        self.button_rect   = pygame.Rect((SCREEN_WIDTH  - self.button_width)  // 2, (SCREEN_HEIGHT // 2) + 40, self.button_width, self.button_height)

        # Initialise click sound effect for main menu
        self.click_sfx = pygame.mixer.Sound(CLICK_SFX_PATH) 
        self.click_sfx.set_volume(0.35)

    def draw(self, palette): # Draws the background, title and start button.
        self.screen.fill(palette["bg"])
        self._draw_title(palette)
        self._draw_button(palette)

    def handle_event(self, event, gsm): # Handles mouse movement and clicks on the Start button.
        # gsm — the GameStateManager, so clicking Start can switch state.

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.button_rect.collidepoint(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button_rect.collidepoint(event.pos):
                self.click_sfx.play() # Play the click sound effect
                gsm.change_state(State.NAME_INPUT)  # Move to name input before the game starts.

    def _draw_title(self, palette): # Draws the game title "ALIAS" centred near the top of the screen.
        title_surface = self.font_title.render(TITLE, True, palette["text"])
        x = (SCREEN_WIDTH  - title_surface.get_width())  // 2
        y = (SCREEN_HEIGHT // 2) - 120
        self.screen.blit(title_surface, (x, y))

    def _draw_button(self, palette): # Draws the Start button, highlighted if the mouse is hovering over it.
        colour = palette["accent"] if self.hovered else palette["ui"]
        pygame.draw.rect(self.screen, colour, self.button_rect, border_radius=8)
        pygame.draw.rect(self.screen, WHITE,  self.button_rect, 2, border_radius=8)

        text_surface = self.font_button.render("Start", True, WHITE)
        text_x = self.button_rect.centerx - text_surface.get_width()  // 2
        text_y = self.button_rect.centery - text_surface.get_height() // 2
        self.screen.blit(text_surface, (text_x, text_y))
