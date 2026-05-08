# game_over.py - File that draws the bad ending / game over screen.
# Author(s): 5752530
# ====================================================
# Shown whenever the player reaches a bad ending node.
# Displays the ending text and offers:
# "Try Again" — rewinds to the last checkpoint (only shown if one exists).
# "Quit"      — closes the game.
# ====================================================

import pygame
import sys
from settings import *

class GameOver:

    def __init__(self, screen):
        self.screen       = screen
        self.font_title   = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        self.font_text    = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)
        self.font_button  = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)

        self.ending_text  = "" # Narrative text for this bad ending.
        self.can_rewind   = False # Whether a checkpoint exists to go back to.
        self.hovered      = None # Index of the button being hovered.

        self.button_width  = 280
        self.button_height = 50
        self.button_gap    = 20

    def load(self, ending_text, can_rewind=True): # Call this before switching to GAME_OVER state.
        self.ending_text = ending_text
        self.can_rewind  = can_rewind
        self.hovered     = None

    def _get_buttons(self):
        buttons = []
        if self.can_rewind:
            buttons.append(("Try Again", "rewind"))
        buttons.append(("Quit", "quit"))
        return buttons

    def _get_rect(self, index, total):
        x       = (SCREEN_WIDTH - self.button_width) // 2
        start_y = (SCREEN_HEIGHT // 2) + 60
        y       = start_y + index * (self.button_height + self.button_gap)
        return pygame.Rect(x, y, self.button_width, self.button_height)

    def handle_event(self, event): # Returns "rewind", "quit", or None.
        buttons = self._get_buttons()

        if event.type == pygame.MOUSEMOTION:
            self.hovered = None
            for i in range(len(buttons)):
                if self._get_rect(i, len(buttons)).collidepoint(event.pos):
                    self.hovered = i

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, (_, action) in enumerate(buttons):
                if self._get_rect(i, len(buttons)).collidepoint(event.pos):
                    return action

        return None

    def draw(self, palette):
        self.screen.fill(palette["bg"])

        # --- "BAD ENDING" title in red ---
        title = self.font_title.render("BAD ENDING", True, ACCENT_RED)
        self.screen.blit(title, ((SCREEN_WIDTH - title.get_width()) // 2, 80))

        # --- Ending description, word-wrapped ---
        self._draw_wrapped(self.ending_text, palette)

        # --- Buttons ---
        buttons = self._get_buttons()
        for i, (label, _) in enumerate(buttons):
            rect   = self._get_rect(i, len(buttons))
            colour = palette["accent"] if self.hovered == i else palette["ui"]
            pygame.draw.rect(self.screen, colour, rect, border_radius=8)
            pygame.draw.rect(self.screen, WHITE,  rect, 2, border_radius=8)
            text   = self.font_button.render(label, True, WHITE)
            self.screen.blit(text, (rect.centerx - text.get_width()  // 2, rect.centery - text.get_height() // 2))

    def _draw_wrapped(self, text, palette):
        words    = text.split(" ")
        lines    = []
        current  = ""
        max_w    = SCREEN_WIDTH - 160

        for word in words:
            test = current + word + " "
            if self.font_text.size(test)[0] <= max_w:
                current = test
            else:
                lines.append(current)
                current = word + " "
        lines.append(current)

        start_y = 160
        for i, line in enumerate(lines):
            surf = self.font_text.render(line, True, palette["text"])
            self.screen.blit(surf, ((SCREEN_WIDTH - surf.get_width()) // 2, start_y + i * (FONT_SIZE_MEDIUM + 8)))