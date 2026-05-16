# player_profile.py - File that stores the player's chosen name.
# Author(s): 5752530
# ====================================================
# Stores the player's chosen name.
# ====================================================

class PlayerProfile:

    def __init__(self):
        self.name = "Player" # Default until the player sets it
        self.gender = "male" # Default until the player sets it
        self.flags = set() # All recorded choices live here

    def set_name(self, name):
        self.name = name.strip() if name.strip() else "Player"

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def get_name(self):
        return self.name

    def record_flag(self, flag): # Call this when a choice is made
        if flag:
            self.flags.add(flag)

    def has_flag(self, flag): # Call this to check a past choice
        return flag in self.flags

    def reset(self): # Call this on new game
        self.flags = set()
        self.name = "Player"
        self.gender = "male"