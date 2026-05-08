# choice_menu.py - File that draws the choice buttons when branching the story
# Author(s): 5752530
# ====================================================
# Displays a list of clickable choice buttons in the centre of the screen when the player reaches a choice node.
# Returns which choice was clicked, if any.
# ====================================================

import pygame
from settings import *

class ChoiceMenu:

    def __init__(self, screen):
        self.screen      = screen
        self.font        = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)
        self.hovered     = None  # Index of the button the mouse is currently over.

        # --- Button dimensions ---
        self.button_width  = 500
        self.button_height = 50
        self.button_gap    = 16   # Vertical space between each button.

    def draw(self, choices, palette): # Draws one button per choice, centred on screen.
            # choices — the list of Choice objects from the current story node.
            # palette — either PALETTE_WARM or PALETTE_COLD from settings.

            total_height = len(choices) * (self.button_height + self.button_gap) - self.button_gap
            start_y      = (SCREEN_HEIGHT - total_height) // 2  # Centre the group vertically.

            for i, choice in enumerate(choices):
                rect = self._get_rect(i, start_y)
                self._draw_button(rect, choice.text, i, palette)

    def handle_event(self, event, choices, palette): # Checks mouse movement and clicks against the choice buttons.
        # Returns the index of the clicked choice, or None if nothing was clicked.

        total_height = len(choices) * (self.button_height + self.button_gap) - self.button_gap
        start_y      = (SCREEN_HEIGHT - total_height) // 2

        if event.type == pygame.MOUSEMOTION:
            self.hovered = None
            for i in range(len(choices)):
                rect = self._get_rect(i, start_y)
                if rect.collidepoint(event.pos):  # collidepoint checks if the mouse is inside the rectangle.
                    self.hovered = i

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # event.button == 1 means left click.
            for i in range(len(choices)):
                rect = self._get_rect(i, start_y)
                if rect.collidepoint(event.pos):
                    return i  # Return the index of the clicked choice.

        return None  # Nothing was clicked.
    
    def _get_rect(self, index, start_y): # Calculates the rectangle for a button at a given index.
        x = (SCREEN_WIDTH - self.button_width) // 2  # Centre horizontally.
        y = start_y + index * (self.button_height + self.button_gap)
        return pygame.Rect(x, y, self.button_width, self.button_height)
    
    def _draw_button(self, rect, text, index, palette): # Draws a single button, highlighted if the mouse is hovering over it.
        if self.hovered == index:
            colour = palette["accent"]   # Highlighted colour on hover.
        else:
            colour = palette["ui"]       # Normal colour.

        pygame.draw.rect(self.screen, colour, rect, border_radius=8)
        pygame.draw.rect(self.screen, WHITE, rect, 2, border_radius=8)  # White border.

        text_surface = self.font.render(text, True, WHITE)
        text_x = rect.centerx - text_surface.get_width()  // 2  # Centre text horizontally in button.
        text_y = rect.centery - text_surface.get_height() // 2  # Centre text vertically in button.
        self.screen.blit(text_surface, (text_x, text_y))