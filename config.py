import collections
import enum

# This file provides constants of game (windows size, colours within game, shape of tetrominos etc.)

# Window size, recommended minimum resolution is 500x720
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 720

# Number of rows and columns in gameboard - where tetrominos fall:
# The original tetris has 22 rows and 10 columns (remember of borders - left, right and bottom!)
BOARD_COLUMNS = 10 + 2  # +2 stands for left and right border lines
BOARD_ROWS = 22 + 1  # +1 stand for bottom border line


# Colors used within game to draw, you can simply add your favorite color and use it within game
class Color(enum.Enum):
    """Make human-readable aliases of colors used in game"""
    BLACK = (81, 70, 90)
    DARKRED = (186, 202, 239)
    # LIGHTBLUE = (173, 216, 230)
    LIGHTBLUE = (243, 144, 15) # tetromino
    ORANGE = (252, 178, 81)
    RED = (198, 162, 226)


BORDER_BLOCK = -1
BUFFER_BLOCK = 1
EMPTY_BLOCK = 0
FALLEN_BLOCK = 2

# For calculating points within Evaluator
POINTS_HEIGHT = 5
POINTS_GAP = 10

# Sizes within game:
BLOCK_SIZE = 18  # (in pixels) single block of tetromino/gameboard
BOARD_WIDTH = BLOCK_SIZE * (BOARD_COLUMNS+1)  # with one border row on the bottom
BOARD_HEIGHT = BLOCK_SIZE * (BOARD_ROWS+2)  # with two borders on left and right

Gameboard_coords_on_screen = collections.namedtuple('Gameboard_coords_on_screen', ['top', 'left'])

# For drawing gameboard with borders around
BOARD_WITH_BORDER_COORDS = Gameboard_coords_on_screen(
    top=(SCREEN_WIDTH / 2 - BOARD_WIDTH / 2),
    left=(SCREEN_HEIGHT / 2 - BOARD_HEIGHT / 2),
)

# For actuall gameboard - when tetromino falls etc.
GAME_BOARD_COORDS = Gameboard_coords_on_screen(
    top=BOARD_WITH_BORDER_COORDS.top,
    left=BOARD_WITH_BORDER_COORDS.left + BLOCK_SIZE,
)

GAME_SINGLE_FRAME_SEC = 0.001  # interval between single steps
TIME_STEPS_TO_FALL_BUFFER = 200  # how many steps is needed to fall tetromino one block down

TETROMINO_SHAPES = {
    "I": [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
    ],
    "Z": [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
    ],
    "S": [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
    ],
    "J": [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0],
    ],
    "L": [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 0],
    ],
    "T": [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0],
    ],
    "O": [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ],
}

MALICIOUS_LEVEL = 9
