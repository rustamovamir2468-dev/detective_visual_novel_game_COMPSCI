# game.py - File that opens window and runs the game loop.
# Author(s): 5752530
# ====================================================
# This is the main file that runs the game.
# Opens the window, runs the loop, and coordinates between the different systems.
# ====================================================

import pygame
import sys # Only needed for sys,exit() to close the game when the player clicks the X button on the window.
from settings                import * # Import all the constants from settings.py.
from core.game_state         import GameStateManager, State
from core.player_profile     import PlayerProfile
from core.save_system        import CheckpointManager
from core.scene_manager      import SceneManager
from systems.dialogue_system import DialogueSystem
from systems.story_tree      import StoryTree
from ui.pause_menu           import PauseMenu
from ui.main_menu            import MainMenu
from ui.name_input           import NameInput
from ui.title_card           import TitleCard
from ui.scene_display        import SceneDisplay
from ui.dialogue_box         import DialogueBox
from ui.choice_menu          import ChoiceMenu
from ui.game_over            import GameOver
from systems.story_builder   import build_story
from scenes.act1             import build_act1

# --- The main game class ---
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock  = pygame.time.Clock()

        # --- Core systems ---
        self.gsm                = GameStateManager()
        self.player_profile     = PlayerProfile()
        self.checkpoint_manager = CheckpointManager()
        self.palette            = PALETTE_WARM # Active palette, swap to PALETTE_COLD when needed.

        # --- Story ---
        self.story_tree    = StoryTree() # Populated by story_builder once that file is written.
        self.scene_manager = None # Created in start_game() after the player enters their name.
        self.story_tree    = build_story() # Call the function to construct the story tree from story_builder.py.

        # --- UI ---
        self.scene_display   = SceneDisplay(self.screen)
        self.dialogue_system = DialogueSystem()
        self.dialogue_box    = DialogueBox(self.screen)
        self.choice_menu     = ChoiceMenu(self.screen)
        self.pause_menu      = PauseMenu(self.screen)
        self.main_menu       = MainMenu(self.screen)
        self.name_input      = NameInput(self.screen)
        self.title_card      = TitleCard(self.screen)
        self.game_over       = GameOver(self.screen)

        self.running = True

    def start_game(self):# Called once the player has confirmed their name.
        # Creates the SceneManager, wires everything together, and kicks off Act 1.
        self.scene_manager = SceneManager(story_tree = build_act1(), checkpoint_manager = self.checkpoint_manager, player_profile = self.player_profile)
        self.scene_manager.start() # Start the scene manager, which will set the current node to the first node in the story tree and do any necessary setup for that node.
        self.title_card.load(ACT_1, "A Normal Day")
        self.gsm.change_state(State.TITLE_CARD)

    

    def run(self):
        while self.running:
            self.handle_events() # Checks for player input and other events.
            self.update() # Updates the game state
            self.draw() # Draws the current state of the game to the screen.
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get(): # Returns list of all events that happened since last frame
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            # --- Escape key: pause / unpause ---
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.gsm.is_state(State.PAUSED):
                    self.gsm.revert()
                elif not self.gsm.is_state(State.MAIN_MENU) and not self.gsm.is_state(State.NAME_INPUT):
                    self.gsm.change_state(State.PAUSED)

            # --- Route events to the active UI ---
            if self.gsm.is_state(State.MAIN_MENU):
                self.main_menu.handle_event(event, self.gsm)

            elif self.gsm.is_state(State.NAME_INPUT):
                result = self.name_input.handle_event(event, self.gsm)
                if result == "confirmed": # Player pressed Enter with a valid name.
                    self.player_profile.set_name(self.name_input.get_name())
                    self.start_game()

            elif self.gsm.is_state(State.DIALOGUE):
                self._handle_dialogue_event(event)

            elif self.gsm.is_state(State.PAUSED):
                self.pause_menu.handle_event(event, self.gsm)

            elif self.gsm.is_state(State.GAME_OVER):
                result = self.game_over.handle_event(event)
                if result == "rewind":
                    self._rewind_to_checkpoint()
                elif result == "quit":
                    pygame.quit()
                    sys.exit()

    def update(self): # REPLACE EACH PASS WITH THE APPROPRIATE FUNCTION CALLS TO UPDATE THE GAME STATE.
        if self.gsm.is_state(State.DIALOGUE):
            self.dialogue_system.update()
            self.dialogue_box.update()
        elif self.gsm.is_state(State.TITLE_CARD):
            self.title_card.update(self.gsm)
        elif self.gsm.is_state(State.NAME_INPUT):
            self.name_input.update()

    def draw(self): # DRAW THE APPROPRIATE THINGS FOR EACH STATE, FOR NOW JUST PLACEHOLDERS.
        self.screen.fill(BLACK) # Clear the screen with a black background before drawing anything.

        if self.gsm.is_state(State.MAIN_MENU):
            self.main_menu.draw(self.palette)

        elif self.gsm.is_state(State.NAME_INPUT):
            self.name_input.draw(self.palette)

        elif self.gsm.is_state(State.SCENE):
            self.scene_display.draw(self.palette)

        elif self.gsm.is_state(State.DIALOGUE):
            self.scene_display.draw(self.palette)
            node = self.scene_manager.get_current_node() if self.scene_manager else None
            if node and node.is_choice_node():
                self.choice_menu.draw(node.choices, self.palette)
            else:
                speaker = node.speaker if node else None
                self.dialogue_box.draw(self.dialogue_system, speaker, self.palette)

        elif self.gsm.is_state(State.PAUSED):
            self.pause_menu.draw(self.palette)

        elif self.gsm.is_state(State.GAME_OVER):
            self.game_over.draw(self.palette)

        elif self.gsm.is_state(State.TITLE_CARD):
            self.title_card.draw(self.palette)

        elif self.gsm.is_state(State.CUTSCENE):
            self._draw_placeholder("CUTSCENE")

        pygame.display.flip() # Update the full screen with this frame, because we are using double buffering (the default in Pygame).

    def _draw_placeholder(self, label: str):
        font    = pygame.font.SysFont("Arial", FONT_SIZE_LARGE)
        surface = font.render(label, True, WHITE) # True for anti-aliasing, WHITE for colour.
        x = (SCREEN_WIDTH  - surface.get_width())  // 2
        y = (SCREEN_HEIGHT - surface.get_height()) // 2
        self.screen.blit(surface, (x, y)) # Blit means to draw the surface onto the screen at the specified coordinates.

# --- Start the game when this file is run directly ---
if __name__ == "__main__":
    game = Game()
    game.run()