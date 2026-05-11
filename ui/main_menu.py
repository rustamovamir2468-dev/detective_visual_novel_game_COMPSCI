"""
Main Menu for Alias - A Narrative Story Game
Displays the game title, animated background, and navigation buttons.
"""

import pygame
import sys
import math


class Button:
    """A clickable button with hover animation for the main menu."""

    def __init__(self, x: int, y: int, width: int, height: int, text: str):
        """
        Initialise a menu button.

        Args:
            x (int): X position (centre-aligned).
            y (int): Y position (centre-aligned).
            width (int): Button width in pixels.
            height (int): Button height in pixels.
            text (str): Label displayed on the button.
        """
        self.rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        self.text: str = text
        self.hovered: bool = False
        self.hover_offset: int = 0  # Pixel shift on hover for feedback

    def draw(self, surface: pygame.Surface, font: pygame.font.Font) -> None:
        """
        Render the button onto the given surface.

        Args:
            surface (pygame.Surface): Target render surface.
            font (pygame.font.Font): Font used for the button label.
        """
        # Colour shifts on hover
        if self.hovered:
            border_colour = (180, 30, 30)   # Bright crimson border
            text_colour = (220, 60, 60)      # Highlighted text
            bg_colour = (30, 5, 5)           # Slightly lighter background
        else:
            border_colour = (100, 15, 15)    # Dim crimson border
            text_colour = (180, 180, 180)    # Muted text
            bg_colour = (15, 0, 0)           # Dark background

        draw_rect = self.rect.move(0, self.hover_offset)

        # Draw button background
        pygame.draw.rect(surface, bg_colour, draw_rect, border_radius=4)
        # Draw border
        pygame.draw.rect(surface, border_colour, draw_rect, width=1, border_radius=4)

        # Render label centred on the button
        label = font.render(self.text, True, text_colour)
        label_rect = label.get_rect(center=draw_rect.center)
        surface.blit(label, label_rect)

    def check_hover(self, mouse_pos: tuple) -> bool:
        """
        Update hover state based on mouse position.

        Args:
            mouse_pos (tuple): Current (x, y) mouse position.

        Returns:
            bool: True if mouse is over the button.
        """
        self.hovered = self.rect.collidepoint(mouse_pos)
        return self.hovered

    def is_clicked(self, event: pygame.event.Event) -> bool:
        """
        Check whether this button was clicked.

        Args:
            event (pygame.event.Event): The mouse event to test.

        Returns:
            bool: True if a left-click landed on this button.
        """
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


class MainMenu:
    """
    Main menu scene for Alias.

    Displays an animated background, the game title, and buttons to
    start the game, load a save, access settings, or quit.
    """

    # Colour palette
    COLOUR_BG: tuple = (5, 0, 0)             # Near-black background
    COLOUR_VIGNETTE: tuple = (0, 0, 0)       # Vignette overlay
    COLOUR_TITLE: tuple = (200, 30, 30)      # Crimson title
    COLOUR_SUBTITLE: tuple = (120, 80, 80)   # Muted subtitle
    COLOUR_PARTICLE: tuple = (140, 20, 20)   # Floating particle colour
    COLOUR_LINE: tuple = (60, 10, 10)        # Decorative line colour

    def __init__(self, screen: pygame.Surface, settings) -> None:
        """
        Initialise the main menu.

        Args:
            screen (pygame.Surface): The main game window surface.
            settings: Settings object containing WIDTH, HEIGHT, FPS, etc.
        """
        self.screen = screen
        self.settings = settings
        self.width: int = settings.WIDTH
        self.height: int = settings.HEIGHT

        # Load fonts — falls back gracefully if custom font not found
        try:
            self.font_title = pygame.font.Font("assets/fonts/title.ttf", 80)
            self.font_subtitle = pygame.font.Font("assets/fonts/body.ttf", 18)
            self.font_button = pygame.font.Font("assets/fonts/body.ttf", 22)
        except (FileNotFoundError, OSError):
            # Fallback to system fonts
            self.font_title = pygame.font.SysFont("Georgia", 80, bold=True)
            self.font_subtitle = pygame.font.SysFont("Georgia", 18)
            self.font_button = pygame.font.SysFont("Georgia", 22)

        # Animation timer (incremented each frame, used for sine-wave effects)
        self.timer: float = 0.0

        # Particle system — each particle is [x, y, speed, size, alpha]
        self.particles: list = self._init_particles(40)

        # Build buttons (centred horizontally)
        cx = self.width // 2  # Horizontal centre
        self.buttons: dict = {
            "start":    Button(cx, self.height * 0.52, 260, 48, "START GAME"),
            "load":     Button(cx, self.height * 0.62, 260, 48, "LOAD GAME"),
            "settings": Button(cx, self.height * 0.72, 260, 48, "SETTINGS"),
            "quit":     Button(cx, self.height * 0.82, 260, 48, "QUIT"),
        }

        # Vignette overlay surface (drawn once, reused each frame)
        self.vignette_surface = self._create_vignette()

        # Next scene flag — set by button handlers, read by the scene manager
        self.next_scene: str | None = None

    # ------------------------------------------------------------------ #
    #  Initialisation helpers                                              #
    # ------------------------------------------------------------------ #

    def _init_particles(self, count: int) -> list:
        """
        Create a list of floating ambient particles.

        Args:
            count (int): Number of particles to generate.

        Returns:
            list: List of particle data [x, y, speed, radius, alpha].
        """
        import random
        particles = []
        for _ in range(count):
            particles.append([
                random.randint(0, self.width),   # x
                random.randint(0, self.height),  # y
                random.uniform(0.2, 0.8),        # upward drift speed
                random.randint(1, 3),            # radius
                random.randint(40, 160),         # alpha (transparency)
            ])
        return particles

    def _create_vignette(self) -> pygame.Surface:
        """
        Pre-render a radial vignette overlay that darkens screen edges.

        Returns:
            pygame.Surface: RGBA surface with vignette gradient.
        """
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        cx, cy = self.width // 2, self.height // 2
        max_dist = math.hypot(cx, cy)

        for y in range(0, self.height, 4):
            for x in range(0, self.width, 4):
                dist = math.hypot(x - cx, y - cy) / max_dist
                # Cubic falloff — dark on edges, transparent in centre
                alpha = int(220 * (dist ** 2.5))
                alpha = min(alpha, 220)
                pygame.draw.rect(surface, (0, 0, 0, alpha), (x, y, 4, 4))

        return surface

    # ------------------------------------------------------------------ #
    #  Per-frame update and draw                                           #
    # ------------------------------------------------------------------ #

    def update(self) -> None:
        """Advance animation state and update particle positions."""
        self.timer += 0.02

        import random
        for p in self.particles:
            p[1] -= p[2]               # Drift upward
            p[0] += math.sin(self.timer + p[1] * 0.01) * 0.3  # Sway left/right
            if p[1] < -10:
                # Reset particle to bottom of screen when it exits the top
                p[0] = random.randint(0, self.width)
                p[1] = self.height + 10

    def draw(self) -> None:
        """Render the full main menu frame."""
        # 1. Solid background
        self.screen.fill(self.COLOUR_BG)

        # 2. Animated particles
        self._draw_particles()

        # 3. Decorative horizontal rules
        self._draw_decorative_lines()

        # 4. Title and subtitle
        self._draw_title()

        # 5. Buttons
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.buttons.values():
            btn.check_hover(mouse_pos)
            btn.draw(self.screen, self.font_button)

        # 6. Vignette overlay (drawn last so it sits on top of everything)
        self.screen.blit(self.vignette_surface, (0, 0))

        # 7. Version watermark
        ver = self.font_subtitle.render("v0.1 — WFS FP016", True, (50, 20, 20))
        self.screen.blit(ver, (10, self.height - 24))

    def _draw_particles(self) -> None:
        """Render ambient floating particles."""
        particle_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for p in self.particles:
            x, y, _, radius, alpha = p
            pygame.draw.circle(
                particle_surf,
                (*self.COLOUR_PARTICLE, alpha),
                (int(x), int(y)),
                radius,
            )
        self.screen.blit(particle_surf, (0, 0))

    def _draw_decorative_lines(self) -> None:
        """Draw thin horizontal lines flanking the title area."""
        y_pos = int(self.height * 0.46)
        margin = 60
        line_width = (self.width - 300) // 2  # Gap in centre for title

        # Left rule
        pygame.draw.line(
            self.screen, self.COLOUR_LINE,
            (margin, y_pos), (self.width // 2 - 160, y_pos), 1
        )
        # Right rule
        pygame.draw.line(
            self.screen, self.COLOUR_LINE,
            (self.width // 2 + 160, y_pos), (self.width - margin, y_pos), 1
        )

    def _draw_title(self) -> None:
        """
        Render the game title with a subtle breathing animation,
        and the subtitle tag line below it.
        """
        # Sine-wave brightness pulse on the title colour
        pulse = int(20 * math.sin(self.timer * 1.5))
        r = min(200 + pulse, 255)
        title_colour = (r, max(30 + pulse // 2, 0), max(30 + pulse // 2, 0))

        title_surf = self.font_title.render("ALIAS", True, title_colour)
        title_rect = title_surf.get_rect(center=(self.width // 2, self.height * 0.35))
        self.screen.blit(title_surf, title_rect)

        # Subtitle beneath the title
        subtitle_surf = self.font_subtitle.render(
            "every truth wears a mask", True, self.COLOUR_SUBTITLE
        )
        sub_rect = subtitle_surf.get_rect(center=(self.width // 2, self.height * 0.35 + 60))
        self.screen.blit(subtitle_surf, sub_rect)

    # ------------------------------------------------------------------ #
    #  Event handling                                                      #
    # ------------------------------------------------------------------ #

    def handle_events(self, events: list) -> None:
        """
        Process input events for the main menu.

        Args:
            events (list): List of pygame events from the current frame.
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Button click detection
            if self.buttons["start"].is_clicked(event):
                self.next_scene = "game"         # Transition to the game scene

            elif self.buttons["load"].is_clicked(event):
                self.next_scene = "load"         # Transition to load screen

            elif self.buttons["settings"].is_clicked(event):
                self.next_scene = "settings"     # Transition to settings screen

            elif self.buttons["quit"].is_clicked(event):
                pygame.quit()
                sys.exit()

    # ------------------------------------------------------------------ #
    #  Scene manager interface                                             #
    # ------------------------------------------------------------------ #

    def run(self) -> str:
        """
        Run the main menu loop until the player selects an option.

        Returns:
            str: The key of the next scene to load (e.g. "game", "settings").
        """
        clock = pygame.time.Clock()
        fps = getattr(self.settings, "FPS", 60)

        while self.next_scene is None:
            events = pygame.event.get()
            self.handle_events(events)
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(fps)

        return self.next_scene
