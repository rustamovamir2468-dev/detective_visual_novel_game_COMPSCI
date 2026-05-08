# name_input.py - File that draws the name entry screen.
# Author(s): 5752530
# ====================================================
# Shown after the player clicks Start on the main menu.
# Lets the player type their name with a blinking cursor.
# Pressing Enter confirms the name and signals game.py to call start_game().
# ====================================================
import pygame
from settings import *

class NameInput:

    MAX_LENGTH = 16 # Maximum characters the player can type.

    def __init__(self, screen):
        self.screen       = screen
        self.font_prompt  = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)
        self.font_input   = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        self.font_hint    = pygame.font.SysFont("Arial", FONT_SIZE_SMALL)

        self.text             = "" # What the player has typed so far.
        self.cursor_visible   = True # For the blinking cursor.
        self.cursor_timer     = 0
        self.cursor_interval  = 30 # Blink every 30 frames.

        # --- Input box rectangle ---
        self.box_rect = pygame.Rect( (SCREEN_WIDTH - 400) // 2, (SCREEN_HEIGHT // 2) - 30, 400, 55)

    def get_name(self):
        return self.text.strip()

    def update(self):
        self.cursor_timer += 1
        if self.cursor_timer >= self.cursor_interval:
            self.cursor_timer   = 0
            self.cursor_visible = not self.cursor_visible

    def handle_event(self, event, gsm): # Returns "confirmed" when the player presses Enter with a non-empty name.
        # Returns None otherwise.
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if self.text.strip():
                    return "confirmed"
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < self.MAX_LENGTH and event.unicode.isprintable():
                    self.text += event.unicode
        return None

    def draw(self, palette):
        self.screen.fill(palette["bg"])

        # --- Prompt ---
        prompt = self.font_prompt.render("What is your name, player?", True, palette["text"])
        self.screen.blit(prompt, ((SCREEN_WIDTH - prompt.get_width()) // 2, SCREEN_HEIGHT // 2 - 100))

        # --- Input box ---
        pygame.draw.rect(self.screen, palette["dialogue_bg"], self.box_rect, border_radius=8)
        pygame.draw.rect(self.screen, palette["ui"], self.box_rect, 2, border_radius=8)

        # --- Typed text + blinking cursor ---
        display      = self.text + ("|" if self.cursor_visible else " ")
        text_surface = self.font_input.render(display, True, palette["text"])
        text_x = self.box_rect.x + 14
        text_y = self.box_rect.centery - text_surface.get_height() // 2
        self.screen.blit(text_surface, (text_x, text_y))

        # --- Hint ---
        hint = self.font_hint.render("Press Enter to confirm", True, palette["text"])
        self.screen.blit(hint, ((SCREEN_WIDTH - hint.get_width()) // 2, self.box_rect.bottom + 18))