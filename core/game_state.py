# core/game_state.py
# =============================================================
# LOGIC TEAM: The Game State Manager (FSM).
# This controls EVERY screen transition in the game.
# Nothing changes state without going through this class.
# Authors: 5752530
# =============================================================

import enum

class State(enum.Enum):
    """All possible game states."""
    MAIN_MENU = "main_menu"
    PLAYING   = "playing"
    DIALOGUE  = "dialogue"
    CUTSCENE  = "cutscene"
    PAUSED    = "paused"
    BULLETIN_BOARD = "bulletin_board"
    DEDUCTION  = "deduction"
    GAME_OVER  = "game_over"

class GameStateManager:
    """Controls which state the game is currently in, and handles transitions."""

    def __init__(self):
        self.current_state = State.MAIN_MENU
        self.previous_state = None

    def change_state(self, new_state: State):
        """Switch to a new state, remembering the previous one."""
        if not isinstance(new_state, State):
            raise ValueError(f"Invalid state: {new_state}")
        self.previous_state = self.current_state
        self.current_state = new_state
        print(f"State changed {self.previous_state.value} -> {self.current_state.value}")

    def revert(self):
        """Go back to the previous state (unpausing/closing bulletin baord, etc.)"""
        if self.previous_state is not None:
            self.current_state, self.previous_state = self.previous_state, self.current_state

    def is_state(self, state: State) -> bool:
        """Check if we're currently in a specific state."""
        return self.current_state == state
    
# core/game_state.py is done using a Finite State Machine. 
# Every system in the game will import State and GameStateManager from this file. 
# If you ever need to add a new screen or state (for example a CREDITS screen), add it to the State enum here — don't create your own state tracking anywhere else.