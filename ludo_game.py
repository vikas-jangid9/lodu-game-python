from tkinter import *
import random
from game_board import *
from game_pieces import *
from game_logic import *

# Global variables
players = ["Red", "Blue", "Green", "Yellow"]
current_player_index = 0
root = None
dice_label = None
current_turn_label = None
roll_count = 0
current_rolls = []

def get_current_player():
    """
    Returns the current player's color.
    """
    return players[current_player_index]

def switch_turn():
    """
    Moves to the next player's turn.
    """
    global current_player_index
    current_player_index = (current_player_index + 1) % len(players)
    display_turn()

def display_turn():
    """
    Updates the label to show whose turn it is.
    """
    global current_turn_label
    current_turn_label.config(text=f"{get_current_player()}'s Turn")

def roll_dice():
    """
    Rolling function that rolls a dice, and allows multiple rolls if sixes are rolled.
    """
    global roll_count, current_rolls, root
    roll_count += 1
    current_dice = random.randint(1, 6)
    current_rolls.append(current_dice)
    print("Roll {}: {}".format(roll_count, current_dice))

    # Display the dice roll
    dice_label.config(text=str(current_dice))
    if current_dice != 6 or roll_count == 3:
        finalize_roll()

def finalize_roll():
    """
    Finalize the rolls and update the game state.
    """
    global roll_count
    roll_count = 0
    switch_turn()  # Custom function to change turn
    clear_dice_display()
    display_turn()

def clear_dice_display():
    """
    Clears the dice display area after each turn.
    """
    global dice_label
    dice_label.config(text="     ")

def setup_ui():
    """
    Setup the UI components.
    """
    global root, dice_label, current_turn_label

    root = Tk()
    root.title("Ludo Game")

    # Dice roll display
    dice_label = Label(root, text="     ", fg='Black', background='green', font=("Arial", 24, "bold"))
    dice_label.place(x=800, y=200)

    # Current turn display
    current_turn_label = Label(root, text="   Red's Turn   ", fg='Black', background='green', font=("Arial", 24, "bold"))
    current_turn_label.place(x=770, y=50)

    # Roll button
    Button(root, text="ROLL", relief="raised", font=("Arial", 20), command=roll_dice).place(x=805, y=120)

    # Initialize game board
    initialize_game_board()

def initialize_game_board():
    """
    Initialize the game board UI.
    """
    global root

    canvas = Canvas(root, width=600, height=600, bg="white")
    canvas.place(x=50, y=200)

    # Example: Draw a simple board with squares
    for i in range(15):
        for j in range(15):
            canvas.create_rectangle(i * 40, j * 40, (i + 1) * 40, (j + 1) * 40, outline="black")

def mainloop():
    """
    Main function to start the game loop.
    """
    setup_ui()
    root.mainloop()

if __name__ == "__main__":
    mainloop()