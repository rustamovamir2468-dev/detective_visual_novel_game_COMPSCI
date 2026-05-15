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
        self.font_text   = pygame.font.SysFont("Arial", FONT_SIZE_SMALL)   # Font for the dialogue text.
        self.font_arrow  = pygame.font.SysFont("Arial", FONT_SIZE_MEDIUM)  # Font for the continue arrow.
        self.font_text_italic = pygame.font.SysFont("Arial", FONT_SIZE_SMALL, italic=True)  # Italic font for narration.

        # --- The main dialogue box rectangle ---
        self.box_rect = pygame.Rect(0, DIALOGUE_BOX_Y, SCREEN_WIDTH, DIALOGUE_BOX_HEIGHT)

        # --- Name tag rectangle, sits just above the dialogue box ---
        self.name_rect = pygame.Rect(DIALOGUE_BOX_PADDING, DIALOGUE_BOX_Y - 36, 130, 32)

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

        self._draw_text(dialogue_system.get_displayed_text(), palette, speaker_name)

        if dialogue_system.is_finished(): # Only show the arrow when typing is done.
            self._draw_arrow(palette)

    def _draw_box(self, palette):  # Draws the main dialogue box background.
        pygame.draw.rect(self.screen, palette["dialogue_bg"], self.box_rect)
        pygame.draw.rect(self.screen, palette["ui"], self.box_rect, 2)  # 2px border.

    def _draw_name_tag(self, speaker_name, palette): # Draws a small box above the dialogue box with the speaker's name.
        name_surface = self.font_name.render(speaker_name.title(), True, WHITE)
        self.name_rect.width = name_surface.get_width() + 16  # Dynamic width to fit name.
        pygame.draw.rect(self.screen, palette["ui"], self.name_rect)
        x = self.name_rect.centerx - name_surface.get_width() // 2   # Centred horizontally
        y = self.name_rect.centery - name_surface.get_height() // 2  # Centred vertically
        self.screen.blit(name_surface, (x, y))

    def _draw_text(self, text, palette, speaker_name=None): # Draws the dialogue text inside the box, with word wrapping.
        font    = self.font_text if speaker_name else self.font_text_italic  # Italic for narration, regular for dialogue.
        words   = text.split(" ") # Chops full sentences into words to handle wrapping.
        lines   = []
        current = ""

    # Narration uses the full box width; dialogue leaves space for the portrait on the left.
        if speaker_name:
            max_width = SCREEN_WIDTH - (DIALOGUE_BOX_PADDING * 2) - PORTRAIT_WIDTH + 200
        else:
            max_width = SCREEN_WIDTH - (DIALOGUE_BOX_PADDING * 4)  # Full width minus generous padding for narration.

        for word in words:
            test_line = current + word + " "
            if font.size(test_line)[0] <= max_width:
                current = test_line
            else:
                lines.append(current)  # This line is full, start a new one.
                current = word + " "
        lines.append(current)  # Add the last remaining line.

        total_text_height = len(lines) * (FONT_SIZE_SMALL + 6)  # Total height of all lines combined.

        for i, line in enumerate(lines): # Enumerate gives us index and line for each line of text, so we can draw them with the correct vertical spacing.
            text_surface = font.render(line, True, palette["text"])
            if speaker_name:
                # Dialogue: left-aligned with portrait offset, starts near the top of the box.
                x = PORTRAIT_WIDTH + DIALOGUE_BOX_PADDING - 200
                y = DIALOGUE_BOX_Y + DIALOGUE_BOX_PADDING + (i * (FONT_SIZE_SMALL + 6))
            else:
                # Narration: each line centred horizontally, all lines centred vertically in the box.
                x = (SCREEN_WIDTH - text_surface.get_width()) // 2
                y = DIALOGUE_BOX_Y + (DIALOGUE_BOX_HEIGHT - total_text_height) // 2 + (i * (FONT_SIZE_SMALL + 6))
            self.screen.blit(text_surface, (x, y))

    def _draw_arrow(self, palette): # Draws a blinking "▼" arrow in the bottom right to signal the player can continue.
        if self.arrow_visible:
            arrow_surface = self.font_arrow.render("▼", True, palette["accent"])
            self.screen.blit(arrow_surface, (SCREEN_WIDTH - DIALOGUE_BOX_PADDING - arrow_surface.get_width(), DIALOGUE_BOX_Y + DIALOGUE_BOX_HEIGHT - DIALOGUE_BOX_PADDING - arrow_surface.get_height()))

    
            