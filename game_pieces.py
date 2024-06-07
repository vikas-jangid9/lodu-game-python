from tkinter import *
from game_img import *

class GamePiece:
    """
    Base class for all game pieces.
    """

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0):
        """
        Initialize a game piece.

        Args:
            num (int): The number of the game piece.
            x (int): The x-coordinate of the game piece.
            y (int): The y-coordinate of the game piece.
            x0 (int): The initial x-coordinate of the game piece.
            y0 (int): The initial y-coordinate of the game piece.
        """
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = None  # Placeholder for the Label object

    def swap(self):
        """
        Place the game piece on the board.
        """
        if self.rap:
            self.rap.place(x=self.x0 + 13, y=self.y0 + 14)

class YBox(GamePiece):
    """
    Class representing a yellow box.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a yellow box game piece.
        """
        super().__init__(*args, **kwargs)
        self.rap = Label(image=logoay, width=20, height=20)  # Image of yellow game piece

class GBox(GamePiece):
    """
    Class representing a green box.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a green box game piece.
        """
        super().__init__(*args, **kwargs)
        self.rap = Label(image=logoag, width=20, height=20)  # Image of green game piece

class BBox(GamePiece):
    """
    Class representing a blue box.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a blue box game piece.
        """
        super().__init__(*args, **kwargs)
        self.rap = Label(image=logoab, width=20, height=20)  # Image of blue game piece

class RBox(GamePiece):
    """
    Class representing a red box.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a red box game piece.
        """
        super().__init__(*args, **kwargs)
        self.rap = Label(image=logo3, width=20, height=20)  # Image of red game piece