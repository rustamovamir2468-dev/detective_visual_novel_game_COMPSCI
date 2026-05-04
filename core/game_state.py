# game_state.py - File that controls which screen the game is on.
# Author(s): 5752530
# ====================================================
# Controls which screen the game is currently on.
# Nothing in the game changes screen without going through this file.
# ====================================================

import enum # Creates a set of named constants for safer(fails loudly, raising ValueError or AttriuteError), readable code.

# --- All possible screens the game can be on ---
class State(enum.Enum):
    MAIN_MENU      = "main_menu"
    SCENE          = "scene"
    DIALOGUE       = "dialogue"
    CUTSCENE       = "cutscene"
    PAUSED         = "paused"
    BULLETIN_BOARD = "bulletin_board"
    DEDUCTION      = "deduction"
    TITLE_CARD     = "title_card"
    GAME_OVER      = "game_over"

# --- Controls switching between states ---
class GameStateManager:
    def __init__(self):
        self.current_state  = State.MAIN_MENU
        self.previous_state = None
    
    def change_state(self, new_state: State): # : State is a label saying it should be a State enum value.
        self.previous_state = self.current_state
        self.current_state  = new_state
        print(f"[State] {self.previous_state.value} --> {self.current_state.value}") # FOR DEBUGGING PURPOSES, REMOVE LATER.

    def revert(self):
        if self.previous_state is not None:
            self.current_state, self.previous_state = self.previous_state, self.current_state

    def is_state(self, state: State) -> bool: # Asks if the current state is the one specified, returns True or False.
        return self.current_state == state