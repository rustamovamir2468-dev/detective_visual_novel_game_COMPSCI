# game.py - File that opens window and runs the game loop.
# Author(s): 5752530
# ====================================================
# This is the main file that runs the game.
# Opens the window, runs the loop, and coordinates between the different systems.
# ====================================================

from pydoc import text

import pygame
import sys # Only needed for sys,exit() to close the game when the player clicks the X button on the window.
from settings                import * # Import all the constants from settings.py.
from core.game_state         import GameStateManager, State
from core.player_profile     import PlayerProfile
from core.save_system        import CheckpointManager
from core.scene_manager      import SceneManager
from systems.dialogue_system import DialogueSystem
from systems.story_tree      import NodeType, StoryTree
from ui.pause_menu           import PauseMenu
from ui.main_menu            import MainMenu
from ui.name_input           import NameInput
from ui.title_card           import TitleCard
from ui.scene_display        import SceneDisplay
from ui.dialogue_box         import DialogueBox
from ui.choice_menu          import ChoiceMenu
from ui.game_over            import GameOver
from systems.story_builder   import build_story

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
        self.story_tree    = build_story() # Call the function to construct the story tree from story_builder.py.
        self.scene_manager = None # Created in start_game() after the player enters their name.

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
        self.pending_ending_type = "bad"

        self.running = True

    def start_game(self):# Called once the player has confirmed their name.
        # Creates the SceneManager, wires everything together, and kicks off Act 1.
        self.scene_manager = SceneManager(story_tree = self.story_tree, checkpoint_manager = self.checkpoint_manager, player_profile = self.player_profile)
        self.scene_manager.start() # Start the scene manager, which will set the current node to the first node in the story tree and do any necessary setup for that node.
        first_node = self.scene_manager.get_current_node()
        if first_node:
            self.dialogue_system.load_line(first_node.text)
            self.scene_display.load_background(first_node.bg if hasattr(first_node, 'bg') else None)
            self.scene_display.load_portrait(first_node.portrait[0] if first_node.portrait else None, first_node.portrait[1] if first_node.portrait else None)
        self.title_card.load(f"Act {ACT_1}", "A Normal Day")
        self.gsm.change_state(State.TITLE_CARD)
        text = first_node.text.replace("[PLAYER]", self.player_profile.get_name())
        self.dialogue_system.load_line(text)


    

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

            elif self.gsm.is_state(State.TITLE_CARD):
                if (
                    (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1)
                    or 
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) # Allow spacebar to progress through the title card - 5744357
                    or
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) # Allow return button to progress through the title card - 5744357
                ):
                    self.gsm.change_state(State.DIALOGUE)
                    node = self.scene_manager.get_current_node()
                    if node:
                        self.dialogue_system.load_line(node.text)

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

    def _handle_dialogue_event(self, event):
        is_left_click = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
        is_spacebar = event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE # Allow spacebar to progress through the dialogues - 5744357
        is_enter = event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN # Allow return button to progress through the dialogues - 5744357

        if not (is_left_click or is_spacebar or is_enter):
            return

        node = self.scene_manager.get_current_node() if self.scene_manager else None
        if node is None:
                return

        if node.is_choice_node():
            result = self.choice_menu.handle_event(event, node.choices, self.palette)
            if result is not None:
                self.scene_manager.select_choice(result)
                self._on_node_changed()  # Check for act change after a choice too
        else:
            if self.dialogue_system.is_finished():
                prev_node = self.scene_manager.get_current_node()  # Remember before
                prev_act = prev_node.act
                self.scene_manager.advance()
                next_node = self.scene_manager.get_current_node()  # Check after

                if next_node is None or next_node is prev_node:
                    self.game_over.load(
                        ending_text = prev_node.text,
                        can_rewind = (self.checkpoint_manager.has_checkpoint() and self.pending_ending_type == "bad"),
                        ending_type = self.pending_ending_type
                    )
                    self.gsm.change_state(State.GAME_OVER)
                else:
                    self._on_node_changed(prev_act)
            else:
                self.dialogue_system.skip()

    def _on_node_changed(self, prev_act=None):
        next_node = self.scene_manager.get_current_node()
        if next_node is None:
            return
        
        nid = next_node.node_id
        print("NODE:", repr(nid), "| pending_ending_type:", self.pending_ending_type)
        
        # Track ending type as we pass through ending nodes
        nid = next_node.node_id
        if nid == ENDING_TRUE_FINAL:
            self.pending_ending_type = "good"
        elif nid in ("ending_sacrifice_self", "ending_sacrifice_self_narration"):
            self.pending_ending_type = "sacrifice_you"
        elif nid in ("ending_sacrifice_hannah", "ending_sacrifice_hannah_narration"):
            self.pending_ending_type = "sacrifice_hannah"
        elif nid.startswith("ending_bad"):
            self.pending_ending_type = "bad"

        # Load the new portrait and background for this node
        self.scene_display.load_background(
            next_node.bg if hasattr(next_node, 'bg') else None
        )
        self.scene_display.load_portrait(
            next_node.portrait[0] if next_node.portrait else None,
            next_node.portrait[1] if next_node.portrait else None
        )

        # If the act number changed, show the title card for the new act
        if prev_act is not None and next_node.act != prev_act:
            if next_node.act in ACT_TITLES:
                self.title_card.load(f"Act {next_node.act}", ACT_TITLES[next_node.act])
                self.gsm.change_state(State.TITLE_CARD)
                # Palette swap: Acts 1-2 warm, Acts 3-4 cold
                if next_node.act in (ACT_3, ACT_4):
                    self.palette = PALETTE_COLD
                else:
                    self.palette = PALETTE_WARM

        # Replace [PLAYER] in the text before loading it
        text = next_node.text.replace("[PLAYER]", self.player_profile.get_name())
        self.dialogue_system.load_line(text)  # ← use substituted text, not next_node.text directly

    def _rewind_to_checkpoint(self):
        if self.scene_manager is None:
            return
        
        self.pending_ending_type = "bad"

        self.scene_manager.rewind_to_checkpoint()
        node = self.scene_manager.get_current_node()
        if node:
            pass
        self.gsm.change_state(State.DIALOGUE)

        text = node.text.replace("[PLAYER]", self.player_profile.get_name())
        self.dialogue_system.load_line(text)

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
                if speaker == "[PLAYER]" or speaker == "player":           
                    speaker = self.player_profile.get_name()

                if speaker == "narrator" or speaker == "none":
                    speaker = None
                is_narration = (node.node_type == NodeType.NARRATION or(node.node_type == NodeType.DIALOGUE and node.speaker == "narrator")) if node else False
                self.dialogue_box.draw(self.dialogue_system, speaker, self.palette, italic=is_narration)

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