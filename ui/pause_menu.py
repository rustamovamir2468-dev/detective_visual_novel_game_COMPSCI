# pause_menu.py - this screen shows up when you hit esc
# author 5734011 + 5752530
# function: stop the game and show "resume" or "quit" buttons
import sys
from settings import *

class PauseMenu:

    def __init__(self, screen):
        self.screen = screen # save the game screen
         # set up text sizes: big for "paused", medium for buttons 📏
        self.font_title = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        self.font_button = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)
        self.hovered= None  # which button is the mouse touching? (none = zero)
        
        # how big the buttons should be
        self.button_width = 300
        self.button_height = 50
        self.button_gap = 20

        # the two choices we give to the player
        self.options = ["Resume", "Quit"]

        # Add sound effect of clicking for the pause menu - 5744357
        self.click_sfx = pygame.mixer.Sound(CLICK_SFX_PATH)
        self.click_sfx.set_volume(0.35)

    def draw(self, palette): 
        # 1. draw a dark shadow over the game 🌑
        self._draw_overlay()
        # 2. draw the word "paused"
        self._draw_title(palette)
        # 3. draw the two buttons
        for i, option in enumerate(self.options):
            rect = self._get_rect(i)
            self._draw_button(rect, option, i, palette)

    def handle_event(self, event, gsm): 
        # this part checks what you do with your mouse 🖱️
       
        # check 1: are you moving the mouse?
        if event.type == pygame.MOUSEMOTION:
            self.hovered = None # reset first
            for i in range(len(self.options)):
                # if mouse is inside a button box, remember which one
                if self._get_rect(i).collidepoint(event.pos):
                    self.hovered = i
        
        # check 2: did you click the left mouse button?
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(len(self.options)):
                if self._get_rect(i).collidepoint(event.pos):
                    
                    # Play clicking sound
                    self.click_sfx.play()
                    
                    if i == 0:         # you clicked "resume"
                        gsm.revert()   # go back to the game! ▶️
                    elif i == 1:       # you clicked "quit"
                        pygame.quit()  # close pygame 
                        sys.exit()     # close the whole window 🛑

    def _draw_overlay(self): 
        # this makes the screen look darker so the game looks "paused"
        # we make a special surface that can be see-through
        overlay= pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA) # fill with black, but with 160 opacity (not totally dark)
        overlay.fill((0, 0, 0, 160))        # Black with 160 out of 255 opacity.
        self.screen.blit(overlay, (0, 0))

    def _draw_title(self, palette): 
        # draw the big "PAUSED" text in the middle
        title_surface = self.font_title.render("PAUSED", True, WHITE)
        x = (SCREEN_WIDTH  - title_surface.get_width())  // 2
        y = (SCREEN_HEIGHT // 2) - 120
        self.screen.blit(title_surface, (x, y))
    
    def _get_rect(self, index): 
        # math: find the position for each button box
        # index 0 is higher, index 1 is lower
        x = (SCREEN_WIDTH  - self.button_width)  // 2
        y = (SCREEN_HEIGHT // 2) - 20 + index * (self.button_height + self.button_gap)
        return pygame.Rect(x, y, self.button_width, self.button_height)

    def _draw_button(self, rect, text, index, palette):  
        # if mouse is on it, use 'accent' color. 🙅 use 'ui' color
        colour = palette["accent"] if self.hovered == index else palette["ui"]

        # 1. draw the button box and its white border
        pygame.draw.rect(self.screen, colour, rect, border_radius=8)
        pygame.draw.rect(self.screen, WHITE,  rect, 2, border_radius=8)
        
        # 2. put the text (resume or quit) in the center of the box
        text_surface = self.font_button.render(text, True, WHITE)
        text_x= rect.centerx - text_surface.get_width()  // 2
        text_y = rect.centery - text_surface.get_height() // 2
        self.screen.blit(text_surface, (text_x, text_y))
