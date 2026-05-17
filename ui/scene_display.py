# scene_display.py - File that draws the backround image and portraits
# Author(s): 5752530
# ====================================================
# Loads and draws the background image for the current scene and the character portrait for the current speaker.
# Uses placeholder coloured rectangles until the creative team provides the actual image assets.
# ====================================================
import pygame
from settings import *

class SceneDisplay:

    def __init__(self, screen):
        self.screen           = screen
        self.bg_cache         = {}       # Stores loaded background images so we don't reload them every frame.
        self.portrait_cache   = {}       # Same for portrait images.
        self.current_bg       = None     # The current background surface ready to draw.
        self.current_portrait = None    # The current portrait surface ready to draw.

    def load_background(self, bg_key):
        if bg_key is None:
            return

        # Try .jpg first, then .png
        for ext in ("jpg", "png"):
            bg_path = f"assets/images/background/{bg_key}.{ext}"
            if bg_path in self.bg_cache:
                self.current_bg = self.bg_cache[bg_path]
                return
            try:
                image = pygame.image.load(bg_path).convert()
                image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.bg_cache[bg_path] = image
                self.current_bg = image
                return
            except FileNotFoundError:
                continue

        # Neither extension found
        print(f"[Missing background] {bg_key}")
        self.current_bg = None

    def load_portrait(self, character, state): # Loads a character portrait based on the character name and emotion state.
        # e.g. character="elias", state="demon" loads assets/portraits/elias_demon.png
        if character is None:
            self.current_portrait = None
            return

        portrait_path = f"assets/images/portraits/{character}_{state}.png" # Modified for implementation of the portraits - 5744357

        if portrait_path not in self.portrait_cache:
            try:
                image = pygame.image.load(portrait_path).convert_alpha()             # convert_alpha() preserves transparency.
                image = pygame.transform.smoothscale(image, (PORTRAIT_WIDTH, PORTRAIT_HEIGHT))
                self.portrait_cache[portrait_path] = image
            except FileNotFoundError:
                print(f"[Missing portrait] {portrait_path}") # Terminal will tell which file is missing - 5744357
                self.portrait_cache[portrait_path] = None  # No asset yet, placeholder will show instead.

        self.current_portrait = self.portrait_cache[portrait_path]

    def draw(self, palette): # Draws the background first, then the portrait on top.

        # --- Background ---
        if self.current_bg:
            self.screen.blit(self.current_bg, (0, 0))
        else:
            self.screen.fill(palette["bg"])  # Fallback: plain colour if no background image yet.

        # --- Portrait ---
        if self.current_portrait:
            name_box_x = DIALOGUE_BOX_PADDING
            name_box_width = 200
            name_box_center_x = name_box_x + name_box_width // 2 # Setting the centre of the box - 5744357

            portrait_x = name_box_center_x - self.current_portrait.get_width() // 2 # Implementing the actual portrait in the centre - 5744357
            portrait_y = PORTRAIT_Y

            self.screen.blit(self.current_portrait, (portrait_x, portrait_y))            

    def _draw_portrait_placeholder(self, palette): # Draws a simple coloured rectangle where the portrait will eventually go.
        # Only shows when the actual portrait image hasn't been provided yet.
        placeholder_rect = pygame.Rect(PORTRAIT_X, PORTRAIT_Y, PORTRAIT_WIDTH, PORTRAIT_HEIGHT)
        pygame.draw.rect(self.screen, palette["ui"], placeholder_rect)
        pygame.draw.rect(self.screen, WHITE, placeholder_rect, 2)  # White border.