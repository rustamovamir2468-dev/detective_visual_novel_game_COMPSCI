# dialogue_system.py - File that controls the typewriter and text progression.
# Author(s): 5752530
# ====================================================
# Handles the typewriter effect for dialogue lines.
# Tracks whether the current line has finished typing.
# Allows the player to skip to the end by clicking again.
# ====================================================

class DialogueSystem:

    def __init__(self, text_speed=2):
        self.full_text      = ""    # The complete line of text to display.
        self.displayed_text = ""    # The portion revealed so far.
        self.char_index     = 0     # Which character we are currently up to.
        self.text_speed     = text_speed  # How many frames to wait before showing the next character.
        self.frame_counter  = 0     # Counts frames since the last character was added.
        self.finished       = False # True when the full line has been revealed.

    def load_line(self, text): # Loads a new line of dialogue and resets everything ready to type it out.
        self.full_text      = text
        self.displayed_text = ""
        self.char_index     = 0
        self.frame_counter  = 0
        self.finished       = False

    def update(self): # Called once per frame. Adds the next character if enough frames have passed.
        if self.finished:
            return  # Nothing left to do.

        self.frame_counter += 1

        if self.frame_counter >= self.text_speed:
            self.frame_counter = 0  # Reset the counter.

            if self.char_index < len(self.full_text):
                self.displayed_text += self.full_text[self.char_index]  # Reveal the next character.
                self.char_index += 1
            
            if self.char_index >= len(self.full_text):
                self.finished = True  # The whole line is now visible.

    def skip(self): # Instantly reveals the full line. Called when the player clicks during typing.
        self.displayed_text = self.full_text
        self.char_index     = len(self.full_text)
        self.finished       = True

    def is_finished(self): # Returns True if the full line has been revealed.
        return self.finished

    def get_displayed_text(self): # Returns the portion of the text revealed so far.
        return self.displayed_text