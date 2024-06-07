from tkinter import *
from game_pieces import *
from game_img import *

# Constants
BOARD_SIZE = 1000
BLOCK_SIZE = 50
HOME_POSITIONS = {
    'yellow': [(50, 50), (100, 50), (50, 100), (100, 100)],
    'green': [(BOARD_SIZE - 150, 50), (BOARD_SIZE - 100, 50), (BOARD_SIZE - 150, 100), (BOARD_SIZE - 100, 100)],
    'blue': [(50, BOARD_SIZE - 150), (100, BOARD_SIZE - 150), (50, BOARD_SIZE - 100), (100, BOARD_SIZE - 100)],
    'red': [(BOARD_SIZE - 150, BOARD_SIZE - 150), (BOARD_SIZE - 100, BOARD_SIZE - 150), (BOARD_SIZE - 150, BOARD_SIZE - 100), (BOARD_SIZE - 100, BOARD_SIZE - 100)]
}
PLAYER_COLORS = ['yellow', 'green', 'blue', 'red']
START_POSITIONS = {
    'yellow': (5, 2),
    'green': (4, 2),
    'blue': (2, 2),
    'red': (3, 2)
}

# Global Variables
turn_index = 0
players = {}
home_pieces = {}
main_board = []

def initialize_game():
    """
    Initialize the game by setting up the board, players, and pieces.
    """
    global players, home_pieces, main_board
    players = {color: [] for color in PLAYER_COLORS}
    home_pieces = {color: [] for color in PLAYER_COLORS}
    main_board = [RBox() for _ in range(57)]  # Main board boxes

    setup_players()
    setup_board()
    setup_home_pieces()
    setup_positions()

def setup_players():
    """
    Set up the player pieces on the board.
    """
    for color in PLAYER_COLORS:
        for i in range(4):
            piece = create_piece(color, i)
            players[color].append(piece)

def create_piece(color, index):
    """
    Create a game piece based on its color and index.
    
    Args:
        color (str): The color of the player piece.
        index (int): The index of the piece.
        
    Returns:
        Box: An instance of the player piece.
    """
    x, y = HOME_POSITIONS[color][index]
    if color == 'yellow':
        return YBox(num=-1, x=x, y=y, x0=x, y0=y)
    elif color == 'green':
        return GBox(num=-1, x=x, y=y, x0=x, y0=y)
    elif color == 'blue':
        return BBox(num=-1, x=x, y=y, x0=x, y0=y)
    elif color == 'red':
        return RBox(num=-1, x=x, y=y, x0=x, y0=y)

def setup_board():
    """
    Set up the main board with its boxes and pieces.
    """
    # Example of setting up some main board positions
    # Add logic for setting up all board positions here
    for i in range(57):
        main_board[i].x = i * BLOCK_SIZE  # Example logic
        main_board[i].y = i * BLOCK_SIZE  # Example logic

def setup_home_pieces():
    """
    Set up the home positions for each player's pieces.
    """
    for color, positions in HOME_POSITIONS.items():
        for x, y in positions:
            home_pieces[color].append(RBox(x=x, y=y))

def setup_positions():
    """
    Initialize the starting positions for the game pieces.
    """
    for color, (x_start, y_start) in START_POSITIONS.items():
        for piece in players[color]:
            piece.x0 = x_start
            piece.y0 = y_start
            piece.swap()

def get_current_turn():
    """
    Get the color of the current player's turn.
    
    Returns:
        str: The color of the current player's turn.
    """
    return PLAYER_COLORS[turn_index]

def next_turn():
    """
    Progress to the next player's turn.
    """
    global turn_index
    turn_index = (turn_index + 1) % len(PLAYER_COLORS)

def move_piece(piece, steps):
    """
    Move a piece on the board by a given number of steps.
    
    Args:
        piece (Box): The piece to move.
        steps (int): The number of steps to move the piece.
    """
    if piece.num == -1 and steps == 6:
        # Place the piece on the starting position
        piece.num = 0
        piece.swap()
    elif piece.num != -1:
        piece.num += steps
        piece.swap()
        check_for_kill(piece)

def check_for_kill(piece):
    """
    Check if the moved piece lands on an opponent's piece, resulting in a kill.
    
    Args:
        piece (Box): The moved piece to check for a kill.
    """
    current_pos = (piece.x0, piece.y0)
    for color, pieces in players.items():
        if color != get_current_turn():
            for opponent_piece in pieces:
                if (opponent_piece.x0, opponent_piece.y0) == current_pos and not opponent_piece.double:
                    reset_piece(opponent_piece)
                    print(f"{color} piece has been killed by {get_current_turn()}")

def reset_piece(piece):
    """
    Reset a piece to its home position after being killed.
    
    Args:
        piece (Box): The piece to reset.
    """
    piece.num = -1
    color = get_piece_color(piece)
    home_position = HOME_POSITIONS[color][piece.num]
    piece.x0, piece.y0 = home_position
    piece.swap()

def get_piece_color(piece):
    """
    Get the color of a given piece.
    
    Args:
        piece (Box): The piece to get the color of.
        
    Returns:
        str: The color of the piece.
    """
    if isinstance(piece, YBox):
        return 'yellow'
    elif isinstance(piece, GBox):
        return 'green'
    elif isinstance(piece, BBox):
        return 'blue'
    elif isinstance(piece, RBox):
        return 'red'

if __name__ == "__main__":
    initialize_game()