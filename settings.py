import math
import random
from enum import Enum
from tkinter import filedialog

# import praw
# import pygame as pg
# import Highscores
# import Card

TITLE = "KanisaRedditGen"
# pg.font.init()

ALPHANUMERIC = "abcdefghijklmnopqrstuvwxyz0123456789"
PUNCTUATION = "!.?,;:\"'_-=+/&"
MIN_CREATION_UTC = 1000000000
MAX_CREATION_UTC = 10000000000
# SAVE MAX_CREATION_UTC = 1633120253 SAVE #

# SCALING AND FPS
FULL_SCREEN = 0
SCALE = 1
FPS = 60

# DISPLAY INFORMATION
NATIVE_WIDTH = 256
NATIVE_HEIGHT = 256
NATIVE_SIZE = (NATIVE_WIDTH, NATIVE_HEIGHT)
NATIVE_WIDTH_CENTER = NATIVE_WIDTH // 2
NATIVE_HEIGHT_CENTER = NATIVE_HEIGHT // 2
NATIVE_TOP = 0
NATIVE_RIGHT = NATIVE_WIDTH
NATIVE_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT_CENTER)
NATIVE_BOTTOM = NATIVE_HEIGHT
NATIVE_LEFT = 0
NATIVE_TOP_LEFT = (NATIVE_LEFT, NATIVE_TOP)
NATIVE_TOP_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_TOP)
NATIVE_TOP_RIGHT = (NATIVE_RIGHT, NATIVE_TOP)
NATIVE_RIGHT_CENTER = (NATIVE_RIGHT, NATIVE_HEIGHT_CENTER)
NATIVE_BOTTOM_RIGHT = (NATIVE_RIGHT, NATIVE_BOTTOM)
NATIVE_BOTTOM_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT)
NATIVE_BOTTOM_LEFT = (NATIVE_LEFT, NATIVE_HEIGHT)
NATIVE_LEFT_CENTER = (NATIVE_LEFT, NATIVE_HEIGHT_CENTER)

DISPLAY_WIDTH = NATIVE_WIDTH * SCALE
DISPLAY_HEIGHT = NATIVE_HEIGHT * SCALE
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY_WIDTH_CENTER = DISPLAY_WIDTH // 2
DISPLAY_HEIGHT_CENTER = DISPLAY_HEIGHT // 2
DISPLAY_TOP = 0
DISPLAY_RIGHT = DISPLAY_WIDTH
DISPLAY_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT_CENTER)
DISPLAY_BOTTOM = DISPLAY_HEIGHT
DISPLAY_LEFT = 0
DISPLAY_TOP_LEFT = (DISPLAY_LEFT, DISPLAY_TOP)
DISPLAY_TOP_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_TOP)
DISPLAY_TOP_RIGHT = (DISPLAY_RIGHT, DISPLAY_TOP)
DISPLAY_RIGHT_CENTER = (DISPLAY_RIGHT, DISPLAY_HEIGHT_CENTER)
DISPLAY_BOTTOM_RIGHT = (DISPLAY_RIGHT, DISPLAY_BOTTOM)
DISPLAY_BOTTOM_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT)
DISPLAY_BOTTOM_LEFT = (DISPLAY_LEFT, DISPLAY_HEIGHT)
DISPLAY_LEFT_CENTER = (DISPLAY_LEFT, DISPLAY_HEIGHT_CENTER)

redditor_list = ["Foreplay241", "3MuchLikeLA", "ACC15ORD", "Deep-Fold",
                 "imma_invincible", "coby----", "atobitt", "Gena1548"]
MTG_card_list = ["Berserk", "Lightning", "Soul"]
HUMAN_DICT = {
    "ryan_reynolds": "0214902085",
    "katy_perry": "0467535662",
    "paul_rudd": "0023299295",
    "michael_render": "0167209274",
    # "trevor_vansack": "0645576577",
    # "rudolfo_benedicto": "0784937479",
    # "megan_vansack": "0588365596",
    # "samantha_vansack": "0536439196",
    # "glenda_mae_miguel": "0845961525"
}

HUMAN_INTERESTS = {
    "trevor_vansack": {
        "Flower": "Marijuana",
        "Color": "Blue",
        "Birth Month": "June",
        "Birth Day": "16",
        "Birth Year": "1990",
        "Animal": "Jellyfish",
        "Pet": "Dog"
    },
    "megan_vansack": {
        "Flower": "Marijuana",
        "Color": "Green",
        "Birth Month": "August",
        "Birth Day": "23",
        "Birth Year": "1988",
        "Animal": "Frog",
        "Pet": "Dog"
    },
    "samantha_vansack": {
        "Flower": "Marijuana",
        "Color": "Purple",
        "Birth Month": "December",
        "Birth Day": "31",
        "Birth Year": "1986",
        "Animal": "Butterfly",
        "Pet": "Dog"
    },
    "rudolfo_benedicto": {
        "Flower": "",
        "Color": "",
        "Birth Month": "November",
        "Birth Day": "15",
        "Birth Year": "1994",
        "Animal": "",
        "Pet": ""

    },
    "glenda_mae_miguel": {
        "Flower": "Sunflower",
        "Color": "Black and White",
        "Birth Month": "October",
        "Birth Day": "22",
        "Birth Year": "1996",
        "Animal": "None"
    }
}
BARCODE_DICT = {
    "parm-gar_pringles": "3800021701",
    "nor-composition": "2622946010",
    "mtg-m13-coresetboost": "5356979177"
}
# reddit = praw.Reddit(
#     client_id="9EXDeyozdzMuhb1COAqnpQ",
#     client_secret="dU1J0681cmtNo2Pkx9JAgK9uMxgqNA",
#     user_agent="Test app for camels and chickens by u/Camel-of_Chicken",
#     username="Camel-of_Chicken",
#     password="Thisn0tThepass"
# )

# PRIMARY COLORS
LIGHT_RED = (230, 173, 216)
LIGHT_GREEN = (216, 230, 173)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (79, 47, 47)
DARK_GREEN = (47, 79, 47)
DARK_BLUE = (47, 47, 79)
GRREEN = (0, 128, 0)
INDIGO = (75, 0, 130)

# SHADES
BLACK = (0, 0, 0)
SPACE_GREY = (22, 22, 22, 69)
DARK_GREY = (60, 60, 60)
DARK_SLATE_GREY = (47, 79, 79)
DIM_GREY = (105, 105, 105)
FREE_SPEECH_GREY = (99, 86, 136)
GREY = (190, 190, 190)
GREY25 = (64, 64, 64)
GREY50 = (127, 127, 127)
GREY75 = (191, 191, 191)
GREY99 = (252, 252, 252)
LIGHT_GREY = (211, 211, 211)
SLATE_GREY = (112, 128, 144)
VERY_LIGHT_GREY = (205, 205, 205)
WHITE = (255, 255, 255)

# BLUES
ALICE_BLUE = (240, 248, 255)
AQUA = (0, 255, 255)
AQUAMARINE = (127, 255, 212)
AZURE = (240, 255, 255)
BLUE_2 = (0, 0, 238)
BLUE_3 = (0, 0, 205)
BLUE_4 = (0, 0, 139)
BLUE_VIOLET = (138, 43, 226)
CADET_BLUE = (95, 159, 159)
CORN_FLOWER_BLUE = (66, 66, 111)
CYAN = (0, 255, 255)
DARK_SLATE_BLUE = (36, 24, 130)
DARK_TURQUOISE = (112, 147, 219)
DEEP_SKY_BLUE = (0, 191, 255)
DODGER_BLUE = (30, 144, 255)
FREE_SPEECH_BLUE = (65, 86, 197)
LIGHT_CYAN = (224, 255, 255)
LIGHT_SKY_BLUE = (135, 206, 250)
LIGHT_SLATE_BLUE = (132, 112, 255)
LIGHT_STEEL_BLUE = (176, 196, 222)
MEDIUM_BLUE = (0, 0, 205)
MEDIUM_SLATE_BLUE = (123, 104, 238)
MEDIUM_TURQUOISE = (72, 209, 204)
MIDNIGHT_BLUE = (25, 25, 112)
NAVY = (0, 0, 128)
NAVY_BLUE = (0, 0, 128)
NEON_BLUE = (77, 77, 255)
NEW_MIDNIGHT_BLUE = (0, 0, 156)
PALE_TURQUOISE = (187, 255, 255)
POWDER_BLUE = (176, 224, 230)
RICH_BLUE = (89, 89, 171)
ROYAL_BLUE = (65, 105, 225)
SKY_BLUE = (135, 206, 235)
SLATE_BLUE = (131, 111, 255)
STEEL_BLUE = (70, 130, 180)
SUMMER_SKY = (56, 176, 222)
TEAL = (0, 128, 128)
TRUE_IRIS_BLUE = (3, 180, 204)
TURQUOISE = (64, 224, 208)

# BROWNS
BAKERS_CHOCOLATE = (92, 51, 23)
BEIGE = (245, 245, 220)
BROWN = (166, 42, 42)
BURLYWOOD = (222, 184, 135)
CHOCOLATE = (210, 105, 30)
DARK_BROWN = (92, 64, 51)
DARK_TAN = (151, 105, 79)
DARK_WOOD = (133, 94, 66)
LIGHT_WOOD = (133, 99, 99)
MEDIUM_WOOD = (166, 128, 100)
NEW_TAN = (235, 199, 158)
PERU = (205, 133, 63)
ROSY_BROWN = (188, 143, 143)
SADDLE_BROWN = (139, 69, 19)
SANDY_BROWN = (244, 164, 96)
SEMI_SWEET_CHOCOLATE = (107, 66, 38)
SIENNA = (142, 107, 35)
TAN = (219, 147, 112)
VERY_DARK_BROWN = (92, 64, 51)

# GREENS
CHARTREUSE = (127, 255, 0)
DARK_GREEN_COPPER = (74, 118, 110)
DARK_KHAKI = (189, 183, 107)
DARK_OLIVE_GREEN = (85, 107, 47)
DARK_SEA_GREEN = (143, 188, 143)
FOREST_GREEN = (34, 139, 34)
FREE_SPEECH_GREEN = (9, 249, 17)
GREEN_YELLOW = (173, 255, 47)
KHAKI = (240, 230, 140)
LAWN_GREEN = (124, 252, 0)
LIGHT_SEA_GREEN = (32, 178, 170)
LIME = (0, 255, 0)
MEDIUM_SEA_GREEN = (60, 179, 113)
MEDIUM_SPRING_GREEN = (0, 250, 154)
MINT_CREAM = (245, 255, 250)
OLIVE = (128, 128, 0)
OLIVE_DRAB = (107, 142, 35)
PALE_GREEN = (152, 251, 152)
SEA_GREEN = (46, 139, 87)
SPRING_GREEN = (0, 255, 127)
YELLOW_GREEN = (154, 205, 50)
SAGE_GREEN = (157, 193, 131)
ARMY_GREEN = (75, 83, 32)

# ORANGES
BISQUE = (255, 228, 196)
CORAL = (255, 127, 0)
DARK_ORANGE = (255, 140, 0)
DARK_SALMON = (233, 150, 122)
HONEYDEW = (240, 255, 240)
LIGHT_CORAL = (240, 128, 128)
LIGHT_SALMON = (255, 160, 122)
MANDARIN_ORANGE = (142, 35, 35)
ORANGE = (255, 165, 0)
ORANGE_RED = (255, 36, 0)
PEACH_PUFF = (255, 218, 185)
SALMON = (250, 128, 114)

# RED/PINK
DEEP_PINK = (255, 20, 147)
DUSTY_ROSE = (133, 99, 99)
FIREBRICK = (178, 34, 34)
FELDSPAR = (209, 146, 117)
FLESH = (245, 204, 176)
FREE_SPEECH_MAGENTA = (227, 91, 216)
FREE_SPEECH_RED = (192, 0, 0)
HOT_PINK = (255, 105, 180)
INDIAN_RED = (205, 92, 92)
LIGHT_PINK = (255, 182, 193)
MEDIUM_VIOLET_RED = (199, 21, 133)
MISTY_ROSE = (255, 228, 225)
PALE_VIOLET_RED = (219, 112, 147)
PINK = (255, 192, 203)
SCARLET = (140, 23, 23)
SPICY_PINK = (255, 28, 174)
TOMATO = (255, 99, 71)
VIOLET_RED = (208, 32, 144)

# PURPLE/PINK
DARK_ORCHID = (153, 50, 204)
DARK_PURPLE = (135, 31, 120)
DARK_VIOLET = (148, 0, 211)
FUCHSIA = (255, 0, 255)
LAVENDER = (230, 230, 250)
LAVENDER_BLUSH = (255, 240, 245)
MAGENTA = (255, 0, 255)
MAROON = (176, 48, 96)
MEDIUM_ORCHID = (186, 85, 211)
MEDIUM_PURPLE = (147, 112, 219)
DRS_PURPLE = (147, 24, 108)
NEON_PINK = (255, 110, 199)
ORCHID = (218, 112, 214)
PLUM = (221, 160, 221)
PURPLE = (160, 32, 240)
THISTLE = (216, 191, 216)
VIOLET = (238, 130, 238)
VIOLET_BLUE = (159, 95, 159)

# YELLOWS/GOLDS
BLANCHED_ALMOND = (255, 235, 205)
DARK_GOLDENROD = (184, 134, 11)
LEMON_CHIFFON = (255, 250, 205)
LIGHT_GOLDENROD = (238, 221, 130)
LIGHT_GOLDENROD_YELLOW = (250, 250, 210)
LIGHT_YELLOW = (255, 255, 224)
PALE_GOLDENROD = (238, 232, 170)
PAPAYA_WHIP = (255, 239, 213)
CORNSILK = (255, 248, 220)
GOLDENROD = (218, 165, 32)
MOCCASIN = (255, 228, 181)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
MEDIUM_GOLDENROD = (234, 234, 174)
MUSTARD_YELLOW = (254, 220, 86)
BURNT_YELLOW = ()

# WHITES/OFF-WHITES
ANTIQUE_WHITE = (250, 235, 215)
FLORAL_WHITE = (255, 250, 240)
GHOST_WHITE = (248, 248, 255)
NAVAJO_WHITE = (255, 222, 173)
OLD_LACE = (253, 245, 230)
WHITE_SMOKE = (245, 245, 245)
GAINSBORO = (220, 220, 220)
IVORY = (255, 255, 240)
LINEN = (250, 240, 230)
SEASHELL = (255, 245, 238)
SNOW = (255, 250, 250)
WHEAT = (245, 222, 179)
QUARTZ = (217, 217, 243)

PUNCTUATION_COLORS = {
    ",": LAWN_GREEN,
    "'": BLANCHED_ALMOND,
    " ": FREE_SPEECH_MAGENTA,
    ":": VIOLET_RED,
    "-": SAGE_GREEN,
    "_": DARK_ORANGE,
    "!": WHEAT,
    ".": SEMI_SWEET_CHOCOLATE,
    "?": BLACK,
    ";": PURPLE,
    "*": POWDER_BLUE,
    "\"": FELDSPAR,
    "=": PEACH_PUFF,
    "+": PAPAYA_WHIP,
    "/": DEEP_PINK,
    "&": BAKERS_CHOCOLATE
}
# Maybe too much purples, find a better balance.
ALPHANUMERIC_COLORS = {
    " ": SNOW,
    ":": LINEN,
    "-": WHEAT,
    "_": GREY,
    "0": GREY75,
    "1": GREY25,
    "2": PURPLE,
    "3": DARK_GREEN_COPPER,
    "4": MINT_CREAM,
    "5": DARK_RED,
    "6": FELDSPAR,
    "7": MEDIUM_PURPLE,
    "8": SEMI_SWEET_CHOCOLATE,
    "9": MOCCASIN,
    "a": MAROON,
    "b": MEDIUM_WOOD,
    "c": CORNSILK,
    "d": DRS_PURPLE,
    "e": DEEP_SKY_BLUE,
    "f": SKY_BLUE,
    "g": DUSTY_ROSE,
    "h": POWDER_BLUE,
    "i": DARK_SLATE_BLUE,
    "j": DARK_ORCHID,
    "k": RED,
    "l": SADDLE_BROWN,
    "m": DARK_VIOLET,
    "n": DARK_PURPLE,
    "o": DARK_TURQUOISE,
    "p": VERY_DARK_BROWN,
    "q": PLUM,
    "r": FOREST_GREEN,
    "s": MEDIUM_VIOLET_RED,
    "t": VIOLET_BLUE,
    "u": MEDIUM_SLATE_BLUE,
    "v": DARK_GOLDENROD,
    "w": ROYAL_BLUE,
    "x": QUARTZ,
    "y": KHAKI,
    "z": GAINSBORO,
}
RANDOM_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
RANDOM_COLOR2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
RANDOM_COLOR3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

RANDOM_RED = (random.randint(185, 255), random.randint(0, 125), random.randint(0, 125))
RANDOM_GREEN = (random.randint(0, 125), random.randint(185, 255), random.randint(0, 125))
RANDOM_BLUE = (random.randint(0, 125), random.randint(0, 125), random.randint(185, 255))

GREY_SHADES = [BLACK, SPACE_GREY, DARK_GREY, DARK_SLATE_GREY, DIM_GREY, FREE_SPEECH_GREY,
               GREY, GREY25, GREY50, GREY75, GREY99, LIGHT_GREY, SLATE_GREY, VERY_LIGHT_GREY, WHITE]

RANDOM_COLOR_LIST = [RANDOM_COLOR, RANDOM_COLOR2, RANDOM_COLOR3,
                     RANDOM_RED, RANDOM_GREEN, RANDOM_BLUE,
                     QUARTZ, BISQUE, MANDARIN_ORANGE, CORN_FLOWER_BLUE]
RANDOM_COLOR_STR_LIST = ["black", "green", "blue", "grey"]
TEXT_ONLY_SUBREDDITS = ["TalesFromTechSupport", "TalesFromThePizzaGuy", "TalesFromRetail", "LifeOfNorman",
                        "PettyRevenge"]
TEXTONLY_STRING = ""
for subreddit in TEXT_ONLY_SUBREDDITS:
    TEXTONLY_STRING += subreddit + "+"

PUNCTUATION_COORDS = {
    ",": [(1, 1), (0, 5), (0, 0)],
    "'": [(2, 0), (1, 2), (4, 1)],
    " ": [(0, 2), (2, 2), (7, 3)],
    ":": [(1, 0), (3, 4), (8, 4)],
    "-": [(0, 0), (4, 6), (1, 5)],
    "_": [(2, 3), (5, 5), (2, 6)],
    "!": [(2, 0), (6, 8), (4, 7)],
    ".": [(3, 1), (7, 7), (5, 8)],
    "?": [(1, 0), (8, 3), (5, 9)],
    ";": [(0, 2), (9, 5), (6, 0)],
    "*": [(2, 0), (0, 9), (9, 1)],
    "\"": [(2, 0), (6, 8), (4, 7)],
    "=": [(3, 1), (7, 7), (5, 8)],
    "/": [(1, 0), (8, 3), (5, 9)],
    "+": [(0, 2), (9, 5), (6, 0)],
    "&": [(2, 0), (0, 9), (9, 1)]
}

ALPHANUMERIC_COORDS = {
    " ": [(1, 1), (0, 5), (0, 0)],
    ":": [(2, 0), (1, 2), (4, 1)],
    "_": [(0, 2), (2, 2), (7, 3)],
    "0": [(1, 0), (3, 4), (8, 4)],
    "1": [(0, 0), (4, 6), (1, 5)],
    "2": [(2, 3), (5, 5), (2, 6)],
    "3": [(2, 0), (6, 8), (4, 7)],
    "4": [(3, 1), (7, 7), (5, 8)],
    "5": [(1, 0), (8, 3), (5, 9)],
    "6": [(0, 2), (9, 5), (6, 0)],
    "7": [(2, 0), (0, 9), (9, 1)],
    "8": [(2, 2), (1, 6), (6, 2)],
    "9": [(1, 3), (2, 5), (3, 3)],
    "a": [(2, 1), (3, 1), (3, 4)],
    "b": [(0, 3), (4, 0), (6, 5)],
    "c": [(2, 0), (5, 2), (5, 6)],
    "d": [(0, 2), (6, 0), (2, 7)],
    "e": [(2, 2), (7, 1), (5, 8)],
    "f": [(0, 2), (8, 2), (2, 9)],
    "g": [(2, 1), (9, 7), (1, 0)],
    "h": [(3, 0), (0, 4), (1, 1)],
    "i": [(1, 2), (1, 5), (1, 2)],
    "j": [(1, 3), (2, 8), (4, 3)],
    "k": [(1, 1), (3, 1), (1, 4)],
    "l": [(0, 3), (4, 2), (4, 5)],
    "m": [(0, 3), (5, 2), (7, 6)],
    "n": [(2, 1), (6, 3), (7, 7)],
    "o": [(2, 0), (7, 6), (8, 8)],
    "p": [(2, 2), (8, 9), (9, 9)],
    "q": [(1, 0), (9, 3), (5, 0)],
    "r": [(0, 2), (0, 6), (3, 1)],
    "s": [(2, 3), (1, 2), (6, 2)],
    "t": [(3, 1), (2, 0), (5, 3)],
    "u": [(0, 1), (3, 3), (2, 4)],
    "v": [(1, 0), (4, 6), (2, 5)],
    "w": [(1, 2), (5, 9), (0, 6)],
    "x": [(1, 3), (6, 1), (1, 7)],
    "y": [(2, 1), (7, 4), (4, 8)],
    "z": [(0, 2), (8, 3), (0, 2)]
}
ALPHANUMERIC_AXIOMS = {
    " ": " ",
    ":": ":",
    "-": "-",
    "_": "_",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "a": "b3a3b",
    "b": "a4b4a",
    "c": "c1a5t",
    "d": "dog",
    "e": "elf",
    "f": "f9f1f1f9f",
    "g": "gg",
    "h": "h9g1h1g9h",
    "i": "ill",
    "j": "jon",
    "k": "ken",
    "l": "l0o0l",
    "m": "man3",
    "n": "ne5t",
    "o": "7owl",
    "p": "0pen",
    "q": "quo",
    "r": "rut",
    "s": "sun",
    "t": "tip",
    "u": "uni",
    "v": "van",
    "w": "w1ap1",
    "x": "xy7z9",
    "y": "yip",
    "z": "ze8n",
}

ALPHANUMERIC_RULES = {
    " ": "PUSH+1",
    ":": "PUSH+2",
    "-": "POP-1",
    "_": "POP-2",
    "0": "ANGLE-120",
    "1": "ANGLE-90",
    "2": "ANGLE-60",
    "3": "ANGLE-45",
    "4": "ANGLE-12",
    "5": "ANGLE+12",
    "6": "ANGLE+45",
    "7": "ANGLE+60",
    "8": "ANGLE+90",
    "9": "ANGLE+120",
    "a": "LINE+8",
    "b": "LINE+8",
    "c": "LINE+8",
    "d": "LINE+6",
    "e": "LINE+8",
    "f": "LINE+8",
    "g": "LINE-36",
    "h": "LINE-1",
    "i": "LINE+8",
    "j": "LINE+8",
    "k": "LINE-8",
    "l": "LINE-45",
    "m": "LINE-8",
    "n": "LINE+12",
    "o": "LINE+8",
    "p": "LINE-1",
    "q": "LINE+8",
    "r": "LINE+45",
    "s": "LINE+8",
    "t": "LINE-8",
    "u": "LINE+1",
    "v": "LINE+8",
    "w": "LINE-1",
    "x": "LINE+8",
    "y": "LINE+8",
    "z": "LINE-8",
}

PUNCTUATION_WORD_LISTS = {
    ",": ["comma", "coma", "kona", "players", "right", "turtle", "look", "please", "feel", "less"],
    "'": ["apostrophe", "trophy", "post", "apostle", "hustle", "bussin", "combine", "pretty", "if", "you"],
    " ": ["space", "blank", "empty", "nope", "paris", "almost", "copper", "whole", "world", "ice"],
    ":": ["colon", "dots", "top", "heart", "frankfurt", "star", "silver", "try", "too", "hard"],
    "-": ["dash", "lined", "middle", "zip", "greenville", "half", "fake", "get", "my", "hair"],
    "_": ["under", "line", "bottom", "score", "moscow", "over", "gold", "why", "do", "I"],
    "!": ["comma", "coma", "kona", "players", "right", "turtle", "look", "please", "feel", "less"],
    ".": ["apostrophe", "trophy", "post", "apostle", "hustle", "bussin", "combine", "pretty", "if", "you"],
    "?": ["space", "blank", "empty", "nope", "paris", "almost", "copper", "whole", "world", "ice"],
    ";": ["colon", "dots", "top", "heart", "frankfurt", "star", "silver", "try", "too", "hard"],
    "*": ["dash", "lined", "middle", "zip", "greenville", "half", "fake", "get", "my", "hair"],
    "\"": ["under", "line", "bottom", "score", "moscow", "over", "gold", "why", "do", "I"],
    "=": ["colon", "dots", "top", "heart", "frankfurt", "star", "silver", "try", "too", "hard"],
    "+": ["dash", "lined", "middle", "zip", "greenville", "half", "fake", "get", "my", "hair"],
    "/": ["dash", "lined", "middle", "zip", "greenville", "half", "fake", "get", "my", "hair"],
    "&": ["under", "line", "bottom", "score", "moscow", "over", "gold", "why", "do", "I"]
}

ALPHANUMERIC_WORD_LISTS = {
    "0": ["zero", "none", "hero", "villain", "beijing", "eye", "platinum", "yeah", "baby", "ever"],
    "1": ["one", "lonely", "win", "juan", "tokyo", "hand", "sapphire", "run", "the", "jewels"],
    "2": ["two", "too", "lose", "to", "madagascar", "foot", "emerald", "render", "final", "fantasy"],
    "3": ["three", "tree", "charm", "triangle", "chicago", "knee", "ruby", "crash", "hit", "wall"],
    "4": ["four", "fore", "core", "square", "seattle", "ear", "diamond", "in", "right", "now"],
    "5": ["five", "high", "hive", "pentagon", "miami", "hair", "opal", "need", "miracle", "stranded"],
    "6": ["six", "sticks", "chicks", "angle", "detroit", "finger", "jade", "let", "down", "around"],
    "7": ["seven", "heaven", "Kevin", "shovel", "mesa", "toe", "topaz", "head", "died", "hole"],
    "8": ["eight", "straight", "infinite", "ate", "youngstown", "bones", "quartz", "call", "name", "side"],
    "9": ["nine", "no", "max", "final", "akron", "teeth", "onyx", "headphone", "window", "door"],
    "a": ["alpha", "after", "aloha", "all", "atlanta", "aisle", "amber", "ape", "apple", "acura"],
    "b": ["bravo", "being", "bang", "bunny", "buffalo", "banquet", "blue", "bat", "broccoli", "bently"],
    "c": ["charlie", "cold", "climb", "cow", "cleveland", "concert", "cerulean", "cat", "cauliflower", "car"],
    "d": ["delta", "dinner", "drink", "dead", "denver", "diner", "dandelion", "dog", "dragonfruit", "dodge"],
    "e": ["echo", "evening", "east", "eat", "ellensburg", "elegant", "ecru", "elephant", "eggplant", "elantra"],
    "f": ["foxtrot", "fire", "flint", "flower", "flynt", "ferocious", "firebrick", "fox", "fennel", "ford"],
    "g": ["golf", "grass", "golden", "game", "georgia", "giant", "green", "gorilla", "grape", "golfcart"],
    "h": ["hotel", "hurried", "hungry", "humble", "houston", "hurling", "hotpink", "hippopotamus", "honeydew", "honda"],
    "i": ["india", "in", "ice", "into", "idaho", "icicle", "indigo", "iguana", "iceberg", "illicit"],
    "j": ["juliette", "just", "jump", "Jessica", "jamestown", "jungle", "jade", "jaguar", "jalapenos", "jetplane"],
    "k": ["kilo", "killed", "knight", "kindle", "kentucky", "kingly", "khaki", "kangaroo", "kale", "kudi"],
    "l": ["lima", "last", "long", "list", "london", "lost", "lavender", "llama", "legumes", "lincoln"],
    "m": ["mike", "month", "mass", "moon", "massachusetts", "more", "magenta", "monkey", "mushroom", "minivan"],
    "n": ["november", "near", "noble", "noon", "nashville", "never", "navyblue", "newt", "napa", "nas"],
    "o": ["oscar", "open", "opera", "out", "oakland", "optic", "orchid", "orangutan", "orange", "october"],
    "p": ["papa", "punch", "prince", "penelope", "philadelphia", "pan", "periwinkle", "platypus", "potato", "poptart"],
    "q": ["quebec", "queen", "quest", "quilt", "queens", "question", "quicksilver", "quail", "quinoa", "quack"],
    "r": ["romeo", "really", "random", "rake", "reno", "ranch", "red", "rhinoceros", "radish", "reel"],
    "s": ["sierra", "sold", "simple", "sake", "scranton", "sacred", "saffron", "snake", "spinach", "soil"],
    "t": ["tango", "time", "topple", "take", "tuscaloosa", "ton", "tawny", "turkey", "taro", "taser"],
    "u": ["uniform", "until", "under", "utility", "ukraine", "ultra", "ube", "unicorn", "ugli", "up"],
    "v": ["victor", "very", "vixen", "vampire", "vienna", "violence", "violet", "vulture", "vanilla", "voss"],
    "w": ["whiskey", "wise", "west", "well", "wuhan", "well", "white", "whale", "watermelon", "wet"],
    "x": ["x-ray", "x-men", "Xena", "xylophone", "xi'an", "xacto", "xanadu", "xenops", "ximenia", "xoom"],
    "y": ["yankee", "yelled", "yip", "yuck", "yakima", "yarn", "yellow", "yak", "yam", "yup"],
    "z": ["zulu", "zebra", "zoinks", "zealand", "zhengzhou", "zombie", "zaffre", "zebra", "zucchini", "zoom"]
}

ANOTHER_WORD_LISTS = {
    "0": ["zero", "Luna", "bed", "smelly", "beijing", "dog", "LeBron James", "alpaca", "pizza", "unicycle"],
    "1": ["one", "Hallow", "couch", "brave", "tokyo", "tree", "Michael Jordan", "skunk", "spaghetti", "bicycle"],
    "2": ["two", "Oreo", "chair", "perfect", "madagascar", "ocean", "Chris Farley", "baboon", "cheeseburger", "tricycle"],
    "3": ["three", "Sunny", "loveseat", "motionless", "chicago", "book", "Bob Marley", "spider", "corn-cob", "four-wheeler"],
    "4": ["four", "Trigger", "recliner", "petite", "seattle", "chair", "Gene Simmons", "narwhal", "lasagna", "tank"],
    "5": ["five", "Frick", "table", "clean", "miami", "car", "Your mom", "tiger", "bread", "semi-truck"],
    "6": ["six", "Frack", "side-table", "colorful", "detroit", "sky", "my 7th grade math teacher", "crab", "crab-legs", "clown car"],
    "7": ["seven", "Butterscotch", "desk", "helpful", "mesa", "computer", "the mailman", "chicken", "dumplings", "hang-glider"],
    "8": ["eight", "Caramel", "end-table", "eager", "youngstown", "moon", "the darkest policeman", "cow", "chimichanga", "dirt-bike"],
    "9": ["nine", "Toffee", "bar-stool", "hilarious", "akron", "guitar", "your grandpa", "salamander", "rice", "motor-cycle"],
    "a": ["ten", "Sergent", "fireplace", "happy", "atlanta", "coffee", "amber", "the slowest kid", "apple", "acura"],
    "b": ["eleven", "Wolfie", "lamp", "muddy", "buffalo", "flower", "the bus driver", "bat", "broccoli", "bently"],
    "c": ["twelve", "Blue", "ottoman", "lovely", "cleveland", "mountain", "the entire marching band", "cat", "cauliflower", "car"],
    "d": ["thirteen", "Mila", "rug", "poor", "denver", "river", "God's dumbest nephew", "dog", "dragonfruit", "dodge"],
    "e": ["fourteen", "Church", "lawn chair", "stupid", "ellensburg", "sun", "the local veterinary", "elephant", "eggplant", "elantra"],
    "f": ["fifteen", "Kora", "patio table", "successful", "flynt", "phone", "the whitest crackhead", "fox", "fennel", "ford"],
    "g": ["sixteen", "Midnight", "bunk beds", "witty", "georgia", "house", "the grey wizard", "gorilla", "grape", "golfcart"],
    "h": ["seventeen", "Smokey", "couch-bed", "terrible", "houston", "hat", "the security guard", "hippopotamus", "honeydew", "honda"],
    "i": ["eighteen", "Oliver", "bean-bag chair", "upset", "idaho", "beach", "that scary clown", "iguana", "iceberg", "train"],
    "j": ["twenty-one", "Bruiser", "vanity dresser", "lazy", "jamestown", "cloud", "this scraggly cat", "jaguar", "jalapenos", "jetplane"],
    "k": ["fourty-five", "Maxwell", "dresser", "light", "kentucky", "key", "that homeless man", "kangaroo", "kale", "kayak"],
    "l": ["sixty-nine", "Fred", "bench", "horrible", "london", "fish", "any of the spice girls", "llama", "legumes", "lincoln"],
    "m": ["one hundred", "Tucker", "cot", "healthy", "massachusetts", "elephant", "Bozo the clown", "monkey", "mushroom", "minivan"],
    "n": ["fifty-two", "Snowball", "lamp", "pleasant", "nashville", "pizza", "Dumbo the janitor", "newt", "napa", "nissan"],
    "o": ["sixty-four", "Henry", "mirror", "proud", "oakland", "friend", "Bert Reynolds", "orangutan", "orange", "ferrarri"],
    "p": ["eighty-eight", "Toby", "curtain-rod", "prickly", "philadelphia", "camera", "Ryan Reynolds", "platypus", "potato", "bus"],
    "q": ["thirty-nine", "Pearl", "pillow", "selfish", "queens", "clock", "Morgan Freeman", "quail", "quinoa", "truck"],
    "r": ["fifteen and a half", "Panther", "dog bed", "putrid", "reno", "butterfly", "the last person in line", "rhinoceros", "radish", "boat"],
    "s": ["eighteen and a half", "Bailey", "table-chair", "sleepy", "scranton", "bridge", "that ginger zookeeper", "snake", "spinach", "hot-air balloon"],
    "t": ["thirty-seven", "Ivy", "stove", "strange", "tuscaloosa", "pen", "this mexican gardner", "turkey", "taro", "trolly"],
    "u": ["twenty-two and a half", "Astrid", "refrigerator", "wild", "ukraine", "salad", "your mom's cousin's brother's nephew's best friend", "unicorn", "ugli", "taxi"],
    "v": ["two-thirds", "Lemiwinks", "sink", "annoying", "vienna", "mirror", "a mermaid", "vulture", "vanilla", "van"],
    "w": ["one hundred thirty-one", "Bear", "cupboard", "beautiful", "wuhan", "rainbow", "The hulk and his sister", "whale", "watermelon", "raft"],
    "x": ["one-tenth", "Penny", "dinner-table", "clumsy", "xi'an", "wallet", "Walter Bishop", "xenops", "ximenia", "submarine"],
    "y": ["ninety-nine", "Frow Frow", "counter-top", "colorful", "yakima", "dungeon", "Ash Ketchem", "yak", "yam", "lawnmower"],
    "z": ["fourty-four", "Peanut", "table-chair", "crazy", "zhengzhou", "attic", "your stoned roommate", "zebra", "zucchini", "zipline"]
}


# _.+-=/
ALPHANUMERIC_NOTE_PATTERNS = {
    " ": ["..+.", "-+-=", "=..="],
    ":": ["..-+", "+--=", "__//"],
    "-": [".._.", "+==+", "--=="],
    "_": ["..=.", "=-++", "/---"],
    "0": ["../.", "-++=", "///="],
    "1": [".++.", "//==", "++.."],
    "2": [".--+", "/==/", "-+-+"],
    "3": [".__+", "=/=+", "/=/="],
    "4": [".==-", "._=+", "-+//"],
    "5": [".//-", "__.+", "/-_-"],
    "6": [".+-.", "+=._", "__=="],
    "7": [".+_+", "-_.=", "_./="],
    "8": [".+=+", "=+/+", "___="],
    "9": [".+/=", "-=/+", "...="],
    "a": [".-+=", "--/_", "=_=="],
    "b": [".---", "=-/_", "_..-"],
    "c": [".-=+", "/_/-", "-+-+"],
    "d": [".-/+", "--/.", ".+-+"],
    "e": ["._++", "==/_", "/-_/"],
    "f": ["._--", "-=/-", "-.-_"],
    "g": ["._-=", ".//=", "_._."],
    "h": ["._-/", "//=/", "._.-"],
    "i": [".=-+", "/_//", "__.."],
    "j": [".=_-", "_+//", "=+=="],
    "k": [".=__", "+==/", "+==="],
    "l": [".=_/", ".=/_", "==+="],
    "m": ["./+-", "_/+=", "===+"],
    "n": ["._/-", "==_/", "...="],
    "o": [".-/_", "=+=/", "_-_="],
    "p": ["._/=", "+=/_", "==__"],
    "q": ["__//", "+//=", "=_-="],
    "r": ["/-_=", "./.+", "=-_="],
    "s": [".+--", "+/._", "=++="],
    "t": ["-+._", "_..=", "=-+="],
    "u": ["/-._", "//+-", "=+-="],
    "v": ["./__", "=._=", "_=_="],
    "w": ["_-/.", "+.=-", "=_=-"],
    "x": [".__/", "+._+", "=--="],
    "y": ["+_-.", "=-==", "/./."],
    "z": [".=_+", "-=++", "././"],
}
TEXIOTY_TONGUE_DICT = {
    "English": {
        "flag_colors": ["red", "white", "blue"],
        "welcome": "Welcome to",
        "finished": "finished",
        "drawing": "is drawing",
        "saved": "saved to"
    },
    "Ukrainian": {
        "flag_colors": ["blue", "gold"],
        "welcome": "Laskavo prosymo do",
        "finished": "zakincheno",
        "drawing": "malyuye",
        "saved": "zberezheno do"
    },
    "French": {
        "flag_colors": ["blue", "white", "red"],
        "welcome": "Bienvenue à",
        "finished": "achevée",
        "drawing": "dessine",
        "saved": "enregistré dans"
    },
    "Spanish": {
        "flag_colors": ["red", "gold"],
        "welcome": "Bienvenida a",
        "finished": "acabada",
        "drawing": "Está dibujando",
        "saved": "guardado en"
    },
    "German": {
        "flag_colors": ["yellow", "black", "red"],
        "welcome": "Willkommen zu",
        "finished": "fertig",
        "drawing": "zeichnet",
        "saved": "gespeichert zu"
    },
    "Japanese": {
        "flag_colors": ["red", "white"],
        "welcome": "Yōkoso",
        "finished": "Shūryō shita",
        "drawing": "Kaite imasu",
        "saved": "Hozon-saki"
    },
    "Chinese": {
        "flag_colors": ["red", "yellow"],
        "welcome": "Huānyíng lái dào",
        "finished": "Wánchéng de",
        "drawing": "Zhèngzài huà",
        "saved": "Bǎocún dào"
    },
    "Filipino": {
        "flag_colors": ["blue", "gold", "white"],
        "welcome": "Maligayang pagdating sa",
        "finished": "tapos na",
        "drawing": "ay gumuhit",
        "saved": "nai-save sa"
    }
}

LAYER_DICT = {
    "None": {
        "tentacles": [10],
        "sparkles": [10],
        "shell": [10],
        "decor": [10]
    },
    "Alien": {
        "body": [10, "ALEEN"],
        "eyes": [10],
        "mouth": [10],
        "tentacles": [10],
    },
    "Asteroid": {
        "core": [10, "ASTROID"],
        "metal": [10],
        "rock": [10],
        "shell": [10],
    },
    "Ball": {
        "base": [10, "OKAY"],
        "casing": [10],
        "shade": [10],
        "sparkles": [10],
    },
    "Portal": {
        "casing": [10],
        "cover": [10],
        "decor": [10],
        "metal": [10],
        "shell": [10],
    },
    # "Ball": {
    #     "base": ["Ants", "Bacteria", "Cave", "Dots", "Eye", "Glitched", "Shines", "Snow", "Spots", "Termites"],
    #     "casing": ["Compass", "Dstar", "Eth", "Jacobs", "Ladder", "Minus", "Spider", "Wall", "Web", "Xhair"],
    #     "shade": ["Cloud", "Crab", "Frog", "Jelly", "Low", "Moon", "Night", "Noon", "Open", "Tree"],
    #     "sparkles": ["Blank", "Check", "Lots", "Milky", "None", "Round", "Shadow", "Split", "Stars", "Trip"],
    # },
    "Medallion": {
        "base": [10],
        "cover": [10],
        "triangle": [10],
        "decor": [10],
    },
    "Platform": {
        "Emoji": [10],
        "Mandel": [10],
        "Vertical": [10],
        "Horizontal": [10],
    },
    "Ship": {
        "nose": [10],
        "body": [10],
        "wings": [10],
        "engine": [10],
    },
    "Sword": {
        "handle": [10],
        "hilt": [10],
        "blade": [10],
        "charm": [10],
    },
    "Tribloc": {
        "block": [10],
        "lepht": [10],
        "rhite": [10],
        "taup": [10],
    },
    "RTJ": {
        "violent_hand": [10],
        "peaceful_hand": [10],
        "pointing": [10],
        "holding": [10],
    },
    "Boat": {
        "bowsprit": [10],
        "hull": [10],
        "masts": [10],
        "rudder": [10]
    },
    "Goal": {
        "arrive": [10],
        "kill": [10],
        "survive": [10],
        "collect": [10]
    }
}


def clamp(n, minn, maxn) -> int:
    return max(min(maxn, n), minn)


def generate_id_string(string_length, char_set) -> str:
    """
    Generate an ID string given the string_length of ID and the character set to use.
    
    :param string_length: The length the ID string will be.
    :param char_set: A string of characters to choose from.
    :return: ID string for use.
    """
    ID_string = ""
    for i in range(string_length):
        ID_string += char_set[random.randint(0, len(char_set) - 1)]
    return ID_string


def create_id_utc(data_source="Random") -> (str, str):
    """
    Creates a new idutc based on data_source variable.
    :param data_source: String that decides what kind of idutc to generate.
    :return: Tuple of strings, an ID and UTC
    """
    use_id = generate_id_string(6, ALPHANUMERIC)
    use_utc = random.randint(MIN_CREATION_UTC, MAX_CREATION_UTC)
    if data_source == "Human":
        use_id = random.choice(list(HUMAN_DICT.keys()))
        use_utc = HUMAN_DICT[use_id]
    elif data_source == "Barcode":
        use_id = random.choice(list(BARCODE_DICT.keys()))
        use_utc = BARCODE_DICT[use_id]
    return use_id, use_utc


def polypointlist(sides: int, offset: int, cx: int, cy: int, radius: int) -> list:
    step = 2 * math.pi / sides
    offset = math.radians(offset)
    pointlist = [(radius * math.cos(step * n + offset) + cx, radius * math.sin(step * n + offset) + cy) for n in
                 range(0, int(sides) + 1)]
    return pointlist


def generate_hex_color(string: str) -> str:
    color_hex = ""
    for c in string:
        if c in "abcdef0123456789":
            color_hex += c
    dif = 6 - len(color_hex)
    for i in range(dif):
        color_hex += random.choice("0123456789abcdef")
    return color_hex


def new_number_list(utc_used: str) -> list:
    """
    Make a list of numbers from the 10-digit number string and return sorted list.
    """
    number_list = []
    for i in range(10):
        xs = list(utc_used)[i]
        number_list.append(int(xs))
    number_list.sort()
    return number_list


def new_color_list(id_used: str, is_float=True) -> list:
    """
    Create a new color list with the given ID string.
    
    :param id_used: ID string being used to create the color list.
    :param is_float: If the tuple is created with Floats or Integers.
    :return: list
    """
    color_list = []
    for c in id_used:
        if c.lower() in ALPHANUMERIC_COLORS:
            color = ALPHANUMERIC_COLORS[c.lower()]
        else:
            color = PUNCTUATION_COLORS[c.lower()]
        if is_float:
            color = (round(color[0] / 255, 3),
                     round(color[1] / 255, 3),
                     round(color[2] / 255, 3))

        color_list.append(color)
    return color_list


def lsystem(axioms: str, rules: dict, iterations: int) -> str:
    """
    L-system creator, turn something small into something big.
    """
    for _ in range(iterations):
        newAxioms = ''
        for axiom in axioms:
            if axiom in rules:
                newAxioms += rules[axiom]
            else:
                newAxioms += axiom
            axioms = newAxioms
        return axioms


def openfilename_str() -> str:
    filename = filedialog.askopenfilename(title='Open')
    return filename
