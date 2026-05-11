"""
Pause Menu for Alias - A Narrative Story Game
Overlays a semi-transparent panel over the game scene when the player
presses ESC, offering options to resume, access settings, or quit.
"""

import pygame
import sys
import math


class PauseButton:
    """
    A button used inside the pause menu overlay.
    Slightly smaller and more compact than the main menu buttons.
    """

    def __init__(self, x: int, y: int, width: int, height: int, text: str):
        """
        Initialise a pause menu button.

        Args:
            x (int): X position (centre-aligned).
            y (int): Y position (centre-aligned).
            width (int): Button width in pixels.
            height (int): Button height in pixels.
            text (str): Label to display on the button.
        """
        self.rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        self.text: str = text
        self.hovered: bool = False

    def draw(self, surface: pygame.Surface, font: pygame.font.Font) -> None:
        """
        Render the button with hover state colouring.

        Args:
            surface (pygame.Surface): Target render surface.
            font (pygame.font.Font): Font for the button label.
        """
        if self.hovered:
            border_colour = (180, 30, 30)
            text_colour = (220, 60, 60)
            bg_colour = (35, 5, 5)
        else:
            border_colour = (80, 12, 12)
            text_colour = (160, 140, 140)
            bg_colour = (18, 3, 3)

        pygame.draw.rect(surface, bg_colour, self.rect, border_radius=4)
        pygame.draw.rect(surface, border_colour, self.rect, width=1, border_radius=4)

        label = font.render(self.text, True, text_colour)
        label_rect = label.get_rect(center=self.rect.center)
        surface.blit(label, label_rect)

    def check_hover(self, mouse_pos: tuple) -> bool:
        """
        Update hover state.

        Args:
            mouse_pos (tuple): Current (x, y) mouse position.

        Returns:
            bool: True if the mouse is over this button.
        """
        self.hovered = self.rect.collidepoint(mouse_pos)
        return self.hovered

    def is_clicked(self, event: pygame.event.Event) -> bool:
        """
        Check whether a left mouse click hit this button.

        Args:
            event (pygame.event.Event): The event to check.

        Returns:
            bool: True if this button was left-clicked.
        """
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


class PauseMenu:
    """
    Pause menu overlay for Alias.

    Rendered on top of the current game scene (which is captured as a
    screenshot surface so it remains visible beneath the overlay).

    Usage:
        # In your game loop, when ESC is pressed:
        pause = PauseMenu(screen, settings, background_snapshot)
        result = pause.run()   # Returns "resume", "settings", or "quit"
    """

    # Overlay colours
    COLOUR_OVERLAY: tuple = (0, 0, 0, 160)       # Semi-transparent black backdrop
    COLOUR_PANEL_BG: tuple = (10, 2, 2)           # Dark panel background
    COLOUR_PANEL_BORDER: tuple = (80, 12, 12)     # Dim crimson panel border
    COLOUR_TITLE: tuple = (180, 25, 25)           # "PAUSED" heading
    COLOUR_DIVIDER: tuple = (50, 8, 8)            # Thin separator line

    def __init__(
        self,
        screen: pygame.Surface,
        settings,
        background: pygame.Surface,
    ) -> None:
        """
        Initialise the pause menu.

        Args:
            screen (pygame.Surface): The main game window.
            settings: Settings object (needs WIDTH, HEIGHT, FPS).
            background (pygame.Surface): Snapshot of the game scene to
                display behind the overlay.
        """
        self.screen = screen
        self.settings = settings
        self.background = background
        self.width: int = settings.WIDTH
        self.height: int = settings.HEIGHT

        # Fonts
        try:
            self.font_heading = pygame.font.Font("assets/fonts/title.ttf", 48)
            self.font_button = pygame.font.Font("assets/fonts/body.ttf", 20)
            self.font_hint = pygame.font.Font("assets/fonts/body.ttf", 14)
        except (FileNotFoundError, OSError):
            self.font_heading = pygame.font.SysFont("Georgia", 48, bold=True)
            self.font_button = pygame.font.SysFont("Georgia", 20)
            self.font_hint = pygame.font.SysFont("Georgia", 14)

        # Panel dimensions — centred on screen
        self.panel_w: int = 320
        self.panel_h: int = 380
        self.panel_x: int = (self.width - self.panel_w) // 2
        self.panel_y: int = (self.height - self.panel_h) // 2
        self.panel_rect = pygame.Rect(self.panel_x, self.panel_y, self.panel_w, self.panel_h)

        # Button layout — vertically stacked inside the panel
        cx = self.width // 2
        btn_top = self.panel_y + 150   # First button Y offset from panel top
        spacing = 68                   # Vertical gap between buttons

        self.buttons: dict = {
            "resume":   PauseButton(cx, btn_top,              240, 44, "RESUME"),
            "settings": PauseButton(cx, btn_top + spacing,    240, 44, "SETTINGS"),
            "main_menu":PauseButton(cx, btn_top + spacing * 2, 240, 44, "MAIN MENU"),
            "quit":     PauseButton(cx, btn_top + spacing * 3, 240, 44, "QUIT GAME"),
        }

        # Pre-render semi-transparent overlay
        self.overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.overlay.fill(self.COLOUR_OVERLAY)

        # Animation timer for subtle heading pulse
        self.timer: float = 0.0

        # Result flag — set when the player chooses an option
        self.result: str | None = None

    # ------------------------------------------------------------------ #
    #  Draw helpers                                                        #
    # ------------------------------------------------------------------ #

    def _draw_panel(self) -> None:
        """Render the dark rounded panel that contains all UI elements."""
        # Panel background
        pygame.draw.rect(
            self.screen, self.COLOUR_PANEL_BG, self.panel_rect, border_radius=8
        )
        # Panel border
        pygame.draw.rect(
            self.screen, self.COLOUR_PANEL_BORDER, self.panel_rect,
            width=1, border_radius=8
        )

    def _draw_heading(self) -> None:
        """Render the 'PAUSED' title with a slow crimson pulse."""
        pulse = int(15 * math.sin(self.timer * 1.8))
        r = min(180 + pulse, 220)
        colour = (r, max(25 + pulse // 3, 0), max(25 + pulse // 3, 0))

        heading = self.font_heading.render("PAUSED", True, colour)
        heading_rect = heading.get_rect(
            center=(self.width // 2, self.panel_y + 60)
        )
        self.screen.blit(heading, heading_rect)

        # Thin divider line below heading
        div_y = self.panel_y + 100
        pygame.draw.line(
            self.screen, self.COLOUR_DIVIDER,
            (self.panel_x + 24, div_y),
            (self.panel_x + self.panel_w - 24, div_y),
            1,
        )

    def _draw_hint(self) -> None:
        """Render a keyboard shortcut hint at the bottom of the panel."""
        hint = self.font_hint.render("ESC — Resume", True, (60, 30, 30))
        hint_rect = hint.get_rect(
            center=(self.width // 2, self.panel_y + self.panel_h - 20)
        )
        self.screen.blit(hint, hint_rect)

    # ------------------------------------------------------------------ #
    #  Public interface                                                    #
    # ------------------------------------------------------------------ #

    def update(self) -> None:
        """Advance the animation timer."""
        self.timer += 0.02

    def draw(self) -> None:
        """Render the complete pause menu frame."""
        # 1. Blurred/dimmed game scene behind the overlay
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.overlay, (0, 0))

        # 2. Panel
        self._draw_panel()

        # 3. Heading
        self._draw_heading()

        # 4. Buttons
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.buttons.values():
            btn.check_hover(mouse_pos)
            btn.draw(self.screen, self.font_button)

        # 5. Hint
        self._draw_hint()

    def handle_events(self, events: list) -> None:
        """
        Handle keyboard and mouse input for the pause menu.

        Args:
            events (list): List of pygame events from the current frame.
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # ESC resumes the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.result = "resume"

            # Button clicks
            if self.buttons["resume"].is_clicked(event):
                self.result = "resume"

            elif self.buttons["settings"].is_clicked(event):
                self.result = "settings"

            elif self.buttons["main_menu"].is_clicked(event):
                self.result = "main_menu"

            elif self.buttons["quit"].is_clicked(event):
                pygame.quit()
                sys.exit()

    def run(self) -> str:
        """
        Block until the player selects a pause menu option.

        Returns:
            str: One of "resume", "settings", or "main_menu".
        """
        clock = pygame.time.Clock()
        fps = getattr(self.settings, "FPS", 60)

        while self.result is None:
            events = pygame.event.get()
            self.handle_events(events)
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(fps)

        return self.result
