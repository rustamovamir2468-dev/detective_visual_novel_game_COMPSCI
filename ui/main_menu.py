# main_menu.py - this is the first screen you see
# author 5734011 + 5752530
# function: show the game title and a start button

import pygame
from core.game_state import State
from settings import *

class MainMenu:

    def __init__(self, screen):
        self.screen = screen # save the screen to draw on it
        # make two sizes of text: big for title, medium for button 📏
        self.font_title = pygame.font.SysFont("Arial", FONT_SIZE_TITLE)
        self.font_button = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)
        self.hovered = False # is the mouse touching the button?

        # button size settings
        self.button_width = 300
        self.button_height = 55
        # math: find the center of the screen to put the button box
        self.button_rect = pygame.Rect((SCREEN_WIDTH - self.button_width) // 2, (SCREEN_HEIGHT // 2) + 40, self.button_width, self.button_height)

    def draw(self, palette): 
        # first, fill the screen with background color 🎨
        self.screen.fill(palette["bg"])
        # then draw the title and the button on top
        self._draw_title(palette)
        self._draw_button(palette)

    def handle_event(self, event, gsm): 
        # this part checks what you are doing with your mouse 🖱️

        # check 1: are you moving the mouse?
        if event.type == pygame.MOUSEMOTION:
            # if the mouse is inside the button box, hovered becomes True
            self.hovered = self.button_rect.collidepoint(event.pos)

        # check 2: did you click the left mouse button?
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # if you click inside the button box
            if self.button_rect.collidepoint(event.pos):
                # tell the game to go to the name typing page
                gsm.change_state(State.NAME_INPUT)

    def _draw_title(self, palette): 
        # this draws the game name "ALIAS" near the top
        title_surface = self.font_title.render(TITLE, True, palette["text"])
        # math: find the middle x and y so the title looks nice
        x = (SCREEN_WIDTH - title_surface.get_width()) // 2
        y = (SCREEN_HEIGHT // 2) - 120
        self.screen.blit(title_surface, (x, y))

    def _draw_button(self, palette): 
        # 1. pick the color: if mouse is on it, use 'accent'. 🙅 use 'ui'
        colour = palette["accent"] if self.hovered else palette["ui"]
        
        # 2. draw the button box with rounded corners
        pygame.draw.rect(self.screen, colour, self.button_rect, border_radius=8)
        # 3. draw a white line around the box
        pygame.draw.rect(self.screen, WHITE, self.button_rect, 2, border_radius=8)

        # 4. draw the "Start" text inside the button
        text_surface = self.font_button.render("Start", True, WHITE)
        # math: make the text stay exactly in the middle of the button box
        text_x = self.button_rect.centerx - text_surface.get_width() // 2
        text_y = self.button_rect.centery - text_surface.get_height() // 2
        self.screen.blit(text_surface, (text_x, text_y))
