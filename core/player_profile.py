# player_profile.py - File that stores the player's chosen name.
# Author(s): 5752530
# ====================================================
# Stores the player's chosen name.
# ====================================================

class PlayerProfile:

    def __init__(self):
        self.name = "???" # Default name before the player sets it.

    def set_name(self, name):
        if name.strip(): # Only set it if the player actually typed something.
            self.name = name.strip()

    def get_name(self):
        return self.name