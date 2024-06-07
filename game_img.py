from tkinter import *  


root = Tk()

root.resizable(width=False, height=False)  # The window size of the game.
root.geometry('1000x750')
root.configure(background='green')
root.title("Checkers")

logo = PhotoImage(file="img/whitebox.gif")      # Loading all the image files that are required in the game.
logo2 = PhotoImage(file="img/red side.gif")     # Loading all the image files that are required in the game.
logo3 = PhotoImage(file="img/red.gif")          # Loading all the image files that are required in the game.
logo4 = PhotoImage(file="img/blue side.gif")
logo5 = PhotoImage(file="img/green side.gif")
logo6 = PhotoImage(file="img/yellow side.gif")
logo7 = PhotoImage(file="img/center.gif")
logoxx = PhotoImage(file="img/test.gif")
logog = PhotoImage(file="img/greenbox.gif")
logogs = PhotoImage(file="img/greenstop.gif")
logoy = PhotoImage(file="img/yellowbox.gif")
logoys = PhotoImage(file="img/yellowstop.gif")
logob = PhotoImage(file="img/bluebox.gif")
logobs = PhotoImage(file="img/bluestop.gif")
logor = PhotoImage(file="img/redbox.gif")
logors = PhotoImage(file="img/redstop.gif")
logoh = PhotoImage(file="img/head.gif")
logot = PhotoImage(file="img/tail.gif")
logoh1 = PhotoImage(file="img/head1.gif")
logot1 = PhotoImage(file="img/tail1.gif")
logoh2 = PhotoImage(file="img/head2.gif")
logot2 = PhotoImage(file="img/tail2.gif")
logoh3 = PhotoImage(file="img/head3.gif")
logot3 = PhotoImage(file="img/tail3.gif")
logoab= PhotoImage(file="img/blue.gif")
logoay= PhotoImage(file="img/yellow.gif")
logoag= PhotoImage(file="img/green.gif")

Label(image=logo2, width=298, height=298).place(x=-1, y=-1)               #setting up board images
Label(image=logo4, width=300, height=300).place(x=(-2), y=(448))
Label(image=logo5, width=296, height=296).place(x=(450), y=(0))
Label(image=logo6, width=294, height=294).place(x=(450), y=(450))
Label(image=logo7, width=150, height=150).place(x=(298), y=(298))

c = 0                                #initializing variable and flags that are to be used in the game
lx = 0
bb =0
nc = 0
rollc = 0
rolls = []
RED = True
BLUE = False
GREEN = False
YELLOW = False
TURN = True
REDKILL = False
BLUEKILL = False
GREENKILL = False
YELLOWKILL = False
