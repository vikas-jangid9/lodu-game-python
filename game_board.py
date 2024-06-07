from tkinter import *
from game_pieces import *
from game_img import *

# Constants for coordinates and dimensions
LABEL_WIDTH = 150
LABEL_HEIGHT = 150
BOARD_SIZE = 750
BLOCK_SIZE = 50

# Colors
BOARD_BG_COLOR = 'green'
TEXT_COLOR = 'black'

def setup_board(root):
    """
    Sets up the Ludo game board with labels and images.
    
    Args:
        root (Tk): The root Tkinter window.
    """
    # Set up the main window properties
    root.resizable(width=False, height=False)
    root.geometry(f'{BOARD_SIZE}x{BOARD_SIZE}')
    root.configure(background=BOARD_BG_COLOR)
    root.title("Ludo Game")

    # List of coordinates for placing images
    image_placements = [
        (logo2, -1, -1),        # Red side
        (logo4, -2, 448),       # Blue side
        (logo5, 450, 0),        # Green side
        (logo6, 450, 450),      # Yellow side
        (logo7, 298, 298)       # Center
    ]

    for img, x, y in image_placements:
        Label(root, image=img, width=LABEL_WIDTH, height=LABEL_HEIGHT).place(x=x, y=y)

    # Placing home boxes (4 for each player)
    place_home_boxes()

def place_home_boxes():
    """
    Places the home boxes for each player on the board.
    """
    # Coordinates for home boxes
    home_boxes_coords = {
        'yellow': [(50, 50), (100, 50), (50, 100), (100, 100)],
        'green': [(BOARD_SIZE - 150, 50), (BOARD_SIZE - 100, 50), (BOARD_SIZE - 150, 100), (BOARD_SIZE - 100, 100)],
        'blue': [(50, BOARD_SIZE - 150), (100, BOARD_SIZE - 150), (50, BOARD_SIZE - 100), (100, BOARD_SIZE - 100)],
        'red': [(BOARD_SIZE - 150, BOARD_SIZE - 150), (BOARD_SIZE - 100, BOARD_SIZE - 150), (BOARD_SIZE - 150, BOARD_SIZE - 100), (BOARD_SIZE - 100, BOARD_SIZE - 100)]
    }

    # Images for home boxes
    home_boxes_images = {
        'yellow': logoay,
        'green': logoag,
        'blue': logoab,
        'red': logo
    }

    # Place each home box on the board
    for color, coords in home_boxes_coords.items():
        for x, y in coords:
            Label(root, image=home_boxes_images[color], width=BLOCK_SIZE, height=BLOCK_SIZE).place(x=x, y=y)

if __name__ == "__main__":
    root = Tk()
    setup_board(root)
    root.mainloop()