# settings.py - File that contains every constant variable used in the game.
# Author(s): 5752530
# ====================================================
# This is the central file for all the constants used in the game.
# Every number, colour, and label used in the game is stored here.
# This allows for easy access (via importing) and modification of the game's settings.
# ====================================================

import pygame

# --- Screen Settings ---
SCREEN_WIDTH  = 960
SCREEN_HEIGHT = 640
FPS           = 60
TITLE         = "Alias"

# --- Colours ---
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)
DARK_GREY  = (50, 50, 50)
LIGHT_GREY = (200, 200, 200)

# --- UI Colours ---
UI_BLUE       = (100, 180, 255)
UI_BLUE_DARK  = (50,  120, 200)
ACCENT_YELLOW = (255, 220, 50)
ACCENT_RED    = (220, 60, 60)

# --- Dialogue Box Colours ---
DIALOGUE_BG   = (245, 245, 220)
DIALOGUE_TEXT = (30,  30, 30)

# --- Dual Palette --- (Mood of the game basically, like in Act 1 it's warm, in Act 2 it's cold etc.).
PALETTE_WARM = {
    "bg"           : (255, 248, 230),
    "text"         : (40,  30,  20 ),
    "ui"           : (100, 180, 255),
    "accent"       : (255, 200, 50 ),
    "dialogue_bg"  : (245, 240, 220),
}

PALETTE_COLD = {
    "bg"           : (210, 215, 220),
    "text"         : (20,  20,  30 ),
    "ui"           : (80,  100, 140),
    "accent"       : (180, 60,  60 ),
    "dialogue_bg"  : (220, 220, 225),
}

# --- Font Sizes ---
FONT_SIZE_SMALL  = 16
FONT_SIZE_MEDIUM = 22
FONT_SIZE_LARGE  = 32
FONT_SIZE_TITLE  = 52

# --- Dialogue Box Layout ---
DIALOGUE_BOX_HEIGHT  = 160
DIALOGUE_BOX_PADDING = 20
DIALOGUE_BOX_Y       = SCREEN_HEIGHT - DIALOGUE_BOX_HEIGHT

# --- Portrait Layout ---
PORTRAIT_WIDTH  = 200
PORTRAIT_HEIGHT = 300
PORTRAIT_X      = 60
PORTRAIT_Y      = SCREEN_HEIGHT - DIALOGUE_BOX_HEIGHT - PORTRAIT_HEIGHT - 10

# --- Characters ---
CHAR_PLAYER   = "player"      # Name set by player at start.
CHAR_MAYA     = "maya"
CHAR_MOTHER   = "mother"
CHAR_ELIAS    = "elias"       # Main villain.
CHAR_FINN     = "finn"       # Red herring suspect.
CHAR_HANNAH   = "hannah"        # Ally, also a suspect briefly.
CHAR_NARRATOR = None          # No name tag, no portrait.

# --- Minor NPCs --- (ADD MORE AS NEEDED, THESE ARE JUST EXAMPLES).
CHAR_BOY1         = "boy1"         # Red jacket kid (kidnapped).
CHAR_BOY2         = "boy2"         # Rude kid in Finn's class.
CHAR_SECURITY     = "security"     # School security guard in Act 2.
CHAR_NEWS_ANCHOR  = "news_anchor"  # Voice on TV news segments.

# --- Portrait States --- (Emotions that the characters can display, make sure to have corresponding images for each state in the assets folder).
PORTRAIT_STATES = ["neutral", "happy", "nervous", "shocked", "sad", "angry", "scared", "suspicious", "demon", "red_eyes", "cold", "holding", "reveal"]

# --- Acts ---
ACT_1 = "Act 1"
ACT_2 = "Act 2"
ACT_3 = "Act 3"
ACT_4 = "Act 4"

ACT_TITLES = {
    ACT_1: "A Normal Day",
    ACT_2: "Something's Wrong",
    ACT_3: "Closing In",
    ACT_4: "The Truth",
}

# --- Endings ---
ENDING_BAD_CANDY       = "ending_bad_candy"      # Act 1 Choice 1.1 death
ENDING_BAD_CO2         = "ending_bad_co2"        # Act 2 Choice 2.1 death
ENDING_BAD_MURDERED    = "ending_bad_murdered" # Act 3 Choice 3.1 death
ENDING_BAD_EXPLOSION   = "ending_bad_explosion"  # Act 3 Choice 4.1 death
ENDING_BAD_POLICE      = "ending_bad_police"     # Act 4 Choice 6.1 death
ENDING_BAD_CHOICE5     = "ending_bad_choice5"    # Act 4 Didn't tell mother (Choice 5.2)
ENDING_SACRIFICE_SELF  = "ending_sacrifice_self"
ENDING_SACRIFICE_HANNAH  = "ending_sacrifice_hannah"
ENDING_TRUE_FINAL      = "ending_true_final"   # Mother called police
ENDING_BAD_NO_MOM_HELP = "ending_bad_no_mom_help"  # Act 4 stall route, didn't tell mom

# --- Transitions ---
TRANSITION_SPEED = 5