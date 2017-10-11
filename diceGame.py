# Author: Olufisayo Joseph Ayodele
# Description: Just messing around, input your wager and find out how much you win

from random import *
from graphics import *

# The rules of the game are.........There are no rules
def diceGame(graphWin, wager):
    rv1 = randint(1, 6)     # Random number for the 1st dice
    rv2 = randint(1, 6)     # Random number for the 2nd dice

    # Displays the dies on the screen
    die1 = Image(Point(230, 170), str(rv1) + ".png")
    die1.draw(graphWin)
    die2 = Image(Point(370, 170), str(rv2) + ".png")
    die2.draw(graphWin)

    # Sums up your dies
    total = rv1 + rv2

    # Determines what you win or loose
    if total is 7:
        txt = Text(Point(310, 270), ("Dice Total: " + str(total) + "\nYou're Lucky Today!\nYou double your wager\nYour Winnings: $" + str(10) + " + Original Wager = $" + str(wager), "= $" + str(wager + 10)))
        txt.setOutline('green')
        txt.draw(graphWin)
    elif total % 2 is 0:
        txt = Text(Point(310, 270), ("Dice Total: " + str(total) + "\nYou win $2 extra for an even roll!\nYour Winnings: $" + str(2) + " + Original Wager = $" + str(wager) +  " = $" + str(wager + 2)))
        txt.setOutline('green')
        txt.draw(graphWin)
    else:
        txt = Text(Point(310, 270), ("Dice Total: " + str(total) + "\nYou loose $2 for an odd roll!\nOriginal Wager: $" + str(wager) + " - Losses: $" + str(wager - 2)))
        txt.setOutline('green')
        txt.draw(graphWin)

# Main Function
def main():
    graphWin = GraphWin("Dice Game", 639, 399)
    graphWin.setBackground('black')

    # Input
    wager = int(input("Enter your wager: ($5 minimum): "))

    # Okay there maybe one rule...you have to have more than $5 to play
    if wager < 5:
        smiley = Image(Point(310, 150), "smiley.png")
        smiley.draw(graphWin)
        txt = Text(Point(310, 270), ("Your wager of $"+ str(wager) + " is less than the required $5\n"
                                     "Please re-run program and enter a larger amount!" ))
        txt.setOutline('green')
        txt.draw(graphWin)
    else:
        diceGame(graphWin, wager)

    graphWin.getMouse()
    graphWin.close()

main()
