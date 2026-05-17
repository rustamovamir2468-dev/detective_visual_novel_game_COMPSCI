# scene_manager.py - File that loads the right scene and background
# Author(s): 5752530
# ====================================================
# Sits between game.py and the story tree.
# Loads nodes one at a time, advances the story forward, handles choices, and triggers checkpoints before choice nodes.
# ====================================================
import random

from systems.choice_tracker import ChoiceTracker

class SceneManager:
    def __init__(self, story_tree, checkpoint_manager, player_profile):
        self.tree             = story_tree          # The full story tree.
        self.checkpoint       = checkpoint_manager  # For saving snapshots before choices.
        self.player_profile   = player_profile      # For reading the player's name.
        self.choice_tracker   = ChoiceTracker()     # Tracks every choice made this run.
        self.current_node     = None                # The node currently being shown.
        self.current_ending   = None                # Set when a bad/good ending is reached.

    def start(self): # Loads the very first node in the story. Call this once when the game begins.
        first_node = self.tree.get_node(self.tree.root_id)
        self._load_node(first_node)

    def advance(self): # Moves to the next node. Call this when the player clicks to continue dialogue.
        if self.current_node is None: # Does nothing if the current node is a choice node — use select_choice() instead.
            return
        
        if self.current_node.is_choice_node():
            return # Wait for the player to pick an option.
        
        next_node = self.tree.get_node(self.current_node.next_node_id)

        # --- Requires_flag check ---
        if next_node is not None and getattr(next_node, 'requires_flag', None):
            if not self.choice_tracker.has_made(next_node.requires_flag):
                next_node = self.tree.get_node("ending_bad_no_mom_help")

        self._load_node(next_node)

    def select_choice(self, choice_index): # Called when the player picks one of the choice options.
        if self.current_node is None or not self.current_node.is_choice_node(): #  choice_index is the position of the option in the choices list (0, 1, 2...).
            return
        
        if choice_index < 0 or choice_index >= len(self.current_node.choices):
            return # Invalid choice index, do nothing.
        
        chosen = self.current_node.choices[choice_index]

        if chosen.choice_to_record:
            self.choice_tracker.record(chosen.choice_to_record)

        next_node = self.tree.get_node(chosen.next_node_id)

        if next_node and next_node.required_choices:
            for required in next_node.required_choices:
                if not self.choice_tracker.has_made(required):
                    return  # Player hasn't met the requirements, block silently.

        self._load_node(next_node) 

    def _load_node(self, node): # Internal method. Loads a node and handles any special logic for it.
        if node is None:
            return
        
        if node.is_choice_node(): # Before loading a choice node, save a checkpoint so the player can rewind.
            random.shuffle(node.choices)
            self.checkpoint.save_checkpoint(current_node_id = node.node_id, choices_made = self.choice_tracker.get_all(), player_name = self.player_profile.get_name())

        self.current_node = node

    def rewind_to_checkpoint(self): # Called when the player hits a bad ending and chooses to try again.
        if not self.checkpoint.has_checkpoint(): # Restores the game to the last choice node.
            return
        
        snapshot = self.checkpoint.load_checkpoint()

        self.choice_tracker.restore(snapshot["choices_made"]) # Overwrite the current choice record with the one from the checkpoint, so the story tree will know which nodes are accessible based on past choices.
        self.current_node = self.tree.get_node(snapshot["current_node_id"])
        self.current_ending = None  # Clear the ending flag.

    def get_current_node(self): # Returns the node currently being shown.
        return self.current_node