# title_card.py - File that draws the "Act #: ..." screen between acts
# Author(s): 5752530
# ====================================================
# Shows the act title (e.g. "Act 1 — A Normal Day") with a fade in and fade out effect.
# Automatically moves to the SCENE state when done.
# ====================================================
import pygame
from settings import *
from core.game_state import State

class TitleCard:

    def __init__(self, screen):
        self.screen      = screen
        self.font_act    = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        self.font_title  = pygame.font.SysFont("Arial", FONT_SIZE_TITLE)

        self.act_text      = ""    # e.g. "Act 1"
        self.title_text    = ""    # e.g. "A Normal Day"
        self.alpha         = 0    # Current opacity of the text (0 = invisible, 255 = fully visible).
        self.phase         = "fade_in"  # Current phase: "fade_in", "hold", or "fade_out".
        self.hold_timer    = 0    # Counts frames during the hold phase.
        self.hold_duration = 120 # How many frames to hold at full opacity (2 seconds at 60 FPS).
        self.fade_speed    = 3    # How many opacity units to change per frame.
        self.done          = False  # True when the full sequence has finished.

    def load(self, act_text, title_text): # Call this before switching to TITLE_CARD state.
        # Resets everything and loads the new act text.
        self.act_text     = act_text
        self.title_text   = title_text
        self.alpha        = 0
        self.phase        = "fade_in"
        self.hold_timer   = 0
        self.done         = False

    def update(self, gsm): # Called once per frame. Advances the fade in, hold, fade out sequence.
        # gsm — the GameStateManager, so we can switch to SCENE when done.

        if self.phase == "fade_in":
            self.alpha += self.fade_speed
            if self.alpha >= 255:
                self.alpha = 255
                self.phase = "hold"  # Fully visible, now hold.

        elif self.phase == "hold":
            self.hold_timer += 1
            if self.hold_timer >= self.hold_duration:
                self.phase = "fade_out"  # Hold finished, start fading out.

        elif self.phase == "fade_out":
            self.alpha -= self.fade_speed
            if self.alpha <= 0:
                self.alpha = 0
                self.done  = True
                gsm.change_state(State.DIALOGUE)  # Fade out done, move to the scene.

    def draw(self, palette):# Draws the act and title text centred on screen with current opacity.
        self.screen.fill(palette["bg"])

        act_surface   = self.font_act.render(self.act_text,   True, palette["text"])
        title_surface = self.font_title.render(self.title_text, True, palette["accent"])

        # Apply the current alpha (opacity) to both surfaces.
        act_surface.set_alpha(self.alpha)
        title_surface.set_alpha(self.alpha)

        act_x = (SCREEN_WIDTH  - act_surface.get_width())   // 2
        act_y = (SCREEN_HEIGHT // 2) - 60
        title_x = (SCREEN_WIDTH  - title_surface.get_width()) // 2
        title_y = (SCREEN_HEIGHT // 2) + 10

        self.screen.blit(act_surface,   (act_x,   act_y))
        self.screen.blit(title_surface, (title_x, title_y))
