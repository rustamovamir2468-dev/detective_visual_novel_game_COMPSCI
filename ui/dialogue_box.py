# dialogue_box.py - File that draws the dialogue box on the screen
# Author(s): 5752530
# ====================================================
# Responsible for drawing the dialogue box, the speaker's name tag, the typewriter text, and the continue arrow.
# Reads directly from DialogueSystem to get the current text.
# ====================================================

import pygame
from settings import *

class DialogueBox:
    def __init__(self, screen):
        self.screen      = screen
        self.font_name   = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)  # Font for the speaker name.
        self.font_text   = pygame.font.SysFont("Arial", FONT_SIZE_SMALL)
        self.font_text_italic = pygame.font.SysFont("Arial", FONT_SIZE_SMALL, italic=True)   # Font for the dialogue text.
        self.font_arrow  = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)  # Font for the continue arrow.

        # The main dialogue box rectangle - adjust box width and prepare it to be centered in the bottom part of the screen
        self.box_width = 760
        self.box_x = (SCREEN_WIDTH - self.box_width) // 2

        self.box_rect = pygame.Rect(
            self.box_x,
            DIALOGUE_BOX_Y,
            self.box_width,
            DIALOGUE_BOX_HEIGHT
        )

        # --- Name tag rectangle, sits just above the dialogue box ---
        self.name_rect = pygame.Rect(DIALOGUE_BOX_PADDING, DIALOGUE_BOX_Y - 36, 200, 32)

        # --- Arrow blinking variables ---
        self.arrow_visible  = True # Controls blinking of the continue arrow.
        self.arrow_timer    = 0 # Counts frames for the blink.
        self.arrow_interval = 30 # Blink every 30 frames (half a second at 60 FPS).

    def update(self): # Called once per frame. Handles the blinking continue arrow.
        self.arrow_timer += 1
        if self.arrow_timer >= self.arrow_interval:
            self.arrow_timer   = 0
            self.arrow_visible = not self.arrow_visible  # Toggle visibility.

    def draw(self, dialogue_system, speaker_name, palette): # Draws the full dialogue box for the current frame.
    # dialogue_system — the DialogueSystem object with the current text.
    # speaker_name    — the character's display name, or None for narration.
    # palette         — either PALETTE_WARM or PALETTE_COLD from settings.

        self._draw_box(palette)

        if speaker_name: # Only draw the name tag if there is a speaker.
            self._draw_name_tag(speaker_name, palette)
            
        is_narration = speaker_name is None # Add a special occasion where a node doesn't have a speaker - 5744357


        # self._draw_text should be outside of the if loop - text must be shown even if there's no "speaker" in the node - 5744357

        self._draw_text(
            dialogue_system.get_displayed_text(),
            palette,
            narration=is_narration
        ) 

        if dialogue_system.is_finished(): # Only show the arrow when typing is done.
            self._draw_arrow(palette)

    def _draw_box(self, palette):  # Draws the main dialogue box background.
        pygame.draw.rect(self.screen, palette["dialogue_bg"], self.box_rect)
        pygame.draw.rect(self.screen, palette["ui"], self.box_rect, 2)  # 2px border.

    def _draw_name_tag(self, speaker_name, palette): # Draws a small box above the dialogue box with the speaker's name.
        pygame.draw.rect(self.screen, palette["ui"], self.name_rect)

        display_name = speaker_name.capitalize()
        name_surface = self.font_name.render(display_name, True, WHITE)

        text_rect = name_surface.get_rect(
            center=self.name_rect.center
        )

        self.screen.blit(name_surface, text_rect)

    def _draw_text(self, text, palette, narration=False): # Draws the dialogue text inside the box, with word wrapping, added narration=False case - 5744357
        font = self.font_text_italic if narration else self.font_text # Font type for specific text types - different for narrator - 5744357

        words   = text.split(" ") # Chops full sentences into words to handle wrapping.
        lines   = []
        current = ""

        max_width = self.box_rect.width - (DIALOGUE_BOX_PADDING * 2)

        for word in words:
            test_line = current + word + " "
            if font.size(test_line)[0] <= max_width:
                current = test_line
            else:
                lines.append(current)  # This line is full, start a new one.
                current = word + " "
        lines.append(current)  # Add the last remaining line.

        for i, line in enumerate(lines): # Enumerate gives us index and line for each line of text, so we can draw them with the correct vertical spacing.
            text_surface = font.render(line, True, palette["text"])

            # Make the text of inside the dialogue box start from the leftmost point of the box - 5744357
            self.screen.blit(
                text_surface,
                (self.box_rect.x + DIALOGUE_BOX_PADDING,
                self.box_rect.y + DIALOGUE_BOX_PADDING + (i * (FONT_SIZE_SMALL + 6)))
            )

    def _draw_arrow(self, palette): # Draws a blinking "▼" arrow in the bottom right to signal the player can continue.
        if self.arrow_visible:
            arrow_surface = self.font_arrow.render("▼", True, palette["accent"])

            # Arrow position - updated so that it matches where the box is - 5744357
            self.screen.blit(
                arrow_surface,
                (
                    self.box_rect.right - DIALOGUE_BOX_PADDING - arrow_surface.get_width(),
                    self.box_rect.bottom - DIALOGUE_BOX_PADDING - arrow_surface.get_height()
                )
            )

    
            