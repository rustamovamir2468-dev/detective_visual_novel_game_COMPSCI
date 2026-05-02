# settings.py
# ============================================================
# LOGIC TEAM: All constants for the game are stored here.
# If a number or colour is used in more than one place, write it here.
# Never hardcode values elsewhere!!!
# Authors: 5752530
# ============================================================

import pygame

# --- Screen settings ---
SCREEN_WIDTH  = 960
SCREEN_HEIGHT = 640
FPS           = 60
TITLE         = "Alias"

# --- Colors (RGB) ---
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)
DARK_GRAY  = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)

# --- Primary UI colours ---
UI_BLUE      = (100, 180, 255)
UI_BLUE_DARK = (50, 120, 200)

# --- Dialogue box ---
DIALOGUE_BG   = (245, 245, 220)
DIALOGUE_TEXT = (30, 30, 30)

# --- Accent/highlight colours ---
ACCENT_YELLOW = (255, 220, 50)
ACCENT_RED    = (220, 60, 60)

# --- World colours [PLACEHOLDER UNTIL CREATIVE ASSETS ARRIVE] ---
PLACEHOLDER_GREEN = (144, 238, 144) # Grass/outdoors
PLACEHOLDER_BROWN = (139, 90, 43) # Indoor floors
PLACEHOLDER_BLUE  = (70, 130, 180) # Water/sky

# --- Font settings ---
FONT_SIZE_SMALL  = 16
FONT_SIZE_MEDIUM = 22
FONT_SIZE_LARGE  = 32
FONT_SIZE_TITLE  = 52

# --- Dialogue Box Layout ---
DIALOGUE_BOX_HEIGHT  = 160
DIALOGUE_BOX_PADDING = 20
DIALOGUE_BOX_Y       = SCREEN_HEIGHT - DIALOGUE_BOX_HEIGHT

# --- Save file settings ---
SAVE_FILE_PATH = "save_data.json"

# --- Game States ---
STATE_MAIN_MENU      = "main_menu"
STATE_PLAYING        = "playing"
STATE_DIALOGUE       = "dialogue"
STATE_PAUSED         = "paused"
STATE_BULLETIN_BOARD = "bulletin_board"
STATE_DEDUCTION      = "deduction"
STATE_CUTSCENE       = "cutscene"
STATE_GAME_OVER      = "game_over"

# --- Acts ---
ACT_1 = "act_1"
ACT_2 = "act_2"
ACT_3 = "act_3"
ACT_4 = "act_4"

# --- Portrait States ---
# Tell creative team each character needs these exact filenames e.g. sado_neutral.png, sado_happy.png, etc.
PORTRAIT_STATES = ["neutral", "happy", "nervous", "shocked", "sad", "angry"]

# --- Characters ---
CHAR_SADO    = "sado"
CHAR_MAYA    = "maya"
CHAR_ELIAS   = "elias"
CHAR_MOTHER  = "mother"
CHAR_NARRATOR = None    # No portrait for narration

# --- Portrait display ---
PORTRAIT_WIDTH  = 200
PORTRAIT_HEIGHT = 300
PORTRAIT_X      = 60    # Left side of screen
PORTRAIT_Y      = SCREEN_HEIGHT - DIALOGUE_BOX_HEIGHT - PORTRAIT_HEIGHT - 10

# --- Scene backgrounds ---
BACKGROUND_WIDTH  = SCREEN_WIDTH
BACKGROUND_HEIGHT = SCREEN_HEIGHT

# --- Dual Palette (Act 1 = warm, Act 2+ = cold) ---
PALETTE_WARM = {
    "bg":      (255, 248, 230),
    "text":    (40,  30,  20 ),
    "ui":      (100, 180, 255),
    "accent":  (255, 200, 50 ),
    "dialogue_bg": (245, 240, 220),
}

PALETTE_COLD = {
    "bg":      (210, 215, 220),
    "text":    (20,  20,  30 ),
    "ui":      (80,  100, 140),
    "accent":  (180, 60,  60 ),
    "dialogue_bg": (220, 220, 225),
}

# --- Transition ---
TRANSITION_SPEED = 5    # Fade speed between scenes (frames)

# settings.py is now written — this is the file everyone imports from.
# Please do NOT hardcode any numbers or colours directly in your files.
# If you need a colour or size, add it to settings.py first and then import it.
# Creative team: the placeholder colours in there are temporary — let us know your final palette and we'll update them.