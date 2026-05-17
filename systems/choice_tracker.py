# choice_tracker.py - File that remembers every choice the player made.
# Author(s): 5752530
# ====================================================
# Keeps a record of all choices made by the player.
# Used by the story tree to check if a node is accessible based on what the player has or hasn't done.
# ====================================================

class ChoiceTracker:

    def __init__(self):
        self.choices_made = [] # This will be a list of strings, where each string is the unique ID of a choice the player made.

    def record(self, choice_key): # Records a choice. Only adds it if it isn't already in the list.
        if choice_key and choice_key not in self.choices_made:
            self.choices_made.append(choice_key)

    def has_made(self, choice_key): # Returns True if the player has already made this choice, False if not.
        return choice_key in self.choices_made

    def has_made_all(self, choice_keys): # Used by required_choices on story nodes.
        return all(self.has_made(key) for key in choice_keys) #  Returns True only if the player has made EVERY choice in the given list. 
    
    def get_all(self): # Returns a copy of the full list. Used by the checkpoint snapshot.
        return list(self.choices_made)
    
    def restore(self, choices_list): # Replaces the current list with a previously saved one.
        self.choices_made = list(choices_list)  # Called by the checkpoint manager when rewinding.

    def reset(self): # Wipes everyhting. Call this on a fresh start.
        self.choices_made = []