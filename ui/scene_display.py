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

    def load_background(self, bg_path): # Loads a background image from a file path and scales it to fill the screen.
        # If the image was already loaded before, uses the cached version instead.
        if bg_path is None:
            self.current_bg = None
            return

        if bg_path not in self.bg_cache:
            try:
                image = pygame.image.load(bg_path).convert()                        # convert() speeds up drawing.
                image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT)) # Scale to fill the screen.
                self.bg_cache[bg_path] = image
            except FileNotFoundError:
                self.bg_cache[bg_path] = None  # File doesn't exist yet, store None as placeholder.

        self.current_bg = self.bg_cache[bg_path]

    def load_portrait(self, character, state): # Loads a character portrait based on the character name and emotion state.
        # e.g. character="elias", state="demon" loads assets/portraits/elias_demon.png
        if character is None:
            self.current_portrait = None
            return

        portrait_path = f"assets/portraits/{character}_{state}.png"

        if portrait_path not in self.portrait_cache:
            try:
                image = pygame.image.load(portrait_path).convert_alpha()             # convert_alpha() preserves transparency.
                image = pygame.transform.scale(image, (PORTRAIT_WIDTH, PORTRAIT_HEIGHT))
                self.portrait_cache[portrait_path] = image
            except FileNotFoundError:
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
            self.screen.blit(self.current_portrait, (PORTRAIT_X, PORTRAIT_Y))
        else:
            self._draw_portrait_placeholder(palette)  # Fallback: coloured rectangle.

    def _draw_portrait_placeholder(self, palette): # Draws a simple coloured rectangle where the portrait will eventually go.
        # Only shows when the actual portrait image hasn't been provided yet.
        placeholder_rect = pygame.Rect(PORTRAIT_X, PORTRAIT_Y, PORTRAIT_WIDTH, PORTRAIT_HEIGHT)
        pygame.draw.rect(self.screen, palette["ui"], placeholder_rect)
        pygame.draw.rect(self.screen, WHITE, placeholder_rect, 2)  # White border.