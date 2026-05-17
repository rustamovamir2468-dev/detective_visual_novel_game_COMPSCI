# save_system.py - File that manages the checkpoint rewind system.
# Author(s): 5752530
# ====================================================
# Stores a single in-memory snapshot of the game state just before every choice node. 
# If the player hits a bad ending, they can rewind to that snapshot and try the choice again.
# ====================================================

class CheckpointManager:

    def __init__(self):
        self.snapshot = None # This will hold the snapshot of the game state. None if there is no checkpoint yet.

    def save_checkpoint(self, current_node_id, choices_made, player_name): # Called automatically just before every choice node is shown.
        self.snapshot = {
            "current_node_id": current_node_id,
            "choices_made"   : list(choices_made),  # Copy the list so future changes don't affect the snapshot.
            "player_name"    : player_name
        }

    def has_checkpoint(self): # Check if there is a checkpoint available to rewind to.
        return self.snapshot is not None
    
    def load_checkpoint(self): # Returns the snapshot data to rewind to, or None if there is no checkpoint.
        return self.snapshot
    
    def clear(self): # Whipes the snapshot. Call this when player reaches a good ending.
        self.snapshot = None
        