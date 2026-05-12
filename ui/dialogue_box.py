"""
Dialogue Box for Alias - A Narrative Story Game
Displays character dialogue and narration with a typewriter effect.
The player advances text by pressing SPACE, ENTER, or left-clicking.
"""

import pygame
import sys


# ---------------------------------------------------------------------------
# Helper: word-wrap a string into lines that fit inside a given pixel width
# ---------------------------------------------------------------------------

def wrap_text(text: str, font: pygame.font.Font, max_width: int) -> list:
    """
    Split a string into a list of lines that each fit within max_width pixels.

    Args:
        text (str): The full text to wrap.
        font (pygame.font.Font): Font used to measure text width.
        max_width (int): Maximum pixel width of a single line.

    Returns:
        list: List of strings, one per display line.
    """
    words: list = text.split(" ")   # Split sentence into individual words
    lines: list = []                # Final list of wrapped lines
    current_line: str = ""          # Line being built word by word

    for word in words:
        # Try adding the next word to the current line
        test_line: str = current_line + word + " "
        line_width, _ = font.size(test_line)   # Measure pixel width

        if line_width <= max_width:
            # Word fits — keep building this line
            current_line = test_line
        else:
            # Word doesn't fit — save current line and start a new one
            if current_line:
                lines.append(current_line.rstrip())
            current_line = word + " "

    # Don't forget the last line
    if current_line:
        lines.append(current_line.rstrip())

    return lines


# ---------------------------------------------------------------------------
# DialogueBox class
# ---------------------------------------------------------------------------

class DialogueBox:
    """
    A dialogue box overlay drawn at the bottom of the screen.

    Features:
        - Typewriter effect: characters appear one at a time.
        - Speaker name displayed in a tab above the dialogue box.
        - Pass None as speaker for narration (no name shown).
        - SPACE, ENTER, or left-click skips to full text on first press,
          then dismisses the box on second press.
        - A blinking indicator shows when text is fully displayed.

    Typical usage inside a scene's update/draw loop:
        dialogue = DialogueBox(screen, settings)
        dialogue.set_text("Maya", "Did you see what happened yesterday?")

        # Each frame:
        done = dialogue.update(events, dt)   # returns True when dismissed
        dialogue.draw()
    """

    # -----------------------------------------------------------------------
    # Colour palette — matches the dark crimson theme of the rest of the game
    # -----------------------------------------------------------------------
    COLOUR_BOX_BG: tuple     = (8, 2, 2)         # Dark box background
    COLOUR_BOX_BORDER: tuple = (90, 15, 15)       # Crimson border
    COLOUR_NAME_BG: tuple    = (20, 4, 4)         # Speaker name tab background
    COLOUR_NAME_TEXT: tuple  = (210, 60, 60)      # Speaker name (crimson)
    COLOUR_BODY_TEXT: tuple  = (210, 200, 200)    # Dialogue body text (off-white)
    COLOUR_NARRATOR: tuple   = (160, 140, 120)    # Narration text (warm grey)
    COLOUR_INDICATOR: tuple  = (180, 40, 40)      # Blinking indicator colour
    COLOUR_OVERLAY: tuple    = (0, 0, 0, 60)      # Subtle dark strip behind box

    # Typewriter speed: characters revealed per second
    CHARS_PER_SECOND: int = 40

    def __init__(self, screen: pygame.Surface, settings) -> None:
        """
        Initialise the dialogue box.

        Args:
            screen (pygame.Surface): The main game window surface.
            settings: Settings object with WIDTH and HEIGHT attributes.
        """
        self.screen = screen
        self.width: int  = settings.WIDTH
        self.height: int = settings.HEIGHT

        # ---- Box geometry --------------------------------------------------
        self.box_height: int = 180        # Height of the dialogue panel
        self.box_margin: int = 24         # Gap from screen edges
        self.box_x: int = self.box_margin
        self.box_y: int = self.height - self.box_height - self.box_margin
        self.box_w: int = self.width - self.box_margin * 2
        self.box_rect = pygame.Rect(
            self.box_x, self.box_y, self.box_w, self.box_height
        )

        # Text area inside the box (with padding so text doesn't touch edges)
        self.text_padding: int = 20
        self.text_x: int = self.box_x + self.text_padding
        self.text_y: int = self.box_y + self.text_padding + 30   # +30 for name tab
        self.text_w: int = self.box_w - self.text_padding * 2

        # ---- Fonts ---------------------------------------------------------
        try:
            self.font_name      = pygame.font.Font("assets/fonts/body.ttf", 18)
            self.font_body      = pygame.font.Font("assets/fonts/body.ttf", 20)
            self.font_indicator = pygame.font.Font("assets/fonts/body.ttf", 16)
        except (FileNotFoundError, OSError):
            # Graceful fallback to system fonts if custom fonts are missing
            self.font_name      = pygame.font.SysFont("Georgia", 18, bold=True)
            self.font_body      = pygame.font.SysFont("Georgia", 20)
            self.font_indicator = pygame.font.SysFont("Georgia", 16)

        # ---- Typewriter state ----------------------------------------------
        self.full_text: str      = ""     # The complete text for this dialogue line
        self.speaker: str | None = None   # Speaker name; None means narration
        self.wrapped_lines: list = []     # Text broken into display-width lines
        self.char_index: float   = 0.0   # How many characters have been revealed
        self.is_complete: bool   = False  # True once all characters are shown
        self.is_done: bool       = False  # True once player dismisses the box

        # ---- Blink timer for the advance indicator -------------------------
        self.blink_timer: float   = 0.0
        self.show_indicator: bool = True

        # ---- Pre-render the semi-transparent overlay strip -----------------
        # Created once here so we don't allocate a new Surface every frame
        self.overlay_surf = pygame.Surface(
            (self.box_w, self.box_height + self.box_margin),
            pygame.SRCALPHA,
        )
        self.overlay_surf.fill(self.COLOUR_OVERLAY)

    # -----------------------------------------------------------------------
    # Public API
    # -----------------------------------------------------------------------

    def set_text(self, speaker: str | None, text: str) -> None:
        """
        Load a new line of dialogue and reset the typewriter to the beginning.

        Call this whenever the story moves to a new piece of dialogue.

        Args:
            speaker (str | None): Character name shown above the box.
                                   Pass None for narrator-style text.
            text (str): The full string to display with typewriter effect.
        """
        self.speaker     = speaker
        self.full_text   = text
        self.char_index  = 0.0
        self.is_complete = False
        self.is_done     = False

        # Pre-calculate the word-wrapped lines from the full text
        # This is done once here, not every frame, for efficiency
        self.wrapped_lines = wrap_text(text, self.font_body, self.text_w)

    def update(self, events: list, dt: float) -> bool:
        """
        Advance the typewriter animation and handle player input.

        Call this once per frame inside the scene's update loop.

        Args:
            events (list): Pygame event list from pygame.event.get().
            dt (float): Delta time in seconds (from clock.tick() / 1000).

        Returns:
            bool: True when the player has dismissed the box and the scene
                  should advance to the next dialogue line or choice.
        """
        # --- Advance typewriter ---
        if not self.is_complete:
            total_chars: int = sum(len(line) for line in self.wrapped_lines)
            self.char_index += self.CHARS_PER_SECOND * dt
            if self.char_index >= total_chars:
                self.char_index  = float(total_chars)
                self.is_complete = True

        # --- Blink the indicator when all text is shown ---
        if self.is_complete:
            self.blink_timer += dt
            if self.blink_timer >= 0.5:    # Flip every half second
                self.blink_timer  = 0.0
                self.show_indicator = not self.show_indicator

        # --- Handle player input ---
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Both SPACE/ENTER key and left mouse click count as "advance"
            advance: bool = (
                (event.type == pygame.KEYDOWN
                 and event.key in (pygame.K_SPACE, pygame.K_RETURN))
                or
                (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1)
            )

            if advance:
                if not self.is_complete:
                    # First press while text is still typing:
                    # skip ahead and show everything immediately
                    self.char_index  = float(
                        sum(len(line) for line in self.wrapped_lines)
                    )
                    self.is_complete = True
                else:
                    # Second press after text is fully shown:
                    # dismiss the box so the scene can advance
                    self.is_done = True

        return self.is_done

    # -----------------------------------------------------------------------
    # Draw
    # -----------------------------------------------------------------------

    def draw(self) -> None:
        """
        Render the dialogue box onto the screen.

        Draws the background panel, optional speaker name tab, the
        typewriter-revealed text, and the blinking advance indicator.
        """
        if not self.full_text:
            return   # Nothing set yet — draw nothing

        # 1. Dark translucent strip behind the box for readability
        self.screen.blit(
            self.overlay_surf,
            (self.box_x, self.box_y - self.box_margin // 2),
        )

        # 2. Main box background
        pygame.draw.rect(
            self.screen, self.COLOUR_BOX_BG, self.box_rect, border_radius=8
        )
        # Main box border
        pygame.draw.rect(
            self.screen, self.COLOUR_BOX_BORDER, self.box_rect,
            width=1, border_radius=8
        )

        # 3. Speaker name tab (skipped for narration when speaker is None)
        if self.speaker is not None:
            self._draw_name_tab()

        # 4. Dialogue/narration text with typewriter reveal
        self._draw_body_text()

        # 5. Blinking indicator when text is fully displayed
        if self.is_complete and self.show_indicator:
            self._draw_indicator()

    # -----------------------------------------------------------------------
    # Private draw helpers
    # -----------------------------------------------------------------------

    def _draw_name_tab(self) -> None:
        """
        Draw a small coloured tab floating just above the dialogue box
        to show who is speaking.
        """
        name_surf = self.font_name.render(self.speaker, True, self.COLOUR_NAME_TEXT)
        name_w, name_h = name_surf.get_size()

        # Tab sized to fit the name with horizontal padding
        tab_pad: int = 12
        tab_rect = pygame.Rect(
            self.box_x,
            self.box_y - name_h - 8,      # Float just above the box
            name_w + tab_pad * 2,
            name_h + 6,
        )
        pygame.draw.rect(self.screen, self.COLOUR_NAME_BG, tab_rect, border_radius=4)
        pygame.draw.rect(
            self.screen, self.COLOUR_BOX_BORDER, tab_rect, width=1, border_radius=4
        )

        # Centre the name text inside the tab
        name_rect = name_surf.get_rect(center=tab_rect.center)
        self.screen.blit(name_surf, name_rect)

    def _draw_body_text(self) -> None:
        """
        Draw the currently-revealed portion of the wrapped dialogue text.

        Iterates over pre-wrapped lines, cutting each one to the number of
        characters that should be visible according to self.char_index.
        """
        # Narration uses a warmer grey; character speech uses off-white
        colour = (
            self.COLOUR_NARRATOR if self.speaker is None
            else self.COLOUR_BODY_TEXT
        )

        line_height: int    = self.font_body.get_linesize() + 2
        chars_left: float   = self.char_index   # Budget of chars to reveal

        for i, line in enumerate(self.wrapped_lines):
            if chars_left <= 0:
                break   # Typewriter cursor hasn't reached this line yet

            # Reveal only as many characters as the budget allows
            chars_to_show: int = min(int(chars_left), len(line))
            visible: str       = line[:chars_to_show]

            text_surf = self.font_body.render(visible, True, colour)
            y: int    = self.text_y + i * line_height
            self.screen.blit(text_surf, (self.text_x, y))

            # Deduct this line's characters from the budget
            chars_left -= len(line)

    def _draw_indicator(self) -> None:
        """
        Draw a blinking '▼ SPACE / CLICK' prompt in the bottom-right corner
        of the box to tell the player they can advance the dialogue.
        """
        ind_surf = self.font_indicator.render(
            "▼  SPACE / CLICK", True, self.COLOUR_INDICATOR
        )
        ind_rect = ind_surf.get_rect(
            bottomright=(
                self.box_x + self.box_w - 16,
                self.box_y + self.box_height - 10,
            )
        )
        self.screen.blit(ind_surf, ind_rect)
