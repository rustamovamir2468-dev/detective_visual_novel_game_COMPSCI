# title_card.py - show the act title like "act 1: hello"
# author 5734011+5752530
# function: make text fade in and out between game levels
import pygame
from settings import *
from core.game_state import State

class TitleCard:

    def __init__(self, screen):
        self.screen = screen # save the screen
        # two text sizes: one for "act 1" and one for the name
        self.font_act = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        self.font_title = pygame.font.SysFont("Arial", FONT_SIZE_TITLE)

        self.act_text = ""   # e.g. "act 1" 📝
        self.title_text = ""   # e.g. "a normal day"
        self.alpha = 0    # how see-through the text is (0 = invisible, 255 = solid)
        self.phase = "fade_in"  # what are we doing? (fade_in, hold, or fade_out)
        self.hold_timer = 0   # count how long the text stays on screen
        self.hold_duration = 120 # stay solid for 120 frames (about 2 seconds)
        self.fade_speed = 3    # how fast to fade in/out
        self.done = False  # is the whole thing finished?

    def load(self, act_text, title_text): 
        # reset everything to zero before we show a new act title
        self.act_text = act_text
        self.title_text= title_text
        self.alpha = 0
        self.phase= "fade_in"
        self.hold_timer = 0
        self.done = False

    def update(self, gsm): 
        # check 1: are we fading in? 📈
        if self.phase == "fade_in":
            self.alpha += self.fade_speed # make it more visible
            if self.alpha >= 255:
                self.alpha = 255
                self.phase = "hold"  # okay, it's solid, now just wait

        # check 2: are we waiting? ⏳
        elif self.phase == "hold":
            self.hold_timer += 1 # tick tock...
            if self.hold_timer >= self.hold_duration:
                self.phase = "fade_out"  # time is up, start disappearing

        # check 3: are we fading out? 📉
        elif self.phase == "fade_out":
            self.alpha -= self.fade_speed # make it more see-through
            if self.alpha <= 0:
                self.alpha = 0
                self.done  = True
                gsm.change_state(State.DIALOGUE)  # now tell the game to start the real scene!
                
    def draw(self, palette):
        # 1. clean the screen first
        self.screen.fill(palette["bg"])
        
        # 2. create the text images
        act_surface   = self.font_act.render(self.act_text,   True, palette["text"])
        title_surface = self.font_title.render(self.title_text, True, palette["accent"])

        # 3. set the "see-through" level for the text
        act_surface.set_alpha(self.alpha)
        title_surface.set_alpha(self.alpha)

        # 4. math: find the center so it looks nice and balanced
        act_x = (SCREEN_WIDTH  - act_surface.get_width())   // 2
        act_y = (SCREEN_HEIGHT // 2) - 60
        title_x = (SCREEN_WIDTH  - title_surface.get_width()) // 2
        title_y = (SCREEN_HEIGHT // 2) + 10

        # 5. put the text on the screen
        self.screen.blit(act_surface,   (act_x,   act_y))
        self.screen.blit(title_surface, (title_x, title_y))
