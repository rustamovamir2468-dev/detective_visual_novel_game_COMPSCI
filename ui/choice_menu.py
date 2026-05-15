# choice_menu.py - Draw buttons for story choices
# Author 5734011 + 5752530
# Function: show buttons, check mouse clicks, return choice ID.

import pygame
from settings import *

class ChoiceMenu:

    def __init__(self, screen):
        self.screen = screen  # save the game screen
        self.font = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM) # set text style
        self.hovered = None   # which button is the mouse pointing at? (None = No button)

        # How big are the buttons?
        self.button_width = 800
        self.button_height = 70
        self.button_gap = 16  # space between buttons

    def draw(self, choices, palette):
        # Math: find where to start drawing so buttons are in the middle of screen
        total_height = len(choices) * (self.button_height + self.button_gap) - self.button_gap
        start_y = (SCREEN_HEIGHT - total_height) // 2

        for i, choice in enumerate(choices):
            # i is the button number (0, 1, 2...)
            rect = self._get_rect(i, start_y)
            self._draw_button(rect, choice.text, i, palette)

    def handle_event(self, event, choices, palette):
        # we need the same math to know where the buttons are
        total_height = len(choices) * (self.button_height + self.button_gap) - self.button_gap
        start_y = (SCREEN_HEIGHT - total_height) // 2

        # check 1: Is the mouse moving?
        if event.type == pygame.MOUSEMOTION:
            self.hovered = None # reset first, then check all buttons
            for i in range(len(choices)):
                rect = self._get_rect(i, start_y)
                if rect.collidepoint(event.pos): # if mouse is inside the button box
                    self.hovered = i # remember this button

        # check 2: did the player click the mouse? (1 = left click)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(len(choices)):
                rect = self._get_rect(i, start_y)
                if rect.collidepoint(event.pos): # if click is inside the button box
                    return i # give back the number of the button clicked

        return None # if no click, return nothing

    def _get_rect(self, index, start_y):
        # calculate the position (X and Y) for one button
        x = (SCREEN_WIDTH - self.button_width) // 2
        y = start_y + index * (self.button_height + self.button_gap)
        return pygame.Rect(x, y, self.button_width, self.button_height)

    def _draw_button(self, rect, text, index, palette):
        # if mouse is on the button, use 'accent' color. 🙅, use 'ui' color.
        if self.hovered == index:
            colour = palette["accent"]
        else:
            colour = palette["ui"]

        # 1. draw the button box (rounded corners)
        pygame.draw.rect(self.screen, colour, rect, border_radius=8)
        # 2. draw a white line around the button
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 2, border_radius=8)

        # 3. draw the choice text
        text_surface = self.font.render(text, True, (255, 255, 255))
        # Math: find the center of the button for the text
        text_x = rect.centerx - text_surface.get_width() // 2
        text_y = rect.centery - text_surface.get_height() // 2
        self.screen.blit(text_surface, (text_x, text_y)) # put text on screen
