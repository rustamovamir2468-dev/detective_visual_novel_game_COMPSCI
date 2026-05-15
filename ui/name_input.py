# name_input.py - page for typing your name
# author 5734011+5752530
# function: let player type name and press enter to start

import pygame
from settings import *
 
class NameInput:
 
    MAX_LENGTH = 16 # stop! cant type more than 16 letters 🛑
 
    def __init__(self, screen):
        self.screen = screen # save the screen so we can draw on it later
        # we make 3 sizes of text: big, medium, and small 📏
        self.font_prompt = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)
        self.font_input = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        self.font_hint = pygame.font.SysFont("Arial", FONT_SIZE_SMALL)
 
        self.text = "" # this is like an empty box to put your name in 📝
        self.cursor_visible = True # start with the "|" line showing
        self.cursor_timer = 0 # timer to count frames
        self.cursor_interval = 30 # wait for 30 frames to change the blink
 
        # math: find the center and draw a 400x55 box for typing 📦
        self.box_rect = pygame.Rect((SCREEN_WIDTH - 400) // 2, (SCREEN_HEIGHT // 2) - 30, 400, 55)
 
    def get_name(self):
        # give the name to the game, but cut off extra spaces at start or end
        return self.text.strip()
 
    def update(self):
        # we want the "|" to blink so it looks like a real typing bar 
        self.cursor_timer += 1
        if self.cursor_timer >= self.cursor_interval:
            self.cursor_timer = 0 # reset timer to zero
            # if it was showing, hide it. 🙅, show it!
            self.cursor_visible = not self.cursor_visible
 
    def handle_event(self, event, gsm): 
        # this part listens to what you do with your keyboard ⌨️
        if event.type == pygame.KEYDOWN:
            
            # check 1: did you press enter? 
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if self.text.strip(): # if you typed something
                    return "confirmed" # tell the game "we are ready!"
            
            # check 2: did you press backspace? (the delete button) ⬅️
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1] # take away the last letter
            
            # check 3: are you typing a new letter?
            else:
                # if the name is not too long AND the key is a real letter
                if len(self.text) < self.MAX_LENGTH and event.unicode.isprintable():
                    self.text += event.unicode # add the new letter to our name box
        return None 
 
    def draw(self, palette):
        # first, wash the screen with the background color 🎨
        self.screen.fill(palette["bg"])
 
        # 1. draw the question: "what is your name?"
        prompt = self.font_prompt.render("What is your name, player?", True, palette["text"])
        # math: put it in the middle but a bit higher up
        self.screen.blit(prompt, ((SCREEN_WIDTH - prompt.get_width()) // 2, SCREEN_HEIGHT // 2 - 100))
 
        # 2. draw the box where the name goes 📦
        # first the inside color, then the line around the box
        pygame.draw.rect(self.screen, palette["dialogue_bg"], self.box_rect, border_radius=8)
        pygame.draw.rect(self.screen, palette["ui"], self.box_rect, 2, border_radius=8)
 
        # 3. draw the name you typed + the blinking line "|"
        # if cursor_visible is true, add "|". 🙅, add a space " "
        display = self.text + ("|" if self.cursor_visible else " ")
        text_surface = self.font_input.render(display, True, palette["text"])
        
        # math: put the text inside the box, a little bit to the left side
        text_x = self.box_rect.x + 14
        text_y = self.box_rect.centery - text_surface.get_height() // 2
        self.screen.blit(text_surface, (text_x, text_y)) # boom! text is on screen
 
        # 4. draw a small tip: "press enter to start"
        hint = self.font_hint.render("Press Enter to confirm", True, palette["text"])
        # put it just below the typing box
        self.screen.blit(hint, ((SCREEN_WIDTH - hint.get_width()) // 2, self.box_rect.bottom + 18))
